"""Build/check the self-contained, namespaced trial skill packages."""

import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def packages(root=ROOT):
    trial = root / "trial"
    manifest = json.loads((trial / "sources.json").read_text(encoding="utf-8"))
    runtime = (trial / "runtime.md").read_bytes()
    result = {}
    for entry in manifest["skills"]:
        name = entry["name"]
        skill = trial / "skills" / name
        source = root / entry["source"]
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if digest != entry["sha256"]:
            raise ValueError(f"{entry['source']}: source changed; review the adaptation and update its provenance")
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not match or not re.search(rf"^name: {re.escape(name)}$", match[1], re.M):
            raise ValueError(f"{name}: missing or inconsistent skill frontmatter")
        if not re.search(r"^description: .+", match[1], re.M):
            raise ValueError(f"{name}: missing description")
        provenance = {"base": manifest["base"], "skill": entry}
        files = {
            "references/runtime.md": runtime,
            "references/provenance.json": (json.dumps(provenance, indent=2) + "\n").encode(),
            "LICENSE": (root / "plugins/pstack/LICENSE").read_bytes(),
            "LICENSE.t3-port": (root / "LICENSE").read_bytes(),
        }
        if name == "pstack-show-me-your-work":
            files["scripts/log.py"] = (trial / "log.py").read_bytes()
        result[skill] = files
    return result


def build(root=ROOT):
    for skill, files in packages(root).items():
        for rel, payload in files.items():
            target = skill / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)


def check(root=ROOT):
    problems = []
    for skill, files in packages(root).items():
        expected = {"SKILL.md", *files}
        actual = {p.relative_to(skill).as_posix() for p in skill.rglob("*") if p.is_file()}
        for extra in actual - expected:
            problems.append(f"{skill.name}: unexpected packaged file {extra}")
        for rel, payload in files.items():
            target = skill / rel
            if not target.exists() or target.read_bytes() != payload:
                problems.append(f"{skill.name}/{rel}: missing or stale; run python tools/trial.py build")
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^\s)]+)\)", text):
            if not re.match(r"[a-z]+:", link) and not (skill / link.split("#")[0]).exists():
                problems.append(f"{skill.name}: broken reference {link}")
    return problems


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["build", "check"])
    args = parser.parse_args()
    try:
        if args.action == "build":
            build()
        problems = check()
    except (ValueError, OSError) as error:
        parser.exit(1, f"trial: {error}\n")
    if problems:
        parser.exit(1, "\n".join(problems) + "\n")
    print(f"Trial packages verified: {len(packages())} skills, bundled runtime, licenses, provenance and log helper")

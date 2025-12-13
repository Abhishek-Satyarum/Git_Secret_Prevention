import json
import re
from pathlib import Path


RULES_PATH = Path("rules/secret_patterns.json")


def load_rules():
    with open(RULES_PATH, "r") as f:
        return json.load(f)


def scan_file(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        return []

    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []

    rules = load_rules()
    findings = []

    for rule in rules:
        pattern = re.compile(rule["pattern"])
        if pattern.search(content):
            findings.append({
                "file": str(file_path),
                "rule": rule["name"],
                "severity": rule["severity"]
            })

    return findings

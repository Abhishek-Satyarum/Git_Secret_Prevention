import re
import json
from pathlib import Path

RULES_PATH = Path(__file__).parent.parent / "rules" / "secret_patterns.json"


def load_rules():
    with open(RULES_PATH, "r") as f:
        return json.load(f)


def scan_file(file_path):
    findings = []
    rules = load_rules()

    try:
        content = Path(file_path).read_text(errors="ignore")
    except Exception:
        return findings

    for rule in rules:
        matches = re.findall(rule["pattern"], content)
        if matches:
            findings.append({
                "file": str(file_path),
                "rule": rule["name"],
                "severity": rule["severity"]
            })

    return findings

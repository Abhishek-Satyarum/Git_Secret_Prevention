import sys
from pathlib import Path
from backend.regex_scanner import scan_file

BLOCK_SEVERITIES = {"CRITICAL", "HIGH"}

def main():
    files = sys.argv[1:]
    should_block = False

    for file in files:
        path = Path(file)

        if not path.exists() or path.is_dir():
            continue

        findings = scan_file(path)

        for f in findings:
            print("\n🔐 SECRET DETECTED")
            print(f"File: {f['file']}")
            print(f"Rule: {f['rule']}")
            print(f"Severity: {f['severity']}")
            print("-" * 40)

            if f["severity"] in BLOCK_SEVERITIES:
                should_block = True

    if should_block:
        print("❌ Commit blocked due to high-risk secrets")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())

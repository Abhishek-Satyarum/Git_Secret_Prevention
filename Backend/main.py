import subprocess
import sys
from pathlib import Path
from backend.regex_scanner import scan_file


def get_staged_files():
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        stdout=subprocess.PIPE,
        text=True
    )

    files = []
    for line in result.stdout.splitlines():
        if line.endswith(".py"):
            files.append(line)

    return files


def main():
    files = get_staged_files()

    if not files:
        print("✅ No Python files staged. Commit allowed.")
        return

    findings_found = False

    for file in files:
        findings = scan_file(file)
        if findings:
            findings_found = True
            print("\n❌ SECRET DETECTED. COMMIT BLOCKED.\n")
            for f in findings:
                print(f"File: {f['file']}")
                print(f"Rule: {f['rule']}")
                print(f"Severity: {f['severity']}")
                print("-" * 40)

    if findings_found:
        sys.exit(1)

    print("✅ No secrets found. Commit allowed.")


if __name__ == "__main__":
    main()

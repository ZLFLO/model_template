import sys
import subprocess
from pathlib import Path

SRC_DIR = Path(__file__).parent.parent.parent / 'src'
SRC_DIR = SRC_DIR.resolve()

def find_python_files(directory):
    return directory.rglob('*.py')

def main():
    errors = []
    for py_file in find_python_files(SRC_DIR):
        print(f"Running: {py_file}")
        result = subprocess.run([sys.executable, str(py_file)], capture_output=True)
        if result.returncode != 0:
            errors.append((py_file, result.stderr.decode()))
            print(f"Error in {py_file}:\n{result.stderr.decode()}")
        else:
            print(f"{py_file} ran successfully.")
    if errors:
        print("\nSummary of errors:")
        for file, err in errors:
            print(f"{file}:\n{err}")
        sys.exit(1)
    else:
        print("\nAll files ran successfully.")

if __name__ == "__main__":
    main()

import subprocess
import sys
from pathlib import Path


def pythonscript_test_exec(filepath):
    result = subprocess.run(
        [sys.executable, str(filepath)], capture_output=True, text=True, check=True
    )
    if result.returncode != 0:
        msg = f"Failed executing {filepath}.\n\n{result.stderr}"
        raise AssertionError(msg)


def test_01_download_data():
    filepath = Path(__file__).parent.parent / "scripts" / "01_download_data.py"

    pythonscript_test_exec(filepath)

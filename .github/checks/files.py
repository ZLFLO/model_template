from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def get_all_files(root):
    return [f.relative_to(root) for f in root.rglob("*") if f.is_file()]


def check_file_extensions(files: list[Path]) -> list[Path]:
    allowed_extensions = {
        "md",
        "py",
        "yml",
        "yaml",
        "json",
        "gitignore",
        "ini",
        "cfg",
        "toml",
        "ipynb",
    }
    disallowed_files = []
    for file in files:
        ext = file.suffix.lower()
        if ext not in allowed_extensions:
            disallowed_files.append(file)
    return disallowed_files


def check_file_sizes(files: list[Path]) -> list[Path]:
    maximum_filesize: int = 5242880  # 5 MB
    disallowed_files = []
    for file in files:
        size = file.stat().st_size
        if size > maximum_filesize:
            disallowed_files.append(file)
    return disallowed_files


if __name__ == "__main__":
    files = get_all_files(REPO_ROOT)
    extensions = check_file_extensions(files)
    sizes = check_file_sizes(files)

    if extensions:
        raise ValueError(f"Files with illegal extensions found: {extensions}")
    if sizes:
        raise ValueError(f"Files exceeding maximum size found: {sizes}")

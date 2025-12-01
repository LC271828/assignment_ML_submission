import os
import pathlib

OUTPUT_FILE = pathlib.Path("docs/project_overview.txt")


def format_size(bytes_size: float) -> str:
    """Convert bytes to human-readable units."""
    for unit in ["B", "KB", "MB", "GB"]:
        if bytes_size < 1024:
            return f"{bytes_size:.1f}{unit}"
        bytes_size /= 1024
    return f"{bytes_size:.1f}TB"


def build_tree(start_path: pathlib.Path, prefix=""):
    """Recursively build a tree display with file sizes.

    Note: the .venv directory is skipped to keep the tree focused on
    project files and avoid a lot of virtual-environment noise.
    """

    # Skip the virtual environment directory entirely
    if start_path.name == ".venv":
        return []
    if start_path.name == ".git":
        return []
    entries = list(start_path.iterdir())
    entries.sort()

    lines = []

    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        path_display = prefix + connector + entry.name

        if entry.is_dir():
            # Check if empty
            is_empty = not any(entry.iterdir())
            label = " (empty)" if is_empty else ""
            lines.append(path_display + "/" + label)

            # Recurse
            new_prefix = prefix + ("    " if i == len(entries) - 1 else "│   ")
            lines.extend(build_tree(entry, new_prefix))

        else:
            # File size
            size = entry.stat().st_size
            readable = format_size(size)
            if size == 0:
                readable += " (empty)"
            lines.append(f"{path_display}  [{readable}]")

    return lines


def main():
    repo_root = pathlib.Path(".").resolve()

    tree_lines = [
        "PROJECT DIRECTORY OVERVIEW",
        "==========================",
        "",
        f"Root: {repo_root}",
        "",
    ]
    tree_lines += build_tree(repo_root)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        f.write("\n".join(tree_lines))

    print(f"Project overview written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

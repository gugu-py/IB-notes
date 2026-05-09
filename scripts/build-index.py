from pathlib import Path


ROOT = Path(".")
OUT = ROOT / "index.md"

IGNORE_DIRS = {
    ".git",
    ".quarto",
    "_freeze",
    "_site",
    "scripts",
}

IGNORE_FILES = {
    "README.md",
    "index.md",
}

INDEX_EXTS = {
    ".md",
    ".pdf",
}


def should_skip(path: Path) -> bool:
    return path.name in IGNORE_FILES or any(part in IGNORE_DIRS for part in path.parts)


def title_for(path: Path) -> str:
    return path.stem.replace("-", " ").replace("_", " ").title()


def is_indexed_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in INDEX_EXTS and not should_skip(path)


def has_indexed_files(path: Path) -> bool:
    return any(is_indexed_file(child) for child in path.rglob("*"))


def file_children(path: Path) -> list[Path]:
    return sorted(
        child
        for child in path.iterdir()
        if is_indexed_file(child)
    )


def dir_children(path: Path) -> list[Path]:
    return sorted(
        child
        for child in path.iterdir()
        if child.is_dir() and not should_skip(child) and has_indexed_files(child)
    )


def append_tree(lines: list[str], path: Path, depth: int = 0) -> None:
    indent = "  " * depth

    for file in file_children(path):
        lines.append(f"{indent}- [{title_for(file)}]({file.as_posix()})")

    for directory in dir_children(path):
        lines.append(f"{indent}- **{directory.name}**")
        append_tree(lines, directory, depth + 1)


def build_index() -> str:
    lines = [
        "---",
        "title: Gugu's IB notes",
        "---",
        "",
        "# Notes Index",
        "",
        "Repository: [gugu-py/IB-notes](https://github.com/gugu-py/IB-notes)",
        "",
        "**Before using this website, please read the [README](README.md) in full.** It explains the scope, license, disclaimer, and recommended use of these notes.",
        "",
        "## Quick Navigation",
        "",
        "Use browser search (`Ctrl+F` / `Cmd+F`) to quickly find a course, topic, paper type, or keyword.",
        "",
        "- Bold items are folders.",
        "- Linked items are notes or PDF files.",
        "- Files appear before subfolders.",
        "- PDF sample papers are included in the tree.",
        "- Some notes contain Obsidian-style links.",
        "",
        "## Full Tree",
        "",
    ]

    append_tree(lines, ROOT)

    return "\n".join(lines) + "\n"


OUT.write_text(build_index(), encoding="utf-8")
print(f"Wrote {OUT}")

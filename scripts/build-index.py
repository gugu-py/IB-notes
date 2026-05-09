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


def should_skip(path: Path) -> bool:
    return path.name in IGNORE_FILES or any(part in IGNORE_DIRS for part in path.parts)


def title_for(path: Path) -> str:
    return path.stem.replace("-", " ").replace("_", " ").title()


def has_notes(path: Path) -> bool:
    return any(child.is_file() and child.suffix == ".md" and not should_skip(child) for child in path.rglob("*.md"))


def note_children(path: Path) -> list[Path]:
    return sorted(
        child
        for child in path.iterdir()
        if child.is_file() and child.suffix == ".md" and not should_skip(child)
    )


def dir_children(path: Path) -> list[Path]:
    return sorted(
        child
        for child in path.iterdir()
        if child.is_dir() and not should_skip(child) and has_notes(child)
    )


def append_tree(lines: list[str], path: Path, depth: int = 0) -> None:
    indent = "  " * depth

    for directory in dir_children(path):
        lines.append(f"{indent}- **{directory.name}**")
        append_tree(lines, directory, depth + 1)

    for note in note_children(path):
        lines.append(f"{indent}- [{title_for(note)}]({note.as_posix()})")


def build_index() -> str:
    lines = [
        "---",
        "title: Home",
        "---",
        "",
        "# Notes Index",
        "",
    ]

    append_tree(lines, ROOT)

    return "\n".join(lines) + "\n"


OUT.write_text(build_index(), encoding="utf-8")
print(f"Wrote {OUT}")

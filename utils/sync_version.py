#!/usr/bin/env python3
"""
Script to sync the package version from pyproject.toml to __init__.py
"""

import re
from pathlib import Path


def get_version_from_pyproject(project_root: Path) -> str:
    """Extract version from pyproject.toml"""
    pyproject_path = project_root / "pyproject.toml"

    if not pyproject_path.exists():
        raise FileNotFoundError(f"pyproject.toml not found at {pyproject_path}")

    with open(pyproject_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match version = "X.Y.Z" in pyproject.toml
    match = re.search(r'version\s*=\s*"([^"]+)"', content)
    if not match:
        raise ValueError("Could not find version in pyproject.toml")

    return match.group(1)


def sync_version_to_init(project_root: Path, version: str) -> None:
    """Update __version__ in package __init__.py"""
    init_path = project_root / "EorzeaEnv" / "__init__.py"

    if not init_path.exists():
        raise FileNotFoundError(f"__init__.py not found at {init_path}")

    with open(init_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace __version__ = "X.Y.Z" with new version
    updated_content = re.sub(
        r'__version__\s*=\s*"[^"]+"', f'__version__ = "{version}"', content
    )

    if content == updated_content:
        print(f"✓ Version is already up to date: {version}")
        return

    with open(init_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"✓ Successfully synced version to {version}")


def main():
    """Main entry point"""
    project_root = Path(__file__).parent.parent.resolve()

    try:
        # Get version from pyproject.toml
        version = get_version_from_pyproject(project_root)
        print(f"Found version in pyproject.toml: {version}")

        # Sync to __init__.py
        sync_version_to_init(project_root, version)

    except (FileNotFoundError, ValueError) as e:
        print(f"✗ Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()

"""Utility helpers for copying artifacts to Google Cloud Storage."""

from __future__ import annotations

from pathlib import Path
import subprocess


def upload_directory(src: Path, bucket: str, prefix: str, use_shell: bool = False) -> None:
    """Upload contents of ``src`` to ``gs://bucket/prefix/``.

    The upload walks ``src`` recursively so that nested directories are also
    copied. ``gsutil`` expands globs only when executed through a shell. When
    ``use_shell`` is false (default) each file is copied individually using
    ``subprocess.run`` to avoid missing files. Setting ``use_shell`` to true
    constructs a single ``gsutil -m cp -r`` command executed with
    ``shell=True``.
    """
    destination = f"gs://{bucket}/{prefix}/"
    if use_shell:
        # ``-m`` enables parallel uploads; ``-r`` copies recursively and
        # ``shell=True`` allows wildcard expansion in the source path.
        subprocess.run(
            f"gsutil -m cp -r {src}/* {destination}", shell=True, check=True
        )
    else:
        for path in src.rglob("*"):
            if path.is_file():
                rel = path.relative_to(src).as_posix()
                subprocess.run(
                    ["gsutil", "cp", str(path), f"{destination}{rel}"],
                    check=True,
                )

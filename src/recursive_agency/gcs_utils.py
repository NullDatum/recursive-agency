from __future__ import annotations

"""Utility helpers for copying artifacts to Google Cloud Storage."""

from pathlib import Path
import subprocess


def upload_directory(src: Path, bucket: str, prefix: str, use_shell: bool = False) -> None:
    """Upload contents of ``src`` to ``gs://bucket/prefix/``.

    ``gsutil`` expands globs only when executed through a shell. When
    ``use_shell`` is false (default) each file is copied individually using
    ``subprocess.run`` to avoid missing files. Setting ``use_shell`` to true
    constructs a single ``gsutil -m cp`` command executed with ``shell=True``.
    """
    destination = f"gs://{bucket}/{prefix}/"
    if use_shell:
        # ``-m`` enables parallel uploads; ``shell=True`` allows wildcard
        # expansion in the source path.
        subprocess.run(
            f"gsutil -m cp {src}/* {destination}", shell=True, check=True
        )
    else:
        for path in src.glob("*"):
            if path.is_file():
                subprocess.run(["gsutil", "cp", str(path), destination], check=True)

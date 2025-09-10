from __future__ import annotations

"""Utilities for interacting with Google Cloud Storage via ``gsutil``."""

from pathlib import Path
import subprocess


def upload_directory_to_gcs(src: Path, dst: str) -> None:
    """Upload contents of ``src`` directory to ``dst`` on GCS.

    The function iterates over all files produced by ``src.glob('*')`` and
    uploads each one individually using ``gsutil cp``.  This avoids
    wildcard-expansion issues that occur when passing patterns to
    :func:`subprocess.run` without ``shell=True``.

    Parameters
    ----------
    src:
        Path to a local directory containing artifacts to upload.
    dst:
        Destination GCS URI (for example ``'gs://bucket/prefix/'``).
    """
    src = Path(src)
    for path in src.glob('*'):
        if path.is_file():
            subprocess.run(["gsutil", "cp", str(path), dst], check=True)

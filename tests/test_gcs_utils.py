from pathlib import Path
from unittest.mock import patch, call
import tempfile

from recursive_agency.gcs_utils import upload_directory


def test_upload_directory_recursively_uploads_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        (root / "root.txt").write_text("root")
        nested = root / "nested"
        nested.mkdir()
        (nested / "child.txt").write_text("child")
        with patch("recursive_agency.gcs_utils.subprocess.run") as run:
            upload_directory(root, "bucket", "prefix", use_shell=False)
            expected = [
                call(
                    ["gsutil", "cp", str(root / "root.txt"), "gs://bucket/prefix/root.txt"],
                    check=True,
                ),
                call(
                    [
                        "gsutil",
                        "cp",
                        str(nested / "child.txt"),
                        "gs://bucket/prefix/nested/child.txt",
                    ],
                    check=True,
                ),
            ]
            assert run.call_args_list == expected


def test_upload_directory_shell_recursive():
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        with patch("recursive_agency.gcs_utils.subprocess.run") as run:
            upload_directory(root, "bucket", "prefix", use_shell=True)
            run.assert_called_once_with(
                f"gsutil -m cp -r {root}/* gs://bucket/prefix/",
                shell=True,
                check=True,
            )

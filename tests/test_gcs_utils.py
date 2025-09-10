from pathlib import Path
import subprocess
from unittest import mock

import pytest

from recursive_agency.gcs_utils import upload_directory_to_gcs


def test_upload_directory_invokes_gsutil_for_each_file(tmp_path, monkeypatch):
    # create dummy files in the temp directory
    first = tmp_path / "one.txt"
    first.write_text("1")
    second = tmp_path / "two.txt"
    second.write_text("2")

    calls = []

    def fake_run(cmd, check):
        calls.append((cmd, check))
        return mock.Mock()

    monkeypatch.setattr(subprocess, "run", fake_run)

    destination = "gs://bucket/prefix/"
    upload_directory_to_gcs(tmp_path, destination)

    assert len(calls) == 2
    uploaded = {tuple(call[0]) for call in calls}
    expected = {
        ("gsutil", "cp", str(first), destination),
        ("gsutil", "cp", str(second), destination),
    }
    assert uploaded == expected
    assert all(call[1] is True for call in calls)

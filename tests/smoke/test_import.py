"""Smoke: installed package imports and answers basic predicates (PS-211).

Subprocess-driven (``sys.executable -c ...``) so this proves the installed
distribution resolves — an in-process import would not. Hermetic: no
network, no credentials, no writes outside tmp dirs.
"""

from __future__ import annotations

import subprocess
import sys

import pytest

pytestmark = pytest.mark.smoke


def test_import_and_predicates_subprocess() -> None:
    # Arrange
    argv = [
        sys.executable,
        "-c",
        "from scitex_types import is_array_like; print(is_array_like([1, 2, 3]))",
    ]
    # Act
    completed = subprocess.run(argv, capture_output=True, text=True, timeout=30)
    # Assert
    assert (completed.returncode, completed.stdout.strip()) == (0, "True")

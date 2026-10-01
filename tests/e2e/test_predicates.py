"""E2E: predicates hold against real array libraries (PS-212).

Drives the real numpy/pandas objects the ``ArrayLike`` union promises —
no fakes, no network, loopback-only by construction (pure in-memory).
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.e2e

np = pytest.importorskip("numpy")
pd = pytest.importorskip("pandas")

from scitex_types import is_array_like, is_list_of_type


def test_numpy_array_is_array_like() -> None:
    # Arrange
    arr = np.arange(6).reshape(2, 3)
    # Act
    result = is_array_like(arr)
    # Assert
    assert result is True


def test_pandas_frame_is_array_like() -> None:
    # Arrange
    frame = pd.DataFrame({"a": [1, 2, 3]})
    # Act
    result = is_array_like(frame)
    # Assert
    assert result is True


def test_plain_string_is_not_array_like() -> None:
    # Arrange
    value = "not array"
    # Act
    result = is_array_like(value)
    # Assert
    assert result is False


def test_uniform_int_list_passes() -> None:
    # Arrange
    value = [1, 2, 3]
    # Act
    result = is_list_of_type(value, int)
    # Assert
    assert result is True

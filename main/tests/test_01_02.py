import pytest
from ..chapter_01_item_02 import to_str, to_bytes


def test_to_str() -> None:
    assert to_str(b"foo") == "foo"
    assert to_str(b"hello") == "hello"
    assert to_str(b"Python") == "Python"


def test_to_bytes() -> None:
    assert to_bytes("foo") == b"foo"
    assert to_bytes("hello") == b"hello"
    assert to_bytes("Python") == b"Python"

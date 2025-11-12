from typing import Literal, assert_type
from bearcheck import Check, bearcheck, beartest
from beartype.roar import BeartypeDoorHintViolation
import pytest


def test_check() -> None:
    with pytest.raises(BeartypeDoorHintViolation):
        bearcheck(123, Check[Literal["a", "b"]])
    b = bearcheck("a", Check[Literal["a", "b"]])
    assert_type(b, Literal["a", "b"])


def test_test() -> None:
    assert beartest(123, Check[str]) is None
    assert beartest(123, Check[int | list[str]]) == 123


def test_missing_generic() -> None:
    with pytest.raises(ValueError):
        bearcheck(123, Check)

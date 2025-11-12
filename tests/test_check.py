from typing import Literal, assert_type
from bearcheck import Check, bearcheck
from beartype.roar import BeartypeDoorHintViolation
import pytest


def test_check() -> None:
    with pytest.raises(BeartypeDoorHintViolation):
        bearcheck(123, Check[Literal["a", "b"]])
    b = bearcheck("a", Check[Literal["a", "b"]])
    assert_type(b, Literal["a", "b"])

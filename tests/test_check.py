from typing import TYPE_CHECKING, Any, Literal, assert_type
from bearcheck import Check, CheckType, bearcheck, beartest
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
    with pytest.raises(ValueError):
        beartest(123, Check)
    with pytest.raises(ValueError):
        bearcheck(123, "bla")  # type: ignore
    with pytest.raises(ValueError):
        beartest(123, "bla")  # type: ignore


if TYPE_CHECKING:

    def wrap(a: Any, check: type[Check[CheckType]]) -> CheckType:
        return bearcheck(a, check)

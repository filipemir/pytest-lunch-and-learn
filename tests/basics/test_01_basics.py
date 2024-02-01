import pytest

from app.utils import async_addition


def test_the_truth():
    """
    The simplest pytest test couldn't be simpler.
    """
    assert True


def test_addition():
    """
    You can add explanations to the assertions by asserting a tuple.
    If the assertion fails, it will print out the text as an explanation
    of what you expected it to happen.
    """
    assert 2 + 4 == 6, "I can do maths"


async def test_async_addition():
    """
    Testing async functions works exactly the same assuming you have the
    pytest-asyncio package installed (we do), and configured to be used
    automatically (we do):
    https://pytest-asyncio.readthedocs.io/en/latest/reference/configuration.html#configuration
    """
    assert await async_addition(2, 4) == 6, "I can do maths ASYNC"


class CustomException(Exception):
    pass


async def test_raising_exception():
    with pytest.raises(CustomException, match="boom!"):
        raise CustomException("boom!")

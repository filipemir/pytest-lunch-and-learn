import pytest
from pytest import FixtureRequest

"""
Markers are just what they sound like: a way for us to "mark" a pytest
with a specific string or specific data. We can then use those marks
for a variety of purposes: focusing on specific tests, skipping others,
passing data to fixtures, test paramaterization, etc

I primarily use them when I want to run a specific subset of tests, maybe
different files.
"""

# Marking all tests in a file. Run with: : `pytest . -m foo`
pytestmark = [pytest.mark.foo]


@pytest.mark.bar
def test_foobar_1():
    """
    Marking individual tests to run with: `pytest . -m bar`
    """
    assert True


@pytest.mark.bar
def test_foobar_2():
    assert True


@pytest.mark.skip(reason="I don't like this one")
def test_marked_skip():
    """
    Pytest also has a bunch of built-in marks, like this
    skip one which instructs pytest to skip the test
    """
    assert True


@pytest.mark.xfail(reason="I know, I know")
def test_expected_failure():
    """
    Or this one to mark an expected failure. This can be really
    useful for submitting bug fixes: you add and xfail annotation on
    a test for a bug you notice but want to solve later, then create
    a ticket to address it. CI will still pass, but you'll have a
    test to work against
    """
    assert True


@pytest.fixture
def dumped_markers(request: FixtureRequest):
    """
    This fixture relies on the built-in `request` fixture
    which provides information on the requesting test
    """
    if "dump" in request.keywords:
        dumped_args = request.keywords["dump"].args
        return dumped_args
    else:
        return ()


@pytest.mark.dump("foo", "bar")
def test_passing_args_to_a_fixture(dumped_markers: list[str]):
    """
    You can use marks to pass args to fixtures.
    We'll come back to this when we look at factory fixtures
    """
    assert dumped_markers == ("foo", "bar")

import pytest

"""
Fixtures are basic building blocks of tests in Pytest.
If you're not using them, you're probably writing tests that are
messier than they need to be.

In Pytest, a fixture is a function that pytest executes for you
when you reference it by name as an argument of a test or another
fixture. They provide a convenient and predictable way
to setup and teardown state, patch modules, reference shared data,
etc.

Fixtures have to be defined either in a test file (if that's
the only file that needs that fixture) or in a conftest.py
that is somewhere in the directory hierarchy of the test files
that rely on that fixture. Unfortunately, there's no way to tell
Pytest that this random test file needs the fixtures in some
other random file.

If you run `pytest --fixtures` you can see all the fixtures that
are available for use anywhere. You can also see those for a specific
file or directory:
`pytest tests/pytest_with_filipe/test_03_fixtures.py --fixtures`

The Pytest fixtures docs are excellent and VERY in depth:
https://docs.pytest.org/en/6.2.x/fixture.html
"""


@pytest.fixture
def boolean_value():
    """
    Basic boolean fixture
    """
    return True


def test_with_a_basic_fixture(boolean_value: bool):
    """
    Fixture here is loaded from this file
    """
    assert boolean_value


def test_with_a_basic_shared_fixture(shared_boolean_value: bool):
    """
    This fixture is loaded from this directory's conftest.py
    """
    assert shared_boolean_value


def test_with_another_basic_shared_fixture(global_boolean_value: bool):
    """
    This fixture is loaded from the global tests/conftest.py
    """
    assert global_boolean_value


@pytest.fixture
def a():
    return 7


@pytest.fixture
def b(a: int):
    return a


@pytest.fixture
def c(a: int):
    return a


def test_nested_fixtures(b: int, c: int):
    """
    Fixtures are reusable by other fixtures. Pytest will instantiate
    each fixture once and only once, and if fixture b depends on fixture a
    (as it does here) pytest will instantiate fixture a first and cache
    its result
    """
    assert b + c == 14


@pytest.fixture
def boolean_value_with_setup_and_teardown():
    """
    Basic boolean fixture with setup and teardown
    """
    print("Hold your horses! Bootstrapping a boolean!")

    yield True

    print("All set! Hope your test went well :)")


def test_fixture_with_setup_and_teardown(boolean_value_with_setup_and_teardown: bool):
    """
    One of the most useful features of fixtures is that they can handle both
    setup AND teardown
    """
    assert boolean_value_with_setup_and_teardown


@pytest.fixture(autouse=True)
def say_hi():
    """
    Autouse fixtures do not need to be explicitly requested by the tests.
    These fixtures are always executed first within their context. So
    the fact that this one is at the bottom of the file is a bit of a
    misdirection.
    """
    print("Hello! I get invoked automagically!")


@pytest.fixture
def raise_hell():
    """
    Failures in fixtures result in test errors
    """
    raise Exception


def test_raise_hell():
    """
    Failures in tests result in test failure
    """
    with pytest.raises(Exception):
        raise Exception

import pytest


@pytest.mark.parametrize(
    "value",
    [
        True,
        "true",
        "true-ish",
        2,
    ],
)
def test_assert_truthiness(
    value,
):
    """
    When you find yourself writing the same test again and again, parameterization
    can help
    """
    assert value


@pytest.mark.parametrize(
    "a, b, expected_sum",
    [(0, 1, 1), (1, 1, 2), (1, 2, 3), (2, 3, 5)],
)
def test_addition(a, b, expected_sum):
    """
    The parameters need not be single value: you can pass tuples too
    (or dicts or lists or whatever you want) which is really useful
    for pairing inputs with expected outputs
    """
    assert a + b == expected_sum


@pytest.fixture(params=["a", 12, True])
def value_via_fixture(request):
    return request.param


def test_truthiness_via_parameterized_fixture(value_via_fixture):
    """
    You can also use fixtures to do parameterization. This can be
    useful if you wanna parameterize a bunch of tests in the exact
    same way
    """
    assert value_via_fixture

import pytest

"""
This is a VERY contrived example of how you can use fixtures to replace
classes for setup and teardown. This module is equivalent to
test_02_testing_witch_classes.py, but the fact that the setup and
teardown are defined in the same functions usually makes for more
maintainable code.
"""

_module_value = False
_method_value = False


@pytest.fixture(scope="module")
def module_value_under_test():
    print("Setting up test module")

    global _module_value
    _module_value = True

    yield _module_value

    print("Tearing down test module")
    _module_value = False


@pytest.fixture
def method_value_under_test(module_value_under_test: bool):
    print("Setting up test method")

    global _method_value
    _method_value = module_value_under_test

    yield _method_value

    print("Tearing down test method")
    _method_value = False


def test_value_under_test_once(method_value_under_test: bool):
    assert method_value_under_test


def test_value_under_test_twice(method_value_under_test: bool):
    assert method_value_under_test

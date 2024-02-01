"""
You can organize tests into classes to keep related tests together.
This is usually unnecessary: you can already do this by module/file,
but if you need or want to have more than 1 related block of tests
in the same file you can use classes to do that

You can also use classes to do setup and teardown before and after tests,
though fixtures are typically a cleaner and more scalable solution (more
on that next)
"""


class TestClass1:
    def __init__(self):
        """
        This would feel like a natural way to handle setup for tests classes.
        Unfortunately, pytest skips any test classes that have a constructor
        defined.
        """
        self.value_under_test = True

    def test_value_under_test(self):
        assert self.value_under_test


class TestClass2:
    @classmethod
    def setup_class(cls):
        print("Setting up test class")
        cls.value_under_test = True

    @classmethod
    def teardown_class(cls):
        print("Tearing down test class")
        cls.value_under_test = False

    def setup_method(self):
        print("Setting up test method")
        self.value_under_test = TestClass2.value_under_test

    def teardown_method(self):
        print("Tearing down test method")
        self.value_under_test = False

    def test_value_under_test_once(self):
        assert self.value_under_test

    def test_value_under_test_twice(self):
        assert self.value_under_test

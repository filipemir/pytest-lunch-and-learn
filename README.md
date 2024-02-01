# Pytest basics, tips and tricks

This is a little toy repo for a brief lunch and learn talk on Pytest. It demonstrates some Pytests fundamentals and then demonstrates afew ways we can deploy them to test a FastAPI app.

## Runnign the tests

1. `docker compose build`
2. `docker compose up`: this will run the one migration, boot up a copy of the app, and reset the test DB
3. Step into a container while the service is running `docker compose run server bash`
4. Run the tests with the Pytest CLI: `pytest .` More details below

## Pytest CLI

* `pytest .`: Run all tests in the current directory
* `ptw .`: Runs tests using `pytest-watcher`. Note that the path you provide is for the files you want to watch, so when you run `ptw .` it will re-run ALL tests when any file in the current directory changes. Very useful when combined with the `-k` flag below, though do be mindful that running the test watcher with integration tests is **sure** to land you in a world of pain (more on this below)

Useful flags:

* `-k`: Filter for a specific test file, class, or method. 
* `-v`: Verbose output. This is useful to see the output of print statements in your tests, and to see a more detailed report of which tests passed and failed and where
* `-vv`: EXTRA verbose output.
* `-x`: Fail fast. Will stop running tests at first failure or error. Really useful for integration tests
* `--fixtures`: see all the fixtures available. You can provide a directory or file for this if you want to see all the fixtures available in a specific context
* `--markers`: see all the markers available. Same as above

## Best practices and tips

### General

* Arrange-Act-Assert-Cleanup is timeless advice, Fixtures make this pattern easy. 
* Arrange and cleanup should typically go in fixtures. Act and assert is the job of the test
* Prefer modules and functions over classes and methods
* Use dependency injection when writing code and take advantage of it when writing tests 
* Use `conftest.py` files. If you have a reason to create a directory in the `tests` directory, you should probably have a `conftest.py` file in it with the fixtures you need for the tests in that directory
* If you are writing a lot of very similar tests, consider whether you can use parametrization
* If you wanna learn how to use a testing tool, force yourself to do TDD for a month

### For integration tests
* DAO methods require integration tests, the rest of our code should be testable with unit tests (with rare exceptions)
* NEVER rely on global data. Each test should introduce the data it needs to run and clean up after itself
* Use fixtures to insert and clean up the data you need.
* Use factory fixtures when you have more than one of the same type of records. The factory should always truncate the table in cleanup
* Integration tests are slow, so there's rarely a need to run all of them locally. Rely on the CI for that. Use test filter and test markers to run subsets of tests locally
* Be careful when you abort an integration test run. Ctrl+C doesn't give tests a chance to cleanup, which probably means that now the test DB will be in a bad state and you'll have to reset it




    

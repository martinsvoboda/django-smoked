import os.path
import sys
import pytest
from mock import Mock

from smoked import default_registry, register


def pytest_configure(config):
    sys.path.insert(0, os.path.dirname(__file__))


@pytest.fixture(autouse=True)
def clean_registry():
    """ Clean all registered smoke test at the beginning of each test func """
    # Modify original list (instead of assigning empty list)
    default_registry._registry[:] = []


@pytest.fixture
def filled_registry(clean_registry, valid_test, invalid_test):
    # Generate test suit
    register(valid_test)
    register(valid_test)
    register(invalid_test)
    register(valid_test)
    register(invalid_test)


@pytest.fixture
def valid_test():
    test = Mock()
    test.__name__ = 'Mocked Test'
    return test


@pytest.fixture
def invalid_test():
    test = Mock()
    test.__name__ = 'Mocked Test'
    test.side_effect = AssertionError('Failed test')
    return test

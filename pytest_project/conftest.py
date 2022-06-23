import pytest
import logging

def pytest_addoption(parser):
    parser.addoption("--invalue", action="store", default='10')

@pytest.fixture()
def invalue(request):
    return request.config.getoption('--invalue')
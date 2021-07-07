import pytest

@pytest.fixture
def login():
    print("I'm a fixture")
    return 213
import pytest
from unittest import mock


def test_plain():
    assert 1 == 1


def test_plain2():
    pass


def return_one():
    return 1


def test_return_one():
    assert return_one() == 1


def plus_one(x):
    return x + 1


@pytest.mark.parametrize(
    "input,output",
    [
        (1, 2),
        (2, 3),
        (100, 101),
    ]
)
def test_plus_one(input, output):
    assert plus_one(input) == output


def test_plus_one_fail():
    with pytest.raises(TypeError):
        plus_one('1')


def long_function():
    import time
    time.sleep(100000000)


def return_one_after_a_long_function():
    long_function()
    return 1


def test_plus_one_to_an_expensive_function():
    # assume `long_function` is tested, and mock it's behavor:
    with mock.patch(__name__ + '.long_function', return_value=None):
        assert return_one_after_a_long_function() == 1

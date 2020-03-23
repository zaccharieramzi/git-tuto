import pytest

from ci_tutorial.simple_functions.zac_function import addition

@pytest.mark.parametrize('a, b, expected_result', [
    (1, 2, 3),
    (-1, 2, 1),
    (2.2, 4.6, 6.8),  # be careful with floats you can have unexpected results
    # see https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    (20, -20, 0),
])
def test_addition(a, b, expected_result):
    result = addition(a, b)
    assert expected_result == result

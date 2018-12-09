from lib.matlib import cal_sum
import pytest

test_data = [ ((2, 3), 5),
              ((4, 6), 10)
            ]

@pytest.mark.parametrize("test_input, expected_output", test_data, ids=repr)
def test_cal_sum(test_input, expected_output):
    res = cal_sum(*test_input)
    assert res == expected_output



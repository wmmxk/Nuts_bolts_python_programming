from lib.math_lib import cal_sum
from lib.math_lib import cal_multiply


def test_cal_sum():
    res = cal_sum(3, 4)
    assert 7 == res


def test_cal_multiply():
    res = cal_multiply(3, 4)
    assert 12 == res

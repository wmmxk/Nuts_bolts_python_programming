from lib.mat_lib import cal_sum
import pytest
import os

def test_one():
    assert 1 == 1


def test_cal_sum():
    res = cal_sum(3, 4)
    assert 7 == res

def test_three():
    expected = (1, 2, 3)
    actual = (1, 2, 3)
    # alt + enter, short cut for flip
    assert actual == expected

def test_two():
    assert 1 == 1


@pytest.mark.parametrize('a, b', [(9, 9), (3, 3), (3, 2)], ids=repr)
def test_compare(a, b):
    assert a == b


@pytest.mark.parametrize('a', [1, 2])
@pytest.mark.parametrize('b', [4, 5], ids=repr)
def test_compare(a, b):
    assert a < b


@pytest.fixture()
def test_1(tmpdir):
    assert 1 == 1


def test_create_file(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.txt")
    print("\ntmpdir-----------:", p)
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1

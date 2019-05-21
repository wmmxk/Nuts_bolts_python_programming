import pytest
from lib.train import Train


@pytest.fixture(scope="module")
def create_train():
    print("\n create a train object")
    train = Train(3, 4)
    return train

def test_move_left(create_train, boundary=2):
    train = create_train
    train.move_left()
    coor_x = train.x
    assert boundary == coor_x

def test_move_down(create_train):
    train = create_train
    train.move_down()
    coor_y = train.y
    assert 3 == coor_y
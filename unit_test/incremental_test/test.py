import pytest


class TestDependence:
    
    @pytest.mark.dependency
    def test_one(self):
        print("\nrun test 1--------------")
        assert 1 == 1

    @pytest.mark.dependency(depends=['TestDependence:test_one'])
    def test_two(self):
        print("run test 2------------")
        assert 1 == 1

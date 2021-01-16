import pytest


class Test_demo3:

    @pytest.mark.parametrize("a, b", [(2, 3), (4, 1)])
    def test_001(self, a, b):

        print(">>>>001")
        assert a + b == 4



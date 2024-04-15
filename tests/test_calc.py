from .. app.calc.calc import Calc


def test_add():
    assert Calc(2, 2).add() == 4


def test_sub():
    assert Calc(4, 2).sub() == 2


def test_mul():
    assert Calc(2, 4).mul() == 8


# def test_div():
#     assert Calc(12, 2).div() == 6

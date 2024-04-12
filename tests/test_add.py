from calc.calc import add, sub, mul


def test_add():
    assert add(2, 2) == 4


def test_sub():
    assert sub(4, 2) == 2


def test_mul():
    assert mul(2, 2) == 4

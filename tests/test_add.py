from calc.calc import add, sub

def test_add():
    assert add(2,2) == 4
    
def test_sub():
    assert sub(4,2) == 2
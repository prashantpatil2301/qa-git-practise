from calculator import subtract


def test_subtraction():
    assert subtract(10, 4) == 6

def test_subtraction_with_zero():
    assert subtract(10, 0) == 10
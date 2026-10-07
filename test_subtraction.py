from calculator import subtract


def test_subtraction():
    assert subtract(10, 4) == 6

def test_subtraction_with_zero():
    assert subtract(5, 0) == 5

def test_subtraction_with_negative_result():
    assert subtract(3, 5) == -2
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(1, 1) == 0
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(4, 6) == 24
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(8, 0) == ValueError("Cannot divide by zero.")
    assert divide(0, 5) == 0

def test_invalid_operation():
    assert perform_operation(4, 5, '%') == "Invalid operation"

# Additional test cases to consider edge cases and boundary conditions

def test_large_numbers():
    assert add(999999999, 1) == 1000000000
    assert subtract(1000000000, 1) == 999999999
    assert multiply(123456789, 0) == 0
    assert divide(1, 999999999) == 1e-09

def test_negative_numbers():
    assert add(-5, -3) == -8
    assert subtract(-5, 3) == -8
    assert multiply(-5, 3) == -15
    assert divide(-6, 2) == -3

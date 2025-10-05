from plates import is_valid

def test_valid():
    assert is_valid("CS50") is True
    assert is_valid("ABC123") is True
    assert is_valid("AB") is True

def test_length():
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False

def test_start():
    assert is_valid("1ABC") is False
    assert is_valid("A1") is False

def test_numbers():
    assert is_valid("ABC12D") is False
    assert is_valid("AB012") is False
    assert is_valid("ABC1") is True

def test_chars():
    assert is_valid("AB C") is False
    assert is_valid("AB.C") is False
    assert is_valid("A!B") is False
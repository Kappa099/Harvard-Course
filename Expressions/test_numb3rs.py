from numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True

def test_invalid_addresses():
    assert validate("275.3.6.28") == False
    assert validate("256.100.50.25") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("cat.dog.1.1") == False
    assert validate("-1.2.3.4") == False
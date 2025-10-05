from bank import value

def test_hello_lower():
    assert value("hello") == 0
    assert value("hello there") == 0

def test_hello_upper():
    assert value("Hello") == 0
    assert value("HeLLo world") == 0

def test_h_but_not_hello():
    assert value("hi") == 20
    assert value("Howdy") == 20
    assert value("hmm") == 20

def test_not_h():
    assert value("good morning") == 100
    assert value("bye") == 100
    assert value("ello") == 100

def test_type():
    assert isinstance(value("hello"), int)
    assert isinstance(value("hi"), int)
    assert isinstance(value("hi there"), int)
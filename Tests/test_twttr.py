from twttr import shorten

def test_twitter():
    assert shorten("twitter") == "twttr"

def test_letters():
    assert shorten("AbEcIdOu") == "bcd"

def test_no_vowel():
    assert shorten("rhythm") == "rhythm"

def test_all_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_symbols():
    assert shorten("Hello, World! 123") == "Hll, Wrld! 123"

def test_type():
    assert isinstance(shorten("Example"), str)
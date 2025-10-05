from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("AbEcIdOu") == "bcd"
    assert shorten("rhythm") == "rhythm"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("Hello, World! 123") == "Hll, Wrld! 123"
    assert isinstance(shorten("Example"), str)
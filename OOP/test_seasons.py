from datetime import date
from seasons import calculate_minutes, number_to_words

def test_calculate_minutes_one_day():
    birth = date(2000, 1, 1)
    today = date(2000, 1, 2)
    assert calculate_minutes(birth, today) == 1440

def test_calculate_minutes_multiple_days():
    birth = date(2000, 1, 1)
    today = date(2000, 1, 11)
    assert calculate_minutes(birth, today) == 14400

def test_calculate_minutes_leap_year():
    birth = date(2019, 1, 1)
    today = date(2020, 1, 1)
    assert calculate_minutes(birth, today) == 525600
    today = date(2021, 1, 1)
    assert calculate_minutes(birth, today) == 1051200

def test_number_to_words_basic():
    result = number_to_words(525600).lower()
    assert "five hundred twenty-five thousand" in result
    assert "six hundred" in result
    assert number_to_words(1440) == "One thousand four hundred forty"

def test_number_to_words_capitalization():
    result = number_to_words(60)
    assert result == "Sixty"

def test_number_to_words_large_number():
    result = number_to_words(1051200).lower()
    assert "million" in result

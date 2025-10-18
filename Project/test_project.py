import pytest
import project

def test_encrypt_basic():
    assert project.encrypt("python") == ["_", "_", "_", "_", "_", "_"]

def test_encrypt_empty():
    assert project.encrypt("") == []

def test_guesser_correct():
    hidden = ["_"] * 6
    lives = project.guesser("p", "python", hidden, 6)
    assert hidden == ["p", "_", "_", "_", "_", "_"]
    assert lives == 6

def test_guesser_incorrect():
    hidden = ["_"] * 6
    lives = project.guesser("z", "python", hidden, 6)
    assert hidden == ["_"] * 6
    assert lives == 5

def test_guesser_multiple():
    hidden = ["_"] * 6
    lives = project.guesser("o", "python", hidden, 6)
    assert hidden == ["_", "_", "_", "_", "o", "_"]
    assert lives == 6

def test_guesser_repeated():
    hidden = ["_"] * 6
    lives = project.guesser("t", "letter", hidden, 6)
    assert hidden == ["_", "t", "t", "_", "_", "_"]
    assert lives == 6

def test_correct_answer(monkeypatch):
    monkeypatch.setattr("random.choice", lambda x: "python")
    assert project.correct_answer(project.hard_mode) == "python"

def test_correct_answer_from_list():
    word_list = ["alpha", "beta", "gamma"]
    result = project.correct_answer(word_list)
    assert result in word_list
from demo_text import TextUtilities
# import pytest


text = TextUtilities()


# ---------- TEXT UTILITIES TEST CASES ----------

def test_word_count():
    assert text.word_count("hello world") == 2


def test_word_count_repeated_words():
    assert text.word_count("hello hello world") == 3


def test_unique_words():
    assert text.unique_words("hello hello world") == ["hello", "world"]


def test_reverse_string():
    assert text.reverse_string("abc") == "cba"


def test_empty_string():
    assert text.word_count("") == 0
    assert text.unique_words("") == []
    assert text.reverse_string("") == ""
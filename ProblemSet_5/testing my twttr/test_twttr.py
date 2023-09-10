from twttr import shorten

def test_no_vowel():
    assert shorten("short") == "shrt"

def test_capital_vowel():
    assert shorten("Short") == "Shrt"

def test_lower_vowel():
    assert shorten("head") == "hd"

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_upper_vowel():
    assert shorten("billing") == "bllng"

def test_punctuation():
    assert shorten("now!") == "nw!"

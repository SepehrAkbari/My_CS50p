import pytest
from working import convert

def test_valid_input_1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_valid_input_2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_input_3():
    assert convert("12:30 PM to 3:45 PM") == "12:30 to 15:45"

def test_valid_input_4():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_valid_input_5():
    assert convert("1 AM to 1 AM") == "01:00 to 01:00"

def test_invalid_format_1():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_format_2():
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")

def test_invalid_time_1():
    with pytest.raises(ValueError):
        convert("13:00 AM to 3:00 PM")

def test_invalid_time_2():
    with pytest.raises(ValueError):
        convert("9:60 AM to 3:00 PM")

def test_invalid_time_3():
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:60 PM")

if __name__ == "__main__":
    pytest.main()

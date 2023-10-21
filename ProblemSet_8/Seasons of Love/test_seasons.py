from seasons import convert

def test_date():
    assert convert(70) == "One hundred thousand, eight hundred minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(5) == "Seven thousand, two hundred minutes"

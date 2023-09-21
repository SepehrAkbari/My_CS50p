from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("18.95.21.88") == True
    assert validate("239.910.288.672") == False
    assert validate("113.113.113.113") == True

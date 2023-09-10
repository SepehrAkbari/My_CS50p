from plates import is_valid

def test_begin_alphabet():
    assert is_valid("WT65") == True
    assert is_valid("GHSB") == True
    assert is_valid("P34") == False
    assert is_valid("45UJI") == False
    assert is_valid("5AMN") == False
    assert is_valid("&40") == False

def test_length():
    assert is_valid("ABC12345") == False
    assert is_valid("H") == False
    assert is_valid("BH8654") == True
    assert is_valid("HEX") == True

def test_num_place():
    assert is_valid("GH35") == True
    assert is_valid("90AW") == False
    assert is_valid("KK8PP") == False
    assert is_valid("BM4W") == False
    assert is_valid("1A") == False

def test_alphanumeric():
    assert is_valid("COS") == True
    assert is_valid("%#") == False
    assert is_valid("BT:$#") == False
    assert is_valid("NPC85") == True

def test_zero_place():
    assert is_valid("ML098") == False
    assert is_valid("LIN809") == True

def test_punctuation():
    assert is_valid("ABCD1") == True
    assert is_valid("ABC D") == False
    assert is_valid("HM.K") == False
    assert is_valid("HEE!X") == False
    assert is_valid("BRR_") == False

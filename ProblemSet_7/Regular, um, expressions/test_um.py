import um

def test_count_no_um():
    assert um.count("yummy") == 0
    assert um.count("The quick brown fox") == 0

def test_count_single_um():
    assert um.count("hello, um, world") == 1
    assert um.count("Um, excuse me!") == 1

def test_count_multiple_um():
    assert um.count("Um, um, um, um") == 4
    assert um.count("Um is not the same as um.") == 2

def test_count_mixed_case_um():
    assert um.count("uM uM uM um UM") == 5

def test_count_within_words():
    assert um.count("album") == 0
    assert um.count("umbrella") == 0

if __name__ == "__main__":
    import pytest
    pytest.main()

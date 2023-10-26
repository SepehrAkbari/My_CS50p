from project import feet_to_meters, meters_to_feet, kilometer_to_mile, mile_to_kilometer, centimeter_to_inch, inch_to_centimeter, kilogram_to_pound, pound_to_kilogram, liter_to_gallon, gallon_to_liter, celsius_to_fahrenheit, fahrenheit_to_celsius

def test_feet_to_meters():
    assert feet_to_meters(1) == 0.30
    assert feet_to_meters(18) == 5.49
    assert feet_to_meters(75) == 22.86

def test_meters_to_feet():
    assert meters_to_feet(1) == 3.28
    assert meters_to_feet(18) == 59.06
    assert meters_to_feet(75) == 246.06

def test_kilometer_to_mile():
    assert kilometer_to_mile(1) == 0.62
    assert kilometer_to_mile(18) == 11.18
    assert kilometer_to_mile(75) == 46.60

def test_mile_to_kilometer():
    assert mile_to_kilometer(1) == 1.61
    assert mile_to_kilometer(18) == 28.97
    assert mile_to_kilometer(75) == 120.70

def test_centimeter_to_inch():
    assert centimeter_to_inch(1) == 0.39
    assert centimeter_to_inch(18) == 7.09
    assert centimeter_to_inch(75) == 29.53

def test_inch_to_centimeter():
    assert inch_to_centimeter(1) == 2.54
    assert inch_to_centimeter(18) == 45.72
    assert inch_to_centimeter(75) == 190.50

def test_kilogram_to_pound():
    assert kilogram_to_pound(1) == 2.20
    assert kilogram_to_pound(18) == 39.68
    assert kilogram_to_pound(75) == 165.35

def test_pound_to_kilogram():
    assert pound_to_kilogram(1) == 0.45
    assert pound_to_kilogram(18) == 8.16
    assert pound_to_kilogram(75) == 34.02

def test_liter_to_gallon():
    assert liter_to_gallon(1) == 0.26
    assert liter_to_gallon(18) == 4.76
    assert liter_to_gallon(75) == 19.81

def test_gallon_to_liter():
    assert gallon_to_liter(1) == 3.79
    assert gallon_to_liter(18) == 68.14
    assert gallon_to_liter(75) == 283.91

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(1) == -17.22
    assert fahrenheit_to_celsius(18) == -7.78
    assert fahrenheit_to_celsius(75) == 23.89

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(1) == 33.80
    assert celsius_to_fahrenheit(18) == 64.40
    assert celsius_to_fahrenheit(75) == 167.00

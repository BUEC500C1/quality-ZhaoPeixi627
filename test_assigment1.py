from assigment1 import arabicToRoman

def test_arabicToRoman():
    assert arabicToRoman(1) == 'I'
    assert arabicToRoman(2) == 'II'
    assert arabicToRoman(2) == 'III'  
    assert arabicToRoman(3999) == 'MMMCMXCIX'
    assert arabicToRoman(123) == 'CXXIII' 
    assert to_roman(4) == 'IV'

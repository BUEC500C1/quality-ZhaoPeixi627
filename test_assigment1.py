from assigment1 import arabicToRoman

def test_arabicToRoman():
    assert arabicToRoman(1) == 'I'
    assert arabicToRoman(2) == 'II'
    assert arabicToRoman(3) == 'III'  
    assert arabicToRoman(3999) == 'MMMCMXCIX'
    assert arabicToRoman(123) == 'CXXIII' 
    assert arabicToRoman(4) == 'IV'

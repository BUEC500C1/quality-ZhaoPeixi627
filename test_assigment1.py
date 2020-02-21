from assigment1 import arabicToRoman

def test_arabicToRoman():
    assert arabicToRoman(1) == 'I'
    assert arabicToRoman(2) == 'II'
    assert arabicToRoman(2) == 'III'  
    assert arabicToRoman(3999) == 'MMMCMXCIX'
    assert arabicToRoman(123) == 'CXXIII' 
    assert arabicToRoman(4) == 'IV'
    assert arabicToRoman(1000) == 'M'
    assert arabicToRoman(13) == 'XIII'
    assert arabicToRoman(2414) == 'MMCDXIV
    assert arabicToRoman(500) == 'D'
    assert arabicToRoman(900) == 'CM
    assert arabicToRoman(4999) == 'MMMMCMXCIX'
    assert arabicToRoman(50) == 'L'
    assert arabicToRoman("test") == -1
    assert arabicToRoman(3.51) == -1

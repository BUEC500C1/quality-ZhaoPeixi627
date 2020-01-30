# copyright Peixi Zhao  bradzhao@bu.edu

def arabicToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    res = ''
    i = 0
    while num:
        remain = num // arabic[i]
        res += roman[i] * remain
        num = num - remain * arabic[i]
        i += 1
    return res

"""
Integer to Roman
"""

def int2rom(num):
    if num == 0:
        return ""
    elif 1 <= num <= 3:
        return 'I' * num
    elif num == 4:
        return 'IV'
    elif 5 <= num < 9:
        return 'V' + int2rom(num - 5)
    elif num == 9:
        return 'IX'
    elif 10 <= num < 40:
        return 'X' * (num // 10) + int2rom(num % 10)
    elif 40 <= num < 50:
        return 'XL' + int2rom(num - 40)
    elif 50 <= num < 90:
        return 'L' + int2rom(num - 50)
    elif 90 <= num < 100:
        return 'XC' + int2rom(num - 90)
    elif 100 <= num < 400:
        return 'C' * (num // 100) + int2rom(num % 100)
    elif 400 <= num < 500:
        return 'CD' + int2rom(num - 400)
    elif 500 <= num < 900:
        return 'D' + int2rom(num - 500)
    elif 900 <= num < 1000:
        return 'CM' + int2rom(num - 900)
    else: # 1000 <= num < 4000
        return 'M' * (num // 1000) + int2rom(num % 1000)


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return int2rom(num)
        
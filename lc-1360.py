class Solution:
    def ifLeapYear(year: int):
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
    
    def solve(self):
        while True:
            x = input("input a year: ")
            print(self.ifLeapYear(int(x)))

daysInMonth = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# dayInYear = 0
# for month, dayCount in daysInMonth.items():
#     dayInYear += dayCount
# print(dayInYear)

from datetime import date

d1 = date(2020, 1, 15)
d2 = date(2019, 12, 31)

print((d1 - d2).days)

# print(daysInMonth[2])
# print(daysInMonth[5])

# def segmentDate(s: str):
#     segs = s.split('-')
#     return segs[0], segs[1], segs[2]

# while True:
#     date = input()
#     print(segmentDate(date))
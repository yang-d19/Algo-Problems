# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem

n = int(input())

for idx in range(n):
    s = input()

    if (s[0] != '(') or (s[-1] != ')'):
        print("Invalid")
        continue

    s = s[1:-1]

    split_s = s.split(", ")

    if len(split_s) != 2:
        print("Invalid")
        continue

    latitude = split_s[0]
    longtitude = split_s[1]

    latitude_f = float(latitude)
    longtitude_f = float(longtitude)

    if latitude_f < -90.0 or latitude_f > 90.0:
        print("Invalid")
        continue
    
    if longtitude_f < -180.0 or longtitude_f > 180.0:
        print("Invalid")
        continue

    isAbnormal = False

    # check redundant zeros
    for ns in [latitude, longtitude]:
        for i in range(len(ns)):
            c = ns[i]
            if c >= '1' and c <= '9':
                break
            if c == '0':
                # for j in range(i + 1, len(ns)):
                if (i < len(ns) - 1) and (ns[i + 1] != '.'):
                    isAbnormal = True
                break
        
    if isAbnormal:
        print("Invalid")
        continue
    
    # check for extra dot
    for ns in [latitude, longtitude]:
        for i in range(len(ns)):
            c = ns[i]
            if c == '.':
                if i == len(ns) - 1:
                    isAbnormal = True
                break

    if isAbnormal:
        print("Invalid")
        continue

    print("Valid")
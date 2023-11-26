intervals = [[1, 3], [2, 6], [15, 18], [8, 10], [5, 13], [2, 4], [2, 2], [2, 5]]

def comp(x, y):
    return x[0] > y[0]

result = sorted(intervals, key=lambda x: x[0])

print(result)
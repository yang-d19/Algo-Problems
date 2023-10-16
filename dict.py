my_dict = {'apple': (5, 10), 'banana': (3, 8), 'orange': (3, 5), 'grape': (1, 10)}

# Sort the dictionary by the first value and, if the same, the second value
sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: (item[1][0], item[1][1]))}

# Iterate over the sorted dictionary
for key, value in sorted_dict.items():
    print(key, value)
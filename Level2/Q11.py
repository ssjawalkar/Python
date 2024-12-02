def split_strings(s):
    res = []
    for w in s:
        res.append(list(w))
    return res

input_list = ['Red', 'Blue', 'Black', 'White', 'Pink']
output = split_strings(input_list)
print(output)

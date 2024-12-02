input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
counter = {}

for i in range(len(input_list)):
    if input_list[i] not in counter:
        counter[input_list[i]]=0
    counter[input_list[i]]+=1
print(counter)

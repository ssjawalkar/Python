def find_median(number_list):

    number_list.sort()
    n = len(number_list)

    if n % 2 == 1:
        return number_list[n // 2]
    else:
        return (number_list[(n // 2) - 1] + number_list[n // 2])/2


number_list = [7, 2, 5, 1, 9, 3]
median = find_median(number_list)
print(median)

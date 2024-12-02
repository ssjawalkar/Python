def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    return n % 2 == 0 and is_power_of_two(n // 2)

number = int(input("Enter a number: "))
print(is_power_of_two(number))

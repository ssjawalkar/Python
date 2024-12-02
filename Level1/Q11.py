def single_digit_sum(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

num = int(input("Enter a number: "))

final_output = single_digit_sum(num)

print(f"Final Output: {final_output}")

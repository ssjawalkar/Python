num = int(input("Input a number:"))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial is {factorial}")

def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(num1, num2):
    return (num1 * num2) // compute_gcd(num1, num2)


num1 = int(input("Input the first number:"))
num2 = int(input("Input the second number:"))


lcm = find_lcm(num1, num2)


print(f"LCM of {num1} and {num2} are {lcm}")

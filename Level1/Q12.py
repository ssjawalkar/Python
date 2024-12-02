def reverse_number(num):
    revnum = 0
    while num > 0:
        revnum = revnum * 10 + num % 10 
        num //= 10  
    return revnum


num = int(input("Enter a number: "))

revnum = reverse_number(num)

print(f"Reversed Number: {revnum}")

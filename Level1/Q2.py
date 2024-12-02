s = input("Enter a string: ")
lCount = 0
dCount = 0
for i in range(len(s)):
    if s[i].isalpha():
        lCount+=1
    elif s[i].isdigit():
        dCount+=1
print(f"Alphabets: {lCount} & Numbers: {dCount}")


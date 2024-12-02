def count_vowels(s):
    vowels = set("aeiouAEIOU") 
    count=0
    for i in range(len(s)):
        if s[i] in vowels:
            count+=1
    return count

string = "Hello, World!"
vowel_count = count_vowels(string)
print(f"Number of vowels: {vowel_count}")
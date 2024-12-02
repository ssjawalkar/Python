def reverse_words(sentence):
    words = sentence.split()
    l, r = 0, len(words) - 1
    
    while l < r:
        words[l], words[r] = words[r], words[l]  
        l += 1  
        r -= 1 
    
   
    return ' '.join(words)

input_sentence = "Hello, World! Welcome to Python programming."
output_sentence = reverse_words(input_sentence)

print("Output after reverse:", output_sentence)

def get_even_length_words(file_path):
    try:
        with open(file_path, 'r') as file: 
            content = file.read()  
            words = content.split()  
            even_length_words = [word for word in words if len(word) % 2 == 0] 
            return " ".join(even_length_words) 
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"


file_path = "doc.txt"
result = get_even_length_words(file_path)
print(result)

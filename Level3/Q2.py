def count_lines(file_path):
    try:
        with open(file_path, 'r') as file: 
            line_count = sum(1 for _ in file)  
        return line_count
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"


file_path = 'demo.txt' 
line_count = count_lines(file_path)
print(f"Number of lines in the file: {line_count}")

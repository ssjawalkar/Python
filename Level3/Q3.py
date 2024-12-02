def JtoI(file_path):
    try:
        with open(file_path, 'r') as file:  
            content = file.read()  
            corrected_content = content.replace('J', 'I')
        print(corrected_content) 
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'words.txt'  
JtoI(file_path)

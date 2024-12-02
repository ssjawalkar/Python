def run_length_encode(input_string):
    #base
    if not input_string: 
        return ""
    
    string_buffer = []
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:  
            count += 1
        else:
            string_buffer.append(f"{input_string[i - 1]}{count}")
            count = 1  

    
    string_buffer.append(f"{input_string[-1]}{count}")

    return "".join(string_buffer)

input_string = "wwwwaaadebbbbbw"
output = run_length_encode(input_string)
print(output)

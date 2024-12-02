def parse_encoded_string(encoded_string):

    parts = list(encoded_string.split('000'))
    
    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }


input_string = "Robert000Smith000123"
output = parse_encoded_string(input_string)
print(output)

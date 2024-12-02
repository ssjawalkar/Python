inputValue = int(input("Input:"))     
if inputValue>1:                        
    output = 0
    for i in range(1, inputValue):      
        if inputValue % i == 0:
            output += i
    if(output == inputValue):
        print("Yes")
    else:
        print("No")
else:
    print("No")
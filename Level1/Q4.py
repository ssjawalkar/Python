print("Enter Start Value")
start = int(input())
stop =  int(input())  
s = 0                           
for i in range(start,stop+1):
    if i%2!=0:
        s+=i
print("Sum of odd number ",s)
def customers_left_without_computer(N, S):
    occupied = set()  
    waiting = set()   
    count = 0  

    for customer in S:
        if customer in occupied:
          
            occupied.remove(customer)
        elif customer not in waiting:
           
            if len(occupied) < N:
               
                occupied.add(customer)
            else:
               
                waiting.add(customer)
                
        else:
            waiting.remove(customer)
            count+=1

    return count

# Example usage
N1, S1 = 3, "GACCBDDBAGEE"
print(customers_left_without_computer(N1, S1)) 

N2, S2 = 1, "ABCBAC"
print(customers_left_without_computer(N2, S2))  

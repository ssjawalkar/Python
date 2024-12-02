marks = {'physics':0.0,'chemistry':0.0,'biology':0.0,'mathematics':0.0,'computer':0.0,}  
for subj in marks.keys():                                                                  
    marks[subj] = float(input("Enter "+subj+" marks (out of 100): "))
avg = sum(marks.values())/5                                                         
print(" Percentage:"+str(avg))  
if avg >= 90:                                                                           
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 70:
    print("Grade: C")
elif avg >= 60:
    print("Grade: D")
elif avg >= 40:
    print("Grade: E")
elif avg < 40:
    print("Grade: F")
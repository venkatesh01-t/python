#task1
i=0
while True:
    i+=1
    print(i)
    if i==10:
        break
 #task 2
 i=0
odd=[]
even=[]
while True: 
    i+=1
    if i==100:
        break
    elif i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"odd numbers :\n {odd}\n even numbers:\n {even}")
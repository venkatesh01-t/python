'''b=0
while True:
    a=int(input("Enter the passtive number to get negative number loop will be stop : "))
    if a>0:
        b+=a
    else:
        
        break
print(f"the answer is : {b}")
'''
LI=[10,22,21,-1,-87,676,-22]
lp=[]
ln=[]

print("the list values : ",LI)
for i in LI:
    if i>0:
        lp.append(i)
    else:
        ln.append(i)
print(f"passtive : {lp} \nnegative : {ln}")

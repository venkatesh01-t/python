#task1
for i in range(10,1,-1):
    print(i)


#task2
a=int(input("enter the range in while loop : "))
i=1
name=input("enter the name")
while a>=i:
    print(name)
    i+=1

#task3
a1=10
i=1
while a1>=i:
    print(i)
    if i==5:
          break
    i+=1
#task4
fact=int(input("enter the number : "))
val=1
for i in range (1,fact+1):
    val*=i
print(val)

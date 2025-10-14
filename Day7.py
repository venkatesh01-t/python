'''#task 1
li=['admin','ex@gmail.com','admin@123']
name=input("Enter The UserName : ")
email=input("Enter Your Email : ")
pas=input("Enter Your Password : ")
if li[0]==name and li[1] ==email and li[2] == pas:
    print(f"hello {name}")
else:
    print("not vaild")
#task 2
lit=["single","double","thirble","four","five"]
a=input("Enter the Number : ")
try:
    if a!='':
        print(lit[len(a)-1],"digit number")
    else:
        print("enter a number to valid ")
except IndexError:
    print("not vaild to entered 6 digit more  ")

li =[]
for i in range(5):
    a=int(input(f"Enter the Subject marks {i+1} : "))
    li.append(a)
su=sum(li)/5
print("our grade is  : ",su)
if su <=25:
    print("grande F -> ",su)
elif su<=25 or su <=40:
    print("grande E -> ",su)
elif su<=40 or su <=50:
    print("grande D -> ",su)
elif su<=50 or su <=60:
    print("grande C -> ",su)
elif su<=60 or su <=80:
    print("grande B -> ",su)
else:
    print("grade A -> ",su)

'''
a=int(input('Enter The class held: '))
b=int(input("Enter The class attend : " ))
print()
print(f"class attendence is {a} . \n The student Attendnace  is : {b} . \nthe student attence is {b/a}/{a} ")

    


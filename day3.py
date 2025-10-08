# Task 1: Even or Odd
num = int(input("Enter the number: "))
print("given number is even number" if num % 2 == 0 else "given number is odd")

# Task 2: Voter Eligibility
age = int(input("Enter your age: "))
print("you are eligible voter" if age >= 18 else "you are not eligible voter")

# Task 3: FizzBuzz
number = int(input("Enter the number: "))
print("fizz Buzz" if number % 3 == 0 and number % 5 == 0 
      else "Buzz" if number % 5 == 0 
      else "fizz buzz" if number % 3 == 0 
      else "nothing")

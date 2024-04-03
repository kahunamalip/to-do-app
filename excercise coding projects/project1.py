import random

user_input1 = int(input("Enter first number: "))
user_input2 = int(input("Enter second number: "))

if user_input1 > user_input2:
    user_input1, user_input2 = user_input2, user_input1

result = random.randint(user_input1, user_input2)

print(f"A random number between {user_input1} and {user_input2} is {result}.")
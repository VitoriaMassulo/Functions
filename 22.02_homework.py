#Question 1 – Print numbers in range (no return)
#Write a function that gets two int parameters: start and stop
#The function should print all numbers from start to stop (inclusive)

#Notes:

#This function does not return a value
#Use a loop (for with range) inside the function

# Resolutiom

def num_range(start: int, stop: int):

    for number in range(start, stop + 1):
        print (number)

num_range(1, 10)


#Question 2 – Basic math list (returns a list)

#Write a function that gets two numbers a and b and returns a list in this exact order:
#[a+b, a-b, a/b, a*b]

#Notes:

#The function returns the list
#Assume b != 0 (no need to handle division by zero)

# Resolutiom

#1rst try

def basic_math_list(a, b):
    return [a + b, a - b, a * b, a / b]

result = basic_math_list(8, 2)
print(result)

print('-'*25)

#2nd

def basic_math_list_2(a, b):

    add_result = a + b
    sub_result = a - b
    mul_result = a * b
    div_result = a / b

    sum_result = []

    sum_result.append(add_result)
    sum_result.append(sub_result)
    sum_result.append(mul_result)
    sum_result.append(div_result)
    return sum_result

result_1 = basic_math_list_2(8, 2)
print(result)
print('-'*25)

#✨✨ Question 3 – Bonus challenge: Mini math game -- Experts only! ✨✨

#Implement a small game
#The computer should:

#Pick a random number between 1 and 10
#Pick a random operation from: +, -, *, %
#Pick another random number between 1 and 10
#Print the equation and ask the user for the result
#Rules:

#if the user is correct, print Correct!
#Otherwise print Wrong.. the answer was ___
#Your task

#Your job is to complete the missing functions:

#####get_random_between_1_10()
#####get_random_operation()
#####alc_result(num1, oper, num2)


#resolution


import random

def get_random_between_1_10() -> int:
    num = random.randint(1, 10)
    return num

def get_random_operation() -> str:
    operator = random.choice(['+', '-', '*', '%'])
    return operator

def calc_result(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '%':
        return num1 % num2

#Main code (DO NOT CHANGE)

num1 = get_random_between_1_10()
oper = get_random_operation()
num2 = get_random_between_1_10()
result = calc_result(num1, oper, num2)

print(f"{num1} {oper} {num2} = ?")
user_result = int(input('whats the result? '))

if result == user_result:
    print('Correct!')
else:
    print(f"Wrong.. the answer was {result}")

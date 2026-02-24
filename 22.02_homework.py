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

result = basic_math_list_2(8, 2)
print(result)
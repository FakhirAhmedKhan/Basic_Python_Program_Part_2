# Task_1
# Write a python program to create a dictionary of spanish world with as their English translation. Provide user with an option to look it up!
# words = {
#     # 🇪🇸 Spanish: #🇪🇸 Spanish
#     "hola": "hallo",
#     "adios": "Goodbye",
#     "Gracias": "Thank you",
#     "Agua": "Water",
#     "pan": "Bread",
# }
# word = input("Enter the spanish word you want to translate in to English: ")
# print(words[word])

# Task_2
# Write a python program to input eight numbers from the user and display all the unique numbers(ones)
# s = set()
# n = input("Enter the number:")
# s.add(int(n))
# n = input("Enter the number:")
# s.add(int(n))
# n = input("Enter the number:")
# s.add(int(n))
# n = input("Enter the number:")
# s.add(int(n))
# n = input("Enter the number:")
# s.add(int(n))
# n = input("Enter the number:")
# s.add(int(n))
# n = input("Enter the number:")
# s.add(int(n))
# n = input("Enter the number:")
# s.add(int(n))
# print(s)

# Task_3
# can we have a set with 18 (int) and "18" (str) as value in it?
# s = set()
# s.add("18")
# s.add(18)
# print(s)

# Task_4
# What will be the length of following  set S:
# s =set()
# s.add(20)
# s.add(20.0)
# s.add('20')# length of s after these  operations?
# print(len(s)) #ans = 2

# Task_5
# s ={} #what is the type of S?
# print(type(s)) #ans = <class 'dict'>

# Task_6
# Create an empty dictionary. Allow to friends to enter their favorite language as value and use key as their manes.Assume that the names are unique
# d = {}
# name = input("Enter friends name: ")
# lang = input("Enter friends name: ")
# d.update({name: lang})
# name = input("Enter friends name: ")
# lang = input("Enter friends name: ")
# d.update({name: lang})
# print(d)

# Task_7
# if the names of 2 friends are same; What will happen to the program?
# d = {}
# name = input("Enter friends name: ")
# lang = input("Enter friends name: ")
# d.update({name: lang})
# name = input("Enter friends name: ")
# lang = input("Enter friends name: ")
# d.update({name: lang})
# print(d)

# Task_8
# if languages of two friends are same; what will happen to the program?
# d = {}
# name = input("Enter friends name: ")
# lang = input("Enter friends name: ")
# d.update({name: lang})
# name = input("Enter friends name: ")
# lang = input("Enter friends name: ")
# d.update({name: lang})
# print(d)

# Task_9
# can  you change the values inside a list which is contained in set S?
# S = {8, 7, 12, "Hary", [1, 2]}
# print(S) # the output is error beascuse does not allow if you want to change w need to change link bracket change in to round bracket

# Task_10
# Write a pyhton program to find the greatest of four numbers entered by the-user.
# a1 = int(input("Enter the number: "))
# a2 = int(input("Enter the number: "))
# a3 = int(input("Enter the number: "))
# a4 = int(input("Enter the number: "))
# a5 = int(input("Enter the number: "))
# if a1 > a2 and a1 > a3 and a1 > a4 and a1 > a5:
#     print("Greatest number is a1: ", a1)
# elif a2 > a1 and a2 > a3 and a2 > a4 and a2 > a5:
#     print("Greatest number is a1: ", a2)
# elif a3 > a2 and a3 > a1 and a3 > a4 and a3 > a5:
#     print("Greatest number is a1: ", a3)
# elif a4 > a2 and a4 > a3 and a4 > a1 and a4 > a5:
#     print("Greatest number is a1: ", a4)
# elif a5 > a2 and a5 > a3 and a5 > a4 and a5 > a1:
#     print("Greatest number is a1: ", a5)

# Task_11
# Write a pyhton program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects anc take marks as an input from the user.
# mark1 = int(input("Enter the number:"))
# mark2 = int(input("Enter the number:"))
# mark3 = int(input("Enter the number:"))
# total_Percentage = (100) * (mark1 + mark2 + mark3) / 300
# if total_Percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33:
#     print("You are passed", total_Percentage)
# else:
#     print("Your are failed", total_Percentage)

# Task_12
# A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now",
# "subscribe this", "click this". Write a program  to detect these spams.
# p1 = "subscribe this"
# p2 = "click this"
# p3 = "Make a lot of money"
# p4 = "buy now"
# message = input("Enter your message")
# if (p1 in message) or (p1 in message) or (p1 in message) or (p1 in message):
#     print("The message is spam")
# else:
#     print("The message is not spam")

# Task_13
# Write a pyhton program to find whether a given username contains less than 10 characters or not.
# username = input("Enter your username: ")
# if len((username) < 18):
#     print("Your username contains less then 10 characters")
# else:
#     print("all is good!")

# Task_14
# write a pyhton program which finds out wheather a given names is present ina list or not
# i = ["Fakhir", "Ahmed", "Khan"]
# name = input("Enter your list: ")
# if name in i:
#     print("Enter name is in the list")

# Task_15
# write a pyhton program to calculate the grade of a student from his marks formthe follwing  scheme:
# 90 - 100 =>EX
# 80 - 90 =>A
# 70 - 80 =>b
# 60 - 70 =>c
# 50 - 60 =>d
# <50 =>F
# mark = int(input("Enter your mark: "))
# if mark <= 100 and mark >= 90:
#     grade = "Ex"
# elif mark < 90 and mark >= 80:
#     grade = "A"
# elif mark < 80 and mark >= 70:
#     grade = "B"
# elif mark < 70 and mark >= 60:
#     grade = "C"
# elif mark < 60 and mark >= 50:
#     grade = "D"
# elif mark < 50:
#     # grade = "f"
# print("Your grade is:", grade)

# Task_16
# write a pyhton program to find out wheather a given post is talking about "Harry" or not.
# post = input("Enter the post: ")
# if ("Fakhri" in post) or ("amhed" in post) or ("Kan" in post):
#     print("The is talking about fakhir ")
# else:
#     print("The is talking an other person")

# Task_17
# Write a program to print multiplication table of a given number using for loop
# n = int(input("Enter the number: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# Task_18
# Write a program to greet all the person names stored in a list and which starts with S. l=["Harry", "Soham", "Sachin", "Rahul"]
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for name in l:
#     if name.startswith("S"):
#         print(f"Hello {name}")

# Task_19
# Attempt problem 1 using while loop
# i = 0
# while i < 11:
#     print(f"{n} x {i} = {n * i}")
#     i += 1
# n = int(input("Enter the number: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# Task_20
# Write a program to find whether a given number is prime or not
# num = int(input("Enter a number: "))
# is_prime = True
# if num < 2:
#     is_prime = False
# for i in range(2, int(num**0.5) + 1):
#     if num % i == 0:
#         is_prime = False
# if is_prime:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# Task_21
# Write a program to calculate the factorial of a given number using for loop.
# n = int(input("Enter a number: "))

# for i in range(2, n):
#     if n % i == 0:
#         print(f"{n} is not a prime number.")
#         break
# else:
#     print(f"{n} is a prime number.")

# Task_22
# Write a program to print the following star pattern
# n = 5
# for i in range(1, n + 1):
#     print("*" * i)

# Task_23
# Write a program to print the following star pattern
# n = 5
# for i in range(n, 0, -1):
#     print("*" * i)

# n = 5
# for i in range(1, n + 1):
#     print("*" * i)

# Task_24
# Write a program to find the sum of first n natural numbers using while loop.
# n = 5
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(f"The sum of first {n} natural numbers is {sum}.")


# # Task_25
# # Write a program using functions to find greatest of three numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# def find_greatest(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > c:
#         return b
#     else:
#         return c

# greatest = find_greatest(a, b, c)
# print(f"The greatest number is: {greatest}")

# #Task_26
# # Write a python program using function to convert Celsius to Fahrenheit.
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# # Task_27
# # How do you prevent a fython print() function to print a new line at the end.
# print("Hello", end=" ")
# print("World", end="!")

# # Task_28
# # Write a recursive function to calculate the sum of first n natural numbers
# def sum_of_natural_numbers(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum_of_natural_numbers(n - 1)

# # Task_29
# # Write a python function to print first n lines of the following pattern
# def print_pattern(n):
#     for i in range(1, n + 1):
#         print("*" * i)

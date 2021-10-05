#!/usr/bin/env python
# coding: utf-8

# 1.
# a.

# In[3]:


day_of_the_week = input("What day is it? ")

if (day_of_the_week == "Monday" or day_of_the_week == "monday"):
      print("Looks like somebody's got a case of the Monday's")
else:
      print("Lucky for you it's not Monday!")


# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# In[6]:


day_of_the_week = input("What day is it? ")

if (day_of_the_week == "Monday" or day_of_the_week == "monday"
    or day_of_the_week == "Tuesday" or day_of_the_week == "tuesday"
    or day_of_the_week == "Wednesday" or day_of_the_week == "wednesday"
    or day_of_the_week == "Thursday" or day_of_the_week == "thursday"
    or day_of_the_week == "Friday" or day_of_the_week == "friday"):
    print("A weekday?! How dreary")
elif (day_of_the_week == "Saturday" or day_of_the_week == "saturday" 
    or day_of_the_week == "Sunday" or day_of_the_week == "sunday"):
    print("I am doing nothing but sitting and watching football all weekend")
else:
    print("I don't know if you understand how this game works.")


# c. create variables and make up values for
# 
# - the number of hours worked in one week
# - the hourly rate
# - how much the week's paycheck will be
# 
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[14]:


hours_worked = 80.00
hourly_rate = 50.00
paycheck_total = 0

if hours_worked <= 40:
    paycheck_total = round((hours_worked * hourly_rate), 2)
    print("You will be paid: {:,.2f}".format(paycheck_total)) #Formatting options
elif hours_worked > 40:
    paycheck_total = (40 * hourly_rate) + ((hours_worked - 40) * (hourly_rate * 1.5))
    print("You will be paid: {:,.2f}".format(paycheck_total))
else:
    print("There is a glitch in the Matrix")


# 2. Loop Basics
# 
#     a. While
#        - Create an integer variable i with a value of 5.
#        - Create a while loop that runs so long as i is less than or equal to 15
#        - Each loop iteration, output the current value of i, then increment i by one.

# In[16]:


i = 5
while i <= 15:
    print(i)
    i += 1    


#     - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# In[17]:


i = 0
while i <= 100:
    print(i)
    i += 2   


# In[18]:


i = 100
while i >= -10:
    print(i)
    i -= 5 


#     - Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

# - Write a loop that uses print to create the output shown below. (100 down to 5 by 5s)

# In[19]:


i = 100
while i >= 5:
    print(i)
    i -= 5 


# b. For Loops
# 
#     i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# In[36]:


user_number = int(input("Enter a number: "))

for i in range(1,11):
    total = i * user_number
    print(user_number, ' x ', i, ' = ', total)

print(i * user_number)

    ii. Create a for loop that uses print to create the output shown below.


    1
    22
    333
    4444
    55555
    666666
    7777777
    88888888
    999999999
# In[31]:


for num in range(1,10):
    print(str(num) * num)


# c. break and continue
# 
#     i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# In[ ]:


while 1 == 1:
    user_number = int(input("Enter an odd number between 1 and 50: "))
    if (user_number % 2 == 1) and (user_number > 0) and (user_number < 50):  #Validate user inputd as odd between 1 & 50
        break
    print("Apparently you don't understand how the game is played, please try again.")

print("Number to skip is", user_number)
for i in range(1,50,2):  #Loop through 1 to 50 counting by 2
    if (i == user_number):
        print("Yikes! Skipping number ", user_number)
    else:
        print("Here is an odd number: ", i)


# d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# In[46]:


while 1 == 1:
    user_input = int(input("Enter a positive integer:"))
    if (user_input > 0):
        break
    print("Apparently you don't understand how the game is played, please try again.")

for i in range(0, user_input + 1):
    print(i)


# e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# In[49]:


while 1 == 1:
    user_input = int(input("Enter a positive integer:"))
    if (user_input > 0):
        break
    print("Apparently you don't understand how the game is played, please try again.")

for i in range(user_input, 0, -1):
    print(i)


# 3. Fizzbuzz
# 
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# 
# - Write a program that prints the numbers from 1 to 100.
# - For multiples of three print "Fizz" instead of the number
# - For the multiples of five print "Buzz".
# - For numbers which are multiples of both three and five print "FizzBuzz".

# In[50]:


for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)


# 4. Display a table of powers.
# 
# - Prompt the user to enter an integer.
# - Display a table of squares and cubes from 1 to the value entered.
# - Ask if the user wants to continue.
# - Assume that the user will enter valid data.
# - Only continue if the user agrees to.

# In[ ]:


while 1 == 1:
    user_input = int(input("What would you like to go up to:"))
    print("Here is your table!")
    print("")
    print("number | squared | cubed")
    for i in range(1, user_input +1):
        print(i, " | ", i**2, " | ", i**3)
    go_again = input("Would you like to continue? y/n: ")
    if go_again == 'n':
        break


# 5. Convert given number grades into letter grades.
# 
#  - Prompt the user for a numerical grade from 0 to 100.
#  - Display the corresponding letter grade.
#  - Prompt the user to continue.
#  - Assume that the user will enter valid integers for the grades.
#  - The application should only continue if the user agrees to.
#  - Grade Ranges:
# 
#      - A : 100 - 88
#      - B : 87 - 80
#      - C : 79 - 67
#      - D : 66 - 60
#      - F : 59 - 0

# In[ ]:


while 1 == 1:
    while 1 == 1:
        user_number = int(input("Enter grade between 0 and 100: "))
        if (user_number >= 0) and (user_number <= 100): #Validate user inputd as odd between ) & 100
            break
        print("Apparently you don't understand how the game is played, please try again.")
    if user_number <= 59:
        print("Your letter grade was an F.")
    elif user_number <= 66:
        print("Your letter grade was a D.")
    elif user_number <= 79:
        print("Your letter grade was a C.")
    elif user_number <= 87: 
        print("Your letter grade was a B.")
    elif user_number <= 100:
        print("Your letter grade was an A.")
    else:
        print ("There is a glitch in the Matrix.")
    go_again = input("Would you like to continue? y/n: ")
    if go_again == 'n':
        break


# In[ ]:


print("Something")


# In[ ]:





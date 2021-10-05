#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())


# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
# 

# In[3]:


uppercased_fruits = []
for fruit in fruits:
    uppercased_fruits.append(fruit.upper())
print(uppercased_fruits)


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

# In[5]:


capitalized_fruits = []
for fruit in fruits:
    capitalized_fruits.append(fruit.capitalize())
print(capitalized_fruits)


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

# In[11]:


fruits_with_more_than_two_vowels =[]
for fruit in fruits:
    vowel_count = 0
    for f in fruit:
        if f in 'aeiou':
            vowel_count += 1
    if vowel_count >= 2:
        fruits_with_more_than_two_vowels.append(fruit)
print(fruits_with_more_than_two_vowels)


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# In[12]:


fruits_with_only_two_vowels =[]
for fruit in fruits:
    vowel_count = 0
    for f in fruit:
        if f in 'aeiou':
            vowel_count += 1
    if vowel_count == 2:
        fruits_with_only_two_vowels.append(fruit)
print(fruits_with_only_two_vowels)


# Exercise 5 - make a list that contains each fruit with more than 5 characters

# In[15]:


fruits_more_than_five_char =[]
for fruit in fruits:
    if len(fruit) > 5:
        fruits_more_than_five_char.append(fruit)
print(fruits_more_than_five_char)


# Exercise 6 - make a list that contains each fruit with exactly 5 characters

# In[16]:


fruits_with_five_char =[]
for fruit in fruits:
    if len(fruit) == 5:
        fruits_with_five_char.append(fruit)
print(fruits_with_five_char)


# Exercise 7 - Make a list that contains fruits that have less than 5 characters

# In[17]:


fruits_less_than_five_char =[]
for fruit in fruits:
    if len(fruit) < 5:
        fruits_less_than_five_char.append(fruit)
print(fruits_less_than_five_char)


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# In[18]:


fruits_char_count =[]
for fruit in fruits:
    fruits_char_count.append(len(fruit))
print(fruits_char_count)


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# In[20]:


fruits_with_letter_a =[]
for fruit in fruits:
    a_count = 0
    for f in fruit:
        if f == 'a':
            a_count += 1
    if a_count > 0:
        fruits_with_letter_a.append(fruit)
print(fruits_with_letter_a)


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

# In[21]:


even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

# In[22]:


odd_numbers = []
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)
print(odd_numbers)


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

# In[23]:


positive_numbers = []
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
print(positive_numbers)


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

# In[24]:


negative_numbers = []
for num in numbers:
    if num < 0:
        negative_numbers.append(num)
print(negative_numbers)


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

# In[25]:


more_than_two_numerals = []
for num in numbers:
    if (num >= 10) or (num <= -10):
        more_than_two_numerals.append(num)
print(more_than_two_numerals)


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
# 

# In[27]:


numbers_squared = []
for number in numbers:
    numbers_squared.append(number ** 2)
print(numbers_squared)


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# In[29]:


odd_negative_numbers = []
for num in numbers:
    if (num % 2 == 1) and (num < 0):
        odd_negative_numbers.append(num)
print(odd_negative_numbers)


# Make a variable named numbers_plus_5. In it, return a list containing each number plus five.

# In[30]:


numbers_plus_5 = [number + 5 for number in numbers]
print(numbers_plus_5)


# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

# In[32]:


def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True

primes = []
for num in numbers:
    if isPrime2(num):
        primes.append(num)
print(primes)


# In[ ]:





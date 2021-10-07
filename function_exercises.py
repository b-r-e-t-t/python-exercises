#!/usr/bin/env python
# coding: utf-8

# ### 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[1]:


def is_two(user_input):
    #checking to see if input is either the int 2 or str '2'
    if (user_input == '2') or (user_input == 2):
        return(True)
    else:
        return(False)


# ### 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[11]:


def is_vowel(user_input):
    #checking to see if string/char is a vowel
    if str(user_input) in 'aeiou':
        return(True)
    else:
        return(False)


# ### 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[16]:


def is_consonant(user_input):
    if (not is_vowel(user_input)):
        return(True)
    else:
        return(False)


# ### 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[20]:


def cap_con(user_input):
    #if the first character in the string is a consonant, capitalize the string
    if user_input[0] in 'bcdfghjklmnpqrstvwxyz':
        return(user_input.capitalize())
    #if not, return the string as-is
    else:
        return(user_input)


# ### 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[47]:


def calculate_tip(tip_percent, bill_total):
    #check that tip_percent is valid, if not return 0
    if (float(tip_percent) < 0) or (float(tip_percent) > 1):
        print("Invalid tip amount specified.")
        return(0)
    #if input was good, multiply tip percent by total to get tip amount
    else:
        return (float(tip_percent) * float(bill_total))


# ### 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[49]:


def apply_discount(original_price, discount_percent):
    return(float(original_price) - (float(original_price)*float(discount_percent)))


# ### 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[57]:


def handle_commas(comma_number):
    no_comma_number = ''
    comma_number = str(comma_number)
    #iterate over string keep everything that isn't a comma
    for i in comma_number:
        if i != ',':
            no_comma_number += i
    return(float(no_comma_number))


# ### 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[59]:


def get_letter_grade(user_number):
    if user_number <= 59:
        return('F')
    elif user_number <= 66:
        return('D')
    elif user_number <= 79:
        return('C')
    elif user_number <= 87: 
        return('B')
    elif user_number <= 100:
        return('A')
    else:
        print ("There is a glitch in the Matrix.")
        return('X')


# ### 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[64]:


def remove_vowels(user_string):
    no_vowel_string = ''
    #loop over the string and only add consonants to the new string
    for i in user_string:
        if i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            no_vowel_string += i
    return(no_vowel_string)


# ### 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is anything that is not a valid python identifier should be removed
# 
#     - leading and trailing whitespace should be removed
#     - everything should be lowercase
#     - spaces should be replaced with underscores
#     - for example:
#        - Name will become name
#        - First Name will become first_name
#        - % Completed will become completed

# In[193]:


def normalize_name(non_normal_name):
    s = non_normal_name
    #strips everything to the first alpha character
    while (not s[0].isalpha()) or (s[0].isspace()): s = s[1:]
        
    #converts everything to lowercase & strips trailing whitespace
    removed_space_name = s.lower().rstrip()  
    normalized_name = ''
    
    #iterate over the new string swapping ' ' for '_' and skipping everything that isn't alphanumeric
    for i in removed_space_name:
        if i == ' ':
            normalized_name += '_'
        elif i.isalnum(): #elif i in 'abcdefghijklmnopqrstuvwxyz1234567890':
            normalized_name += i
            
    #Now check to make sure the final product is not a python keyword
    if normalized_name in keyword.kwlist:
        return("Error: Using a python keyword is not permitted.")
    return(normalized_name)


# ### 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[121]:


def cumulative_sum(list_of_nums):
    temp_list = []
    running_total = 0
    # for loop will iterate over each item in the list
    for i in list_of_nums:
        #take the item from the list, add running total, and append to new list
        temp_list.append(i + running_total)
        running_total += i
    return(temp_list)


# ### B1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 

# In[190]:


def twelveto24(mickey_mouse_time):
    #the first hour of the day special case
    if '12' in mickey_mouse_time and (('am' in mickey_mouse_time) or ('AM' in mickey_mouse_time)):
        #replaces the 12 with 00 and tacks the minutes back on without the 'am'
        return ('00' + mickey_mouse_time[2:5])
    
    #if the time is AM, strip off the AM and return
    elif ('am' in mickey_mouse_time):
        return mickey_mouse_time.rstrip('am')
    
    #if the time is PM
    elif ('pm' in mickey_mouse_time):
        s = mickey_mouse_time
        hour = ''
        
        #Pull the hours off the front
        while s[0] != ':':
            hour += s[0]
            s = s[1:]
        #add 12 to that number (unless we're in the 12pm hour)
        if int(hour) > 12:
            hour = int(hour) + 12
        
        #put the hours back, strip off PM and return
        s = str(hour) + s
        s = s.rstrip('pm')
        return s


# In[192]:


twelveto24('12:30am')


# ### Bonus write a function that does the opposite.

# In[179]:


def twentyfourto12(military_time):
    
    hour = ''
    s = military_time
    #Pop the hours off
    while s[0] != ':':
        hour += s[0]
        s = s[1:]
    #In 12am/00 hour
    if int(hour) == 0:
        s = '12' + s + 'am'
        return(s)
    #From 1am - 11am
    elif int(hour) <= 11:
        s = str(hour) + s + 'am'
        return(s)
    #In the 12 pm hour
    elif int(hour) <= 12:
        s = str(hour) + s + 'pm'
        return(s)
    #From 1300 - 2359
    elif int(hour) <= 23:
        s = str(int(hour) - 12) + s + 'pm'
        return(s)
    #If whatever was passed didn't fit in the 24hour clock
    else:
        return("There is a glitch in the matrix")


# In[180]:


twentyfourto12('12:00')


# In[ ]:





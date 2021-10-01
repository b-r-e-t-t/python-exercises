#!/usr/bin/env python
# coding: utf-8

# Create a Python script file named data_types_and_variables.py. Inside it, write some Python code, that is, variables and operators, to describe the following scenarios. Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions can be represented with code.
# 
# - You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

# In[1]:


Little_Mermaid = 3
Hercules = 1
Brother_Bear = 5
Cost_per_day = 3

Total_Cost = (Brother_Bear + Little_Mermaid + Hercules) * Cost_per_day
print("Total Movie Cost is: ", Total_Cost)


# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

# In[2]:


Google_Rate = 400
Amazon_Rate = 380
Facebook_Rate = 350
Google_Hours = 6
Amazon_Hours = 4
Facebook_Hours = 10
Weekly_Earned = (Google_Rate * Google_Hours) + (Amazon_Rate * Amazon_Hours) + (Facebook_Rate * Facebook_Hours)
print("Total Earned for the week before tax and expenses is: $", Weekly_Earned)


# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

# In[7]:


Class_Full = False
Class_Conflict = False
Allow_Enroll = not (Class_Full) and not (Class_Conflict)
print(Allow_Enroll)


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

# In[9]:


Item_Count = 2
Offer_Expired = False
Premium_Member = False
Apply_Offer = ((Item_Count >= 2) and not Offer_Expired) or Premium_Member
print(Apply_Offer)


# Use the following code to follow the instructions below:

# In[55]:


username = 'codeup'
password = 'notastrongpassword'


# Create a variable that holds a boolean value for each of the following conditions:
# 
# - the password must be at least 5 characters
# - the username must be no more than 20 characters
# - the password must not be the same as the username
# - bonus neither the username or password can start or end with whitespace

# In[56]:


Min_Password_Length = len(password) >= 5
Max_Username_Length = len(username) <= 20
Username_Not_Password =  username != password
No_Spaces_Username = not (username[0].isspace() or username[-1].isspace())
No_Spaces_Password = not (password[0].isspace() or password[-1].isspace())
print(No_Spaces_Username)
print(No_Spaces_Password)


# In[ ]:





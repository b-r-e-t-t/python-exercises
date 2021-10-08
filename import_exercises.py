#!/usr/bin/env python
# coding: utf-8

# In[1]:


from function_exercises import calculate_tip


# In[2]:


calculate_tip(.2, 100)


# In[3]:


import itertools as it


# ### How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# In[4]:


list(it.combinations('ABC123', 3))


# In[26]:


len(list(it.permutations('ABCD', 2)))


# In[27]:


len(list(it.combinations('ABCD', 2)))


# In[7]:


import json

user_list = json.load(open('profiles.json'))


# ### Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
# 
# - Total number of users

# In[8]:


len(user_list)


# - Number of active users

# In[9]:


total_active = 0
for users in user_list:
    if users['isActive']:
        total_active += 1
print(total_active)


# - Number of inactive users

# In[10]:


total_inactive = 0
#loop through counting each user not active
for users in user_list:
    if not users['isActive']:
        total_inactive += 1
print(total_inactive)


# - Grand total of balances for all users

# In[11]:


user_total_balance = 0
#loop through the list looking at the users 'balance'
for users in user_list:
    money = users['balance']
    #converts the string to decimal amount by pulling only digits
    #and divide by 100 to get the cents back
    money = float("".join(d for d in money if d.isdigit()))/100
    user_total_balance += money
print(user_total_balance)


# - Average balance per user

# In[12]:


#Take total from previous question and divide by total users to get average
user_average_balance = round(user_total_balance/len(user_list), 2)
print(user_average_balance)


# - User with the lowest balance
# - User with the highest balance

# In[13]:


money = user_list[0]['balance']
money = float("".join(d for d in money if d.isdigit()))/100
user_low_balance = [user_list[0]['name'], money]
user_high_balance = [user_list[0]['name'], money]

for users in user_list:
    money = users['balance']
    #converts the string to decimal amount by pulling only digits
    #and divide by 100 to get the cents back
    money = float("".join(d for d in money if d.isdigit()))/100
    if money < user_low_balance[1]:
        user_low_balance = [users['name'], money]
    if money > user_high_balance[1]:
        user_high_balance = [users['name'], money]

print(user_low_balance)
print(user_high_balance)


# - Most common favorite fruit
# - Least most common favorite fruit

# In[14]:


fav_fruits = []

#Traverse list adding all favorite fruits to a list
for users in user_list:
    fav_fruits.append(users['favoriteFruit'])

print(max(fav_fruits))
print(min(fav_fruits))


# - Total number of unread messages for all users

# In[25]:


msg_tot = 0
#Traverse the list
for users in user_list:
    #Filter out anything that isn't numeric in greeting msg and convert to str
    msg_num = filter(str.isdigit, users['greeting'])
    msg_str = "".join(msg_num)
    #Convert to int & add to running total
    msg_tot += int(msg_str)
print(msg_tot)


# In[31]:


msg_tot = 0
for users in user_list:
    #A less readable version, working from inside out...
    #Filters out anything that's not a digit, takes the list, joins it to a string,
    #converts it to an int, and adds to the runnig total
    msg_tot += int("".join(list(filter(str.isdigit, users['greeting']))))
print(msg_tot)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Zomato data analysis project

# # Step 1- Importing Libraries

# In[ ]:


#Pandas is used for data manipulation and analysis.
#numpy is used for numerical operations.
#matplotlib.pyplot and seaborn are used for data visualisation.


# In[2]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


# # Step 2- Create the data frame

# In[4]:


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe)


# In[5]:


dataframe


# # Convert the data type of column -rate

# In[8]:


def handleRate(value):
    value = str(value).split('/')
    value = value[0];
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[9]:


dataframe.info()


# # 1) What type of restaurant do the majority of customers order from?

# In[10]:


dataframe.head()


# In[12]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type of restaurant")


# # Conclusion - majority of the restaurant falls in dining category

# # 2) How many votes has each type of restaurant received from customers?

# In[13]:


dataframe.head()


# In[14]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of restaurant", c="red", size=20)
plt.ylabel("Votes", c="red", size=20)


# # Conclusion - Dining restaurants has received maximum votes

# # 3) What are the ratings that the majority of restaurants have received ?

# In[15]:


dataframe.head()


# In[16]:


plt.hist(dataframe['rate'],bins =5)
plt.title("ratings distribution")
plt.show()


# # Conclusion - the majority restaurant received ratings from 3.5 to 4.0

# # 4) Zomato has observed that most couples order most of their food online. What is their average spending on each order?

# In[17]:


dataframe.head()


# In[18]:


couple_data = dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # Conclusion - The majority of couples prefer restaurants with an approximate cost of 300 rupees

# # 5) Which mode (online or offline) has received the maximum rating?

# In[19]:


dataframe.head()


# In[20]:


plt.figure(figsize =(6,6))
sns.boxplot(x= 'online_order',y= 'rate', data = dataframe)


# # Conclusion - Offline order received lower rating in comparison to online order

# # 6) Which type of restaurant received more offline orders, so that Zomato can provide customers with some good offers?

# In[22]:


dataframe.head()


# In[21]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()


# # Conclusion -Dining restaurants primarily accept offline orders, whereas cafes primarily receive online orders. This suggests that clients prefers orders in person at restaurants, but prefer online ordering at cafes.

# In[ ]:





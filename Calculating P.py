#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


# In[2]:


data=pd.read_csv('Urfa_Dailyrainfall_2013_2024 .csv')
data


# In[3]:


data.isnull().sum()


# In[4]:


df = pd.DataFrame(data)


# In[5]:


df


# In[6]:


df['DATE'] = pd.to_datetime(df['DATE'])
df


# In[7]:


df.set_index('DATE', inplace=True)
df


# In[8]:


monthly_rainfall = df.resample('M').sum()


# In[9]:


print(monthly_rainfall)


# In[10]:


import matplotlib.pyplot as plt


# In[30]:


plt.figure(figsize=(10, 6))
plt.plot(df)
plt.savefig('image3.png', dpi=300)  # Adjust the DPI as needed
plt.show()


# In[31]:


start_date = '2023-01-31'
end_date = '2024-12-31'

filtered_df = df.loc[start_date:end_date]
filtered_df 


# In[33]:


plt.figure(figsize=(10, 6))
plt.plot(filtered_df)
plt.savefig('image4.png', dpi=300)  # Adjust the DPI as needed
plt.show()


# In[23]:


plt.savefig('Urfa_Monthlyrainfall_2023_2024.jpg')


# In[17]:


start_date = '2022-01-31'
end_date = '2022-12-31'

filtered_df2 = df.loc[start_date:end_date]
filtered_df2 


# In[18]:


plt.plot(filtered_df2, label='Line Plot')


# In[19]:


data=pd.read_csv('Urfa_monthly_rainfall_2013_2023.csv')
data


# In[20]:


data['Year'] = pd.to_datetime(data['DATE']).dt.year
data['Month'] = pd.to_datetime(data['DATE']).dt.month


# In[21]:


data = data.drop(columns=['DATE'])
data


# In[22]:


data


# In[ ]:





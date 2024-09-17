#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv(r"C:\Users\Owner\OneDrive\Documents\Data Analyst\Pandas file reading\Deathdata.csv")

df


# In[2]:


df.info()


# In[3]:


df.shape


# In[6]:


num = df.select_dtypes(include=np.number).columns
len(num)


# In[10]:


r = 3
c = 4
it = 1
for i in num:
    plt.subplot(r,c,it)
    sns.histplot(df.loc[:,i])
    plt.title(i)
    plt.grid()
    it+=1
plt.tight_layout()
plt.show()


# In[11]:


rate = pd.read_csv(r"C:\Users\Owner\OneDrive\Documents\Data Analyst\Pandas file reading\rate.csv")
rate.head()


# In[12]:


rate.info()


# In[13]:


rate.shape


# In[14]:


sns.lineplot(x='YEAR',y='POPULATION',data=rate,color='blue')
plt.grid()
plt.show()


# In[15]:


sns.lineplot(x='YEAR',y='RATEBIRTH',data=rate,color='green')
sns.lineplot(x='YEAR',y='RATEDEATH',data=rate,color='purple')

plt.grid()
plt.show()


# In[16]:


sns.lineplot(x='POPULATION',y='RATEBIRTH',data=rate)
plt.grid()
plt.show()


# In[17]:


sns.lineplot(x='POPULATION',y='RATEDEATH',data=rate)
plt.grid()
plt.show()


# In[18]:


states = pd.read_csv(r"C:\Users\Owner\OneDrive\Documents\Data Analyst\Pandas file reading\states.csv")
states.head()


# In[19]:


states.info()


# In[20]:


states.shape


# In[21]:


sns.barplot(x='States',y='People',data=states)
plt.xticks(rotation=90)
plt.show()


# In[22]:


sns.barplot(x='States',y='Female',data=states)
plt.xticks(rotation=90)
plt.show()


# In[23]:


sns.barplot(x='States',y='Male',data=states)
plt.xticks(rotation=90)
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import datetime
import psycopg2


# In[2]:


df1=pd.read_csv("all_years_o3.csv")
df1.head()


# In[3]:


df1.drop(df1.columns[[3,5,6,7]],axis=1,inplace=True)
df1.head()


# In[4]:


df2=pd.read_csv("all_years_pm25.csv")
df2.head()


# In[5]:


df2.drop(df2.columns[[3,5,6,7]],axis=1,inplace=True)
df2.head()


# In[7]:


df3=pd.merge(df1,df2, how='left',left_on=['Date','Country','City'],right_on=['Date','Country','City'])
df3.head()


# In[11]:


from sqlalchemy import create_engine
p_engine=create_engine("postgresql://postgres:shivani@localhost:5432/air_etl")


# In[13]:


df=pd.DataFrame(df3)
df.to_csv("Downloads/file1.csv")


# In[14]:


df4=pd.read_csv('Downloads/file1.csv',index_col=False)
df4.to_sql('file1',p_engine,if_exists='replace',index=False)


# In[ ]:





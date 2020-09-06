#!/usr/bin/env python
# coding: utf-8

# # pilot example(assignment 1)

# In[2]:


num=input("enter number..")


# In[6]:


num=input("enter the number..")

if num <= '1000':
    print("Safe to land")
elif num>'1000' and num<='5000':
    print("bring down to 1000")
else:
    print("turn around")


# # assignment 2

# In[16]:


for i in range(2,202):
    for j in range(2,i):
        if i%j==0:
           break
    else:
        print(i)


# In[ ]:





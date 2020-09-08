#!/usr/bin/env python
# coding: utf-8

# # hw-1

# In[4]:


lst=list(range(1,2500))
def prime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True


# In[5]:


prime_one=filter(prime,lst)


# In[6]:


print(list(prime_one))


# # hw-2

# In[21]:


str="hey this is sai.i am in mumbai"
def check(str):
    return str


# In[22]:


checkLambdaVersion=lambda str:str.title()


# In[23]:


checkLambdaVersion(str)


# # hw-3

# In[1]:


def Input():
    numList=[]
    i=0
    while i < 7:
        value = int(input(f"Enter Number from 1 to 100   {i+1}: "))
        numList.append(value)
        i+=1
    return numList


def checking(s):
    compareList = [1,1,5]
    for i in s:
        for j in compareList:
            if(len(compareList)>=0 and j == i):
                compareList.pop(0)
            else:
                break
    
    if len(compareList)==0:
        return "Congratulation,It's a match"
    else:
        return "Try agian,It's gone"


compareList = Input()        
print("User List is :",compareList)
checking(compareList)


# In[ ]:





# In[ ]:





# In[ ]:





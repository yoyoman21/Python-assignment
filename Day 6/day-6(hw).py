#!/usr/bin/env python
# coding: utf-8

# 
# # assignment1

# In[6]:


class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the bankapkeliye Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
  
            


# In[7]:


s = Bank_Account() 


# In[3]:


s.deposit() 


# In[4]:


s.withdraw() 


# In[5]:


s.display() 


# # assignment-2

# In[24]:


import math
class cone():
    def __init__(self,r,h):
        self.r=r
        self.h=h
    def volume(self):
        result_of_volume=3.14*self.r*self.r*(self.h/3)
        print(result_of_volume,"=volume of cone")
    def Surfacearea(self):
        base=3.14*self.r*self.r
        s1=math.sqrt(self.r*self.r+self.h*self.h)
        side=3.14*self.r*s1
        result_of_area=base+side
        print(result_of_area,"=surface area of cone")


# In[25]:


final=cone(5,7)


# In[26]:


final.volume()


# In[27]:


final.Surfacearea()


# In[ ]:





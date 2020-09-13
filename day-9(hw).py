#!/usr/bin/env python
# coding: utf-8

# In[39]:


get_ipython().run_cell_magic('writefile', 'samp_le.pylintrc', 'def is_prime(number):\n    """\n    Return True if *number* is prime.\n    """\n    for element in range(number):\n        if number % element == 0:\n            return False\n    return True\n\ndef print_next_prime(number):\n    """\n    Print the closest prime number larger than *number*.\n    """\n    index = number\n    while True:\n        index += 1\n        if is_prime(index):\n            print(index)')


# In[40]:


get_ipython().system(' pylint "samp_le.pylintrc"')


# # assignment 2

# In[16]:


# Program to check Armstrong numbers in a certain interval

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
 
for num in range(lower,upper + 1):
   # initialize sum
   sum = 0
 
   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num)
         


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





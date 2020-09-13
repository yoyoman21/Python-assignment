#!/usr/bin/env python
# coding: utf-8

# # assignment-1

# In[25]:


def sampleDecorator(func):
    def addingFunction():
        # some new statments or flow control
        print("hey i have added some text in this function dont forget.")
        # calling the function
        func()

    return addingFunction


@sampleDecorator
def actualFunction():
    print("this is a actual function .")


# In[26]:


actualFunction()


# # assignment2

# In[44]:


get_ipython().run_cell_magic('writefile', 'homework.py', 'home=open(homework.py)\nprint(home.read())')


# In[45]:


try:
    file_example = open ("homework.py")
    print("The file given is existed in read only format")
except IOError:
    print("An error was found. Either path is incorrect or file doesn't exist!")

finally:
    print("Terminating process!")


# In[ ]:





# In[ ]:





# In[ ]:





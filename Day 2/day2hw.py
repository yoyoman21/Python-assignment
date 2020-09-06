#!/usr/bin/env python
# coding: utf-8

# In[1]:


#list


# In[2]:


lst=["letsupgrade","cat",5,3,2.24,[2,"g",4]]


# In[3]:


lst.append(36)


# In[5]:


lst.copy()


# In[7]:


lst.count(5)


# In[8]:


lst[1]


# In[10]:


lst.index(36)


# In[12]:


lst.insert(3,9)


# In[14]:


lst.pop()


# In[15]:


lst.reverse()


# In[16]:


lst


# In[21]:


lst.reverse()


# In[22]:


lst


# In[23]:


lst.remove("cat")


# In[24]:


lst


# In[25]:


#dictionary


# In[26]:


dict={"name":"letsupgrade","rating":"5/5","teaching":"superb"}


# In[28]:


dict.get("rating")


# In[30]:


dict.fromkeys("superb")


# In[31]:


dict.copy()


# In[32]:


dict.values()


# In[33]:


dict.items()


# In[35]:


dict.setdefault("null")


# In[36]:


dict


# In[37]:


#sets


# In[45]:


set1={"a","b","f","p","t",8,6,9,0}
set2={"a","t","p",3,4,1}


# In[49]:


set1.add(10)


# In[50]:


set1.difference(set2)


# In[51]:


set1.intersection(set2)


# In[53]:


set1.isdisjoint(set2)


# In[54]:


set1.symmetric_difference(set2)


# In[55]:


set1.copy()


# In[56]:


set1.discard(0)


# In[68]:


set1.union(set2)


# In[60]:


set1


# #tuple

# In[61]:


tuple={"letsupgrade","@","gmail.","com"}


# In[62]:


tuple.add("email")


# In[64]:


tuple.issubset("com")


# In[65]:


tuple.issuperset("@")


# In[66]:


tuple.intersection()


# In[67]:


tuple.union()


# In[69]:


tuple.remove("email")


# In[70]:


tuple.pop()


# In[72]:


tuple.discard("@")


# In[73]:


tuple


# In[74]:


#string


# In[75]:


food1="chole bhature"
food2="chhese sandwish"
food3="dal bhat"


# In[79]:


food1.capitalize()


# In[81]:


food1.count("chole bhature")


# In[82]:


food2.islower()


# In[83]:


food2.upper()


# In[89]:


food3.isdecimal()


# In[ ]:





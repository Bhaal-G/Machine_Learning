#!/usr/bin/env python
# coding: utf-8

# #                                               Numpy

# In[1]:


pip install numpy


# # The Basics

# In[3]:


import numpy as np


# In[15]:


a=np.array([1,2,3],dtype='int16')#We can specify type of int
print(a)


# In[23]:


b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)


# In[10]:


#Get Dimension
a.ndim


# In[11]:


b.ndim


# In[12]:


#Get shape
a.shape


# In[13]:


b.shape


# In[16]:


a.dtype


# In[17]:


#Get item size
a.itemsize


# In[24]:


b.itemsize


# In[25]:


#Get total elements
a.size


# In[26]:


b.size


# In[28]:


#Get total size
a.nbytes


# In[29]:


b.nbytes


# #Accesing/Changing Specific elements,rows,columns etc.

# In[42]:


a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)


# In[32]:


#Get specific Element
a[1,5]


# In[33]:


a[1,-2]


# In[34]:


#Get specific Element
a[1,5]


# In[35]:


#Get Specific row
a[0,:]


# In[36]:


#Get Specific Column
a[:,2]


# In[70]:


#Getting little more fancy[startindex:endindex:Stepsize] if multidimensional [row,startindex:endindex:step]
a[0,1:6:2]
a[0,1:-1:2]
#Both upper syntax means same


# In[40]:


a[1,5]


# In[43]:


a[:,2]=5
print(a)


# In[44]:


a[:,2]=[1,2]
print(a)


# In[46]:


b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


# In[47]:


#Get Specific Elements work outside in
b[0,1,1]


# In[49]:


b[:,1,:]


# In[50]:


#Replace
b[:,1,:]=[[9,9],[8,8]]


# In[51]:


print(b)


# In[55]:


np.zeros((2,3))


# In[56]:


np.ones((4,2,2),dtype='int32')


# In[59]:


#An other number
np.full((2,2),99,dtype='float32')


# In[58]:


#Any other number(full_like)
np.full_like(a,44)


# In[60]:


#Random Decimal Numbers
np.random.rand(4,2)


# In[61]:


np.random.rand(4,3,2)


# In[62]:


np.random.random_sample(a.shape)


# In[66]:


#Random Integer values
np.random.randint(-4,8,size=(3,3))


# In[67]:


#The identuty Matrix
np.identity(5)


# In[69]:


#Repeat An Array
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)


# In[86]:


output=np.ones((5,5))
print(output)

z=np.zeros((3,3))
z[1,1]=9
output[1:4,1:4]=z
print(output)


# # Be careful when copying arrays!!!

# In[99]:


a=np.array([1,2,3])
d=np.array([1,2,3])
b=a
b[0]=100
print(b)
print(a)
#Both variable points to the same array
#Prevention
c=d.copy()
c[0]=100
print(d)
print(c)


# In[ ]:





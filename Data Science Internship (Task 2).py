#!/usr/bin/env python
# coding: utf-8

# # Name = Xeviers Koner 
# 
# 
# ## Task= Image to Pencil Sketch with Python

# ##  1. importing libraries

# In[1]:


import cv2
import matplotlib.pyplot as plt
plt.style.use('seaborn')


# ## 2. loading the original image

# In[14]:


img_1 = cv2.imread("C:\\Users\\User\\Downloads\\virat.jpeg")


# In[45]:


img_1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.show()


# ## 3. converting image to a grey scale image

# In[16]:


img_1_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# In[42]:


plt.figure(figsize=(10,10))
plt.imshow(img_1_gray,cmap="gray")
plt.axis("off")
plt.title("GrayScale Image")
plt.show()


# ## 4. inverting the image

# In[18]:


img_1_invert = cv2.bitwise_not(img_gray)


# In[41]:


plt.figure(figsize=(10,10))
plt.imshow(img_1_invert,cmap="gray")
plt.axis("off")
plt.title("Inverted Image")
plt.show()


# In[40]:


img_1_smoothing = cv2.GaussianBlur(img_1_invert, (21, 21),sigmaX=0, sigmaY=0)


# In[38]:


plt.figure(figsize=(10,10))
plt.imshow(img_1_smoothing,cmap="gray")
plt.axis("off")
plt.title("Smoothen Image")


# ## 5. converting our image to pencil sketch

# In[35]:


final_1 = cv2.divide(img_gray, 255 - img_1_smoothing, scale=255)


# In[37]:


plt.figure(figsize=(10,10))
plt.imshow(final_1,cmap="gray")
plt.axis("off")
plt.title("Final Pencil Sketch Image")
plt.show()
plt.show()


# In[ ]:





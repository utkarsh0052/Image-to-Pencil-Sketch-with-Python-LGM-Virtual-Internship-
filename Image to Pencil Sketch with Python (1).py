#!/usr/bin/env python
# coding: utf-8

# # Let's Grow More Virtual Internship Program:
# Task Name: Image to Pencil Sketch
#     By Utkarsh Sharma

# # Importing Libraries

# In[21]:


get_ipython().system('pip install imageio')


# In[22]:


import imageio
import requests
import matplotlib.pyplot as plt
import IPython.display as dp


# # Reading and importing the Image

# In[23]:


img = 'https://www.thesprucepets.com/thmb/nosT3p7bteBk_Hf-BUJZJCXfRWQ=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/GettyImages-962608834-fd496cfed51e4d2abe61c0af864fa681.jpg'
dp.Image(requests.get(img).content)


# In[24]:


source_img = imageio.imread(r'C:\Users\Harshit Tyagi\Downloads\image\dog2.png')


# In[25]:


import numpy as np
def grayscaleing(rgb):
  return np.dot(rgb[...,:3],[0.299,0.587,0.114])
gryscl_img = grayscaleing(source_img)


# In[26]:


inv_img = (255 - gryscl_img)
plt.imshow(inv_img)


# In[27]:


import scipy.ndimage
blurred_img = scipy.ndimage.filters.gaussian_filter(inv_img, sigma=5)
plt.imshow(blurred_img)


# In[28]:


def dodging(blur_img,gryscl_img):
  resultant_dodge=blur_img*255/(255-gryscl_img)
  resultant_dodge[resultant_dodge>255]=255
  resultant_dodge[gryscl_img==255]=255
  return resultant_dodge.astype('uint8')


# In[29]:


target_img= dodging(blurred_img, gryscl_img)


# In[30]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.imshow(target_img, cmap='gray')


# # Thankyou

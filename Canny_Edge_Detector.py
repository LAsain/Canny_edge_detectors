
# coding: utf-8

# In[1]:


pwd


# In[2]:


import os


# In[3]:


os.chdir('C:\\Users\\Umar\\Desktop\\CV2')


# In[4]:


import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('C:/Users/Umar/Desktop/CV2/DataSet(Input)/zalatan.jpg',0)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()


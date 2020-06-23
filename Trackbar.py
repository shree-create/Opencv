#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np

def nothing(x):
    print(x)


img=np.zeros((512, 512, 3),np.uint8)
windowname='Image'
cv2.namedWindow(windowname)
cv2.createTrackbar('B', windowname, 0, 255, nothing)
cv2.createTrackbar('G', windowname, 0, 255, nothing)
cv2.createTrackbar('R', windowname, 0, 255, nothing)

switch ='0 : OFF\n 1: ON'
cv2.createTrackbar(switch, windowname, 0, 1, nothing)

while(True):
    cv2.imshow(windowname,img)
    if cv2.waitKey(1) == 27:
        break
        
    blue=cv2.getTrackbarPos('B', windowname)
    green=cv2.getTrackbarPos('G', windowname)
    red=cv2.getTrackbarPos('R', windowname)
    s=cv2.getTrackbarPos(switch, windowname)
    if s == 0:
        img[:] = 0
    else:
        img[:]=[blue, green, red]
   
    
cv2.destroyAllWindows()


# In[ ]:





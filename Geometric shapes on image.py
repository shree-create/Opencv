#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
img=cv2.imread('lena_color_512.tif',1)
img=cv2.line(img, (0,0), (512,512), (255, 0, 0), 3)
img=cv2.arrowedLine(img, (0,250), (250,240), (255, 0, 0), 3)
img=cv2.rectangle(img, (250,0), (512,200), (0, 0, 255), -1)
img=cv2.circle(img, (250,250), 60, (0, 255, 0), 3)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img, 'YOUR TEXT', (40,500), font, 2, (255, 255, 255), 5, cv2.LINE_AA)
cv2.imshow('image',img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()


# In[ ]:





import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('C:/Users/agno3/Desktop/1.jpg')

mask=np.zeros((img.shape[:2]),np.uint8)
bgdModel=np.zeros((1,65),np.float64)
fgdModel=np.zeros((1,65),np.float64)
rect=(81,189,587,1041)
#这里计算了5次
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,10,cv2.GC_INIT_WITH_RECT)
#关于where函数第一个参数是条件，满足条件的话赋值为0，否则是1。如果只有第一个参数的话返回满足条件元素的坐标。
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
#mask2就是这样固定的
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('original image ')
plt.xticks([])
plt.yticks([])
plt.subplot(1,2,2)
#这里的img也是固定的。
img=img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.title('target image')
plt.xticks([])
plt.yticks([])
plt.show()

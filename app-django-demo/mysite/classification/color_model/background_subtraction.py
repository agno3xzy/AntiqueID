import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def bg_sb(pic_path, pic_name , pic_rect):

    img = cv2.imread(pic_path)
    mask = np.zeros((img.shape[:2]), np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    cv2.grabCut(img, mask, pic_rect, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]

    pic_name1 = 'pre1_' + pic_name
    pic_path1 = os.path.join(os.getcwd() + '/mysite/media/image_preprocessing/', pic_name1)
    pic_path1 = pic_path1.replace('\\', '/')

    cv2.imwrite(pic_path1, img)

    pic_name2 = 'pre2_' + pic_name
    pic_path2 = os.path.join(os.getcwd() + '/mysite/media/image_preprocessing/', pic_name2)
    pic_path2 = pic_path2.replace('\\', '/')

    src = cv2.imread(pic_path1, 1)
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b, g, r, alpha]
    dst = cv2.merge(rgba, 4)
    cv2.imwrite(pic_path2, dst)
    return pic_path2

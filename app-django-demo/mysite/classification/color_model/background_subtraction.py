import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def bg_sb(pic_path, pic_name , pic_rect):
    #基础迭代次数为两次
    iterations_count = 2
    print(pic_name)
    #若图片大小横坐标大于500，则增加迭代次数
    print('cv2 imread ' + pic_path)
    img = cv2.imdecode(np.fromfile(pic_path, dtype=np.uint8), -1)
    print(img)
    if img.shape[1] > 500:
        iterations_count = 4

    mask = np.zeros((img.shape[:2]), np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    cv2.grabCut(img, mask, pic_rect, bgdModel, fgdModel, iterations_count, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]

    pic_name1 = 'pre1_' + pic_name.replace("jpg", "png")
    pic_path1 = os.path.join(os.getcwd() + '/mysite/media/image_preprocessing/', pic_name1)
    pic_path1 = pic_path1.replace('\\', '/')

    cv2.imencode(".png", img)[1].tofile(pic_path1)
    #cv2.imwrite(pic_path1, img)

    pic_name2 = 'pre2_' + pic_name.replace("jpg", "png")
    pic_path2 = os.path.join(os.getcwd() + '/mysite/media/image_preprocessing/', pic_name2)
    pic_path2 = pic_path2.replace('\\', '/')

    src = cv2.imdecode(np.fromfile(pic_path1, dtype=np.uint8), -1)
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b, g, r, alpha]
    dst = cv2.merge(rgba, 4)
    cv2.imencode(".png", dst)[1].tofile(pic_path2)
    #cv2.imwrite(pic_path2, dst)
    return pic_path2

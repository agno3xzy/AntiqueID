import os
import cv2
import numpy as np
from PIL import Image
import requests
import json
import matplotlib.pyplot as plt

def bg_sb(pic_path, pic_name , pic_rect):
    #基础迭代次数为两次
    iterations_count = 2
    #print(pic_name)
    #若图片大小横坐标大于500，则增加迭代次数
    #print('cv2 imread ' + pic_path)
    #img = cv2.imdecode(np.fromfile(pic_path, dtype=np.uint8), -1)
    img = cv2.imread(pic_path)
    #print(img)
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

    #cv2.imencode(".png", img)[1].tofile(pic_path1)

    cv2.imwrite(pic_path1, img)

    pic_name2 = 'pre2_' + pic_name.replace("jpg", "png")
    pic_path2 = os.path.join(os.getcwd() + '/mysite/media/image_preprocessing/', pic_name2)
    pic_path2 = pic_path2.replace('\\', '/')

    #src = cv2.imdecode(np.fromfile(pic_path1, dtype=np.uint8), -1)
    src = cv2.imread(pic_path1)
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b, g, r, alpha]
    dst = cv2.merge(rgba, 4)
    #cv2.imencode(".png", dst)[1].tofile(pic_path2)
    cv2.imwrite(pic_path2, dst)
    return pic_path2

#唐三彩器皿目标检测
def get_jar_cropbox(pic_path):

    #crop_box代表每个所画区域，labels代表其对应标签
    crop_box = []

    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/47ea4541-acbf-4aa1-95cd-25d69d8f1711/LabelFile/'
    data = {'file': open(pic_path, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('55kaNUAnPTPcMMCJdXaP6ss4MbWOaZBu', ''), files=data)
    dic = json.loads(response.text)

    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            crop_box.append([i['xmin'], i['ymin'], i['xmax'], i['ymax']])
    return crop_box

#唐三彩人俑目标检测
def get_man_cropbox(pic_path):
    # crop_box代表每个所画区域，labels代表其对应标签
    crop_box = []

    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/ce0e8909-166c-4cc4-92d6-9ab41b1eb605/LabelFile/'
    data = {'file': open(pic_path, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('55kaNUAnPTPcMMCJdXaP6ss4MbWOaZBu', ''), files=data)
    dic = json.loads(response.text)

    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            crop_box.append([i['xmin'], i['ymin'], i['xmax'], i['ymax']])
    return crop_box

#唐三彩马俑目标检测
def get_horse_cropbox(pic_path):
    # crop_box代表每个所画区域，labels代表其对应标签
    crop_box = []

    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/c65af3d0-25b6-45c3-a9a8-01bb0321d155/LabelFile/'
    data = {'file': open(pic_path, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('55kaNUAnPTPcMMCJdXaP6ss4MbWOaZBu', ''), files=data)

    dic = json.loads(response.text)

    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            crop_box.append([i['xmin'], i['ymin'], i['xmax'], i['ymax']])
    return crop_box


# 唐三彩马俑目标检测
def get_horse_man_cropbox(pic_path):
    # crop_box代表每个所画区域，labels代表其对应标签
    crop_box = []

    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/e1a78745-2a8e-4b21-912e-9b4c96e31cc9/LabelFile/'
    data = {'file': open(pic_path, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('55kaNUAnPTPcMMCJdXaP6ss4MbWOaZBu', ''), files=data)

    dic = json.loads(response.text)

    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            crop_box.append([i['xmin'], i['ymin'], i['xmax'], i['ymax']])
    return crop_box
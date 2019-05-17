from PIL import Image
import os
import requests
import json

def get_cropbox_from_jar(dir):
    labels = []
    probabilities = {}
    crop_box = []

    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/9195d487-2ef1-4e88-a0d8-7f61aa905e65/LabelFile/'
    data = {'file': open(dir, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('55kaNUAnPTPcMMCJdXaP6ss4MbWOaZBu', ''), files=data)
    dic = json.loads(response.text)

    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            labels.append(i['label'])
            probabilities[i['label']] = i['score']
            crop_box.append([i['xmin'], i['ymin'], i['xmax'], i['ymax']])
    return labels, probabilities, crop_box


def get_cropbox_from_horse(dir):

    #crop_box代表每个所画区域，labels代表其对应标签
    labels = []
    probabilities = {}
    crop_box = []
    labels, probabilities, crop_box = get_cropbox_from_horse_pattern(dir)
    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/f5eed641-a84f-4324-b448-b6d049f4c0c0/LabelFile/'
    data = {'file': open(dir, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('55kaNUAnPTPcMMCJdXaP6ss4MbWOaZBu', ''), files=data)
    dic = json.loads(response.text)

    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            labels.append(i['label'])
            probabilities[i['label']] = i['score']
            crop_box.append([i['xmin'], i['ymin'], i['xmax'], i['ymax']])
    return labels, probabilities, crop_box

def get_cropbox_from_horse_pattern(dir):

    #crop_box代表每个所画区域，labels代表其对应标签
    labels = []
    probabilities = {}
    crop_box = []

    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/fe14c650-fc08-4430-b8a4-cd23e2d3d84a/LabelFile/'
    data = {'file': open(dir, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('ocChqbJKRc6lhDfFsVeKQN_1Bscw1u5t', ''), files=data)
    dic = json.loads(response.text)

    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            labels.append(i['label'])
            probabilities[i['label']] = i['score']
            crop_box.append([i['xmin'], i['ymin'], i['xmax'], i['ymax']])
    return labels, probabilities, crop_box

def get_cropbox_from_man(dir):

    #crop_box代表每个所画区域，labels代表其对应标签
    labels = []
    probabilities = {}
    crop_box = []

    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/29c1d298-677a-4d02-ba63-d141a2cad363/LabelUrls/'
    data = {'file': open(dir, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('ocChqbJKRc6lhDfFsVeKQN_1Bscw1u5t', ''), files=data)
    dic = json.loads(response.text)

    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            labels.append(i['label'])
            probabilities[i['label']] = i['score']
            crop_box.append([i['xmin'], i['ymin'], i['xmax'], i['ymax']])
    return labels, probabilities, crop_box

def get_file_name(dir):
    filename = dir.split('/')[-1].split('.')[0]
    return filename

def localize(dir, category):
    file_name_list = []
    if category == "horse" or category =="horse_man":
        labels, probabilities, crop_box = get_cropbox_from_horse(dir)
    elif category == 'jar':
        labels, probabilities, crop_box = get_cropbox_from_jar(dir)
    else:
        labels, probabilities, crop_box = get_cropbox_from_man(dir)
    target = os.getcwd().split('classification')[0] + '\\mysite\\media\\localized\\'
    filename = get_file_name(dir)
    im = Image.open(dir)
    for index, i in enumerate(crop_box):
        suffix = filename + '_' + str(labels[index]) + '_' + str(index) + '.png'
        file_name_list.append(suffix)
        target_path = target + suffix
        tmp = im.crop(i)
        tmp.save(target_path)
    return file_name_list






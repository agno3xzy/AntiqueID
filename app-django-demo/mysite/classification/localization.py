from PIL import Image
import os
import requests
import json

#------------------如需单独信息，调用get_cropbox_from_nano(dir)即可--------------#
def get_cropbox_from_nano(dir):

    #crop_box代表每个所画区域，labels代表其对应标签
    labels = []
    probabilities = {}
    crop_box = []

    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/f5eed641-a84f-4324-b448-b6d049f4c0c0/LabelFile/'
    data = {'file': open(dir, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('55kaNUAnPTPcMMCJdXaP6ss4MbWOaZBu', ''), files=data)

    dic = json.loads(response.text)
    #print(dic)

    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            #if i['score'] >= 0.50:
            labels.append(i['label'])
            probabilities[i['label']] = i['score']
            crop_box.append([i['xmin'], i['ymin'], i['xmax'], i['ymax']])


    print(labels)
    print(probabilities)
    print(crop_box)
    return labels, probabilities, crop_box

def get_file_name(dir):
    filename = dir.split('/')[-1].split('.')[0]
    return filename

def localize(dir):
    file_name_list = []
    labels, probabilities, crop_box = get_cropbox_from_nano(dir)
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

#localize方法，存储所有切片图，并返回文件名列表
#如需标签和probabilities信息，见get_cropbox_from_nano方法




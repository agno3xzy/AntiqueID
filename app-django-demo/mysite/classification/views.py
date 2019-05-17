import sys
import os
import time
import requests
import json
import random
import cv2
from . import img_loader as ld
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render, redirect
from keras import backend as K
from keras.models import load_model

import login.models as models

from . import color_predict
from . import background_subtraction
from . import color_similarity
from . import class_content
from . import localization

size = 128,128
category = {'camel':0, 'horse':1, 'horse_man':2, 'man':3, 'jar':4, 'fakehorse':5}
category_name = {0:'唐三彩骆驼', 1:'唐三彩马', 2:'唐三彩骑俑', 3:'唐三彩人像',4:'唐三彩器皿',5:'唐三彩工艺品马'}
tomb_category = {0:'唐昭陵韦贵妃墓',1:'唐惠庄太子李撝墓',2:'懿德太子墓'}
dynasty_category = {0:'初唐', 1:'盛唐'}

def index(request):
    if not request.session.get('is_login', None):
        return redirect("/login/signin/")
    return render(request, 'classification/intro.html')

def color_mind(request):
    return render(request, 'classification/color_mind.html')

def upload_file(request):

    if request.method == "POST":  # 请求方法为POST时，进行处理
        #这里的img是h5表单里的name
        Dict = {}
        myFile = request.FILES.get("imageFile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        image = Image.open(myFile)
        Timestamp = int(time.time())
        pic_name = str(Timestamp) + '.png'
        pic_path = os.path.join(os.getcwd() + '/mysite/media/upload/', pic_name)
        pic_path = pic_path.replace('\\', '/')
        image.save(pic_path)


        resize_pic_path  = resize_image(pic_path, pic_name)
        if resize_pic_path == "null":
            class_dic, classmsg = get_from_classification(pic_path)
        else:
            class_dic, classmsg = get_from_classification(resize_pic_path)

        if classmsg == 'jar':
            rect_list = background_subtraction.get_jar_cropbox(pic_path)
            if len(rect_list) != 0:
                pic_rect = (
                    int(rect_list[0][0]), int(rect_list[0][1]), int(rect_list[0][2]), int(rect_list[0][3]))
            else:
                pic_rect = (0, 0, int(image.size[0]) - 1, int(image.size[1]) - 1)
        elif classmsg == 'man':
            rect_list = background_subtraction.get_man_cropbox(pic_path)
            if len(rect_list) != 0:
                pic_rect = (
                    int(rect_list[0][0]), int(rect_list[0][1]), int(rect_list[0][2]), int(rect_list[0][3]))
            else:
                pic_rect = (0, 0, int(image.size[0]) - 1, int(image.size[1]) - 1)
        elif classmsg == 'horse_man':
            rect_list = background_subtraction.get_horse_man_cropbox(pic_path)
            if len(rect_list) != 0:
                pic_rect = (
                    int(rect_list[0][0]), int(rect_list[0][1]), int(rect_list[0][2]), int(rect_list[0][3]))
            else:
                pic_rect = (0, 0, int(image.size[0]) - 1, int(image.size[1]) - 1)
        elif classmsg == 'horse':
            rect_list = background_subtraction.get_horse_cropbox(pic_path)
            if len(rect_list) != 0:
                pic_rect = (
                    int(rect_list[0][0]), int(rect_list[0][1]), int(rect_list[0][2]), int(rect_list[0][3]))
            else:
                pic_rect = (0, 0, int(image.size[0]) - 1, int(image.size[1]) - 1)
        else:
            # 处理用户输入的坐标参数
            raw_coordinate = request.POST.get("coordinate", None)
            if not raw_coordinate:
                pic_rect = (0, 0, int(image.size[0]) - 1, int(image.size[1]) - 1)
            else:
                real_coordinate = raw_coordinate.split("#", raw_coordinate.count('#'))
                pic_rect = (
                    int(real_coordinate[0]), int(real_coordinate[1]), int(real_coordinate[2]), int(real_coordinate[2]))



        #图像前景分离
        pre_pic_path = background_subtraction.bg_sb(pic_path, pic_name, pic_rect)
        #颜色模型:以十六进制字符串的形式返回语义分割后各个部分的rgb值
        feature_color, dec_feature_color = color_predict.feature_color(pre_pic_path)
        #分类模型鉴定逻辑
        model_path = "D:/2019Spring/Intel杯/model/trained_model_horse_man_fake_plate.h5"

        '''
        #暂时使用NanoNets，因此注释模型本地模型判断
        result = predict(model_path, pic_path)
        #以下四个变量控制前端页面显示的结果
        classtype = 0
        if int(result[0][0]) == 1:
            classtype = 0
        elif int(result[0][1]) == 1:
            classtype = 1
        elif int(result[0][2]) == 1:
            classtype = 2
        elif int(result[0][3]) == 1:
            classtype = 3
        '''

        a = color_similarity.ColorHub()
        a.read_from_data(dec_feature_color)
        a.calculate_k_nearest(color_similarity.ColorHub.EUCLIDEAN, 10)
        color_showcase = a.get_showcase(a.calculate_nearest_sum())
        classresult = json.dumps(class_dic)
        feature_list = localization.localize(pre_pic_path, classmsg)
        feature_set = get_feature_set(feature_list)

        tomb, tomb_pic = predict_tomb(pre_pic_path, color_showcase)
        dynasty = predict_dynasty(pre_pic_path)
        save_as_report(request,Timestamp,pic_path,color_showcase,feature_color,category[classmsg], classresult, str(tomb), str(tomb_pic), feature_list, dynasty)

        #输出相应前端报告格式
        report = models.Classification.objects.get(class_id = Timestamp)

        antique_name = category_name[report.class_type]

        report_color_list = report.class_color.split('#')
        for i in range(len(report_color_list)):
            if i == 0:
                pass
            else:
                report_color_list[i] = '#' + report_color_list[i]
        color_list = report_color_list[1:]

        color_sum_str = []
        color_sum_str.append(class_content.get_content('釉色分析', '综述', 0, 0))
        color_sum_str.append(class_content.get_content('釉色分析', color_showcase[0], 0, 0))
        color_showcase = color_showcase[1:]
        tomb_list = report.class_tomb.split('#')
        tomb_content = class_content.get_content('墓穴分析', '文案', int(tomb_list[0]), 0)


        if dynasty == 0 :
            dynasty_content = class_content.get_content('朝代', '初唐', 0, 0)
        else:
            dynasty_content = class_content.get_content('朝代', '盛唐', 0, 0)

        dynasty_name = dynasty_category[dynasty]
        tomb_name = tomb_category[int(tomb_list[0])]

        feature_content = feature_analysis(report.class_type, feature_set)

        class_dic = category_explanation(class_dic)

        return render(request, "classification/report.html", locals())

def predict(model_path, pic_path):
    K.clear_session()
    model = load_model(model_path)
    p = ld.transform_pic(pic_path, size)
    p = p.reshape([1,128,128,3])
    return model.predict(p)

#鉴定报告展示
def report(request):
    report_id = request.POST.get("report_id", "")
    report = models.Classification.objects.get(class_id=report_id)
    report_color_list = report.class_color.split('#')
    tomb_list = report.class_tomb.split('#')
    tomb_content = class_content.get_content('墓穴分析', '文案', int(tomb_list[0]), 0)
    tomb_name = tomb_category[int(tomb_list[0])]
    feature_list = report.class_feature.split('#')
    feature_set = get_feature_set(feature_list)
    get_feature_set(feature_list)
    if int(report.class_dynasty) == 0:
        dynasty_content = class_content.get_content('朝代', '初唐', 0, 0)
    else:
        dynasty_content = class_content.get_content('朝代', '盛唐', 0, 0)
    dynasty_name = dynasty_category[int(report.class_dynasty)]
    for i in range(len(report_color_list)):
        if i == 0:
            pass
        else:
            report_color_list[i] = '#' + report_color_list[i]
    antique_name = category_name[report.class_type]
    feature_content = feature_analysis(report.class_type, feature_set)
    class_dic = json.loads(report.class_result)
    class_dic = category_explanation(class_dic)
    color_showcase = json.loads(report_color_list[0])
    color_list = report_color_list[1:]
    color_sum_str = []
    color_sum_str.append(class_content.get_content('釉色分析', '综述', 0, 0))
    color_sum_str.append(class_content.get_content('釉色分析', color_showcase[0], 0, 0))
    color_showcase = color_showcase[1:]
    return render(request, "classification/report.html", locals())

#存储为鉴定报告
def save_as_report(request, Timestamp, pic_path, color_showcase, feature_color, classtype, classresult, tomb, tomb_pic, feature_list, dynasty):
    # 保存鉴定报告
    userID = request.session['user_id']
    user = models.User.objects.get(user_id=userID)
    mainpage = models.Mainpage.objects.get(main_id=userID)
    report = models.Classification()
    report.user_user = user
    report.class_id = Timestamp
    report.class_img = pic_path
    report.class_color = json.dumps(color_showcase) + "".join(feature_color)
    report.class_type = classtype
    report.class_result = classresult
    report.class_tomb = tomb + '#' + tomb_pic
    report.class_dynasty = str(dynasty)
    if len(feature_list) != 0:
        featureStr = feature_list[0]
        for index in range(len(feature_list)):
            if index > 0:
                featureStr = featureStr + '#' + feature_list[index]
        report.class_feature = featureStr
    report.save()


#分类预测模型
def get_from_classification(pic_path):

    url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'
    data = {'file': open(pic_path, 'rb'), 'modelId': ('', '93d67a85-04a2-4788-84c9-d692962d7557')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('55kaNUAnPTPcMMCJdXaP6ss4MbWOaZBu', ''), files=data)

    dic = json.loads(response.text)
    class_msg = "null"
    result_dic = {}

    tmp_class_msg = "null"
    tmp_result_dic = {}

    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            result_dic[i['label']] = i['probability']
    if not bool(result_dic):
        pass
    else:
        class_msg = str(max(result_dic, key=result_dic.get))
    if class_msg == 'horse':
        tmp_result_dic, tmp_class_msg = get_from_fakehorse(pic_path)
        if tmp_class_msg == 'fakehorse':
            result_dic = tmp_result_dic
            class_msg = tmp_class_msg
    return result_dic, class_msg

#真假马预测分析
def get_from_fakehorse(pic_path):

    url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'
    data = {'file': open(pic_path, 'rb'), 'modelId': ('', '9504306e-1853-4fc8-8a45-e62aeff18720')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('55kaNUAnPTPcMMCJdXaP6ss4MbWOaZBu', ''), files=data)

    dic = json.loads(response.text)
    class_msg = "null"
    result_dic = {}
    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            result_dic[i['label']] = i['probability']
    if not bool(result_dic):
        pass
    else:
        class_msg = str(max(result_dic, key=result_dic.get))
    return result_dic, class_msg

#墓穴预测
def predict_tomb(pic_path, color_list):

    tomb = random.randint(0,2)
    if color_list[0] in range(0,2):
        tomb = 0
    elif color_list[0] in range(2,4):
        tomb = 1
    elif color_list[0] in range(4,6):
        tomb = 2

    tomb_pic_name = random.randint(1,7)
    return tomb, tomb_pic_name

#朝代预测
def predict_dynasty(pic_path):
    dynasty = random.randint(0,1)
    return dynasty

#特征分析
def feature_analysis(category, feature_set):
    featrue_content = []
    if category == 1 or category == 2:
        featrue_content.append(class_content.get_content('大类分析和介绍', '马', '综述', 0))
        featrue_content.append(class_content.get_content('大类分析和介绍', '马', '艺术特征', random.randint(1,3)))
        featrue_content.append(class_content.get_content('大类分析和介绍', '马', '艺术特征', random.randint(4,6)))
        featrue_content.append(class_content.get_content('大类分析和介绍', '马', '艺术特征', random.randint(7,9)))
        if "saddle" in feature_set:
            featrue_content.append(class_content.get_content('大类分析和介绍', '马', '马鞍', random.randint(1, 2)))
        if "ribbon" in feature_set or "pattern" in feature_set:
            featrue_content.append(class_content.get_content('大类分析和介绍', '马', '花纹', random.randint(1, 2)))
        if "man_on_horse" in feature_set:
            featrue_content.append(class_content.get_content('大类分析和介绍', '马', '骑者', random.randint(1, 6)))
    elif category == 4:
        featrue_content.append(class_content.get_content('大类分析和介绍', '器皿', '综述', 0))
        featrue_content.append(class_content.get_content('大类分析和介绍', '器皿', '艺术特征', random.randint(1, 3)))
        featrue_content.append(class_content.get_content('大类分析和介绍', '器皿', '艺术特征', random.randint(4, 6)))
        featrue_content.append(class_content.get_content('大类分析和介绍', '器皿', '艺术特征', random.randint(7, 9)))
        if "stripe" in feature_set:
            featrue_content.append(class_content.get_content('大类分析和介绍', '器皿', '花纹', random.randint(1, 3)))
    elif category == 0:
        featrue_content.append(class_content.get_content('大类分析和介绍', '骆驼', '综述', 0))
        featrue_content.append(class_content.get_content('大类分析和介绍', '骆驼', '颜色', 1))
    elif category == 3:
        featrue_content.append(class_content.get_content('大类分析和介绍', '人', '综述', 0))
        featrue_content.append(class_content.get_content('大类分析和介绍', '人', '艺术特征', random.randint(1, 3)))
        featrue_content.append(class_content.get_content('大类分析和介绍', '人', '艺术特征', random.randint(4, 7)))
        if "sleeve" in feature_set:
            featrue_content.append(class_content.get_content('大类分析和介绍', '人', '袖子', random.randint(1, 3)))
    else:
        featrue_content.append("此文玩可能是工艺品！")
        featrue_content.append("此文玩可能是工艺品！")
    return featrue_content

def category_explanation(before):
    after = {}
    for key, value in before.items():
        after[category_name[category[key]]] = value
    return after

def resize_image(pic_path, pic_name):
    img = cv2.imread(pic_path)
    resize_image_path = "null"
    x, y = img.shape[0:2]
    if max(x, y) < 500 :
        return resize_image_path
    else:
        if x > y:
            rate = 500.00 / x
        else:
            rate = 500.00 / y
        img_resize = cv2.resize(img, (0, 0), fx=rate, fy=rate, interpolation=cv2.INTER_NEAREST)
        resize_pic_path = os.path.join(os.getcwd() + '/mysite/media/after_resize/', pic_name)
        resize_pic_path = resize_pic_path.replace('\\', '/')
        cv2.imwrite(resize_pic_path, img_resize)
        return resize_image_path

def get_feature_set(feature_list):
    tmp_list = []
    feature_set = ()
    for feature in feature_list:
        tmp = feature.split('_')
        tmp_list.append(tmp[2])
    feature_set = set(tmp_list)
    return feature_set
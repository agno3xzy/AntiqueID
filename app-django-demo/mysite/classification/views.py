import sys
import os
import time
import requests
import json
import random
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
category = {'horse':0, 'jar':1, 'man':2, 'bowl':3, 'head':4}
category_name = {0:'唐三彩马俑', 1:'唐三彩罐', 2:'唐三彩人像', 3:'唐三彩碗',4:'唐三彩人像——头部'}
tomb_category = {0:'唐昭陵韦贵妃墓',1:'唐惠庄太子李撝墓',2:'懿德太子墓'}

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

        #处理用户输入的坐标参数
        raw_coordinate = request.POST.get("coordinate", None)
        if not raw_coordinate:
            pic_rect =(0, 0, int(image.size[0])-1, int(image.size[1])-1)
            print(pic_rect)
        else:
            real_coordinate = raw_coordinate.split("#", raw_coordinate.count('#'))
            pic_rect =(int(real_coordinate[0]),int(real_coordinate[1]),int(real_coordinate[2]),int(real_coordinate[2]))

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

        std_rgb=[(122,100,103),(87,125,35)]

        a = color_similarity.ColorHub()
        a.read_from_data(dec_feature_color,std_rgb)
        a.print_info()

        # 计算k-nearest颜色（用欧几里得距离）
        a.calculate_k_nearest(color_similarity.ColorHub.EUCLIDEAN, 1)

        # 获取nearest数组和distance_sum数组并打印
        color_score = a.get_distance_avgsum(a.get_distance_sum())

        classresult, classmsg = get_from_nano(pic_path)

        tomb, tomb_pic = predict_tomb(pic_path)
        feature_list = localization.localize(pic_path)

        save_as_report(request,Timestamp,pic_path,color_score,feature_color,category[classmsg], classresult, str(tomb), str(tomb_pic), feature_list)

        #输出相应前端报告格式
        report = models.Classification.objects.get(class_id = Timestamp)
        report_color_list = report.class_color.split('#')
        antique_name = category_name[report.class_type]
        for i in range(len(report_color_list)):
            if i == 0:
                pass
            else:
                report_color_list[i] = '#' + report_color_list[i]
        print(report_color_list)
        tomb_list = report.class_tomb.split('#')
        tomb_content = class_content.get_content('墓穴分析', '文案', int(tomb_list[0]))
        tomb_name = tomb_category[int(tomb_list[0])]

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
    tomb_content = class_content.get_content('墓穴分析', '文案', int(tomb_list[0]))
    tomb_name = tomb_category[int(tomb_list[0])]
    feature_list = report.class_feature.split('#')
    for i in range(len(report_color_list)):
        if i == 0:
            pass
        else:
            report_color_list[i] = '#' + report_color_list[i]
    antique_name = category_name[report.class_type]

    return render(request, "classification/report.html", locals())

#存储为鉴定报告
def save_as_report(request, Timestamp, pic_path, color_score, feature_color, classtype, classresult, tomb, tomb_pic, feature_list):
    # 保存鉴定报告
    userID = request.session['user_id']
    user = models.User.objects.get(user_id=userID)
    mainpage = models.Mainpage.objects.get(main_id=userID)
    report = models.Classification()
    report.user_user = user
    report.class_id = Timestamp
    report.class_img = pic_path
    report.class_color = str(color_score) + "".join(feature_color)
    report.class_type = classtype
    report.class_result = classresult
    report.class_tomb = tomb + '#' + tomb_pic
    featureStr = feature_list[0]
    for index in range(len(feature_list)):
        if index > 0:
            featureStr = featureStr + '#' + feature_list[index]
    report.class_feature = featureStr
    report.save()

#nanoNets
def get_from_nano(pic_path):
    url = 'https://app.nanonets.com/api/v2/MultiLabelClassification/Model/c41da85a-1303-451a-9077-71128b3e7acd/LabelFiles/'
    data = {'files': open(pic_path, 'rb'),
            'modelId': ('', 'c41da85a-1303-451a-9077-71128b3e7acd')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('55kaNUAnPTPcMMCJdXaP6ss4MbWOaZBu', ''), files=data)
    dic = json.loads(response.text)
    print(dic)
    class_msg = "null"
    result_dic = {}
    if dic['message'] == 'Success':
        for i in dic['result'][0]['prediction']:
            print(i)
            if i['probability'] >= 0.50:
                result_dic[i['label']] = i['probability']

    if not bool(result_dic):
        pass
    else:
        class_msg = str(max(result_dic,key=result_dic.get))
    return response.text, class_msg

#墓穴预测
def predict_tomb(pic_path):

    tomb = random.randint(0,2)
    tomb_pic_name = random.randint(1,7)

    return tomb, tomb_pic_name

#朝代预测
def predict_dynasty():
    pass


#特征分析
def feature_analysis():
    pass
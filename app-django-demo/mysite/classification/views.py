import sys
import os
import time
from . import img_loader as ld
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render, redirect
from keras import backend as K
from keras.models import load_model
import login.models as models

sys.path.insert(0, 'mysite/classification/color_model')
import color_predict
import background_subtraction
# Create your views here.
size = 128,128

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
        print(pic_path)
        image.save(pic_path)
        #pic_name = myFile.name

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
        #dominant_color = color_predict.dominant_predict(pre_pic_path, pic_name)
        feature_color = color_predict.feature_color(pre_pic_path)
        #分类模型鉴定逻辑
        model_path = "D:/2019Spring/Intel杯/model/trained_model_horse_man_fake_plate.h5"
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

        #保存鉴定报告
        userID = request.session['user_id']
        user = models.User.objects.get(user_id=userID)
        mainpage = models.Mainpage.objects.get(main_id=userID)
        report = models.Classification()
        report.user_user = user
        report.class_id = Timestamp
        report.class_img = pic_path
        report.class_color = "".join(feature_color)
        report.class_type = classtype
        report.save()
        report = models.Classification.objects.get(class_id = Timestamp)
        report_color_list = report.class_color.split('#')
        for i in range(len(report_color_list)):
            report_color_list[i] = '#' + report_color_list[i]
        print(report_color_list)
        return render(request, "classification/report.html", locals())


def predict(model_path, pic_path):
    K.clear_session()
    model = load_model(model_path)
    p = ld.transform_pic(pic_path, size)
    p = p.reshape([1,128,128,3])
    return model.predict(p)

def report(request):
    report_id = request.POST.get("report_id", "")
    report = models.Classification.objects.get(class_id=report_id)
    report_color_list = report.class_color.split('#')
    for i in range(len(report_color_list)):
        report_color_list[i] = '#' + report_color_list[i]
    print(report_color_list)
    return render(request, "classification/report.html", locals())
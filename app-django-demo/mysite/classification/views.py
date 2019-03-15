import os
import sys
from . import img_loader as ld
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render
from keras import backend as K
from keras.models import load_model

sys.path.insert(0, 'mysite/classification/color_model')
import color_predict
import background_subtraction


# Create your views here.
size = 128,128

def index(request):
    return render(request, 'classification/intro.html')

def color_mind(request):
    return render(request, 'classification/color_mind.html')

def result(request):
    return render(request, 'classification/intro2.html')

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return render(request, 'classification/logout.html')
    request.session.flush()
    return render(request, 'classification/logout.html')

def upload_file(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        #这里的img是h5表单里的name
        Dict = {}
        myFile = request.FILES.get("imageFile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        image = Image.open(myFile)

        pic_path = os.path.join(os.getcwd() + '/mysite/media/upload/', myFile.name)
        pic_path = pic_path.replace('\\', '/')
        image.save(pic_path)
        pic_name = myFile.name

        #这里预先输入了相应的rect
        pic_rect = rect=(226,249,1480,1987)
        pre_pic_path = background_subtraction.bg_sb(pic_path, pic_name, pic_rect)
        dominant_color = color_predict.dominant_predict(pre_pic_path, pic_name)
        #分类模型鉴定逻辑
        model_path = "D:/2019Spring/Intel杯/数据集/Tangsancai/model_to_reformat/trained_model_horse_man_fake_plate.h5"
        result = predict(model_path, pic_path)
        #以下四个变量控制前端页面显示的结果
        is_horse = False
        is_man = False
        is_fake = False
        is_plate = False
        if int(result[0][0]) == 1:
            is_horse = True
        if int(result[0][1]) == 1:
            is_man = True
        if int(result[0][2]) == 1:
            is_fake = True
        if int(result[0][3]) == 1:
            is_plate = True


        return render(request, "classification/intro2.html", locals())


def predict(model_path, pic_path):
    K.clear_session()
    model = load_model(model_path)
    p = ld.transform_pic(pic_path, size)
    p = p.reshape([1,128,128,3])
    return model.predict(p)
        #model.predict_proba(p)




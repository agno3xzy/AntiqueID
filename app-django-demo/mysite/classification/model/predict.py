from keras.models import load_model
from keras.models import Model
import img_loader as ld
import os
size = 600, 600
print("请输入h5模型文件名，不含后缀。")
filename = input()
input_path = "Tangsancai/model_to_reformat/"
path = input_path
path += filename
path += ".h5"
model = load_model(path)
testlist = ['Tangsancai/test_horse/', 'Tangsancai/test_fakehorse/']
for i in testlist:
    print("正在预测"+i+"目录下的所有图片...")
    for n in os.listdir(i):
        pdir = i + n
        p = ld.transform_pic(pdir, size)
        ld.show_pic(pdir, size)
        #change this
        p=p.reshape([1,600,600,3])
        print(n)
        print(model.predict(p))

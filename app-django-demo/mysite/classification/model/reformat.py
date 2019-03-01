from keras.models import load_model
from keras.models import Model
import os
import tensorflowjs as tfjs
print("请输入文件名，不含后缀。")
filename = input()
input_path = "Tangsancai/model_to_reformat/"
product_path = "Tangsancai/model_reformat/"
product_path += filename + '/'
path = input_path
path += filename
path += ".h5"
model = load_model(path)
if model:
    print("开始转换。")
    tfjs.converters.save_keras_model(model, product_path)
    print("转换成功。")
else:
    print("无此文件。")

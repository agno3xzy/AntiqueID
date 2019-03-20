import os
import numpy as np
from colorthief import ColorThief
from PIL import Image
import matplotlib.pyplot as plt

def dominant_predict(pic_path, pic_name):
    color_thief = ColorThief(pic_path)
    dominant_color = color_thief.get_color(quality=1)
    dominant_img = Image.new("RGB", (25, 25), dominant_color)
    pic_name = "coloranalysis_" + pic_name
    color_path = os.path.join(os.getcwd() + '/mysite/media/color_analysis/', pic_name)
    color_path = color_path.replace('\\', '/')
    dominant_img.save(color_path)
    return dominant_color
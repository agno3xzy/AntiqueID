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
    color_path = os.path.join(os.getcwd() + '/media/color_analysis/', pic_name)
    color_path = color_path.replace('\\', '/')
    dominant_img.save(color_path)
    return dominant_color

def feature_color(pic_path):
    color_thief = ColorThief(pic_path)
    feature_color = color_thief.get_palette(3,1)
    hex_rgb_list = []
    for rgb in feature_color:
        hex_rgb_list.append(rgb_to_hex(rgb))
    return hex_rgb_list

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

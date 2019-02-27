import os
import numpy as np
from colorthief import ColorThief
from PIL import Image
import matplotlib.pyplot as plt

horse_dominantcolor = []
color_dir = os.path.join(os.getcwd(), 'Tangsancai/plate')
for root, dirs, files in os.walk(color_dir):
    for file in files:
        # print(file)     #文件名
        color_thief = ColorThief(os.path.join(root, file))
        dominant_color = color_thief.get_color(quality=1)
        print(file)
        print(dominant_color)
        dominant_img = Image.new("RGB", (25, 25), dominant_color)
        horse_dominantcolor.append(dominant_color)
        plt.imshow(dominant_img)
        plt.show()

width = 700
height = 700
background = Image.new("RGB", (width, height), (255, 255, 255))
len = 0
iter = 0
y_iter = 0
horizontal = 50
vertical = 50
r_list = []
g_list = []
b_list = []
for i in horse_dominantcolor:
    r_list.append(i[0])
    g_list.append(i[1])
    b_list.append(i[2])
    temp = (i[0], i[1], i[2])
    ''''
    len = (len + horizontal) % width
    if len == 0:
        y_iter += vertical
    background.paste(temp, (iter, y_iter, len, y_iter + vertical))
    iter = (iter + horizontal) % width
    '''
    len = len + horizontal
    background.paste(temp, (iter, y_iter, len, y_iter + vertical))
    iter = iter + horizontal

    len = len % width
    iter = iter % width
    if len == 0:
        y_iter += vertical

print('以下是所有唐三彩器皿主色统计')
plt.imshow(background)
plt.show()
print('以下是所有唐三彩器皿主色均值')
r_mean = np.mean(r_list)
g_mean = np.mean(g_list)
b_mean = np.mean(b_list)
rgb_means = (r_mean, g_mean, b_mean)
print(rgb_means)
rgb_means = (int(r_mean), int(g_mean), int(b_mean))
dominant_all = Image.new("RGB", (25, 25), rgb_means)
plt.imshow(dominant_all)
plt.show()
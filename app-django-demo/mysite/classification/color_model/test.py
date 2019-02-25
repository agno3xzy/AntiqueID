import os
from colorthief import ColorThief
from PIL import Image

horse_dominantcolor = []
for root, dirs, files in os.walk('D:\\2019Spring\Intel杯\数据集\Tangsancai\\test'):
    for file in files:
        # print(file)     #文件名
        color_thief = ColorThief(os.path.join(root, file))
        dominant_color = color_thief.get_color(quality=1)
        print(dominant_color)
        horse_dominantcolor.append(dominant_color)
print(horse_dominantcolor)
# get the dominant color


# build a color palette
#palette = color_thief.get_palette(color_count=6)
#print(palette)
#width = 60 * 4
#height = 60
#image = Image.new('RGB', (width, height), dominant_color)
#image.save('code.jpg', 'jpeg')

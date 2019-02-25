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
background = Image.new("RGB", (1000, 1000), (255, 255, 255))
background.show()
iter = 0
for i in range(5):
    temp = (horse_dominantcolor[i][0], horse_dominantcolor[i][1], horse_dominantcolor[i][2])
    background.paste(temp, (iter, 0, iter + 20, 20))
    iter += 20
background.show()

# get the dominant color


# build a color palette
#palette = color_thief.get_palette(color_count=6)
#print(palette)
#width = 60 * 4
#height = 60
#image = Image.new('RGB', (width, height), dominant_color)
#image.save('code.jpg', 'jpeg')

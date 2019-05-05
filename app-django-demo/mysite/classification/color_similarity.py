#-*- coding: UTF-8 -*-
import random as rd
import numpy as np

#用Numpy按欧式、曼哈顿、切比雪夫、余弦距离选取若干最近颜色
#标准颜色最多100个

class ColorHub:

    color_category = {
        0:'绿',
        1:'白',
        2:'浅棕红',
        3:'深棕',
        4:'蓝',
        5:'深蓝黑'
    }
#21, 15, 20, 16,19,17
    rgb_pool = {
        0: [(93, 121, 80), (138, 156, 116), (81, 100, 68), (78, 100, 62), (97, 121, 85), (114, 130, 93),
            (131, 142, 110), (99, 115, 78), (113, 141, 66), (156, 191, 109), (113, 124, 66), (141, 155, 96),
            (91, 101, 66), (168, 178, 109), (106, 127, 62), (153, 166, 120), (63, 72, 27), (76, 79, 62), (71, 68, 53),
            (83, 90, 38), (74, 88, 63), ],
        1: [(212, 197, 154), (226, 212, 183), (205, 183, 142), (179, 166, 132), (190, 170, 119), (164, 150, 123),
            (185, 170, 139), (241, 230, 208), (231, 219, 197), (241, 226, 205), (228, 212, 178), (220, 197, 155),
            (233, 217, 183), (220, 204, 168), (241, 219, 170), ],
        2: [(171, 115, 40), (211, 146, 62), (168, 108, 46), (147, 97, 44), (198, 143, 61), (215, 157, 84),
            (172, 112, 152), (145, 99, 49), (175, 123, 66), (138, 85, 69), (160, 82, 16), (188, 88, 3),
            (163, 71, 24), (163, 75, 35), (169, 63, 13), (138, 61, 35), (185, 128, 61), (157, 88, 49), (149, 50, 8),
            (147, 78, 39)],
        3 : [(87, 29, 15), (64, 20, 11), (88, 26, 3), (75, 15, 4), (74, 20, 8), (81, 23, 1), (61, 25, 29),
             (76, 31, 28), (51, 30, 25), (39, 16, 10), (49, 38, 42), (74, 19, 12), (94, 70, 60), (94, 40, 28),
             (58, 32, 35), (74, 44, 33)],
        4 : [(71, 94, 102), (34, 57, 71), (59, 75, 88), (51, 67, 83), (39, 58, 75), (70, 89, 96), (58, 71, 79),
             (88, 97, 102), (63, 74, 76), (65, 74, 79), (44, 66, 103), (55, 67, 83), (58, 85, 112), (56, 82, 107),
             (46, 64, 88), (60, 79, 96), (61, 81, 88), (39, 63, 97), (43, 78, 97)],
        5 : [(31, 35, 46), (42, 44, 56), (64, 66, 78), (39, 42, 51), (51, 44, 38), (43, 42, 48), (41, 32, 23),
             (37, 37, 39), (28, 28, 28), (45, 45, 45), (42, 45, 64), (31, 34, 53), (37, 31, 15), (40, 38, 25),
             (40, 36, 37), (24, 15, 18), (28, 19, 22), ]
    }
    showcase_filename = {
        0: ['6.jpg','7.jpg','8.jpg','9.jpg'],
        1: ['1.jpg','2.jpg','3.jpg'],
        2: ['10.jpg','11.jpg','12.jpg'],
        3: ['16.jpg','17.jpg','18.jpg'],
        4: ['4.jpg','5.jpg' ],
        5: ['13.jpg','14.jpg','15.jpg'],
    }

    #两个图片list的常量
    PIC_CONST = 1
    STD_CONST = 2

    #各种距离的常量
    CURRENT = 100
    EUCLIDEAN = 100
    MANHATTAN = 101
    CHEBYSHEV = 102
    COSINE = 103

    #词典，用于格式化输出
    dic = {
        EUCLIDEAN : '使用欧几里得距离',
        MANHATTAN: '使用曼哈顿距离',
        CHEBYSHEV: '使用切比雪夫距离',
        COSINE: '使用余弦距离',
    }

    #提前计算好的最远距离
    const = {
        EUCLIDEAN: 0.0,
        MANHATTAN: 0.0,
        CHEBYSHEV: 0.0,
        COSINE: 0.0,
    }

    #默认为8，可覆盖
    K = 5

    #pic是用户颜色，std是标准颜色
    #_vec为numpy数组形式
    #distance为距离矩阵
    #distance为距离之和列表
    #nearest为最近颜色列表
    #nearest_sum为最近颜色计数
    pic = []
    std = [(93, 121, 80), (138, 156, 116), (81, 100, 68), (78, 100, 62), (97, 121, 85), (114, 130, 93),
            (131, 142, 110), (99, 115, 78), (113, 141, 66), (156, 191, 109), (113, 124, 66), (141, 155, 96),
            (91, 101, 66), (168, 178, 109), (106, 127, 62), (153, 166, 120), (63, 72, 27), (76, 79, 62), (71, 68, 53),
            (83, 90, 38), (74, 88, 63),(212, 197, 154), (226, 212, 183), (205, 183, 142), (179, 166, 132), (190, 170, 119), (164, 150, 123),
            (185, 170, 139), (241, 230, 208), (231, 219, 197), (241, 226, 205), (228, 212, 178), (220, 197, 155),
            (233, 217, 183), (220, 204, 168), (241, 219, 170),(171, 115, 40), (211, 146, 62), (168, 108, 46), (147, 97, 44), (198, 143, 61), (215, 157, 84),
            (172, 112, 152), (145, 99, 49), (175, 123, 66), (138, 85, 69), (160, 82, 16), (188, 88, 3),
            (163, 71, 24), (163, 75, 35), (169, 63, 13), (138, 61, 35), (185, 128, 61), (157, 88, 49), (149, 50, 8),
            (147, 78, 39),(87, 29, 15), (64, 20, 11), (88, 26, 3), (75, 15, 4), (74, 20, 8), (81, 23, 1), (61, 25, 29),
             (76, 31, 28), (51, 30, 25), (39, 16, 10), (49, 38, 42), (74, 19, 12), (94, 70, 60), (94, 40, 28),
             (58, 32, 35), (74, 44, 33),(71, 94, 102), (34, 57, 71), (59, 75, 88), (51, 67, 83), (39, 58, 75), (70, 89, 96), (58, 71, 79),
             (88, 97, 102), (63, 74, 76), (65, 74, 79), (44, 66, 103), (55, 67, 83), (58, 85, 112), (56, 82, 107),
             (46, 64, 88), (60, 79, 96), (61, 81, 88), (39, 63, 97), (43, 78, 97),(31, 35, 46), (42, 44, 56), (64, 66, 78), (39, 42, 51), (51, 44, 38), (43, 42, 48), (41, 32, 23),
             (37, 37, 39), (28, 28, 28), (45, 45, 45), (42, 45, 64),  (31, 34, 53), (37, 31, 15), (40, 38, 25),
             (40, 36, 37), (24, 15, 18), (28, 19, 22)]
    pic_vec, std_vec = [], []
    distance = []
    distance_sum = []
    nearest = []
    nearest_sum = []
    nearest_sum_max = 0

    def __init__(self):
        self.calculate_constants()
        pass

    #从数据读取的功能，需要填写此函数。如需要可以增加参数
    def read_from_data(self, l1):
        self.pic = l1
        self.pic_vec = np.array(self.pic)
        self.std_vec = np.array(self.std)
        self.distance = np.zeros((len(self.pic), len(self.std)), dtype='float')

    #输出颜色信息
    def print_info(self):
        print('您的颜色:')
        print(self.pic_vec)
        print('标准颜色:')
        print(self.std_vec)

    def calculate_constants(self):
        a = np.array([0, 0, 0])
        b = np.array([255, 255, 255])

        self.const[self.EUCLIDEAN] = np.linalg.norm(a-b)
        self.const[self.MANHATTAN] = np.linalg.norm(a-b, ord=1)
        #self.const[self.CHEBYSHEV] = np.linalg.norm(a-b, ord=np.inf)
        #self.const[self.COSINE] = np.dot(a, b)/((np.linalg.norm(a))*(np.linalg.norm(b)))

    #计算出k个最近邻颜色并填入相应的数组
    def calculate_k_nearest(self, type: int, K: int):
        self.CURRENT = type
        self.K = K
        if len(self.pic) == 0 and len(self.std) == 0:
            print('Please initialize your colors data.')
            return -1

        for i in range(0,len(self.pic)):
            for j in range(0,len(self.std)):
                if type == self.EUCLIDEAN:
                    self.distance[i][j] = np.linalg.norm(self.pic_vec[i] - self.std_vec[j])
                elif type == self.MANHATTAN:
                    self.distance[i][j] = np.linalg.norm(self.pic_vec[i] - self.std_vec[j], ord = 1)
                elif type == self.CHEBYSHEV:
                    self.distance[i][j] = np.linalg.norm(self.pic_vec[i] - self.std_vec[j], ord = np.inf)
                elif type == self.COSINE:
                    self.distance[i][j] = np.dot(self.pic_vec[i], self.std_vec[j])/((np.linalg.norm(self.pic_vec[i]))*(np.linalg.norm(self.std_vec[j])))
                else:
                    pass

        for i in range(0, len(self.pic)):
            dist, color = zip(*sorted(zip(self.distance[i], self.std)))
            self.nearest.append(color[:self.K])

            #计算总距离
            dist_sum = 0
            for j in dist[:self.K]:
                dist_sum += j

            dist_sum /= K
            dist_sum = dist_sum / self.const[type] * 100.0

            self.distance_sum.append(dist_sum)

    #获取最近颜色和距离信息
    def get_k_nearest(self):
        if self.nearest is not None:
            return self.nearest
        else:
            return None

    def get_distance_sum(self):
        if self.nearest is not None:
            return self.distance_sum
        else:
            return None

    #打印出每个输入颜色的最近邻颜色矩阵
    def print_nearest(self):
        print(self.nearest)
        print(self.dic[self.CURRENT])
        for i in range(0, len(self.pic)):
            print(str(self.pic[i]) + '的最近邻颜色：')
            for j in range(0, self.K):
                print(self.nearest[i][j], end=' ')
            print('')

    #打印出每个输入颜色的距离列表
    def print_distance_sum(self, distance_sum):
        print(self.dic[self.CURRENT])
        for i in range(0, len(self.pic)):
            print(str(self.pic[i]) + '的与最近邻颜色的平均距离为： ' + str(distance_sum[i]))

    def get_distance_avgsum(self, distance_sum):
        totalsum = 0
        for i in range(0, len(self.pic)):
            totalsum += distance_sum[i]
        return totalsum / len(self.pic)

    #计算最近邻颜色出现的个数
    def calculate_nearest_sum(self):
        temp = [0]*6
        index = 0
        self.nearest_sum = [0]*len(self.pic)
        for each_nearest in self.nearest:
            for rgb_each in each_nearest:
                temp[self.calculate_color_type(self.std.index(rgb_each))]+=1
            self.nearest_sum[index] = max(temp)
            index+=1
            temp = [0] * 6
        self.nearest_sum_max = max(self.nearest_sum)
        return self.nearest_sum_max


    def calculate_color_type(self, index):
        if index >= 0 and index <= 20:
            return 0
        elif index >= 21 and index <= 35:
            return 1
        elif index >= 36 and index <= 55:
            return 2
        elif index >= 56 and index <= 71:
            return 3
        elif index >= 72 and index <= 90:
            return 4
        elif index >= 91 and index <= 107:
            return 5
    def get_showcase(self, index):
        return self.showcase_filename[index]
'''
b = [(98, 101, 89), (128, 158, 106), (71, 108, 78)]
a = ColorHub()
a.read_from_data(b)

    # 计算k-nearest颜色（用欧几里得距离）
a.calculate_k_nearest(a.EUCLIDEAN, 5)

print(a.get_showcase(a.calculate_nearest_sum()))
'''

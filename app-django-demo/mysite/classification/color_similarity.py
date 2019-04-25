import random as rd
import numpy as np

#用Numpy按欧式、曼哈顿、切比雪夫、余弦距离选取若干最近颜色
#标准颜色最多100个

class ColorHub:

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

    #默认为2，可覆盖
    K = 2

    #pic是用户颜色，std是标准颜色
    #_vec为numpy数组形式
    #distance为距离矩阵
    #distance为距离之和列表
    #nearest为最近颜色列表
    pic = []
    std = []
    pic_vec, std_vec = [], []
    distance = []
    distance_sum = []
    nearest = []


    def __init__(self):
        self.calculate_constants()
        pass

    '''
    #随机生成用户颜色和标准颜色的构造函数
    def __init__(self, num: int, id: int):
        self.calculate_constants()
        self.stuff_rand(num, ColorHub.PIC_CONST)
        self.stuff_rand(id, ColorHub.STD_CONST)
    '''

    #从数据读取的功能，需要填写此函数。如需要可以增加参数
    def read_from_data(self, l1, l2):
        self.pic = l1
        self.std = l2
        self.pic_vec = np.array(self.pic)
        self.std_vec = np.array(self.std)
        self.distance = np.zeros((len(self.pic), len(self.std)), dtype='float')


    #随机生成n个颜色
    def stuff_rand(self, num: int, id: int):
        for i in range(0, num):
            if id == self.PIC_CONST:
                self.pic.append([rd.randint(0,255), rd.randint(0,255), rd.randint(0,255)])
            elif id == self.STD_CONST:
                self.std.append([rd.randint(0,255), rd.randint(0,255), rd.randint(0,255)])
            else:
                pass
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
        self.const[self.CHEBYSHEV] = np.linalg.norm(a-b, ord=np.inf)
        self.const[self.COSINE] = np.dot(a, b)/((np.linalg.norm(a))*(np.linalg.norm(b)))

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
            dist, color = zip(*sorted(zip(self.distance[i], self.std_vec)))
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
    def print_nearest(self, nearest):
        print(self.dic[self.CURRENT])
        for i in range(0, len(self.pic)):
            print(str(self.pic[i]) + '的最近邻颜色：')
            for j in range(0, self.K):
                print(nearest[i][j], end=' ')
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

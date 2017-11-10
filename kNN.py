# -*- coding: utf-8 -*-
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import operator

# 原始数据
sj = array(
    [[41.8, 3.17, 166.33, 98.13, 460.48], [59.26, 3.14, 374.34, 49.81, 418.65], [54.49, 2.89, 228.23, 51.56, 252.19],
     [52.79, 2.63, 161.04, 47.17, 370.71], [42.88, 2.66, 150.28, 83.24, 497.91], [44.66, 2.83, 215.61, 80.97, 273.52],
     [53.65, 2.29, 213.29, 54.62, 331.04], [92.68, 2.87, 297.6, 71.25, 346.33], [56.27, 2.41, 257.4, 54.78, 387.54],
     [53.66, 2.28, 254.91, 40.16, 351.53], [53.19, 2.06, 255.04, 73.25, 421.88], [56.79, 3.1, 273.92, 67.88, 466.17],
     [88.55, 3.05, 216.93, 82.8, 340.2], [42.56, 2.3, 304.54, 71.95, 452.82], [51.05, 2.1, 223.01, 59.91, 306.98],
     [44.3, 2.8, 260.5, 77.84, 224.2], [49.52, 2.77, 265.69, 42.36, 179.68], [80.26, 2.27, 194.23, 87.13, 469.96],
     [74.7, 3.25, 208.15, 61.81, 315.34], [71.68, 3.25, 250.73, 41.11, 431.64], [60.28, 2.35, 181.97, 60.93, 410.22],
     [30.32, 1.74, 149.44, 28.11, 169.56], [35.05, 1.85, 138.06, 28.87, 197.23], [31.6, 1.55, 121.71, 34.9, 151.01],
     [32.18, 1.6, 129.18, 28.26, 166.58], [37.43, 1.55, 146.36, 24.49, 180.19], [31.11, 1.56, 123.7, 29.51, 166.39],
     [38.54, 1.54, 122.73, 38.45, 176.35], [31.92, 1.61, 138.37, 31.1, 165.09], [32.21, 1.93, 136.81, 26.96, 176.86],
     [37.01, 1.96, 144.85, 27.69, 167.12], [36.04, 1.97, 131.45, 31.68, 166.65], [38.15, 1.73, 120.23, 21.77, 167.45],
     [30.74, 1.9, 132.73, 35.73, 191.17], [38.68, 1.55, 131.35, 36.52, 172.62], [37.29, 1.85, 127.6, 20.33, 172.09],
     [36.99, 1.68, 125.17, 35.61, 189.1], [38.84, 1.87, 124.63, 35.04, 174.26], [33.85, 1.62, 132.96, 39.76, 158.97],
     [32.42, 1.87, 133.07, 23.6, 184.37], [36.98, 1.66, 144.39, 27.17, 182.43], [39.12, 1.59, 134.15, 24.1, 177.23],
     [21.56, 1.05, 96.06, 14.16, 110.93], [27.47, 1.25, 106.66, 17.42, 132.24], [25.03, 1.34, 99.26, 14.81, 100.11],
     [22.4, 1.17, 105.98, 13.12, 138.19], [29.92, 1.38, 99.6, 11.37, 101.31], [25.75, 1.03, 109.58, 14.73, 125.81],
     [20.24, 1.42, 112.94, 15.55, 116.01], [20.79, 1.05, 101.64, 19.74, 101.33], [26.43, 1.29, 107.69, 13.05, 121.33],
     [28.34, 1.23, 100.38, 18.31, 116.19], [25.02, 1.31, 97.3, 17.01, 141.0], [28.11, 1.31, 95.07, 18.04, 120.97],
     [27.64, 1.36, 114.99, 17.96, 142.47], [25.89, 1.34, 114.74, 12.67, 102.7], [23.82, 1.07, 112.91, 17.95, 133.71],
     [24.73, 1.4, 98.85, 13.65, 109.68], [26.57, 1.2, 98.94, 17.88, 115.15], [23.69, 1.32, 108.61, 16.13, 107.5],
     [27.72, 1.49, 106.06, 10.56, 104.83], [25.13, 1.35, 114.78, 17.33, 117.45], [21.66, 1.24, 96.98, 11.29, 123.45],
     [15.43, 0.7, 92.87, 9.1, 96.53], [16.27, 0.97, 83.37, 5.45, 72.0], [10.35, 0.81, 83.98, 7.07, 78.69],
     [12.85, 0.85, 66.14, 7.82, 72.89], [18.99, 0.78, 77.69, 9.07, 80.82], [11.29, 0.74, 65.85, 5.97, 77.47],
     [19.18, 0.72, 87.74, 7.02, 64.9], [15.68, 0.75, 76.93, 8.86, 72.91], [19.38, 0.88, 78.15, 6.59, 79.06],
     [13.77, 0.87, 63.76, 6.24, 95.69], [16.55, 0.77, 66.4, 7.83, 86.26], [16.18, 0.87, 74.1, 5.13, 75.17],
     [17.73, 0.79, 76.27, 8.54, 72.86], [16.42, 0.77, 71.21, 9.09, 67.2], [12.65, 0.78, 69.28, 7.32, 66.78],
     [11.34, 0.8, 72.78, 7.76, 52.76], [15.92, 0.7, 87.22, 5.13, 62.83], [15.24, 0.8, 81.07, 8.34, 77.88],
     [10.4, 0.8, 69.97, 7.57, 75.01], [10.3, 0.85, 61.42, 6.72, 65.95], [13.0, 0.91, 85.14, 9.69, 69.68],
     [6.97, 0.65, 34.65, 3.56, 36.17], [6.44, 0.62, 46.19, 3.83, 34.35], [7.54, 0.68, 38.24, 4.56, 31.21],
     [7.93, 0.68, 39.23, 3.03, 41.35], [7.13, 0.56, 40.4, 3.53, 43.37], [9.96, 0.65, 42.4, 3.82, 41.14],
     [7.86, 0.7, 58.07, 3.41, 36.26], [6.79, 0.64, 40.01, 4.18, 41.94], [8.78, 0.69, 55.38, 4.84, 44.91],
     [8.82, 0.61, 44.97, 4.02, 37.05], [8.18, 0.61, 53.05, 3.14, 40.92], [8.02, 0.57, 39.03, 4.26, 48.44],
     [6.66, 0.51, 37.27, 3.75, 44.55], [9.65, 0.59, 40.42, 4.12, 34.79], [7.5, 0.62, 37.52, 3.9, 32.66],
     [8.2, 0.57, 51.78, 4.19, 42.96], [7.91, 0.7, 52.82, 3.68, 41.22], [9.96, 0.66, 49.42, 4.38, 43.29],
     [6.46, 0.61, 46.56, 4.83, 44.27], [7.59, 0.69, 47.65, 3.31, 38.77], [6.3, 0.59, 53.3, 4.57, 46.07],
     [4.36, 0.44, 10.7, 2.72, 25.86], [3.2, 0.49, 17.79, 0.34, 27.51], [2.26, 0.45, 5.0, 0.85, 6.18],
     [2.92, 0.42, 15.74, 1.78, 27.27], [5.49, 0.06, 1.37, 1.12, 20.29], [5.27, 0.43, 3.99, 0.01, 12.18],
     [4.09, 0.46, 27.23, 1.15, 26.66], [5.46, 0.6, 30.65, 0.25, 20.85], [2.72, 0.05, 29.9, 1.1, 1.85],
     [5.02, 0.27, 9.92, 2.24, 4.2], [2.51, 0.23, 5.69, 2.07, 17.14], [0.95, 0.13, 19.92, 2.24, 14.15],
     [0.6, 0.36, 3.43, 1.86, 0.84], [3.61, 0.35, 21.28, 0.37, 1.28], [2.84, 0.3, 15.95, 0.64, 14.5],
     [0.95, 0.42, 28.87, 1.99, 7.07], [1.48, 0.12, 21.16, 0.18, 3.11], [5.03, 0.11, 0.48, 2.08, 18.24],
     [0.81, 0.21, 29.22, 2.67, 25.51], [5.05, 0.09, 27.58, 0.83, 10.52], [5.48, 0.08, 28.78, 2.23, 21.03]])

# 原始等级数据
dengji = array(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
     4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6,
     6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])

# 测试原始数据
ceshi_sj = array(
    [[42.39, 2.46, 239.8, 61.84, 368.96], [90.33, 2.18, 236.16, 71.0, 252.12], [54.67, 2.13, 176.69, 59.95, 310.56],
     [59.71, 2.13, 197.85, 71.13, 298.92], [87.27, 2.48, 292.54, 69.12, 216.38], [55.72, 2.69, 225.63, 71.93, 224.01],
     [53.63, 2.85, 286.48, 56.47, 350.34], [73.91, 2.53, 192.81, 97.37, 296.73], [40.38, 2.74, 267.5, 53.77, 327.56],
     [30.96, 1.73, 130.42, 34.95, 181.15], [34.98, 1.74, 125.81, 31.3, 160.17], [37.8, 1.86, 134.68, 26.59, 169.8],
     [35.96, 1.51, 134.73, 29.19, 173.82], [34.79, 1.76, 132.73, 20.19, 169.19], [30.55, 1.87, 136.77, 25.37, 170.89],
     [34.93, 1.55, 120.79, 30.97, 199.72], [39.43, 1.82, 130.11, 25.73, 185.31], [32.85, 1.61, 144.69, 25.34, 154.45],
     [23.65, 1.27, 110.98, 14.77, 108.57], [27.58, 1.16, 107.82, 12.89, 116.22], [23.3, 1.31, 95.15, 14.51, 121.85],
     [22.39, 1.02, 118.26, 19.28, 105.64], [30.9, 1.33, 110.62, 17.92, 110.99], [25.04, 1.36, 94.46, 10.74, 114.73],
     [25.02, 1.11, 98.88, 12.97, 139.68], [24.07, 1.3, 102.78, 11.92, 121.67], [24.78, 1.29, 113.54, 15.02, 140.88],
     [14.43, 0.89, 82.88, 5.12, 50.95], [10.18, 0.71, 61.08, 6.43, 61.96], [12.6, 0.85, 90.58, 7.78, 78.0],
     [14.9, 0.76, 70.67, 7.44, 84.2], [13.26, 0.98, 85.56, 6.76, 78.9], [18.12, 0.98, 84.61, 5.37, 74.83],
     [19.73, 0.79, 73.42, 8.7, 60.87], [16.41, 0.81, 69.7, 7.48, 96.66], [14.65, 1.0, 61.11, 7.23, 86.42],
     [9.18, 0.61, 59.17, 3.4, 37.78], [8.15, 0.56, 59.78, 3.21, 44.47], [8.76, 0.64, 49.58, 3.96, 37.67],
     [9.54, 0.6, 57.18, 4.3, 49.46], [9.0, 0.5, 48.92, 3.32, 49.22], [8.31, 0.59, 42.56, 3.57, 35.28],
     [8.09, 0.64, 44.96, 4.19, 42.67], [8.46, 0.63, 59.69, 4.06, 40.18], [7.9, 0.66, 37.44, 4.17, 46.43],
     [4.25, 0.21, 11.84, 2.01, 29.53], [1.47, 0.24, 20.88, 2.9, 26.36], [2.17, 0.27, 11.01, 1.76, 24.94],
     [1.35, 0.22, 26.7, 1.0, 1.26], [0.14, 0.45, 11.8, 0.46, 7.11], [4.8, 0.28, 26.26, 2.84, 25.68],
     [4.68, 0.01, 7.44, 2.25, 3.32], [1.67, 0.19, 12.21, 1.74, 8.13], [5.69, 0.25, 11.94, 1.87, 0.45]])

# 测试原始等级数据
ceshi_dengji = array(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5,
     5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6
     ])


# 数据集归一化，防止单一属性太大导致影响计算
# 公式 newValue=(oldValue-min)/(max-min)
# 其中oldValue为原始数据
# min、max分别是原始数据里最小、最大值
def autoNorm(dataSet):
    min_value = dataSet.min(0)
    max_value = dataSet.max(0)
    range = max_value - min_value
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(min_value, (m, 1))
    normDataSet = normDataSet / tile(range, (m, 1))
    return normDataSet, range, min_value


# K-近邻算法
# 距离公式 d=((X1-X2)**2+(Y1-Y2)**2)**0.5
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  # 原始数据行数
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet  # 创建一个值为输入的inX的值的并和原始数据一样空间的数组每个值减去原始数据
    sqDiffMat = diffMat ** 2  # diffMat的2次方
    sqDistances = sqDiffMat.sum(axis=1)  # 行相加
    distances = sqDistances ** 0.5  # sqDistances的0.5次方（开根号）
    sortedDistIndicies = distances.argsort()  # 从小到大排列，用索引重新附值
    classCount = {}
    for i in range(k):  # 循环k次查找所对应标签
        voteIlabel = labels[sortedDistIndicies[i]]  # 取sortedDistIndicies中i索引的值，通过labels取出对应的标签
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1  # 查找字典中的值，如果不存在默认为0，然后加1

    # sorted排序函数
    # classCount.iteritems()迭代器，返回键和值
    # operator.itemgetter(1)根据第二个元素（现在是值）
    # reverse = True 降序排列
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


errorCount = 0  # 错误计数
normData, ranges, minVals = autoNorm(sj)  # 原始数据归一化
for i in range(1):
    # 循环提取测试数据
    isarr = ceshi_sj[i]
    # 输入归一化测试数据，和原始数据，和标签，和寻找最近多少个点
    fanhui = classify0((isarr - minVals) / ranges, normData, dengji, 5)
    # 输出第标签与测试标签不一致就，错误就加1
    if (fanhui != ceshi_dengji[i]): errorCount += 1

print "success：" + str((54 - errorCount) / 54 * 100) + "%"


# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(sj[:, 3], sj[:, 4], 15.0 * dengji, 15.0 * dengji)
# plt.show()

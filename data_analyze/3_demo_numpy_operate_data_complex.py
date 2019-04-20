import numpy as np
from scipy.stats.stats import pearsonr

# demo about softmax
#
def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum(axis=0)

def demo_softmax():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='object')
    sepallength = np.array([float(row[0]) for row in iris])
    print(sepallength)
    print(softmax(sepallength))

def demo_softmax_get_miss_value_index():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris_2d = np.genfromtxt(url, delimiter=',', usecols=[0,1,2,3], dtype='float')
    iris_2d[np.random.randint(150, size=20), np.random.randint(4,size=20)] = np.nan
    print("Number of missing values: \n", np.isnan(iris_2d[:,0]).sum())
    print("Position of missing values: \n", np.where(np.isnan(iris_2d[:,0])))

def demo_filter_array_by_condition():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris_2d = np.genfromtxt(url, delimiter=',', usecols=[0, 1, 2, 3], dtype='float')
    condition = (iris_2d[:,2]>1.5) & (iris_2d[:,0] < 5.0)
    print(iris_2d[condition])

def demo_get_row_without_nan():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris_2d = np.genfromtxt(url, delimiter=',', usecols=[0,1,2,3], dtype='float')
    iris_2d[np.random.randint(150, size=20), np.random.randint(4,size=20)] = np.nan
    print(iris_2d[np.sum(np.isnan(iris_2d), axis=1) == 0][:5])

# 找到numpy数组的两列之间的相关性
def get_relation_about_array():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', usecols=[0, 1, 2, 3], dtype='float')
    corr, p_value = pearsonr(iris[:,0], iris[:,2])
    print(corr)
    print(p_value)

# 查找给定数组是否具有任何空值
def get_any_nan():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris_2d = np.genfromtxt(url, delimiter=',', usecols=[0,1,2,3], dtype='float')
    print(np.isnan(iris_2d).any())

# calculator data about numpy math by devision
def calculator_data_about_math_devision():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
    mean, med, std = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
    print('{} {} {}'.format(mean, med, std))

def group_num():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='object')
    names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
    # group
    petal_length_bin = np.digitize(iris[:,2].astype('float'), [0,3,5,8])
    # map text
    label_map = {1:'small', 2:'medium', 3:'large', 4:np.nan}
    petal_length_cat = [label_map[x] for x in petal_length_bin]
    print(petal_length_cat[:4])

# 概率抽样
def get_data_by_probability():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='object')
    

if __name__ == '__main__':
    demo_softmax()
    demo_softmax_get_miss_value_index()
    demo_filter_array_by_condition()
    get_relation_about_array()
    get_any_nan()
    calculator_data_about_math_devision()
    group_num()
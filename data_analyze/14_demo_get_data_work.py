# 1.加载真实数据集（dcdata.data）
# 2.Numpy读取文件后读取对应的样本数据
# 3.抽取对应的建模数据集（训练数据集和测试数据集）
# 4.抽取自变量矩阵X
# 5.抽取因变量矩阵Y
# 6.基于（X-Y）训练集构建决策树模型
# 7.生成模型文件Decisiontree.model
# 8.根据生成的模型文件，输入测试数据样本，调用模型预测测试样本数据

import time
from sklearn import metrics
from sklearn import tree
from sklearn.externals import joblib
import numpy as np

def demo_make_model():
    raw_data = "data/dcdata.data"
    # 加载数据集
    dataset = np.loadtxt(raw_data, delimiter=",")
    # 分割数据为X和Y
    X = dataset[:,0:8]
    Y = dataset[:,8]
    # 训练结合
    X_train = dataset[0:500, 0:8]
    Y_train = dataset[0:500, 8]
    # 测试集合
    X_test = dataset[500:, 0:8]
    Y_test = dataset[500:, 8]
    print('\n调用scikit的tree.DecisionTreeClassifier()')
    model = tree.DecisionTreeClassifier(min_samples_leaf=2)
    start_time = time.time()
    model.fit(X_train, Y_train)
    print('training took %fs!' % (time.time() -  start_time))
    joblib.dump(value=model, filename='data/Decisiontree.model')
    expected = Y_test
    predicted = model.predict(X_test)
    print(metrics.confusion_matrix(expected, predicted))
    print(metrics.classification_report(expected, predicted))

def demo_test_model():
    dataset = np.loadtxt(fname="data/dcdata.data", delimiter=",")
    x_predict = dataset[0:10, 0:8]
    y_real = dataset[0:10, 8]
    gnbmodel = joblib.load(filename="data/Decisiontree.model")
    y_predict = gnbmodel.predict(x_predict)
    print('预测值：')
    print(y_predict)
    print('真实值：')
    print(y_real)

if __name__ == '__main__':
    # demo_make_model()
    demo_test_model()
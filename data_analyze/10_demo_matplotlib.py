from matplotlib.pyplot import *

def demo_matplotlib():
    x = [1,2,3,4,5,6]
    y = [3,4,5,6,7,8]
    figure()
    # 线
    subplot(2,3,1)
    plot(x,y)
    # 柱状图
    subplot(2,3,2)
    bar(x,y)
    # 水平柱状图
    subplot(2,3,3)
    barh(x,y)
    # 叠加柱状图
    subplot(2,3,4)
    bar(x,y)
    y1 = [2,3,4,5,6,7]
    bar(x,y1,bottom=y, color='r')
    # 箱线图
    subplot(2, 3, 5)
    boxplot(x)
    # 散点图
    subplot(2,3,6)
    scatter(x,y)
    show()

if __name__ == '__main__':
    demo_matplotlib()
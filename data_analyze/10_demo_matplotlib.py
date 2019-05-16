from matplotlib.pyplot import *
import numpy as np

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

def demo_hist():
    figure()
    dataset = [1,2,30,4,5,54,2,45,12,23,5,9,6,3,2,12,56,73,2]
    subplot(1,2,1)
    boxplot(dataset, vert=False)
    subplot(1,2,2)
    # 直方图
    hist(dataset)
    show()

def demo_sin_cos():
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    y = np.cos(x)
    y1 = np.sin(x)
    plot(x,y)
    plot(x,y1)
    # 图表名称
    title('Functions $\sin$ and $\cos$')
    # x,y轴坐标范围
    xlim(-3,3)
    ylim(-1,1)
    # 坐标上刻度
    xticks([-np.pi, -np.pi/2.0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    yticks([-1,0,1],
           [r'$-1$', r'$0$', r'$+1$'])
    # 网格
    grid()
    show()


if __name__ == '__main__':
    # demo_matplotlib()
    # demo_hist()
    demo_sin_cos()
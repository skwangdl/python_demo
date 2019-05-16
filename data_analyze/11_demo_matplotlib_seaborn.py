from matplotlib import pyplot as plt
import matplotlib
import numpy as np

def demo_matplotlib():
    x = np.arange(1,11)
    y = 2 * x * x + 5
    plt.title('kepler demo')
    plt.xlabel('x caption')
    plt.ylabel('t caption')
    plt.plot(x,y)
    plt.show()

def demo_matplotlib_zh():
    zhfont = matplotlib.font_manager.FontProperties(fname="data/simhei.ttf")
    x = np.arange(-11,11)
    y = 2 * x * x * x + 5
    plt.title('pyplot绘图', fontproperties=zhfont)
    plt.xlabel('x轴', fontproperties=zhfont)
    plt.ylabel('y轴', fontproperties=zhfont)
    # '*' 参数设定散点图样式, 'r'设定颜色
    plt.plot(x,y,'r*')
    plt.show()

def demo_dif_color_bar():
    x = [5,8,10]
    y = [12,16,6]
    x2 = [6,9,11]
    y2 = [6,15,7]
    plt.bar(x,y,align='center',)
    plt.bar(x2,y2,align='center',color='g')
    plt.title('kepler demo')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()

# 判断a数组元素在bins区间间隔内的频率，输出频率数组
def demo_numpy_histogram():
    a = np.array([1,2,3,14,15,16,27,38,39])
    hist, bins = np.histogram(a,bins=[0,10,20,30,40])
    plt.hist(a, bins=bins)
    print(hist)
    print(bins)
    plt.show()

if __name__ == '__main__':
    # demo_matplotlib()
    # demo_matplotlib_zh()
    # demo_dif_color_bar()
    demo_numpy_histogram()
import matplotlib.pyplot as mpl
from pylab import *
import datetime
import numpy as np
import pandas as pd
import seaborn as sns

def demo_line():
    # 创建一个8 * 6点的图，设置分辨率为80
    figure(figsize=(8,6),dpi=80)
    subplot(1,1,1)
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C,S = np.cos(X),np.sin(X)
    plot(X,C,color="blue", linewidth=1.0, linestyle="-")
    plot(X,S,color="red", linewidth=1.0, linestyle="-")
    xlim(-4.0,4.0)
    xticks(np.linspace(-4,4,9,endpoint=True))
    ylim(-1.0, 1.0)
    yticks(np.linspace(-1, 1, 5, endpoint=True))
    # 以72分辨率保存图片
    savefig("data/fig.png", dpi=72)
    show()

def demo_contour():
    n = 256
    x = np.linspace(-3,3,n)
    y = np.linspace(-3,3,n)
    X,Y = np.meshgrid(x,y)
    contourf(X,Y,temp(X,Y),8,alpha=.75,cmap="jet")
    C = contour(X,Y,temp(X,Y),8,colors='black')
    show()

def temp(x,y):
    return (1-x/2 + x**5 + y**3)*np.exp(-x**2-y**2)

# 折线图
def demo_show_block():
    fig = figure()
    ax = gca()
    start = datetime.datetime(2019,3,11)
    stop = datetime.datetime(2019,3,29)
    delta = datetime.timedelta(days=1)
    dates = mpl.dates.drange(start,stop,delta)
    values = np.random.rand(len(dates))
    ax.plot_date(dates, values, ls='-')
    date_format = mpl.dates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    show()

# 正态分布
def demo_normal_distribution():
    mu = 100
    sigma = 15
    x = np.random.normal(mu, sigma, 10000)
    ax = plt.gca()
    ax.hist(x,bins=30,color='g')
    ax.set_xlabel('V')
    ax.set_ylabel('F')
    ax.set_title(r'$\mathrm{Histogram:}\mu=%d,\sigma=%d$' % (mu, sigma))
    plt.show()

# 散点图
def demo_scatter():
    x = np.random.randn(1000)
    y1 = np.random.randn(len(x))
    y2 = 1.8 + np.exp(x)
    ax1 = plt.subplot(1,2,1)
    ax1.scatter(x,y1,color='r',alpha=.3,edgecolors='white',label='no correl')
    plt.xlabel('no correlation')
    plt.grid(True)
    plt.legend()
    ax1 = plt.subplot(1,2,2)
    # alpha 透明度，edgecolors边缘颜色，label图例
    ax1.scatter(x, y2, color='g', alpha=.3, edgecolors='gray', label='correl')
    plt.xlabel('correlation')
    plt.grid(True)
    plt.legend()
    plt.show()

# seaborn demo
def demo_seaborn():
    sns.set(style="ticks")
    # 创建数据集具有多个子图,构建数据集
    rs = np.random.RandomState(4)
    pos = rs.randint(-1,2,(20,5)).cumsum(axis=1)
    pos -= pos[:,0,np.newaxis]
    step = np.tile(range(5), 20)
    walk = np.repeat(range(20), 5)
    df = pd.DataFrame(np.c_[pos.flat, step, walk], columns=["position", "step", "walk"])

    # 初始化一个网络
    grid = sns.FacetGrid(df, col="walk", hue="walk", palette="tab20c", col_wrap=4)
    # 绘制一条水平线
    grid.map(plt.axhline,y=0,ls=":",c=".5")
    grid.map(plt.plot, "step", "position", marker="o")
    grid.set(xticks=np.arange(5), yticks=[-3,3], xlim=(-.5, 4.5), ylim=(-3.5, 3.5))
    grid.fig.tight_layout(w_pad=1)
    plt.show()

if __name__ == '__main__':
    # demo_line()
    # demo_contour()
    # demo_show_block()
    # demo_normal_distribution()
    # demo_scatter()
    demo_seaborn()
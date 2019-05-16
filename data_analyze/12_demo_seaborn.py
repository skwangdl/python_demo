from pylab import *

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

if __name__ == '__main__':
    # demo_line()
    demo_contour()
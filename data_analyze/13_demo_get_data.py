import numpy as np

def demo_get_data_from_file():
    rdata = np.arange(0,16).reshape(4,4)
    print(rdata)
    # 写入文件
    rdata.tofile(r'data/rd1.bin')
    rdata.tofile(r'data/rd1.txt')
    # 读取文件
    bdata = np.fromfile(r'data/rd1.txt', dtype=np.int32)
    print(bdata)
    bdata.shape=4,4
    print(bdata)
    cdata = np.fromfile('data/rd1.bin')
    print(cdata)

def demo_save_load_txt():
    a = np.arange(0,12,0.5).reshape(4,-1)
    print(a)
    np.savetxt(r'data/npTxt2.txt', a)# 缺省值按照“%.18e”格式保存数据，以空格分隔
    print('get message:')
    print(np.loadtxt(r'data/npTxt2.txt'))
    np.savetxt(r'data/npTxt3.txt', a, fmt="%d", delimiter=",")# 改保存为整数，以逗号分隔
    print(np.loadtxt(r'data/npTxt3.txt', delimiter=','))

if __name__ == '__main__':
    # demo_get_data_from_file()
    demo_save_load_txt()
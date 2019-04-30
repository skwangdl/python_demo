import os
from multiprocessing import Process

def run_proc(name):
    print('Run child Process %s (%s)... ' %(name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s .' %(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print('child process will start')
    p.start()
    # 进程同步使用join
    p.join()
    print('child process end')
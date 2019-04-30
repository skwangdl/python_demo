import time, threading

# python 拥有GIL(Global Interpreter Lock)，每执行100条字节码就会将锁释放，即使多线程在100核的CPU，也只能用到1核
# 但是可以用多进程，每个进程有独立的GIL互不影响

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

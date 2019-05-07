import psutil

def demo_psutil_cpu():
    print(psutil.cpu_count)
    print(psutil.cpu_count(logical=False))
    for i in range(10):
        print(psutil.cpu_percent(interval=1, percpu=True))

def demo_psutil_memory():
    print(psutil.swap_memory())
    print(psutil.virtual_memory())

def demo_psutil_process():
    print(psutil.pids())
    print(psutil.Process(2208))

if __name__ == '__main__':
    demo_psutil_cpu()
    demo_psutil_memory()
    demo_psutil_process()
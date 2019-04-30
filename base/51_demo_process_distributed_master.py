import time, random, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def re_task_queue():
    global task_queue
    return task_queue

def re_result_queue():
    global result_queue
    return result_queue

if __name__ == '__main__':
    QueueManager.register('get_task_queue', callable=re_task_queue)
    QueueManager.register('get_result_queue', callable=re_result_queue)
    manager = QueueManager(address=('127.0.0.1', 8088), authkey=b'kepler')
    manager.start()

    task_q = manager.get_task_queue()
    result_q = manager.get_result_queue()

    for i in range(5):
        n = random.randint(0, 100)
        print('Put task %d...' %n)
        task_q.put(n)

    print('Try get result...')
    time.sleep(20)
    for i in range(5):
        r = result_q.get(timeout=20)
        print('Result: %s' %r)

    manager.shutdown()
    print('master exit.')

from collections import deque

# 在迭代操作或者其他操作的时候，怎样只保留最后d有限几个元素的历史记录
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open(r'D:\\Temp\\pome.txt') as f:
        for line, prevlines in search(f, 'kepler', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

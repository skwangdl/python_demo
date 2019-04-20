import heapq

# get max or min value in collection
def demo_heapq():
    nums = [1,5,8,7,3,6,2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

def get_min_max_in_collection():
    portfolio = [{'name':'a', 'age':2}, {'name':'b', 'age':3}]
    print(heapq.nlargest(1, portfolio, key=lambda a:a['age']))
    print(heapq.nsmallest(1, portfolio, key=lambda a:a['age']))

def demo_heap_list():
    nums = [1,5,8,7,4,6,2]
    heap = list(nums)
    heapq.heapify(heap)
    while heap.__len__() != 0:
        print(heapq.heappop(heap))

if __name__ == '__main__':
    demo_heapq()
    get_min_max_in_collection()
    demo_heap_list()

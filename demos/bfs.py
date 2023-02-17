from collections import deque
import time
from functools import wraps

# from https://www.daniweb.com/programming/software-development/code/486298/a-timing-decorator-python
def print_timing(func):
    '''
    create a timing decorator function
    use
    @print_timing
    just above the function you want to time
    '''
    @wraps(func)  # improves debugging
    def wrapper(*arg):
        start = time.perf_counter()  # needs python3.3 or higher
        result = func(*arg)
        end = time.perf_counter()
        fs = '{} took {:.6f} seconds'
        print(fs.format(func.__name__, (end - start)))
        return result
    return wrapper

@print_timing
def BFS(graph, start, target):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return False

graph = {i: [] for i in range(1, 2001)}
for l in open("graph.gd").read().splitlines():
    nums = [int(num) for num in l.split()]
    graph[nums[0]].append(nums[1])

BFS(graph, 1, 1970)

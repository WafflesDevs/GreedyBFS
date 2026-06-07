
import collections
from collections import deque
from queue import PriorityQueue
grid = [
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0]
]





start = (0, 0)
goal = (5, 5)
current = start 
frontier = PriorityQueue()
explore = []
path = dict()
truepath = dict()
def manhattan_dist(current):
    currentrow,currentcol = current
    goalrow,goalcol = goal
    goal1 =  abs(goalrow  - currentrow)
    current1 = abs(goalcol - currentcol)
    final =  goal1 + current1
    return final
main = manhattan_dist(current) # type: ignore
frontier.put((main,current))

while  frontier.qsize() != 0:
    if (current == goal):
        print("goal has been reached")
        break
    if(current[1] + 1 < len(grid) and grid[current[0]][current[1]+1] == 0 and (current[0],current[1]+1)  not in explore):
        a = manhattan_dist((current[0],current[1]+1))
        frontier.put((a,(current[0],current[1]+1)))
        path[(current[0],current[1]+1)] = current
    if(current[1]-1 >= 0 and grid[current[0]][current[1]-1] == 0 and (current[0],current[1]-1) not in explore):
        b = manhattan_dist((current[0],current[1]-1))
        frontier.put((b,(current[0],current[1]-1)))
        path[(current[0],current[1]-1)] = current
    if(current[0]-1 >= 0  and grid[current[0]-1][current[1]] == 0 and (current[0]-1,current[1]) not in explore ):
        c = manhattan_dist((current[0]-1,current[1]))
        frontier.put((c,(current[0]-1,current[1])))
        path[(current[0]-1,current[1])] = current
    if(current[0]+1 < len(grid) and grid[current[0]+1][current[1]] == 0 and (current[0]+1,current[1]) not in explore ):
        d = manhattan_dist((current[0]+1,current[1]))
        frontier.put((d,(current[0]+1,current[1])))
        path[(current[0]+1,current[1])] = current
    explore.append(current)

    dist,current = frontier.get()
pathway = []
cell = goal
while cell != start:
    pathway.append(cell)
    cell = path[cell]
pathway.append(start)

pathway.reverse()
print(pathway)
    
        
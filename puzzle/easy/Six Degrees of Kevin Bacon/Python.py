import sys
import math
from collections import deque, defaultdict

actor_name = input().strip()
n = int(input())
graph = defaultdict(set)

for i in range(n):
    movie_cast = input().strip()
    movie, actors = movie_cast.split(': ')
    actors_list = actors.split(', ')
    
    for actor in actors_list:
        for co_actor in actors_list:
            if actor != co_actor:
                graph[actor].add(co_actor)

def bfs(start):
    queue = deque([(start, 0)]) 
    visited = set()
    visited.add(start)

    while queue:
        current_actor, distance = queue.popleft()
        
        if current_actor == "Kevin Bacon":
            return distance
        
        for neighbor in graph[current_actor]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

bacon_number = bfs(actor_name)
print(bacon_number)

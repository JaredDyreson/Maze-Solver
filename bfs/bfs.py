#!/usr/bin/env python3.5

from pprint import pprint as pp

graph = {
  'A': ['B', 'C', 'D'],
  'B': ['A','D', 'E'],
  'C': ['A', 'F', 'G'],
  'D': ['B'],
  'E': ['A', 'B','D'],
  'F': ['C'],
  'G': ['C']
}

def bfs_connected_components(graph : dict, start : str):
    explored = []
    queue = [start]

    while queue:
      node = queue.pop(0)
      if node not in explored:
        explored.append(node)
        neighbours = graph[node]
        for neighbour in neighbours:
          queue.append(neighbour)
    return explored

# print(bfs_connected_components(graph, "A"))

def get_components(graph : dict, start : str):
    if start not in graph: return
    return [element for element in graph[start]]

print(get_components(graph, "A"))

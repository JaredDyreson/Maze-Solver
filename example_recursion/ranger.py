#!/usr/bin/env python3.5

# prints values n to k recursively

arr = []
def range_function(start : int, end : int):
    if(start == end): return arr
    elif(start > end): return
    arr.append(start)
    return range_function(start+1, end)

print(*range_function(0, 100))

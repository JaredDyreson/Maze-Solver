#!/usr/bin/env python3.5

arr = [1, 2, 3]

def recursive_counter(arr : list):
    if(len(arr) == 0): return 0
    else: return arr[0] + recursive_counter(arr[1:])
def sum_of_squares(arr : list):
    # exit condition
    if(len(arr) == 0): return 0
    # each element is squared, then added to the rest
    else: return (arr[0]**2) + sum_of_squares(arr[1:])
print(sum_of_squares(arr))

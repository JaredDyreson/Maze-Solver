#!/usr/bin/env python3.5

def reverse_str(string):
    if(len(string) == 0): return
    tmp = string[0]
    reverse_str(string[1:])
    print(tmp, end='')
reverse_str("Hell")

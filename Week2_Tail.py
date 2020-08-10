# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 08:31:27 2020

@author: pjhal
"""

#Week 2: make a function that takes a sequence (like a list, string, or tuple) 
#and a number n and returns the last n elements from the given sequence, as a list

#Test 1
#def tail(sequence, n):
#    return sequence[-n:]

#problem - return value will be same as given sequence type, we want a list

#Test 2
#def tail(sequence, n):
#    return list(sequence[-n:])

#problem - does not work when given value is zero. Will return entire sequence.

#Test 3
#def tail(sequence, n):
#    if n == 0:
#        return []
#    return list(sequence[-n:])

#Bonus 1: Make your function return an empty list for negative values of n
#literally just change n == 0 to n <= 0

#Bonus 2: Make sure your function works with any iterable, not just sequences

#Bonus Test 1
'''
def tail(iterable, n):
    sequence = list(iterable)
    if n <= 0:
        return []
    return sequence[-n:]
'''
#problem - if someone calls a large iterable, we'll make a copy and then give them the last n items
#If the file were large enough (a dozen+ GB) it would be extremely inefficient to loop over and store every line
'''
def tail(iterable, n):
    items = []
    if n <= 0:
        return []
    for item in iterable:
        item = [*items[-(n-1):], item]
    return items
'''
#note - we're using * to unpack (n-1) items into a new list with our current item at the end
#problem - this does not work when value is one. When n = 1 (n-1) is zero and our items list will grow continually

#Bonus Test 2
'''
def tail(iterable, n):
    items = []
    if n == 1:
        for item in iterable:
            items = [item]
    elif n > 0:
        for item in iterable:
            items = [*items[-(n-1):], item]
    return items
'''
#more efficient but looks repetitive, can move if-else outside for loop without repeating if we pass in slice objects

#Bonus Test 3
'''
def tail(iterable, n):
    items = []
    if n <= 0:
        return []
    elif n == 1:
        index = slice(0,0)
    else:
        index = slice(-(n-1), None)
    for item in iterable:
        items = [*items[index], item]
    return items
'''

#Better Method with [deque] from the [collections] module

from collections import deque

'''
def tail(iterable, n):
    if n <= 0:
        return []
    items = deque(maxlen=n)
    for item in iterable:
        items.append(item)
    return list(items)
'''
#note - when you append to a deque which has reached its maximum length, it will remove the item closest to beginning before appending

#Optimal Method
def tail(iterable, n):
    if n <= 0:
        return []
    return list(deque(iterable, maxlen=n))
#-*- coding:utf-8 -*-
#########################################################################
# File Name: quickSort.py
# Author: Shen Bo
# mail: Bo.A.Shen@alcatel-sbell.com.cn
# Created Time: Mon Nov  5 15:54:07 2018
#########################################################################
#!usr/bin/env python3

def quicksort(array):
    less = []
    greater = []

    if len(array) <= 1:
        return array

    pivot = array.pop()

    for x in array:
        if x <= pivot : less.append(x)
        else: greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)

if "__main__" == __name__:

    array = [9, 8, 4, 5, 32, 64, 2, 1, 0, 10, 19, 27]
    print("Original array: ", array)

    sorted_array = quicksort(array)
    print("Sorted array: ", sorted_array)

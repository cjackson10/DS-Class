#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Candice Jackson
10/23/19
Description: Using Sorting Algothrim
"""

def bubbleSort(list): #defining bubble sort function
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum): #using in operator to search the list
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [12,200,45,1,57,23] #creating list variable
bubbleSort(list) #calling bubble sort function
print(list) #printing the sorted list 

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    new_list1 = []
    new_list2 = []
    k = 2
    for i in range(2,n+1):
        if k >= len(new_list1):
            if n%i == 0 :
                new_list1.append(i)
    for i in range(1,n+1) :
        if n%new_list1[0] == 0 :
            new_list2.append("Fizz")
        elif n%new_list1[1] == 0 :
            new_list2.append("Buzz")
        elif n%new_list1[0] == 0 and n%new_list1[1] == 0 :
            new_list2.append("FizzBuzz")
        else :
            new_list2.append(i)
    for i in new_list2 :
        print(i)
            
                
        

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)

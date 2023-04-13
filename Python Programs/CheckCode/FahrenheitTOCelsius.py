from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
# Celsius = (Fahrenheit - 32) x 5/9
S = int(input())
E = int(input())
W = int(input())

for i in range(S,E+1,78):
    Celsius = (i-32) * (5//9)
    print(f"{i}\t{Celsius}")

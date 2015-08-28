__author__ = 'Daeho'
import random

A = []

for k in range(1,46):
    A.append(k)
    random.shuffle(A)

for i in range(0,6):
    print(A[i])


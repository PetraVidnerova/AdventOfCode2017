import numpy as np

matrix = np.loadtxt('input02.txt')

sum = 0 
for line in matrix:
    for x in line:
        for y in line:
            if x != y and x % y == 0:
                sum += x / y

print(sum)

import numpy as np

matrix = np.loadtxt('input02.txt')

sum = 0 
for line in matrix:
    sum += np.max(line) - np.min(line)
print(sum)

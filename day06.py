import numpy as np

banks = input().split()
banks = tuple(map(int, banks))

seen = set()
seen.add(banks)
steps = 0

while True:
    new = list(banks)
    max = np.argmax(new)
    count = new[max] 
    new[max] = 0
    i = (max + 1) % len(new) 
    while count:
        new[i] += 1
        count -= 1
        i = (i + 1) % len(new)
    banks = tuple(new)
    steps += 1 
    if banks in seen:
        break
    else:
        seen.add(banks)
    
print(steps)

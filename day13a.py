ranges = {}
scanners = {}
directions = {} 
periods = {} 

max = 0
with open("input13.txt") as f:
    for line in f:
        left, right = line.split(": ")
        depth, drange = int(left), int(right)
        ranges[depth] = drange
        scanners[depth] = 0
        directions[depth] = 1
        periods[depth] = 2 * drange - 2
        if depth > max:
            max = depth 


def delay_save(delay):
    for s in periods:
        if (delay + s) % periods[s] == 0:
            return False
    return True 
            
delay = 0
while not delay_save(delay):
    print(delay)
    delay += 1

print(delay)


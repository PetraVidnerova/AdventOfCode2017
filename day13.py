ranges = {}
scanners = {}
directions = {} 

max = 0
with open("input13.txt") as f:
    for line in f:
        left, right = line.split(": ")
        depth, drange = int(left), int(right)
        ranges[depth] = drange
        scanners[depth] = 0
        directions[depth] = 1
        if depth > max:
            max = depth 

def update_scanners():
    for s in scanners:
        if directions[s] == 1:
            scanners[s] += 1
            # change direction 
            if scanners[s] == ranges[s]-1:
                directions[s] = -1 
        else:
            scanners[s] -= 1
            # change direction
            if scanners[s] == 0:
                directions[s] = 1 

severity = 0
for i in range(max+1):
    if i in scanners and scanners[i] == 0:
        severity += i * ranges[i] 
    update_scanners()

print(severity)

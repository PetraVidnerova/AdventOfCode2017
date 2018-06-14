pixels_on = set()

size = None
with open('input22.txt') as f:
    for i, line in enumerate(f):
        if i == 0: size = len(line.strip())
        for j, ch in enumerate(line):
            if ch == "#":
                pixels_on.add((i, j))

start = ( size // 2, size // 2)
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3 
steps = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1)
}
direction = UP
count = 0 


def burst(pos, direction):
    global count
    global pixels_on
    
    # change direction
    if pos in pixels_on:
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    # infect node
    if pos in pixels_on:
        pixels_on.remove(pos)
    else:
        pixels_on.add(pos)
        count += 1
    #change position
    newpos = pos[0] + steps[direction][0], pos[1] + steps[direction][1]
    return newpos, direction

for _ in range(10000):
    start, direction = burst(start, direction)

print(count)


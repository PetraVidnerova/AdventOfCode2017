RIGHT, UP, LEFT, DOWN = range(4)
steps = { RIGHT : 1,
          UP : 1,
          LEFT : 2,
          DOWN : 2 }
moves = { RIGHT : (1, 0),
          UP : (0, 1),
          LEFT : (-1, 0),
          DOWN : (0, -1) }
neighbors = [ (0, 1), (-1, 1), (1, 1),
              (0, -1), (-1, -1), (1, -1),
              (-1, 0), (1, 0) ] 


def find(number):
    x, y = 0, 0
    direction = RIGHT
    keep_dir = steps[direction]
    numbers = { (0, 0) : 1 }

    while numbers[(x, y)] <= number:
        keep_dir -= 1
        x += moves[direction][0]
        y += moves[direction][1]
        numbers[(x, y)] = sum([ numbers.get((x+i, y+j), 0) for i, j in neighbors ]) 
        if keep_dir == 0:
            steps[direction] = steps[direction] + 2
            direction = (direction + 1) % 4
            keep_dir = steps[direction]

    return numbers[(x, y)]


number = find(int(input()))
print(number)


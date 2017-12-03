RIGHT, UP, LEFT, DOWN = range(4)
steps = { RIGHT : 1,
          UP : 1,
          LEFT : 2,
          DOWN : 2 }
moves = { RIGHT : (1, 0),
          UP : (0, 1),
          LEFT : (-1, 0),
          DOWN : (0, -1) }

def coords(number):
    x, y = 0, 0
    direction = RIGHT
    keep_dir = steps[direction]
    
    while number > 1:
        keep_dir -= 1
        number -= 1
        x += moves[direction][0]
        y += moves[direction][1]
        if keep_dir == 0:
            steps[direction] = steps[direction] + 2
            direction = (direction + 1) % 4
            keep_dir = steps[direction]

    return x, y


x, y = coords(int(input()))
print(x, y)
print(abs(x) + abs(y))


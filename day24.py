parts = [] 
with open("input24.txt") as f:
    for line in f:
        x, y = line.split("/")
        parts.append((int(x), int(y)))

                     

def max_bridge(parts, start=0):
    max = 0
    for x in parts:
        if x[0] == start:
            left = parts.copy()
            left.remove(x)
            w = x[0] + x[1] +  max_bridge(left, x[1]) 
            if w > max:
                max = w
        if x[1] == start:
            left = parts.copy()
            left.remove(x)
            w = x[0] + x[1] + max_bridge(left, x[0])
            if w > max:
                max = w
    return max


print(max_bridge(parts))

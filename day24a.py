parts = [] 
with open("input24.txt") as f:
    for line in f:
        x, y = line.split("/")
        parts.append((int(x), int(y)))

                     

def max_bridge(parts, start=0):
    max = 0
    len = 0
    for x in parts:
        if x[0] == start:
            left = parts.copy()
            left.remove(x)
            w, l =  max_bridge(left, x[1])
            l += 1
            w += x[0] + x[1]
            if l > len:
                max = w
                len = l
            elif l == len and w > max:
                max = w
        if x[1] == start:
            left = parts.copy()
            left.remove(x)
            w, l =  max_bridge(left, x[0])
            l += 1
            w += x[0] + x[1]
            if l > len:
                max = w
                len = l
            elif l == len and w > max:
                max = w
    return  max, len


print(max_bridge(parts))

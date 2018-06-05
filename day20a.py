# advent of code 2017
# day 20
import numpy as np 
import re 

class Particle:

    def __init__(self, p, v, a):
        self.p = np.array(p)
        self.v = np.array(v)
        self.a = np.array(a)

    def update(self):
        self.v = self.v + self.a
        self.p = self.p + self.v

    def distance(self):
        return np.sum(np.abs(self.p))

def convert(s):
    """ Convert string x, y, z to tuple of integers (x, y, z) """ 
    (x, y, z) = map(int, s.split(','))
    return (x, y, z)

    
def read_input():
    particles = [] 
    with open("input20.txt") as f:
        for line in f:
            match = re.match(r'p=<(.*)>, v=<(.*)>, a=<(.*)>', line)
            p, v, a = convert(match[1]), convert(match[2]), convert(match[3])
            particles.append(Particle(p, v, a))
    return particles 


def delete_collisions(particles):
    slots = dict()
    for x in particles:
        p = tuple(x.p)
        if p in slots:
            slots[p].append(x)
        else:
            slots[p] = [ x ]
            
    for slot in slots:
        if len(slots[slot]) > 1:
            for x in slots[slot]:
                particles.remove(x)
    return particles 

particles = read_input()
for _ in range(10000):
    if _ % 100 == 0:
        print(_)
    for x in particles:
        x.update()
    particles = delete_collisions(particles)

print(len(particles))

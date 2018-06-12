# advent of code 2017
# day 21

import numpy as np
import math

class Pattern():
    
    def __init__(self, string):
        lines = string.split('/')
        self.size = len(lines)
        self.pattern = [ list(self.convert(line)) for line in lines ] 
        self.pattern = np.array(self.pattern)

        
    def convert(self, line):
        res = []
        for ch in line:
            if ch == '#':
                res.append(1)
            else:
                assert ch == '.'
                res.append(0)
        return res 

    
    def equals(self, pattern):
        if self.size != pattern.size:
            return False

        for p in [ pattern.pattern,
                   np.flip(pattern.pattern, axis=0),
                   np.flip(pattern.pattern, axis=1) ]:            
        
            if np.all(self.pattern == p):
                return True
        
            for k in range(1,4):
                if np.all(self.pattern == np.rot90(p, k=k)):
                    return True
            
        return False 

    def split(self):
        
        for size in [2, 3]:
            if self.size % size == 0:
                number = self.size // size 
                patterns = [ self.pattern[i*size:(i+1)*size,j*size:(j+1)*size] for i in range(number) for j in range(number) ]
                ret = []
                for p in patterns:
                    newp = Pattern("")
                    newp.size = size
                    newp.pattern = p
                    ret.append(newp)
                return ret 

        raise Exception("Invalid size of pattern.")

    def __str__(self):
        m, n = self.pattern.shape
        ret = "" 
        for i in range(m):
            for j in range(n):
                ret += "#" if self.pattern[i,j] else "."
            ret += "\n"
        return ret
                    

    
def concatenate_pats(patterns):
    pattern = Pattern("")
    size = patterns[0].size
    line_size = int(math.sqrt(len(patterns)))
    pattern.size = line_size * patterns[0].size
    
    patterns = np.asarray([p.pattern for p in patterns])
    lines = [ np.hstack(x) for x in np.split(patterns, line_size)]
    pattern.pattern = np.vstack(lines)
    return pattern 
        
class Rule():

    def __init__(self, line):
        left, right = line.split(" => ")
        left = left.strip()
        right = right.strip()
        self.left = Pattern(left)
        self.right = Pattern(right)
    
    def try_apply(self, pattern):
        if self.left.equals(pattern):
            return self.right
        else:
            return None



def one_iteration(pattern, rules):

#    print("one iteration")
#    print(pattern)
#    print("----")
    
    if pattern.size < 4:
        for r in rules:
            new_pattern = r.try_apply(pattern)
            if new_pattern:
                return new_pattern
        print("No rule applicable")
        return pattern

    patterns = pattern.split()
    new_patterns = []
    for p in patterns:
        new_patterns.append(one_iteration(p, rules))
    pattern = concatenate_pats(new_patterns)
        
    return pattern

if __name__ == "__main__":

    start = Pattern(".#./..#/###")
    rules = []
    with open("input21.txt") as f:
        for line in f:
            rules.append(Rule(line))

    for i in range(18):
        print(start)
        print("iter", i)
        start = one_iteration(start, rules)

    print(start)

    print(np.sum(start.pattern))

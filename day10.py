class CircularList():
    def __init__(self):
        self.numbers = list(range(256))
        self.len = 256
        
    def set(self, index, x):
        self.numbers[index % self.len] = x

    def get(self, index):
        return self.numbers[index % self.len] 

    def check(self):
        return self.numbers[0]*self.numbers[1]

    def print(self):
        print(self.numbers)
    
lengths = input()
lengths = lengths.split(",")
lengths = list(map(int, lengths))

mylist = CircularList()
start = 0
skip = 0
for len in lengths:
    #mylist.print()
    print("proceed ", len)
    # rotate
    rs = start
    re = start+len-1
    while rs < re:
        s_val, e_val = mylist.get(rs), mylist.get(re)
        mylist.set(rs, e_val)
        mylist.set(re, s_val)
        rs += 1
        re -= 1

    # skip
    start += len
    start += skip

    # update skip 
    skip += 1

print(mylist.check())

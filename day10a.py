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
lengths = lengths.strip()
lengths = list(lengths)
lengths = list(map(lambda x: ord(x), lengths))
lengths += [17, 31, 73, 47, 23]


mylist = CircularList()
start = 0
skip = 0
for i in range(64):
    for length in lengths:
        #mylist.print()
        print("proceed ", length)
        # rotate
        rs = start
        re = start+length-1
        while rs < re:
            s_val, e_val = mylist.get(rs), mylist.get(re)
            mylist.set(rs, e_val)
            mylist.set(re, s_val)
            rs += 1
            re -= 1

        # skip
        start += length
        start += skip

        # update skip 
        skip += 1

# reduce to dense hash
long_list = mylist.numbers
dense_list = []

for i in range(16):
    hash = long_list[i*16]
    for j in range(1, 16):
        hash ^= long_list[i*16+j]
    dense_list.append(hash)

print(dense_list)

hexhash = ""
for x in dense_list:
    hexstring = "{0:0{1}x}".format(x, 2)
    hexhash += hexstring

print(hexhash)

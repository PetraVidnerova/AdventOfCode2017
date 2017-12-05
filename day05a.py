instructions = []

with open("input05.txt") as f:
     for line in f:
     	 instructions.append(int(line))

cursor = 0
steps = 0

while cursor >= 0 and cursor < len(instructions):
     steps += 1
     last = cursor 
     cursor += instructions[cursor]
     if instructions[last] >= 3:
          instructions[last] -= 1
     else:
          instructions[last] += 1
          
print(steps)

     

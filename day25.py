import re

LEFT = -1
RIGHT = 1

start = None
steps = None

rules = dict()
tape = dict()
cur = 0 

with open("input25.txt") as f:
    inrule = False
    state = None
    in_possitive = False
    in_negative = False
    move, write, cont = None, None, None
    possitive = None
    negative = None
    
    for line in f:
        m = re.match(r'Begin in state (.)', line)
        if m:
            start = m.group(1)
            continue
        m = re.match(r'Perform a diagnostic checksum after (\d+) steps.', line)
        if m:
            steps = int(m.group(1))
            continue
        m = re.match(r'In state (.)', line)
        if m:
            inrule = True
            state = m.group(1)
            continue
        m = re.match(r'\W+If the current value is 0:', line)
        if m:
            if not inrule:
                raise Exception("parse error")
            in_negative = True
            continue
        m = re.match(r'\W+If the current value is 1:', line)
        if m:
            if not inrule:
                raise Exception("parse error")
            in_possitive = True
            continue
        m = re.match(r'\W+- Write the value ([0,1]).', line)
        if m:
            if not inrule or not (in_negative or in_possitive):
                raise Exception("parse error")
            write = int(m.group(1))
            continue
        m = re. match(r'\W+- Move one slot to the (right|left).', line)
        if m:
            if not inrule or not (in_negative or in_possitive):
                raise Exception("parse error")
            if m.group(1) == "right":
                move = RIGHT
            else:
                move = LEFT
            continue
        m = re.match(r'\W+- Continue with state (.).', line)
        if m:
            if not inrule or not (in_negative or in_possitive):
                raise Exception("parse error")
            cont = m.group(1)
            if in_negative:
                negative = (write, move, cont)
                in_negative = False
                continue
            if in_possitive:
                possitive = (write, move, cont)
                in_possitive = False
                inrule = False
                rules[state] = (possitive, negative)
                continue

state = start 
for _ in range(steps):
    # choose rule 
    if tape.get(cur, 0):
        rule = rules[state][0]
    else:
        rule = rules[state][1]
        
    # update tape
    tape[cur] = rule[0]
    # move cursor 
    cur += rule[1]
    # update state 
    state = rule[2] 


print(len([x for x, i  in tape.items() if i == 1]))    

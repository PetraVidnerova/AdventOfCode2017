program_weights = {} 
program_sons = {}
programs = set()
beeing_hold = set()

# read the input and find the top 
with open('input07.txt') as f:
    for line in f:
        # take name and weight
        name = line.split()[0]
        programs.add(name)
        weight = int(line.split()[1].lstrip('(').rstrip(')'))
        program_weights[name] = weight 
        
        # add programs it is holding to list beeing_hold
        if '->' in line:
            names = line.split('->')[1]
            names = names.strip().split(', ')
            program_sons[name] = names
            beeing_hold = beeing_hold | set(names)

top = list(programs - beeing_hold)[0]
print(top)

def is_list(name):
    return not (name in program_sons)
    
def weight(name):
    if is_list(name):
        return program_weights[name]
    else:
        my_weight = program_weights[name]
        for son in program_sons[name]:
            my_weight += weight(son)
        return my_weight

def find(name):
    w_counts = {} 
    for son in program_sons[name]:
        son_weight = weight(son)
        if not son_weight in w_counts:
            w_counts[son_weight] = set()
        w_counts[son_weight].add(son)
    for key in w_counts:
        if len(w_counts[key]) == 1:
            unbalanced = list(w_counts[key])[0]
            if is_list(unbalanced):
                return unbalanced
            else:
                ret = find(unbalanced)
                if ret is None:
                    return unbalanced
                else:
                    return ret

unbalanced = find(top)
print(unbalanced)

def find_weight(top, name):
    if not top in program_sons:
        return None
    if name in program_sons[top]:
        if name != program_sons[top][0]:
            wanted = weight(program_sons[top][0])
        else:
            wanted = weight(program_sons[top][1])
        w = program_weights[name]
        total = weight(name)
        return w + (wanted - total)
    else:
        for son in program_sons[top]:
            ret = find_weight(son, name)
            if ret is not None:
                return ret 
    

print(find_weight(top, unbalanced))
        

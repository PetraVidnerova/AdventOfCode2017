sequence = input()

groups = 0
ignore = False
garbage = False
score = 0
canceled = 0 

for ch in sequence:
    if not ignore:
        if garbage:
            if ch == "!":
                ignore = True
                continue
            if ch == ">":
                garbage = False
                continue
            canceled += 1
        else:
            if ch == "{":
                groups += 1
                continue
            if ch == "}":
                score += groups 
                groups -= 1
                continue
            if ch == "<":
                garbage = True
                continue
    else:
        ignore = False
    
print(canceled)

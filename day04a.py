def valid(passphrase):
    passwds = passphrase.split(' ')
    passwds = list(map(lambda x: "".join(sorted(x)), passwds))
    return len(passwds) == len(set(passwds))

count = 0
with open('input04.txt') as f:
    for line in f:
        if valid(line.rstrip()):
            count += 1

print(count)

input = input()
sum = 0
halfway = int(len(input)/2)

for i in range(len(input)):
    if input[i] == input[(i+halfway)%len(input)]:
        sum += int(input[i])
print(sum)

input = input()
sum = 0

if not input:
    print(sum)
    exit()  

input += input[0]
for i in range(len(input)-1):
    if input[i] == input[i+1]:
        sum += int(input[i])
print(sum)

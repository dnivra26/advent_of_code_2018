file = open("input.txt", "r")
result = 0
for line in file:
    if line[0] == '+':
        result += int(line[1:])
    else:
        result -= int(line[1:])
print(result)
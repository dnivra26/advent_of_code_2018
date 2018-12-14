from string import ascii_lowercase
file = open("input.txt", "r")

line = file.read().splitlines()[0]
min_size = 50000

def react(line):
    while True:
        removed = False
        for i in range(0, len(line) - 1): 
            first = line[i]
            second = line[i+1]
            if abs(ord(first) - ord(second)) == 32:
                removed = True
                line = line[:i] + line[i+1+1:]
                break
        if not removed:
            return len(line)

for alpha in ascii_lowercase:
    temp = line.replace(alpha, '').replace(alpha.upper(), '')
    length = react(temp)
    if(length < min_size):
        min_size = length
    
print(min_size)

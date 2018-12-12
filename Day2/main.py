from collections import Counter

file = open("input.txt", "r")
count2 = 0
count3 = 0

def two_three(counter):
    two = False
    three = False
    for _, obj in enumerate(counter):
        if counter[obj] == 2:
            two = True
        if counter[obj] == 3:
            three = True
    return two,three

for line in file:
    counter = Counter(line)
    two, three = two_three(counter)
    if two:
        count2 = count2+1
    if three:
        count3 = count3+1    

print(count2*count3)    



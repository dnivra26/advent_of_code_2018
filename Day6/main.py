file = open("input.txt", "r")

lines = file.read().splitlines()

min_x = 1000
min_y = 1000
max_x = 0
max_y = 0
for line in lines:
    point_array = line.split(",")
    x = int(point_array[0])
    y = int(point_array[1])
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y            

print(min_x, min_y, max_x, max_y)

def get_distance(x1, y1, line_item):
    point_array = line_item.split(",")
    x2 = int(point_array[0])
    y2 = int(point_array[1])
    return abs(x1-x2) + abs(y1-y2)

# Part 2 of the problem starts
total = 0
for i  in range(min_x, max_x):
    for j in range(min_y, max_y):
        distance = 0
        for line in lines:
            distance = distance + get_distance(i, j, line)
        if distance < 10000:
            total = total + 1

print(total)
# Part 2 of the problem ends

def get_index_or_duplicate(distances):
    min_d = min(distances)
    indices = [i for i, x in enumerate(distances) if x == min_d]
    if len(indices) > 1:
        return None
    else:
        return indices[0]

temp = {}

for i  in range(min_x, max_x):
    for j in range(min_y, max_y):
        distances = []
        for line in lines:
            distances.append(get_distance(i, j, line))
        temp[(i, j)] = get_index_or_duplicate(distances)

values = {}
for key in temp:
    if temp[key] not in values:
        values[temp[key]] = 0
    else:
        values[temp[key]] = values[temp[key]] + 1

max = 0
for key in values:
    if values[key] > max:
        max = values[key]

print(max + 1)
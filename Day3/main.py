file = open("input.txt", "r")
output = {}
points = {}
for line in file:
    temp_array1 = line.split("@")
    claim_id = temp_array1[0].split("#")[1]
    temp_array2 = temp_array1[1].split(":")
    temp_array3 = temp_array2[0].split(",")
    temp_array4 = temp_array2[1].split("x")

    left = int(temp_array3[0])
    top = int(temp_array3[1])
    width = int(temp_array4[0])
    height = int(temp_array4[1])
    x1 = left
    x2 = left + width - 1
    y1 = top
    y2 = top + height - 1

    
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if claim_id in points:
                points[claim_id].append((i, j))
            else:
                points[claim_id] = [(i, j)]

            if (i,j) in output:
                output[i,j] = output[i,j] + 1
            else:
                output[i,j] = 1

count = 0
for key in output:
    if output[key] > 1:
        count = count + 1

for key in points:
    not_touched = True
    for point in points[key]:
        if output[point] != 1:
            not_touched = False
            break

    if not_touched:
        print(key)
        break
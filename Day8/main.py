file = open("input2.txt", "r")

values = file.read().splitlines()[0].split(" ")

def iterate(index):
    child_count = int(values[index])
    metadata_count = int(values[index + 1])
    
    print("node index: ", index, "child count: ", child_count, "metadata count: ", metadata_count)
    if child_count == 0:
        return index + 2 + metadata_count
    else:
        depth = index + 2
        for child in range(0, child_count):
            depth = iterate(depth)

iterate(0)
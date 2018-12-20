file = open("input.txt", "r")
values = file.read().splitlines()[0].split(" ")

def iter(index, metadata):
    if index >= len(values):
        return index, metadata

    child_count = int(values[index])
    metadata_count = int(values[index + 1])
    
    if child_count == 0:
        return index + 2 + metadata_count, metadata + values[index+2 : index+2+metadata_count]
    else:
        depth = index + 2
        for _ in range(0, child_count):
            depth, metadata = iter(depth, metadata)
        return depth+ metadata_count, metadata + values[depth : depth+metadata_count]

depth, metadata = iter(0, [])
print(sum(list(map(int, metadata))))
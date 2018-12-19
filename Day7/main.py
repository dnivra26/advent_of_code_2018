import re
file = open("input.txt", "r")

lines = file.read().splitlines()

dependencies = {}
dependents = {}
unique_items = []
traversed_items = []
assigned_items = []

worker1 = []
worker2 = []
worker3 = []
worker4 = []
worker5 = []


for line in lines:
    match = re.match(r'Step (.*) must be finished before step (.*) can begin', line)
    first = match.group(1)
    second = match.group(2)
    if first not in unique_items:
        unique_items.append(first)
    if second not in unique_items:    
        unique_items.append(second)
    if first not in dependents:
        dependents[first] = [second]
    else:
        dependents[first].append(second)

    if second not in dependencies:
        dependencies[second] = [first]
    else:
        dependencies[second].append(first)

time = 0
while (not set(unique_items).issubset(traversed_items)):
    for worker in worker1, worker2, worker3, worker4, worker5:
        available_items = []

        if len(worker) != 0:
            if (worker[-1] != '.')  & ((len(worker) - worker[::-1].index(worker[-1]) - worker.index(worker[-1])) == ((ord(worker[-1]) - 64) + 60)):
                traversed_items.append(worker[-1])

        for c in unique_items:
            if c not in dependencies:
                available_items.append(c)

        for a in traversed_items:
            if a in dependents:
                for b in dependents[a]:
                    if (b not in traversed_items) & (b not in available_items) & (set(dependencies[b]).issubset(traversed_items)):
                        available_items.append(b)
        
        for avai in assigned_items:
            if avai in available_items:
                available_items.remove(avai)

        available_items.sort()

        if len(available_items) == 0:
            if len(worker) == 0:
                worker.append('.')
            elif (worker[-1] != '.')  & ((len(worker) - worker[::-1].index(worker[-1]) - worker.index(worker[-1])) == ((ord(worker[-1]) - 64) + 60)):
                worker.append('.')    
            else:
                worker.append(worker[-1])

        else: 
            for item in available_items:
                if len(worker) == 0:
                    worker.append(item)
                    assigned_items.append(item)
                    available_items.remove(item)
                    break
                elif worker[-1] == '.':
                    worker.append(item)
                    assigned_items.append(item)
                    available_items.remove(item)
                    break
                elif (worker[-1] != '.')  & ((len(worker) - worker[::-1].index(worker[-1]) - worker.index(worker[-1])) == ((ord(worker[-1]) - 64) + 60)):
                    worker.append(item)
                    assigned_items.append(item)
                    available_items.remove(item)
                    break
                else:
                    worker.append(worker[-1])
    
    time = time + 1

print(time - 1)
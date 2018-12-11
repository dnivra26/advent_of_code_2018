
result = 0
result_array = []


def iterate(result, result_array):
    file = open("input.txt", "r")
    for line in file:
        result = first(result, line)
        if result not in result_array:
            result_array.append(result)
        else:
            return result, result, result_array    
    return None, result, result_array

def first(result, line):
    if line[0] == '+':
        return (result + int(line[1:]))
    else:
        return (result - int(line[1:]))


while True:
    output, result, result_array = iterate(result, result_array)
    if output is not None:
        print(output)
        break
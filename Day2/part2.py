file = open("input.txt", "r")

lines = file.read().splitlines()


for i, val1 in enumerate(lines):
    for j, val2 in enumerate(lines):
        if (i != j) & (len(val1) == len(val2)):
            single_difference_found = False
            ideal_combination = True
            differing_index = 0
            for k in range(len(val1)):
                if(ord(val1[k]) == ord(val2[k])):
                    continue
                elif (not single_difference_found):
                    single_difference_found = True
                    differing_index = k
                    continue
                else:
                    ideal_combination = False
                    break

            if ideal_combination:
                print(val1[:differing_index] + val1[differing_index+1:])
            

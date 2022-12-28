import pdb

puzzle_input = open('../inputs/day6_input.txt', 'r')

def is_marker(charset):
    #pdb.set_trace()
    for i in range(0, len(charset)-1):
        if charset[i] in charset[i+1:]: 
            return False

    return True

def find_marker(file):
    datastream = file.readline().strip()
    i = 4
    marker_found = is_marker(datastream[i-4:i])

    while (not marker_found) and (i < len(datastream)):
        i += 1
        #print(datastream[i-4:i])
        marker_found = is_marker(datastream[i-4:i])

    return i

print(find_marker(puzzle_input))

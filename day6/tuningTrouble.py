import pdb

puzzle_input = open('../inputs/day6_input.txt', 'r')
markers = {'packet': 4, 'message': 14}

def is_marker(charset):
    #pdb.set_trace()
    for i in range(0, len(charset)-1):
        if charset[i] in charset[i+1:]: 
            return False

    return True

#marker_type should be 'packet' or 'message'
def find_marker(datastream, marker_type):
    stream_length = markers[marker_type]
    i = stream_length
    marker_found = is_marker(datastream[i-stream_length:i])

    while (not marker_found) and (i < len(datastream)):
        i += 1
        marker_found = is_marker(datastream[i-stream_length:i])

    return i

datastream = puzzle_input.read().strip()
start_of_packet = find_marker(datastream, 'packet')
start_of_message = find_marker(datastream, 'message')
print("start_of_packet: " + str(start_of_packet))
print("start_of_message: " + str(start_of_message))

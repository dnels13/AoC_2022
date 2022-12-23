puzzle_input = open('../inputs/day4_input.txt', 'r')

def complete_overlap(ass1, ass2):
    return (((ass1[0] <= ass2[0]) and (ass1[1] >= ass2[1])) or
    ((ass1[0] >= ass2[0]) and (ass1[1] <= ass2[1])))

def any_overlap(ass1, ass2):
    overlap = False
    overlap = ( overlap or (ass1[0] <= ass2[1] and ass1[0] >= ass2[0]) or
    (ass1[1] <= ass2[1] and ass1[1] >= ass2[0]) )

    overlap = ( overlap or (ass2[0] <= ass1[1] and ass2[0] >= ass1[0]) or
    (ass2[1] <= ass1[1] and ass2[1] >= ass1[1]) )

    return overlap

def build_pair(input_line):
    assignments = [ass.split('-') for ass in input_line.split(",")]
    assignments[0] = [int(x) for x in assignments[0]]
    assignments[1] = [int(x) for x in assignments[1]]

    return assignments
    
cleaning_pair = puzzle_input.readline().strip()
complete_overlapping_count = 0
any_overlapping_count = 0

while cleaning_pair != '':
    pair = build_pair(cleaning_pair)

    if complete_overlap(pair[0], pair[1]):
        complete_overlapping_count += 1

    if any_overlap(pair[0], pair[1]):
        any_overlapping_count += 1

    cleaning_pair = puzzle_input.readline().strip()

print("-----Part 1-----\nNumber of pairs that completely overlap: " + str(complete_overlapping_count) + "\n\n")
print("-----Part 2-----\nNumber of pairs that overlap at all: " + str(any_overlapping_count))

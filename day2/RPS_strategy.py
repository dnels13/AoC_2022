puzzle_input = open('../inputs/day2_input1.txt', 'r')

OPP_THROWS = ['A', 'B', 'C']
SELF_THROWS = ['X', 'Y', 'Z']

WIN_BONUS = 6

def score_match(opp_throw, self_throw):
    score = SELF_THROWS.index(self_throw) + 1
    
    if opp_throw == 'A' and self_throw == 'Y':
        score += WIN_BONUS
    elif opp_throw == 'B' and self_throw == 'Z':
        score += WIN_BONUS
    elif opp_throw == 'C' and self_throw == 'X':
        score += WIN_BONUS
    elif OPP_THROWS.index(opp_throw) == SELF_THROWS.index(self_throw):
        score += 3

    return score


game = puzzle_input.readline().strip().split()
total_score = 0
while len(game) != 0:
    #print(game[0] + " vs " + game[1] + " = " + str(score_match(game[0], game[1])))
    total_score += score_match(game[0], game[1])
    game = puzzle_input.readline().strip().split()
puzzle_input.close()    

print("_____PART 1_____\nTotal Score = " + str(total_score) + "\n\n")

puzzle_input = open('../inputs/day2_input1.txt', 'r')
game = puzzle_input.readline().strip().split()
total_score = 0
while len(game) != 0:
    opp_draw = game[0]
    condition = game[1]

    if condition == 'X':
        total_score += score_match(opp_draw, SELF_THROWS[(OPP_THROWS.index(opp_draw)-1)%3])
    elif condition == 'Y':
        total_score += score_match(opp_draw, SELF_THROWS[(OPP_THROWS.index(opp_draw))])
    elif condition == 'Z':
        total_score += score_match(opp_draw, SELF_THROWS[(OPP_THROWS.index(opp_draw)+1)%3])

    game = puzzle_input.readline().strip().split()


print("_____PART 2_____\nTotal Score = " + str(total_score) + "\n")                

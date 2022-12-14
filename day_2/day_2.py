"""
A,X = Rock worth 1 pts
B,Y = Paper worth 2 pts
C,Z = Scissors worth 3 pts
2 beats 1, 3 beats 2, 1 beats 3
Z beats B, Y beats A and X beats C 

Loss = 0 pts
Draw = 3 pts
Win = 6 pts
"""
file = open('input_day_2.txt', 'r')
Lines = file.readlines()
opponent = []
you = []
hand_converter = {'A':1,
                  'B':2,
                  'C':3,
                  'X':1,
                  'Y':2,
                  'Z':3}
for line in Lines:
    opponent.append(hand_converter[line.split()[0]])
    you.append(hand_converter[line.split()[1]])

score = []
score = []
score = []
for i in range(len(Lines)):
    # If hands are equal, draw
    if opponent[i] == you[i]:
        score.append(you[i] + 3)
    
    if abs(opponent[i]-you[i]) == 1: 
        if opponent[i] > you[i]:
            score.append(you[i])
        if you[i] > opponent[i]:
            score.append(you[i] + 6)
    else: 
        if opponent[i] < you[i]:
            score.append(you[i])
        if you[i] < opponent[i]:
            score.append(you[i] + 6)

print("My total score is",
       sum(score))


# Part 2

draw = {'A':1,
        'B':2,
        'C':3}
win = {'A':2,
       'B':3,
       'C':1}
loss = {'A':3,
        'B':1,
        'C':2}

hand_converter_master = {'draw' : draw,
                         'win'  : win,
                         'loss' : loss}
results_master = {'X' : ['loss',0],
                   'Y' : ['draw',3],
                   'Z' : ['win',6]}
new_score = 0

for i in range(len(Lines)):
    opponent = Lines[i].split()[0]
    result = Lines[i].split()[1]
    new_score += hand_converter_master[results_master[result][0]][opponent] \
               + results_master[result][1]
print(new_score)

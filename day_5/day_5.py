import pprint as p 

file = open('input_day_5.txt', 'r')                                            

Lines = file.readlines()

box = []
instructions = []

for line in range(len(Lines)): 
    if line<9:
        box.append(Lines[line])
    elif not Lines[line].strip():
        pass
    else:
        instructions.append(Lines[line].strip().split(' '))
box_pos = []
for i in range(8):
    column = []
    for j in range(1,len(box[i]),4):
        column.append(box[i][j])
    box_pos.append(column)
box_dict = {}
for i in range(9):
    box_dict[str(i+1)] = []
for i in range(len(box_pos)):
    for j in range(len(box_pos[i])):
        if box_pos[-1-i][j] == ' ':
            pass
        else:
            box_dict[str(j+1)].append(box_pos[-1-i][j])
p.pprint(box_dict)      
for i in range(len(instructions)):
    pile_1 = instructions[i][3]
    pile_2 = instructions[i][-1]
    num_of_boxes = int(instructions[i][1])
    moving = box_dict[str(pile_1)][-num_of_boxes:]
    
    for j in range(len(moving)):
        box_dict[str(pile_2)].append(moving[-j-1])
    box_dict[str(pile_1)]=box_dict[str(pile_1)][:-num_of_boxes]
    print(num_of_boxes,pile_1,pile_2)
    p.pprint(box_dict)
#p.pprint(box_dict)
tops = ''
for key in box_dict:
    tops = tops+box_dict[key][-1]
print(tops)

'''  Was an idiot and didn't realise they wanted to move one box at a time not 
the whole stack of boxes. Anyway that was part two anyway oops. To find second
answer (already inputted as a wrong answer so just copied) change the moving 
index in line 40 to "j" from -j-1. '''

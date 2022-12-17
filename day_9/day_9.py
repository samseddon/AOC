import numpy as np


class Head:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __setitem__(self,instruction):
        if instruction[0] == 'R':
            self.x_pos = self.x_pos + int(instruction[1])
        if instruction[0] == 'L':
            self.x_pos = self.x_pos - int(instruction[1])
        if instruction[0] == 'U':
            self.y_pos = self.y_pos + int(instruction[1])
        if instruction[0] == 'D':
            self.y_pos = self.y_pos - int(instruction[1])
    
    def update_pos(self,instruction):
        self.__setitem__(instruction)

class Tail:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.history = []
        self.history.append([x_pos,y_pos])
    

    def __setitem__(self,axis,sign):
        if axis == 'x':
            self.x_pos = self.x_pos + sign
        if axis == 'y':
            self.y_pos = self.y_pos + sign


    def update_pos_1d(self,axis,sign):
        self.__setitem__(axis,sign)
        if [self.x_pos,self.y_pos] in self.history:
            pass
        else:
            self.history.append([self.x_pos,self.y_pos])
    

    def update_pos_2d(self, signx, signy):
        self.__setitem__('x',signx)
        self.__setitem__('y',signy)
        if [self.x_pos,self.y_pos] in self.history:
            pass
        else:
            self.history.append([self.x_pos,self.y_pos])

        


file = open('input_day_9.txt', 'r')                                            
#file = open('test_input-2.txt', 'r')                                            
Lines = file.readlines()     
head = Head(0,0)
tail = Tail(0,0)

for line in Lines:
    if not line.strip():
        break
    instruction = line.strip().split(' ')
    for step_num in range(int(instruction[1])):
        instruction = [instruction[0],1]
        head.update_pos(instruction)
        dx = head.x_pos - tail.x_pos
        dy = head.y_pos - tail.y_pos
        if abs(dx) <= 1 and abs(dy) <=1:
            pass
        elif abs(dx) >= 1 and abs(dy) >= 1:
            tail.update_pos_2d(np.sign(dx),np.sign(dy))
            dx = head.x_pos - tail.x_pos
            dy = head.y_pos - tail.y_pos
            if abs(dx) > abs(dy):
                while(abs(dx) > 1):
                    tail.update_pos_1d('x',np.sign(dx))
                    dx = head.x_pos - tail.x_pos
            if abs(dy) > abs(dx):
                while(abs(dy) > 1):
                    tail.update_pos_1d('y',np.sign(dy))
                    dy = head.y_pos - tail.y_pos
        else:
            if abs(dx) > abs(dy):
                while(abs(dx) > 1):
                    tail.update_pos_1d('x',np.sign(dx))
                    dx = head.x_pos - tail.x_pos
            if abs(dy) > abs(dx):
                while(abs(dy) > 1):
                    tail.update_pos_1d('y',np.sign(dy))
                    dy = head.y_pos - tail.y_pos
    #print('head =',head.x_pos, head.y_pos)
    #print('tail =',tail.x_pos, tail.y_pos)
print(len(tail.history))
head = Head(0,0)
Tails = []
for i in range(9):
    Tails.append(Tail(0,0))

for line in Lines:
    if not line.strip():
        break
    instruction = line.strip().split(' ')
    for step_num in range(int(instruction[1])):
        instruction = [instruction[0],1]
        head.update_pos(instruction)
        for i in range(len(Tails)):
            if i ==0:
                lead = head
                foll = Tails[0]
            else:
                lead = Tails[i-1]
                foll = Tails[i]
            dx = lead.x_pos - foll.x_pos
            dy = lead.y_pos - foll.y_pos
            if abs(dx) <= 1 and abs(dy) <=1:
                pass
            elif abs(dx) >= 1 and abs(dy) >= 1:
                foll.update_pos_2d(np.sign(dx),np.sign(dy))
                dx = lead.x_pos - foll.x_pos
                dy = lead.y_pos - foll.y_pos
                if abs(dx) > abs(dy):
                    while(abs(dx) > 1):
                        foll.update_pos_1d('x',np.sign(dx))
                        dx = lead.x_pos - foll.x_pos
                if abs(dy) > abs(dx):
                    while(abs(dy) > 1):
                        foll.update_pos_1d('y',np.sign(dy))
                        dy = lead.y_pos - foll.y_pos
            else:
                if abs(dx) > abs(dy):
                    while(abs(dx) > 1):
                        foll.update_pos_1d('x',np.sign(dx))
                        dx = lead.x_pos - foll.x_pos
                if abs(dy) > abs(dx):
                    while(abs(dy) > 1):
                        foll.update_pos_1d('y',np.sign(dy))
                        dy = lead.y_pos - foll.y_pos
print(len(Tails[-1].history))

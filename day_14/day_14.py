import numpy as np

class Real_rock:
    
    def __init__(self, lowlim_x, higlim_x, higlim_y):
        self.lowlim_x = lowlim_x
        self.higlim_x = higlim_x
        self.higlim_y = higlim_y + 1
        self.shape = (higlim_y + 2, 2*higlim_y + 5)
        self.rocks = np.zeros(self.shape)
        self.index = int(500-(higlim_y))-2
        self.infinity = False
    
    def rock_fill(self, xy):
        self.rocks[xy[1], (xy[0]-self.index)] = 1

    
    def rock_fill_coordinates(self, x1y1, x2y2):
        dx = int(x1y1[0]) - int(x2y2[0])
        dy = int(x1y1[1]) - int(x2y2[1])
        coord_line = []
        if dx != 0: 
            for i in range(int(min(x1y1[0],x2y2[0])), int(max(x1y1[0],x2y2[0]))+1, 1):
                coord_line.append([i,int(x1y1[1])])
        if dy != 0:
            for i in range(int(min(x1y1[1],x2y2[1])), int(max(x1y1[1],x2y2[1]))+1, 1):
                coord_line.append([int(x1y1[0]),i]) 

        for coord in coord_line:
            self.rock_fill(coord)

    def change_status(self):
        self.infinity = True

class Sand: 
    
    def __init__(self):
        self.x = 500
        self.y = 0 
        self.rest = False

    def fall(self,realrocks):
        while(self.rest == False):
            if self.y == realrocks.higlim_y:
                realrocks.rock_fill([self.x,self.y])
                self.rest = True
            elif realrocks.rocks[self.y+1, (self.x-realrocks.index)] == 1 \
                    and realrocks.rocks[self.y+1, (self.x-realrocks.index) - 1] == 1\
                    and realrocks.rocks[self.y+1, (self.x-realrocks.index) + 1] == 1\
                    and self.y ==0:
            
                realrocks.rock_fill([self.x,self.y])
                self.rest = True
                realrocks.change_status()
            elif realrocks.rocks[self.y+1,(self.x-realrocks.index)] == 0:
                self.y += 1
            elif realrocks.rocks[self.y+1,(self.x-realrocks.index)] != 0\
                    and realrocks.rocks[self.y+1, (self.x-realrocks.index) - 1] == 0: 
                self.y += 1
                self.x -= 1
            elif realrocks.rocks[self.y+1,(self.x-realrocks.index)] != 0\
                    and realrocks.rocks[self.y+1, (self.x-realrocks.index) + 1] == 0: 
                self.y += 1
                self.x += 1

            else:
                realrocks.rock_fill([self.x,self.y])
                self.rest = True


file = open('input_day_14.txt', 'r')
#file = open('test_input.txt', 'r')  

Lines = file.readlines()
x = []
y = []
for line in Lines:
    Coordinates = line.strip().split(' -> ')
    for coordinate in Coordinates:
        x.append(int(coordinate.split(',')[0]))
        y.append(int(coordinate.split(',')[1]))
realrocks = Real_rock(int(min(x)),int(max(x)),int(max(y)))

for line in Lines:
    Coordinates = line.strip().split(' -> ')
    for _ in range(len(Coordinates)-1):
        x1y1 = []
        x2y2 = []
        realrocks.rock_fill_coordinates(Coordinates[_].split(','), Coordinates[_+1].split(','))

sand_pos = 1
print(realrocks.rocks)
_ = 0
while(realrocks.infinity == False):
    sand = Sand()
    sand.fall(realrocks)
    _ += 1
print(realrocks.rocks)
print(_)

import numpy as np


class Sensor:
    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y):
        self.s_x = int(sensor_x[2:-1])
        self.s_y = int(sensor_y[2:-1])
        self.b_x = int(beacon_x[2:-1])
        self.b_y = int(beacon_y[2:])
        self.diamond_limits = abs(self.b_x-self.s_x) + abs(self.s_y - self.b_y)


#    def diamond_maker(self):
        # 8,7 2,10 == horizontal width 
#        self.max_hor = abs(self.b_x-self.s_x) + abs(self.s_y - self.b_y)

    def print_all(self):
        print(vars(self).items())

class Area: 
    def __init__(self,max_val):
        self.x_low = 0
        self.x_hig = 0 
        self.y_low = 0
        self.y_hig = 0
        self.max_limit = max_val
        self.scan_area = []
        self.scan_area_new = []
        self.boundary = []
        self.x_range = abs(self.x_hig - self.x_low)
        self.y_range = abs(self.y_hig - self.y_low)

    def find_lims(self, sensor):
        if (sensor.s_x - sensor.diamond_limits) < self.x_low:
            self.x_low = sensor.s_x - sensor.diamond_limits 
        if (sensor.s_x + sensor.diamond_limits) > self.x_hig:
            self.x_hig = sensor.s_x + sensor.diamond_limits 
        if (sensor.s_y - sensor.diamond_limits) < self.y_low:
            self.y_low = sensor.s_y - sensor.diamond_limits  
        if abs(sensor.s_y + sensor.diamond_limits) > abs(self.y_hig):
            self.y_hig = sensor.s_y + sensor.diamond_limits 
   
    def update_lims(self):
        self.x_range = abs(self.x_hig - self.x_low + 1 + 4)
        self.y_range = abs(self.y_hig - self.y_low + 1 + 4)
        self.x_low = self.x_low-2
        self.x_hig = self.x_hig+2
        self.y_low = self.y_low-2
        self.y_hig = self.y_hig+2

    def initilise_array(self):
        row = []
        for i in range(area.x_range):
            column = []
            for j in range(area.y_range):
                column.append(0)
            row.append(column)
        self.scan_area = row
    
    def init_different(self):
        for i in range(self.max_limit):
            self.scan_area.append(0)

    def new_sensor_data(self, sensor, value):
        #if sensor.diamond_limits - self.y_low + sensor.diamond_limits + 2 <= value\
        #or sensor.diamond_limits - self.y_low - sensor.diamond_limits - 2 >= value:
        #    print('here')
        #    pass
        #else:
        for j in range(sensor.diamond_limits + 2):
            if sensor.s_y -self.y_low + j == value\
                    or sensor.s_y - self.y_low - j == value:
                for i in range(sensor.s_x  - sensor.diamond_limits - self.x_low + j, 
                               sensor.s_x + 1 + sensor.diamond_limits - self.x_low - j):
                    if i > (self.max_limit - self.x_low) or i < ( 0- self.x_low):
                        pass
                    else:
                        self.scan_area[i] = 1
    
    def beacon_sensor_check(self,sensor,value): 
        if sensor.s_y - self.y_low == value:
            self.scan_area[sensor.s_x - self.x_low] = 0 
        if sensor.b_y - self.y_low == value:
            self.scan_area[sensor.b_x - self.x_low] = 0 

    def add_sensor_data(self, sensor):
        for j in range(sensor.diamond_limits + 2):
            for i in range(sensor.s_x  - sensor.diamond_limits - self.x_low + j, 
                           sensor.s_x + 1 + sensor.diamond_limits - self.x_low - j):
                self.scan_area[sensor.s_y - self.y_low + j][i] = 1 
                self.scan_area[sensor.s_y - self.y_low - j][i] = 1 
                #self.scan_area[i][sensor.s_y - self.y_low + j] = 1 
                #self.scan_area[i][sensor.s_y - self.y_low - j] = 1 
               # if sensor.s_y -self.y_low + j == value:
               #     self.scan_area[i + j] = 1
               # if sensor.s_y - self.y_low  - j == value: 
               #     self.scan_area[i - j] = 0
        #print(sensor.s_y,sensor.s_y - self.y_low, sensor.s_x,sensor.s_x - self.x_low)
        self.scan_area[sensor.s_y - self.y_low][sensor.s_x - self.x_low] = 1
        self.scan_area[sensor.b_y - self.y_low][sensor.b_x - self.x_low] = 1

    def print_all(self):
        print('x between', self.x_low, self.x_hig, 'with range', self.x_range)
        print('y between', self.y_low, self.y_hig, 'with range', self.y_range)

    def add_point(self, inner, outer, sensors):
        for i in range(len(inner)):
            tracker = 0
            if  0 + self.x_low < inner[i][0] < self.max_limit + self.x_low\
            and 0 + self.y_low < inner[i][1] < self.max_limit + self.y_low\
            and 0 + self.x_low < outer[i][0] < self.max_limit + self.x_low\
            and 0 + self.y_low < outer[i][1] < self.max_limit + self.y_low:
                for sensor in sensors:
                    if abs(sensor.s_x - inner[i][0]) + abs(sensor.s_y - inner[i][1]) > sensor.diamond_limits\
                            and abs(sensor.s_x - outer[i][0]) + abs(sensor.s_y - outer[i][1]) < sensor.diamond_limits:
                        print(sensor.s_x, sensor.s_y, sensor.diamond_limits, inner[i], outer[i])
                        print(abs(sensor.s_x - inner[i][0]) + abs(sensor.s_y - inner[i][1]))
                        print(abs(sensor.s_x - outer[i][0]) + abs(sensor.s_y - outer[i][1]))
                        tracker += 1
            print(tracker)
            if tracker == 1:
                self.boundary.append([inner[i],outer[i]])
#        if x < self.max_limit and y < self.max_limit:
#            self.boundary.append([x,y])

class Boundary:
    def __init__(self, m, c, zero_y, zero_x, sign_x, sign_y, bump):
        self.m = m
        self.zero_x = zero_x
        self.zero_y = zero_y
        self.c = c
        self.sign_x = sign_x
        self.sign_y = sign_y
        self.bump = bump
        self.boundary = []

    def coord(self, x):
        return self.zero_x + self.sign_x * x,\
                ((-1 * self.m  * self.sign_x * (x)) + self.zero_y - self.sign_y * (self.c + self.bump))

    def populate(self, area):
        for i in range(abs(self.c) + 1 + self.bump):
            if i > area.max_limit:
                break
            else:
                x, y = self.coord(i)
                if [x, y] not in self.boundary:
                   self.boundary.append([x,y])
    
    def print_all(self):
        print(vars(self).items())

    def return_c(self):
        return self.zero_y - self.sign_y * self.c

def sensor_check(sensors, point):
    for sensor in sensors:
        if abs(sensor.s_x - point[0]) + abs(sensor.s_y - point[1]) <= sensor.diamond_limits:
            return False
    return True



file = open('input_day_15.txt', 'r')
#file = open('test_input.txt', 'r')
max_val = 4000000
#max_val = 20
Lines = file.readlines()
sensors = []
dim_x_low = 0
dim_y_low = 0
area = Area(max_val)
area2 = Area(max_val)
relevant_sensors = []
#val = 2000000
val = 10

for line in Lines: 
    line_array = line.strip().split(' ')
    sensors.append(Sensor(line_array[2], line_array[3], line_array[-2], line_array[-1]))
    #area.find_lims(sensors[-1])
#area.update_lims()
#area.initilise_array()
master_lines: dict[tuple[int,int],int] = {}
for _ in range(len(sensors)):
    #area.add_sensor_data(sensors[_])
    SW_inner_boundary = Boundary(-1,
                  sensors[_].diamond_limits + 1,
                  sensors[_].s_y - area.y_low, 
                  sensors[_].s_x - area.x_low,
                  -1,
                  -1,
                  0)
    SW_low = (1, sensors[_].s_y - area.y_low + (sensors[_].diamond_limits + 1) - sensors[_].s_x)
    SW_hig = (1, sensors[_].s_y - area.y_low - (sensors[_].diamond_limits + 1) - sensors[_].s_x)
   # SW_inner_boundary.populate(area)
   # SW_outer_boundary = Boundary(-1,
   #               sensors[_].diamond_limits + 1,
   #               sensors[_].s_y - area.y_low, 
   #               sensors[_].s_x - area.x_low,
   #               -1,
   #               -1,
   #               1)
   # SW_outer_boundary.populate(area)
   # area.add_point(SW_inner_boundary.boundary, SW_outer_boundary.boundary, sensors)
    NW_inner_boundary = Boundary(1,
                  sensors[_].diamond_limits + 1,
                  sensors[_].s_y - area.y_low, 
                  sensors[_].s_x - area.x_low,
                  -1,
                  1,
                  0)
    NW_low = (-1, sensors[_].s_y - area.y_low + (sensors[_].diamond_limits + 1) + sensors[_].s_x)
    NW_hig = (-1, sensors[_].s_y - area.y_low - (sensors[_].diamond_limits + 1) + sensors[_].s_x)
   # NW_inner_boundary.populate(area)
   # NW_outer_boundary = Boundary(1,
   #               sensors[_].diamond_limits + 1,
   #               sensors[_].s_y - area.y_low, 
   #               sensors[_].s_x - area.x_low,
   #               -1,
   #               1,
   #               1)
   # NW_outer_boundary.populate(area)
   # area.add_point(NW_inner_boundary.boundary, NW_outer_boundary.boundary, sensors)
    
    SE_inner_boundary = Boundary(1,
                  sensors[_].diamond_limits + 1,
                  sensors[_].s_y - area.y_low, 
                  sensors[_].s_x - area.x_low,
                  1,
                  -1,
                  0)
    #SE = (SE_inner_boundary.m, SE_inner_boundary.return_c())
   # SE_outer_boundary = Boundary(1,
   #               sensors[_].diamond_limits + 1,
   #               sensors[_].s_y - area.y_low, 
   #               sensors[_].s_x - area.x_low,
   #               1,
   #               -1,
   #               1)
   # SE_outer_boundary.populate(area)
   # area.add_point(SE_inner_boundary.boundary, SE_outer_boundary.boundary, sensors)

    NE_inner_boundary = Boundary(1,
                  sensors[_].diamond_limits + 1,
                  sensors[_].s_y - area.y_low, 
                  sensors[_].s_x - area.x_low,
                  1,
                  -1,
                  0)
    # NE = (NE_inner_boundary.m, NE_inner_boundary.return_c())
    for line in [SW_low,SW_hig,NW_low,NW_hig]:
        if line in master_lines:
            master_lines[line] = True
        else:
            master_lines[line] = False
   # NE_outer_boundary = Boundary(-1,
   #               sensors[_].diamond_limits + 1,
   #               sensors[_].s_y - area.y_low, 
   #               sensors[_].s_x - area.x_low,
   #               1,
   #               1,
   #               1)
   # NE_outer_boundary.populate(area)
   # area.add_point(NE_inner_boundary.boundary, NE_outer_boundary.boundary, sensors)
#for element in area.boundary:
south_westerlys = []
north_westerlys = []
for key in master_lines:
    if master_lines[key] == True:
        if key[0] == 1:
            south_westerlys.append(key[1])
        else:
            north_westerlys.append(key[1])
intersections = []
# south_westerly = rising
for i in range(len(south_westerlys)):
    for j in range(len(north_westerlys)):
        x = (- south_westerlys[i] + north_westerlys[j]) // 2
        y = (x + south_westerlys[i])
        intersections.append((x,y))
for point in intersections:
    if 0 <= point[0] <= max_val\
    and 0 <= point[1] <= max_val\
    and sensor_check(sensors,point) == True:
        print(point[0] * 4000000 + point[1])
#print(intersections)

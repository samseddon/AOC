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
        self.x_range = abs(self.x_hig - self.x_low + 1)
        self.y_range = abs(self.y_hig - self.y_low + 1)

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

    def add_point(self, x, y):
        self.scan_area[y][x] = 5

class Boundary:
    def __init__(self, m, offset, zero):
        self.m = m
        self.zero = zero
        self.c = self.zero + offset

    def coord(self, x):
        return ((self.m * x) + self.c)

    def populate(self, area):
        for i in range(self.c):
            area.add_point(i, self.coord(i))
    
    def print_all(self):
        print(vars(self).items())



file = open('input_day_15.txt', 'r')
file = open('test_input.txt', 'r')
max_val = 4000000
max_val = 20
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
    area.find_lims(sensors[-1])

area.update_lims()
sensors[6].print_all()
area.initilise_array()
area.add_sensor_data(sensors[6])

for _ in range(len(sensors)):
    _ = 6
    sensors[_].print_all()
    test_bound = Boundary(1,(-sensors[_].diamond_limits), sensors[_].s_x-area.x_low)
    test_bound.print_all()
    test_bound.populate(area)


print(area.scan_area)


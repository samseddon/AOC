import pprint as p

class addx:
    def __init__(self, cycle, wait, value):
        self.cycle = cycle
        self.wait = wait
        self.value = value

    def check_cycle(self,cycle):
        if cycle - self.cycle >= 1:
            self.wait = False

class X:
    def __init__(self, value, cycle, output):
        self.value = value
        self.cycle = cycle
        self.output = output
        self.crt = [[]]
        self.sprite = 0

    def check_crt(self):
        if self.sprite == 40:
            self.output +=1
            self.sprite = 0
            self.crt.append([])

        if self.value-1 <= self.sprite <= self.value + 1:
            self.crt[self.output].append('█')
        else:
            self.crt[self.output].append(' ') 
        self.sprite += 1

    def time_bump(self):
        self.check_crt()
        self.cycle = self.cycle + 1
    

    def value_bump(self,value):
        self.value = self.value + value


file = open('input_day_10.txt', 'r')
#file = open('test_input.txt', 'r')   
Lines = file.readlines()                                                       

Signals = []                                                                   
for line in Lines:                                                           
    if not line.strip():                                                       
        pass                                                                   
    else:                                                                      
        Signals.append(line.strip())                                              


x = X(1,1,0)
for signal in Signals:
    if signal == 'noop':
        x.time_bump()
        pass
    else:
        add = addx(x.cycle, True, int(signal.split(' ')[1]))
        while add.wait == True:
            add.check_cycle(x.cycle)
            x.time_bump()
        x.value_bump(add.value)

for i in range(len(x.crt)):
    print(x.crt[i])

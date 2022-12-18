class Monkey:
    def __init__(self, starting_items, operation, test, throw_1,throw_2):
        self.starting_items = starting_items
        self.operation_func = operation[0]
        self.operation_val  = operation[1]
        self.test           = test
        self.true_throw     = throw_1
        self.false_throw    = throw_2


    def Operation(self, worry):
        if self.operation_val == 'old':
            easy_op = False
        else: 
            operation_val = int(self.operation_val)
            easy_op = True
   
        if self.operation_func == '*' and easy_op == True:
            return worry * operation_val
        if self.operation_func == '+' and easy_op == True:
            return worry + operation_val 
        if easy_op == False:
            return worry * worry 

file = open('input_day_10.txt', 'r')
file = open('test_input.txt')
Lines = file.readlines()  
monkey = []

for i in range(len(Lines)):
    if Lines[i][:6] == 'Monkey':
        monkey.append(Monkey(Lines[i+1].strip().split(' ')[2:],
                             Lines[i+2].strip().split(' ')[-2:],
                             Lines[i+3].strip().split(' ')[-1],
                             Lines[i+4].strip().split(' ')[-1],
                             Lines[i+5].strip().split(' ')[-1]))

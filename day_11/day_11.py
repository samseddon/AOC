import math
import numpy as np

class Monkey:
    def __init__(self, starting_items, operation, test, throw_1,throw_2):
        self.items = starting_items
        self.operation_func = operation[0]
        self.operation_val  = operation[1]
        self.test           = test
        self.true_throw     = throw_1
        self.false_throw    = throw_2
        self.inspected      = 0

    def operation(self, worry, divisor):
        if self.operation_val == 'old':
            easy_op = False
        else: 
            operation_val = int(self.operation_val)
            easy_op = True
   
        if self.operation_func == '*' and easy_op == True:
            return (worry * operation_val) % divisor
        if self.operation_func == '+' and easy_op == True:
            return (worry + operation_val) % divisor
        if easy_op == False:
            return (worry * worry) % divisor

    def test_worry(self, worry):
        if worry % self.test == 0:
            return(True)

        else:
            return(False)


    def where_throw_item(self, worry, bool):
        if bool == True:
            return self.true_throw

        else:
            return self.false_throw
    
    def inspect(self):
        self.inspected += 1

    def throw(self):
        new_items = self.items[1:]
        self.items = new_items

file = open('input_day_10.txt', 'r')
#file = open('test_input.txt')
Lines = file.readlines()  
Monkeys= []

for i in range(len(Lines)):
    if Lines[i][:6] == 'Monkey':
        items_unsplit = Lines[i+1].strip().split(' ')[2:]
        items_split = []
        for item in items_unsplit:
            item = item.split(',')
            items_split.append(int(item[0]))
        Monkeys.append(Monkey(items_split,
                             Lines[i+2].strip().split(' ')[-2:],
                             int(Lines[i+3].strip().split(' ')[-1]),
                             int(Lines[i+4].strip().split(' ')[-1]),
                             int(Lines[i+5].strip().split(' ')[-1])))
divisor = []
for monkey in Monkeys:
    divisor.append(monkey.test)

divisor = np.lcm.reduce(divisor)
for _ in range(10000):
    for monkey in Monkeys:
        for item in monkey.items:
            monkey.inspect()
            worry = monkey.operation(item,divisor)
            next_monkey = monkey.where_throw_item(worry,monkey.test_worry(worry)) 
            monkey.throw()
            Monkeys[next_monkey].items.append(worry)
    
monkey_buisness = []
for i in range(len(Monkeys)):
    monkey_buisness.append(Monkeys[i].inspected)
monkey_buisness = sorted(monkey_buisness)
print(monkey_buisness[-1]*monkey_buisness[-2])

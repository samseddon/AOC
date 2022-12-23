from ast import literal_eval
import pprint as p 

class Signal:
    def __init__(self, array):
        self.array = array


class Compare_Signals:
    def __init__(self,left,right):
        self.left = left
        self.right = right
        self.order = True
        self.done = False


    def compare_ints(self,left_element,right_element):
        if left_element < right_element:
            self.order = True
            self.done = True 
        if left_element > right_element:
            self.order = False
            self.done = True
    def compare_lists(self,left_element,right_element):
        for i in range(max(len(left_element),len(right_element))):
            if self.done == True:
                pass
            elif i >= len(left_element):  # if empty
                self.order = True
                self.done = True
            elif i >= len(right_element):
                self.order = False
                self.done = True
                break

            else:
                if type(left_element[i]) == int and type(right_element[i]) == int and self.done == False:
                    self.compare_ints(left_element[i],right_element[i])

                elif type(left_element[i]) == list and type(right_element[i]) == list and self.done == False:
                    self.compare_lists(left_element[i],right_element[i])
                    break
                elif self.done == False:
                    x_l,x_r = self.make_int(left_element[i],right_element[i])
                    self.compare_lists(x_l,x_r)

    def change_order(self):
        if self.order == True:
            self.order = False
            self.done = True
        else:
            self.order = True
            self.done = True

    def make_int(self,left,right):
        new_list = []
        if type(left) == int:
            new_list.append(left)
            return new_list, right
        elif type(right) == int:
            new_list.append(right)
            return left, new_list

    def comparer(self):
        print(self.left,self.right)
        for i in range(max(len(self.left),len(self.right))):
            if self.done == True:
                break
            elif i >= len(self.left):
                break
            elif i >= len(self.right):
                self.change_order()
            else:
                left_element = self.left[i]
                right_element = self.right[i]

                if type(left_element) == int and type(right_element) == int and self.done == False:
                    self.compare_ints(left_element,right_element)

                elif type(left_element) == list and type(right_element) == list and self.done == False:
                    self.compare_lists(left_element,right_element)
                elif self.done == False:
                    left_element, right_element = self.make_int(left_element,right_element)
                    self.compare_lists(left_element, right_element)
        print(self.order)
    
    def swapper(self,freshlist,i):
        print('swapper')
        print(self.left)
        print(self.right)
        if self.order == False:
            freshlist[i] = self.right
            freshlist[i+1] = self.left
            return freshlist,1
        else:
            return freshlist, 0

file = open('input_day_13.txt', 'r')
#file = open('test_input', 'r')  
#file = open('test_input-2.txt', 'r')

Lines = file.readlines()
indexes = []
freshlist = []

for k in range(0,len(Lines),3):
    scan_skip = False

#    compare = Compare_Signals(literal_eval(Lines[k].strip()), literal_eval(Lines[k+1].strip()))
#    compare.comparer()
    
 #   if compare.order == True:
        #freshlist.append(compare.left)
        #freshlist.append(compare.right)
  #      indexes.append(int((k+3)/3))
    freshlist.append(literal_eval(Lines[k].strip()))
    freshlist.append(literal_eval(Lines[k+1].strip()))
freshlist.append([[2]])
freshlist.append([[6]])
false_test = 1


#print(indexes)
a = 4

#print(freshlist[a])
#print(freshlist[a+1])
#
#tester = Compare_Signals(freshlist[a],freshlist[a+1])
#tester.comparer()
#print(tester.order)
#freshlist = tester.swapper(freshlist, a)
#
#print(freshlist[a])
#print(freshlist[a+1])
#
while(false_test == 1):
    false_check = 1
    false_check_array = []
    for i in range(len(freshlist)-1):
        print()
        print()
        print()
        packets = Compare_Signals(freshlist[i],freshlist[i+1])
        packets.comparer()
        freshlist, false_check = packets.swapper(freshlist,i)
        print()
        false_check_array.append(false_check)
    if sum(false_check_array) == 0:
        false_test = 0
        break

print(freshlist)
for i in range(len(freshlist)):
    if freshlist[i] == [[2]]:
        num_1 = i+1
    elif freshlist[i] ==[[6]]:
        num_2 = i+1
print(num_2 * num_1)
#position_1 = 1 + sum(1 for packet in packets if compare(packet, [[2]]))
#position_2 = 2 + sum(1 for packet in packets if compare(packet, [[6]]))
#print(position_1 * position_2)

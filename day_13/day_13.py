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
            print('compare_ints made false')
            self.order = False
            self.done = True

    def compare_lists(self,left_element,right_element):
        print()
        print('in compare lists')
        print(left_element,type(left_element),len(left_element))
        print(right_element,type(right_element), len(right_element))
        for i in range(max(len(left_element),len(right_element))):
            if self.done == True:
                pass
            elif i >= len(left_element):  # if empty
                self.order = True
                self.done = True
            elif i >= len(right_element):
                print('running out of right elements made false') 
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
                    left_element[i], right_element[i] = self.make_int(left_element[i],right_element[i])
                    self.compare_lists(left_element[i],right_element[i])

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




file = open('input_day_13.txt', 'r')                                            
#file = open('test_input', 'r')  
#file = open('test_input-2.txt', 'r')

Lines = file.readlines()
indexes = []
for k in range(0,len(Lines),3):
    #scan = 9
    scan_skip = False
    #k = int((3*scan)-3)
    print()
    compare = Compare_Signals(literal_eval(Lines[k].strip()), literal_eval(Lines[k+1].strip()))
    print('left')
    p.pprint(compare.left)
    print('right')
    p.pprint(compare.right)
    while(compare.done==False):
        for i in range(max(len(compare.left),len(compare.right))):
            if compare.done == True:
                break
            elif i >= len(compare.left):
                break
            elif i >= len(compare.right):
                compare.change_order()
            else:
                left_element = compare.left[i]
                print('left element',i)
                p.pprint(left_element)
                print(type(left_element))
                right_element = compare.right[i]
                print('right',i)
                p.pprint(right_element)
                print(type(right_element))
                
                if type(left_element) == int and type(right_element) == int and compare.done == False:
                    compare.compare_ints(left_element,right_element)
            
                elif type(left_element) == list and type(right_element) == list and compare.done == False:
                    compare.compare_lists(left_element,right_element)
                elif compare.done == False:
                    left_element, right_element = compare.make_int(left_element,right_element)
                    compare.compare_lists(left_element, right_element)
        break
    print()
    print(compare.order)
    print()
    if compare.order == True:
        indexes.append(int((k+3)/3))
    if scan_skip == True:
        break
print(sum(indexes))

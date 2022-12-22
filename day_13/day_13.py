from ast import literal_eval

class Signal:
    def __init__(self, array):
        self.array = array


class Compare_Signals:
    def __init__(self,left,right):
        self.left = left
        self.right = right
        self.order = True
   
    def compare_ints(self,left_element,right_element):
        if left_element > right_element:
            self.order = False
     
    def compare_lists(self,left_element,right_element):
        i = 0

        for i in range(max(len(left_element),len(right_element))):
            if i >= len(left_element):  # if empty
                print('fist_list_element_empty')
                self.order = True 
            elif i >= len(right_element):
                self.order = False

            else:
                if type(left_element[i]) == int and type(right_element[i]) == int:
                    self.compare_ints(left_element[i],right_element[i])
                elif type(left_element) == list and type(right_element) == list:   
                    self.compare_lists(left_element[i],right_element[i])
                    break
                else:
                    break

    def change_order(self):
        if self.order == True:
            self.order = False
        else:
            self.order = True 
    
    def make_int(self,left,right):
        new_list = []
        if type(left) == int:
            new_list.append(left)




file = open('input_day_13.txt', 'r')                                            
file = open('test_input', 'r')  

Lines = file.readlines()

for i in range(0,len(Lines),3):
    
    compare = Compare_Signals(literal_eval(Lines[i].strip()), literal_eval(Lines[i+1].strip()))
    while(compare.order==True):
        for i in range(max(len(compare.left),len(compare.right))):
            if i >= len(compare.left):
                break
            elif i >= len(compare.right):
                compare.change_order()
            else:
                left_element = compare.left[i]
                right_element = compare.right[i]
                print(left_element,right_element)
                if type(left_element) == int and type(right_element) == int:
                    compare.compare_ints(left_element,right_element)
            
                elif type(left_element) == list and type(right_element) == list:
                    compare.compare_lists(left_element,right_element)
                else:
                    compare.make_int(left_element,right_element)
                    break
        print(compare.order)
        break

    print('final',compare.order)

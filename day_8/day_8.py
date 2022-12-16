import pprint as p
import numpy as np

def tree_search(data,data_idx,dim):
    for i in range(1,dim):
        for j in range(dim):
            if data[j,:i+1][-1] > max(data[j,:i+1][:-1]):
                data_idx[j,i] = 1
    return data,data_idx

def nearest_tall_tree(data,scenic_idx,dim):
    for i in range(1,dim):
        for j in range(dim):
            tree_focus = data[j,:i+1][-1]
            tree_consider = data[j,:i+1][:-1]
            tree_consider = tree_consider[::-1]
            for k in range(len(tree_consider)):
                if tree_focus > max(tree_consider):
                    scenic_idx[j,i] = scenic_idx[j,i] * len(tree_consider)
                    break
                elif tree_focus <= tree_consider[k]:               
                    scenic_idx[j,i] = scenic_idx[j,i]*(k+1)
                    break
    return data,scenic_idx




file = open('input_day_8.txt', 'r')                                            
#file = open('test_input.txt', 'r')                                            
Lines = file.readlines()     
data = []
data_idx = []
scenic_idx = []
for line in Lines:
    column = []
    column_idx = []
    column_scen = []
    for number in line.strip():
        column.append(number)
        column_idx.append(0)
        column_scen.append(1)
    data.append(column)
    data_idx.append(column_idx)
    scenic_idx.append(column_scen)
data = np.array(data)
data_idx = np.array(data_idx)
scenic_idx = np.array(scenic_idx)
data_1 = data
data_idx_1 = data_idx
dim = np.shape(data)[0]
for i in range(dim):
    scenic_idx[i,0] = 0
    scenic_idx[i,dim-1] = 0
    scenic_idx[0,i] = 0
    scenic_idx[dim-1,i] = 0
    data_idx[i,0] = 1
    data_idx[i,dim-1] = 1
    data_idx[0,i] = 1
    data_idx[dim-1,i] = 1

data,data_idx = tree_search(data,data_idx,dim)

data = np.fliplr(data)
data_idx = np.fliplr(data_idx)
data,data_idx = tree_search(data,data_idx,dim)
data = np.fliplr(data)
data_idx = np.fliplr(data_idx)


data = data.T
data_idx = data_idx.T
data,data_idx = tree_search(data,data_idx,dim)

data = np.fliplr(data)
data_idx = np.fliplr(data_idx)
data,data_idx = tree_search(data,data_idx,dim)
data = np.fliplr(data)
data_idx = np.fliplr(data_idx)

#print(sum(sum(data_idx)))

data = data.T

data,scenic_idx = nearest_tall_tree(data,scenic_idx,dim)



data = np.fliplr(data)
scenic_idx = np.fliplr(scenic_idx)
data,scenic_idx = nearest_tall_tree(data,scenic_idx,dim)
data = np.fliplr(data)
scenic_idx = np.fliplr(scenic_idx)


data = data.T
scenic_idx = scenic_idx.T
data,scenic_idx = nearest_tall_tree(data,scenic_idx,dim)


data = np.fliplr(data)
scenic_idx = np.fliplr(scenic_idx)
data,scenic_idx = nearest_tall_tree(data,scenic_idx,dim)
data = np.fliplr(data)
scenic_idx = np.fliplr(scenic_idx)
data = data.T
scenic_idx = scenic_idx.T



print(np.amax(scenic_idx))

import pandas as pd
import pprint as p

file = open('input_day_8.txt', 'r')                                            
file = open('test_input.txt', 'r')                                            
Lines = file.readlines()     
row = []
row_idx = []
for line in Lines:
    column = []
    column_idx = []
    for number in line.strip():
        column.append(number)
        column_idx.append(0)
    row.append(column)
    row_idx.append(column_idx)
df = pd.DataFrame(row)
df_idx = pd.DataFrame(row_idx)
for i in range(df_idx.shape[0]): 
    df_idx[i][0] = 1
    df_idx[i][df_idx.shape[0]-1] = 1
    df_idx[0][i] = 1
    df_idx[df_idx.shape[0]-1][i] = 1


for i in range(0,df_idx.shape[1]): # rows
    for j in range(1,int((df_idx.shape[0]+1)/2)): # columns 
        print(i,j,df[j][i])
        #if df[i][j] > max(df[:i][j]):
        #    df_idx[i][j] = 1

       


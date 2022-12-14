import time                                                                    
import numpy as np                                                                
                                                                                  
start_time = time.time()                                                          
                                                                                  
file = open('input_day_1.txt', 'r')                                               
Lines = file.readlines()                                                          
counter = 0                                                                       
elves = [0]                                                                       
                                                                                  
                                                                                  
for line in Lines:                                                                
    if line.strip(): # Checks if there is anything in a line                   
        elves[counter]=elves[counter] + int(line.strip())                         
    if not line.strip(): # If line blank, bumps to the next elf                
        elves.append(0)                                                           
        counter += 1                                                              
                                                                                  
print("The elf carrying the most calories is elf number",                      
        elves.index(max(elves)) + 1,                                           
        "carrying",                                                            
        max(elves),                                                            
        "calories")                                                            
                                                                               
elves_sorted = sorted(elves)                                                   
finish_time = time.time()                                                      
print("Top three elves calories summed",                                          
      elves_sorted[-1]                                                            
      + elves_sorted[-2]                                                          
      + elves_sorted[-3])                                                         
#        max(elves),                                                            
#        "calories")                                                            
print("Time taken was", finish_time-start_time)                                   

import string
alpha_value = {}

for i in range(len(string.ascii_lowercase)):
    alpha_value[string.ascii_lowercase[i]] = i + 1
    alpha_value[string.ascii_uppercase[i]] = i + 27

file = open('input_day_3.txt', 'r')                                            
Lines = file.readlines()   
priority_sum = 0

for line in Lines: 
    lower_half = line.strip()[:int(len(line.strip())/2)]
    upper_half = line.strip()[int(len(line.strip())/2):]
    priority_sum += alpha_value[''
                                .join(set(lower_half)
                                .intersection(upper_half))]

print('Task 1 is', priority_sum)
priority_sum_trios = 0
for i in range(0,len(Lines)-2,3):
    elf_1 = Lines[i].strip()
    elf_2 = Lines[i+1].strip()
    elf_3 = Lines[i+2].strip()
    priority_sum_trios += alpha_value[''
                                      .join(set(''
                                                .join(set(elf_1)
                                                .intersection(elf_2)))
                                      .intersection(elf_3))]
print('Task 2 is', priority_sum_trios)

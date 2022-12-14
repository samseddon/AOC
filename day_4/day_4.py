file = open('input_day_4.txt', 'r')                                            
Lines = file.readlines()  
counter = 0

for line in Lines: 
    elf_both = line.strip().split(',')
    elf_1 = elf_both[0].split('-')
    elf_2 = elf_both[1].split('-')
    MIN_ELF_1 = int(elf_1[0])
    MAX_ELF_1 = int(elf_1[1])
    MIN_ELF_2 = int(elf_2[0])
    MAX_ELF_2 = int(elf_2[1])
    print(MIN_ELF_1, MAX_ELF_1,MIN_ELF_2,MAX_ELF_2)
    if elf_1[0] == elf_2[0] and elf_1[1] == elf_2[1]:
        counter += 1
        pass
    
    elif MIN_ELF_1 <= MIN_ELF_2 and MAX_ELF_1 >= MAX_ELF_2:
        
        counter += 1
    elif MIN_ELF_2 <= MIN_ELF_1 and MAX_ELF_2 >= MAX_ELF_1:
        counter += 1
print(counter)

counter = 0 
for line in Lines: 
    elf_both = line.strip().split(',')
    elf_1 = elf_both[0].split('-')
    elf_2 = elf_both[1].split('-')
    MIN_ELF_1 = int(elf_1[0])
    MAX_ELF_1 = int(elf_1[1])
    MIN_ELF_2 = int(elf_2[0])
    MAX_ELF_2 = int(elf_2[1])
    print(MIN_ELF_1, MAX_ELF_1,MIN_ELF_2,MAX_ELF_2)
    if elf_1[0] == elf_2[0] and elf_1[1] == elf_2[1]:
        counter += 1
        pass
    elif MIN_ELF_1 <= MIN_ELF_2 <= MAX_ELF_1\
      or MIN_ELF_1 <= MAX_ELF_2 <= MAX_ELF_1\
      or MIN_ELF_2 <= MIN_ELF_1 <= MAX_ELF_2\
      or MIN_ELF_2 <= MIN_ELF_1 <= MAX_ELF_2:
          counter += 1
print(counter)

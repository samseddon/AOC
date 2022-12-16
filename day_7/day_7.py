import pprint as p

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

max_size = 100000
file = open('input_day_7.txt', 'r')                                            
Lines = file.readlines() 
pwd = ''
current_directory = ''
file_structure = Dictlist()

for line in Lines: 
    line = line.strip()
    if line[0] == '$': # We have a command
        if line[2:4] == 'cd':
            if line[5:] == '..':
                pwd_split = pwd.split('/')
                for i in range(2,len(pwd_split)-1,1):
                    pwd = '//' + pwd_split[i] + '/'
                
            else:
                current_directory = line[5:]
                pwd = pwd + current_directory + '/'
        elif line[2:4] == 'ls':
            pass
    elif line[:3] == 'dir':
        pass
    else:
        file_structure[pwd] =  int(line.split(' ')[0])
small_folders = []
big_folders = []
p.pprint(file_structure)
directories = []
for key in file_structure:        
    if sum(file_structure[key]) <= max_size:
        small_folders.append(key)
    directories.append(key)
p.pprint(sorted(directories))


#for key in small_folders:
#    key_split = key.split('/')
#    for i in range(2,len(key_split)-1,1):
#        key_up_one = '//' + key_split[i] + '/'
#    file_structure[key_up_one] = file_structure[key]

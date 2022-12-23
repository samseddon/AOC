import pprint as p
import numpy as np

class Dictlist(dict):                                                          
    def __setitem__(self, key, value):                                         
        try:                                                                   
            self[key]                                                          
        except KeyError:                                                       
            super(Dictlist, self).__setitem__(key, [])                         
        self[key].append(value)


class Directory:
    def __init__(self, name, pwd, level, files, file_size, dir_size):
        self.name = name
        self.pwd = pwd
        self.level = level
        self.files = files
        self.file_size = file_size
        self.dir_size = dir_size
        self.total_size = 0

    def update_size(self):
        self.total_size = self.file_size + self.dir_size

def return_parent_path(pwd):
    pwd_split = pwd.split('/')
    pwd = '//'
    if len(pwd_split) == 4:
        return pwd
    else:
        for i in range(2,len(pwd_split)-2,1):
            pwd = pwd + pwd_split[i] + '/'
        return pwd

file = open('input_day_7.txt', 'r')                                            
Lines = file.readlines()

dir_size = Dictlist()
pwd = ""
stopper = 0

all_dir = [Directory('//','//',0,[],0,0)]
level = -1
file_dict = Dictlist()

for line in Lines:                                                             
    line = line.strip()
    if line.strip() == '$ cd ..':
        pwd = return_parent_path(pwd)
        level -= 1
    
    elif line[0:4] == '$ cd': 
        current_directory = line[5:]                                   
        pwd = pwd + current_directory + '/'  
        level += 1
    elif line[:3] == 'dir':
        all_dir.append(Directory(line[4:],pwd  + line[4:] + '/',level+1,[],0,0))
    elif line == '$ ls':
        pass
    else:
        file_dict[pwd] = [line.split(' ')[1],line.split(' ')[0]] 

print(len(all_dir))
names = []
for folder in all_dir:
    names.append(folder.name)
    if folder.pwd in file_dict:
        for file in file_dict[folder.pwd]:
            folder.files.append(file[0])
            folder.file_size = folder.file_size + int(file[1])

print(len(names))
print(sorted(names))
print(len(np.unique(names)))
all_dir = sorted(all_dir,key=lambda x: x.level, reverse = True)

for folder in all_dir:
    if folder.name == '//':
        pass
    else:
        pwd_variable = folder.pwd
        while(pwd_variable != '//'):
            pwd_variable = return_parent_path(pwd_variable)
            dir_size[pwd_variable] = folder.file_size 

for folder in all_dir:
    if folder.pwd in dir_size:
        for ds in dir_size[folder.pwd]:
            folder.dir_size = folder.dir_size + int(ds)
    folder.update_size()
answer = 0
for folder in all_dir: 
    if folder.name == '//':
        current_file_system = folder.total_size
    if folder.total_size < 100000:
        answer = answer + folder.total_size
total_system = 70000000
total_req = 30000000
delete_threshold = -1*(total_system - current_file_system - total_req)

all_dir = sorted(all_dir,key=lambda x: x.total_size, reverse = False)     

#for folder in all_dir:
#    if folder.total_size < delete_threshold:
#        pass
#    else:
#        print(folder.total_size,delete_threshold)

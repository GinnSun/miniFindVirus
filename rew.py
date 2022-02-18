import os
import time
path = 'C:\\Games'

def findvirus(path, level=1):
    print('Level', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            print('Find virus in', path+'\\'+i)
            findvirus(path + '\\' + i)
        if i in 'virus.txt':
            print('Found virus', path+'\\'+i)
            print('Pls write <<ok>> enter  if you want to delete virus')
            input()
            print(i, 'Delete complite!')
            exit()
        else:
            print('I dont find virus in ',path+'\\'+i,' i keep searching')
            time.sleep(2)

findvirus(path)


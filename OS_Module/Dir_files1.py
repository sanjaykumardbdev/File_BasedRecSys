# https://www.youtube.com/watch?v=tJxcKyFMTGo&t=566s
import os
from datetime import datetime

print(os.name)
print(os.listdir())

print('=========================')
print(os.getcwd())

os.chdir('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/OS_Module/')
print(os.getcwd())
os.rename('test1.txt', 'test')
os.rename('test', 'test1.txt')

print('=========================')

print(os.stat('test1.txt'))

print(os.stat('test1.txt').st_size)

print(os.stat('test1.txt').st_mtime)

temp = os.stat('test1.txt').st_mtime        # modified time
print(datetime.fromtimestamp(temp))

temp = os.stat('test1.txt').st_atime        #
print(datetime.fromtimestamp(temp))

temp = os.stat('test1.txt').st_ctime        # create time
print(datetime.fromtimestamp(temp))


print('=========================os.walk')

os.chdir('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/')

for dirpath, dirfolder, dirfiles in os.walk('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/'):
    print('CurDir:   ', dirpath)
    print('DirFol: ', dirfolder)
    if dirfiles is None:
        pass
    else:
        print('DirFiles: ', dirfiles)
    print('')


print('=========================environment variables')



print('=========================os.path')

print(dir(os.path))
print(os.getcwd())
print(os.path.isfile('LoginTest.py'))
print(os.path.isdir('OS_Module'))

print(os.path.splitext('LoginTest.py'))         # present
print(os.path.splitext('LoginTest11.py'))       # not present

print(os.path.getsize('LoginTest.py'))       # present
# print(os.path.getsize('LoginTest11.py'))       # not present

print(os.path.realpath('LoginTest.py'))
print(os.path.relpath('LoginTest.py'))

print(os.path.exists('LoginTest11.py'))       # not present
print(os.path.exists('LoginTest.py'))       # present

file_name = 'LoginTest.py'
temp = os.path.exists(file_name)

if temp:
    print('file is present with name {}'.format(file_name))
    print(os.path.realpath(file_name))
else:
    print('file is not present')

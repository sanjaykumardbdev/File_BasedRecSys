# https://www.youtube.com/watch?v=yA4eI-m7ONI&pp=QAA%3D
import os
from datetime import datetime
import shutil

print(os.name)
print(os.listdir())

print('=========================')
print(os.getcwd())

os.chdir('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/OS_Module/')
print(os.getcwd())

print('=========================os.walk')

os.chdir('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/')

for dirpath, dirfolder, dirfiles in os.walk('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/OS_Module/'):
    print('CurDir:   ', dirpath)
    print('DirFol: ', dirfolder)
    if dirfiles is None:
        pass
    else:
        print('DirFiles: ', dirfiles)
    print('')

print('=========================move files')
os.chdir('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/OS_Module')
print(os.getcwd())

dira = r'C:\users\sanjay.kumar12\PycharmProjects\Projects\File_BasedRecSys\OS_Module\a\test.txt'

dirb = r'C:\users\sanjay.kumar12\PycharmProjects\Projects\File_BasedRecSys\OS_Module\b'

dirc = r'C:\users\sanjay.kumar12\PycharmProjects\Projects\File_BasedRecSys\OS_Module\c'

# shutil.move(trg_dir,src_dir)

shutil.move(dira, dirb)
# trg_dir_c = os.path.join(dirc, 'test.txt')
# print(trg_dir_c)
shutil.copy(dirb, dirc)



# https://www.geeksforgeeks.org/python-os-path-join-method/

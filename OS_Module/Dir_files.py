# https://www.youtube.com/watch?v=tJxcKyFMTGo&t=566s

import os

print(os.name)
print(os.listdir())

print('=========================')
print(os.getcwd())

os.chdir('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/')
print(os.getcwd())
os.chdir('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/OS_Module/')
print(os.getcwd())
print(os.listdir())

print('========================= create dir')
os.chdir('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/OS_Module/')
print(os.getcwd())
os.removedirs('A/B/C/D')

# to create single dir
os.mkdir('A')
os.rmdir('A')
os.mkdir('A')
os.chdir('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/OS_Module/A/')

# to create single dir

os.makedirs('B/C/D')
os.makedirs('B1/C1/D1')
os.chdir('C:/users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/OS_Module/')
print('===============')
print(os.getcwd())



# os.removedirs('/A/B/C')
# os.removedirs('/A/B')

# os.mkdir('A')

# os.rename('test', 'test1.txt')




print('=========================')

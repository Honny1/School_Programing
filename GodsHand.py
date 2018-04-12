import os
file_list=open("list_file.txt","w")
for file in os.listdir('.'):
    file+="\n"
    file_list.write(file)
file_list.close()

file_list = open("list_file.txt", "r")
for line in file_list:
    print(line)
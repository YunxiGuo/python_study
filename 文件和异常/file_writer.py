"""写入文件"""

file_name = 'write_test.txt'
# with open(file_name,'w') as file_object:
#     file_object.write('i like programming.')

with open(file_name,'a') as file_object1:
    file_object1.write('附加第一行\n')
    file_object1.write('附加第二行\n')
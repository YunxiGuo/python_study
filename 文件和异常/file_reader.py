"""读取文件"""

file_name = 'read_test.txt'
with open(file_name) as file_object:
    # file_contents = file_object.read()
    # print(file_contents)

    # lines = file_object.readlines()
    # for line in lines:
    #     print(line.rstrip())

    """使用从文件中读取的数据"""
    lines = file_object.readlines()
    content = ''.join(lines)
    print(content)
    message = 'i like dogs'
    print('old messga:' + message)
    message = message.replace('dog','cat')
    print('new message:' + message)

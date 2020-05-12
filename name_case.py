#变量
message = str('hello，world')
print(message)
message1 = str(",lucy")
#字符串拼接
print(message + message1)
#首字母大写
message2 = message + message1
print(message2.title())
#全大写
print(message2.upper())
#全小写
print(message2.lower())
#删除空白
message3 = '  python  kk'
print(message3.rstrip())
print(message3.strip())
print(message3.lstrip())
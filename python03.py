# 测试break，break结束当前循环，指最近的一层循环
message = str("hello world!")
print(message)
while True:
    i = input("请输入内容：")
    if i == "q" or i == "Q":
        print("循环结束，跳出当前循环")
        break
    else:
        print(i)
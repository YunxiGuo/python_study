# 循环嵌套 
# 打印九九乘法表

for m in range(1,10):
    for n in range(1,m+1):
        print("{0}*{1}={2}".format(n,m,m*n),end="\t")
    print()


#打印出工资大于15000的员工

e1 = dict(name="张一",age=18,salary=10000)
e2 = dict(name="张二",age=18,salary=12000)
e3 = dict(name="张三",age=18,salary=14000)
e4 = dict(name="张四",age=18,salary=17000)
t = [e1,e2,e3,e4]
for x in t:
    if x.get("salary") > 15000:
        print(x)
score = input("请输入一个分数：")
grade = ""
if int(score) < 60:
    grade = "不及格"
elif int(score) < 80:
    grade = "及格"
elif int(score) < 90:
    grade = "良"
elif int(score) >= 90:
    grade = "优秀"
print("输入的分数为：{0} 等级为：{1}".format(score,grade))
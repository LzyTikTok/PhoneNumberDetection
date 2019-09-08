def judge(text):
    length = len(text)
    if length == 3 :
        print("紧急号码")

text = input("输入您的电话号码：")
if text.isnumeric() :
    judge(text)
else :
    print("请输入数字！")
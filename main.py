import os
import pymysql
import numpy as np
import tkinter as tk
from tkinter import messagebox

def search(figure1,figure2,text,name,mess):             #figure1 = 截取字符串的起始位置, figure2=长度，text= 用户输入的号码， name = 数据库中表名 mess = 号码类型
    # 打开数据库连接
    db = pymysql.connect("localhost","root","root","phone" )
    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()
    #SQL 查询语句
    sql = "SELECT * FROM " + name
    num_1 = '000'
    num_0 = '000'
    if name ==  'telephone' :
        if text[0] == '8':
            num_0 = text[0:3]
        else:                   #第一位到第四位为普通区号，第一位到第三位为特殊区号，此处都截取
            num_0 = text[0:3]
            num_1 = text[0:4]
    else  :
        num_0 = text[figure1:figure2]
    flag = 0
    try:
        #执行SQL语句
        cursor.execute(sql)
        #获取所有记录列表
        results = cursor.fetchall()
        i = 1
        for row in results:
            if row[i] == num_1 or row[i] == num_0:
                #打印结果
                property = row[i-1]
                flag = 1
                tk.messagebox.showinfo(title='结果', message=property+" "+mess)
                break
    except :
        print("数据库已读完")
    if flag == 0 :
        tk.messagebox.showerror(message='数据库中没有此号码，再试一遍吧')
    #关闭数据库连接
    db.close()

def judge(text):
    length = len(text)
    n1 = text[0]
    if length == 3 :
        if n1 != '1' and n1 != '9':
            tk.messagebox.showerror(message='不存在此号码，再试一遍吧')
        else :
            figure1 = 0
            figure2 = 3
            name = 'emergency'
            mess = '紧急号码'
            search(figure1,figure2, text, name, mess)
    elif length == 5:
        if n1 != '1':
            tk.messagebox.showerror(message='不存在此号码，再试一遍吧')
        else:
            figure1 = 0
            figure2 = 5
            name = 'service'
            mess = '服务号码'
            search(figure1,figure2, text, name, mess)

    elif length == 7:
        tk.messagebox.showinfo(title='结果', message='本地座机 ')
    elif length == 8:
        tk.messagebox.showinfo(title='结果', message='本地座机 ')
    elif length == 11:
        if n1 != '1' and n1 != '0' and n1 != '8'  :
            tk.messagebox.showerror(message='不存在此号码，再试一遍吧')
        elif n1 == '0' or n1 == '8':
            figure1 = 0
            figure2 = 0                         #此处随便赋值，因为座机的特殊性，要截取两次，此操作放到函数进行
            name = 'telephone'
            mess = '座机'
            search(figure1,figure2,text, name, mess)
        elif n1 == '1':
            figure1 = 0
            figure2 = 7
            name = 'cellphone'
            mess = '手机'
            search(figure1, figure2, text, name, mess)
    else :
        tk.messagebox.showerror(message='号码长度错误，再试一遍吧')

#主程序main 调用窗口


window = tk.Tk()
window.title('电话号码测试程序')
window.geometry('450x300')

# welcome image

canvas = tk.Canvas(window, height=200, width=200)
# image_file = tk.PhotoImage(file='photo.gif')
#
# image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# information
tk.Label(window, text='电话号码: ').place(x=50, y=150)

var_usr_num = tk.StringVar()
entry_usr_num = tk.Entry(window, textvariable= var_usr_num )
entry_usr_num.place(x=160, y=150)
usr_num = var_usr_num.get()

def enter():
    usr_num = var_usr_num.get()
    if usr_num.isnumeric():
        judge(usr_num)
    else:
        tk.messagebox.showerror(message='请输入数字')

# login and sign up button
btn_enter = tk.Button(window, text='确认', command=enter)
btn_enter.place(x=320, y=145)

window.mainloop()

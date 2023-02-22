from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('30 Days Challenge Program')
GUI.geometry('500x400')

L1 = Label(GUI,text='30 Day Challenge Program',font=('Ansana New',30),fg='black')
L1.place(x=30,y=20)  

def Button1():
    text = '1.ข้าวทั้งวัน 120 - 150 กรัม แบ่งทาน 3 มืื้อ (มื้อละ 50 กรัม)\n  Remark: ขนมปัง 2 แผ่น/วัน\n \n2.โปรตีน 200 กรัม\n  - ไข่ขาวต่อมื้อ 2 แดง 1\n  - ปลา ไก่ เนื้อ หมู กุ้ง ไม่ติดมันติดให้น้อยที่สุด\n  - นมจากธัญพืช น้ำตาลต่ำ\n  - นมอัลมอนกล่องเล็ก\n  - ดีน่าน้ำตาลน้อย\n  - นมวัวอย่างเดียวที่ทาานได้ คือ ผสมเวย์โปรตีน 1 ขวด\n \n! ทานผักแทรกเข้าไปให้ได้ 2 มื้อ\n! มื้อสุดท้าย 6 โมง เลทสุดไม่เกิน 1 ทุ่ม'
    messagebox.showinfo('Week 1',text)


FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=30, y=100)
B1 = ttk.Button(FB1,text='Week 1',command=Button1)
B1.pack(ipadx=20,ipady=20)

def Button2():
    text = 'IF18/6\nปริมาณอาหารเท่า Week 1\n \n! ดื่มน้ำเพิ่ม 2.3 - 3 ลิตร\n! ปรับเวลานอนให้เร็วขึ้นไม่เกินเที่ยงคืน'
    messagebox.showinfo('Week2',text)


FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=30, y=200)
B2 = ttk.Button(FB1,text='Week 2',command=Button2)
B2.pack(ipadx=20,ipady=20)


def Button3():
    text = 'IF18/6\nปริมาณอาหารเท่า Week 1\n \n! กินขนมได้นิดหน่อย คือ ของว่างได้แค่ครั้งเดียว'
    messagebox.showinfo('Week3',text)


FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=30, y=300)
B3 = ttk.Button(FB1,text='Week 3',command=Button3)
B3.pack(ipadx=20,ipady=20)

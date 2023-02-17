from tkinter import *
from tkinter import ttk # Theme of Tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') # ชื่อโปรแกรม
GUI.geometry('500x400') # ขนาดหน้าต่าง

#B1 = Button(GUI,text='เงินมีอยู่กี่บาท') # สร้างปุ่มที่มีข้อความ
#B1.pack() # ทำให้ปุ่มอยู่ตรงกลาง


L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font('Angsana New',30),fg='green')
L1.place(x=30,y=20)

def Button2(): # สร้างฟังก์ชั่นชื่อว่า Button2
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

#FB1 = Frame(GUI) # คล้ายกระดาน
FB1 = LabelFrame(GUI,text='Money') # คล้ายกระดาน
FB1.place(x=100,y=30)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2) # ผูกปุ่มกับฟังก์ชั่น
B2.pack(ipadx=20,ipady=20) 
############################################

############################################
def Button3():
    text = 'Python 101, Math'
    messagebox.showinfo('วิชาเรียนวันที่  10-20 ก.พ.',text)

FB2 = LabelFrame2(GUI,text='Subject') 
FB2.place(x=100,y=30)
B3 = ttk.Button(FB1,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20) 
############################################

GUI.mainloop()

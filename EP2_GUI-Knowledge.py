from tkinter import *
from tkinter import ttk # Theme of Tk
from tkinter import messagebox

GUI = Tk() # หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูลด้วย Python') # ชื่อโปรแกรม
GUI.geometry('340x300') # ขนาดหน้าต่าง

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('TH SarabunPSK',22),fg='green')
L1.place(x=10,y=10)
##############################
def Button1 () :
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
    #messagebox.showwarning('เงินในบัญชี',text)
    #messagebox.showerror('เงินในบัญชี',text)
#FB1 = Frame(GUI) # สร้างเฟรมคล้ายกระดานขึ้นมา
FB1 = LabelFrame(GUI,text='Money') # สร้างเฟรมที่มีข้อความชื่อเฟรมแสดง
FB1.place(x=20,y=60)
B1 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button1) # สร้างปุ่มที่มีข้อความ โดยเรียก Theme มาใช้
B1.pack(ipadx=20,ipady=20)  #B1.pack(ipadx=20,ipady=20,padx=30,pady=30)
##############################
def Button2 () :
    text = 'เรียน Python 101 กับ ChatGPT'
    messagebox.showinfo('วิชาที่เรียน',text)
FB2 = LabelFrame(GUI,text='Subject')
FB2.place(x=180,y=60)
B2 = ttk.Button(FB2,text='เรียนอะไรไปบ้าง',command=Button2)
B2.pack(ipadx=20,ipady=20) 
##############################

def Button3 () :
    text = 'ข้อควรระวังคือ การใส่ค่า Position X,Y มักจะสับสน'
    messagebox.showwarning('ข้อควรระวัง',text)

FB3 = LabelFrame(GUI,text='Warning')
FB3.place(x=20,y=180)
B3 = ttk.Button(FB3,text='ข้อควรระวัง',command=Button3)
B3.pack(ipadx=20,ipady=20) 
##############################

def Button4 () :
    text = 'Error ที่มักจะเจอคือ การอ้างอิงชื่อ function กับชื่อตัวแปร ผิด หรือแก้ไขไม่ครบ'
    messagebox.showwarning('Error ที่เจอบ่อย',text)

FB4 = LabelFrame(GUI,text='Error')
FB4.place(x=180,y=180)
B4 = ttk.Button(FB4,text='Error ที่เจอบ่อย',command=Button4)
B4.pack(ipadx=20,ipady=20) 
##############################

GUI.mainloop()

from tkinter import *
from tkinter import ttk # Theme of Tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') # ชื่อโปรแกรม
GUI.geometry('500x400') # ขนาดหน้าต่าง

#B1 = Button(GUI,text='เงินมีอยู่กี่บาท') # สร้างปุ่มที่มีข้อความ
#B1.pack() # ทำให้ปุ่มอยู่ตรงกลาง

B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท') # สร้างปุ่มที่มีข้อความ โดยเรียก Theme มาใช้
B1.pack(ipadx=20,ipady=20) # pack ทำให้ปุ่มอยู่ตรงกลางหน้าจอ กำหนดค่า internal padding = 20


#B2 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท') # สร้างปุ่มที่มีข้อความ โดยเรียก Theme มาใช้
#B2.place(x=50,y=200) # place จะเป็นการกำหนด Position X,Y

FB1 = Frame(GUI) # คล้ายกระดาน
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท') # สร้างปุ่มที่มีข้อความ โดยเรียก Theme มาใช้
B2.pack(ipadx=20,ipady=20) 

GUI.mainloop()

//Python turtle documents
//นำเข้าชุดคำสั่ง turtle
import turtle
//เปิดหน้าต่างใหม่ขึ้นมา พร้อมเมาส์ปากกาสำหรับลากเส้น
tao = turtle.Pen()
//ให้ tao เปลี่ยน shape ไปเป็นรูปเต่า turtle
tao.shape('turtle')
//ให้เต่าเดินหน้าไป 100 pixel
tao.forward(100)
//ให้เต่าหันซ้าย 90 องศา
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
//ลบเส้นบนหน้าจอ
tao.clear()
//คาถาวนซ้ำ 4 ครั้ง
for i in range(4) :
    tao.forward(100)
    tao.left(90)
//แล้ว Enter 2 ครั้ง

// tao.penup() ให้เต่าเดินไปโดยยังไม่ต้องลากเส้น
//tao.goto(200,200) อธิบายควบคู่กับแกน X,Y
//tao.pendown()

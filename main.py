
from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Face Recognition System')
        
        #first image
        img=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\face.jpeg")
        img=img.resize((275,183),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image 
        img1=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\sha.jpeg")
        img1=img1.resize((299,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image 
        img2=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\shaLogo.jpeg")
        img2=img2.resize((197,145),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #big image 

        img3=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\b2.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="    ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=20)
       # title_lbl.configure(anchor="center")

        #student button 
        img4=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\lec.jpeg")
        img4=img4.resize((275,183),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)

        b1_1=Button(bg_img,text="اضافة محاضرة",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=260,width=200,height=40)

        #Detect face button 
        img5=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\fac.jpeg")
        img5=img5.resize((250,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=200,height=200)

        b1_1=Button(bg_img,text="تسجيل الغياب",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=260,width=200,height=40)

         #Detect face button 
        img6=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\repo.jpeg")
        img6=img6.resize((197,256),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=200,height=200)

        b1_1=Button(bg_img,text="قائمة الحضور ",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=260,width=200,height=40)

        #ss button 
        img7=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\st.jpeg")
        img7=img7.resize((275,183),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=200,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="ادارة الطلاب",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=480,width=200,height=40)

        #ss button 
        img8=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\ai.jpeg")
        img8=img8.resize((300,168),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=500,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="train data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=480,width=200,height=40)

         #ss button 
        img9=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\ex.jpeg")
        img9=img9.resize((276,183),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=800,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="خروج",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=480,width=200,height=40)

        #================Functions buttons=======
        




if __name__ =="__main__":
    root =Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

print('a7a')
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\face recognition system\images\lo.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="darkslategray")
        frame.place(x=550,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\shaLogo.jpeg")
        img1=img1.resize((100,100))
        self.PhotoImage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.PhotoImage1,bg="black",borderwidth=0)
        lblimg1.place(x=680,y=175,width=100,height=100)


        username=lbl=Label(frame,text="اسم المستخدم",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=150)

        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        
        password=lbl=Label(frame,text="كلمة السر",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=257)

        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=290,width=270)


        #Icon Image 
        img2=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\dd.jpeg")
        img2=img2.resize((25,25))
        self.PhotoImage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.PhotoImage2,bg="black",borderwidth=0)
        lblimg1.place(x=590,y=320,width=25,height=25)

        img3=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\pas.jpeg")
        img3=img3.resize((25,25))
        self.PhotoImage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.PhotoImage3,bg="black",borderwidth=0)
        lblimg1.place(x=590,y=427,width=25,height=25)


        loginbtn=Button(frame,text="تسجيل الدخول",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        loginbtn.place(x=110,y=350,width=120,height=35)



if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()

    


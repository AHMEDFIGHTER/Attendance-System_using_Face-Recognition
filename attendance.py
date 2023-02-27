from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
#from tkinter import messsagebox 
#import mysql.connector
import cv2


class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("Attendance system")

          #first image
        img=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\face.jpeg")
        img=img.resize((800,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #second image 
        img1=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\sha.jpeg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

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

        img3=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\bs.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

       # title_lbl=Label(bg_img,text="Attendance Mangment System ",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
       # title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=1500,height=650)

         #left label frame 

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ادارة البيانات", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=580)

        img_left=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\shaLogo.jpeg")
        img_left=img_left.resize((197,145),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=660,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=135,width=635,height=400)

        #labland Entry 

        id_label=Label(left_inside_frame,text="الرقم الجامعي: ",font=("comicsansns 11 bold"),bg="white",fg="darkgreen")
        id_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_entry=ttk.Entry(left_inside_frame,width=25,font=("comicsansns 10 bold"))
        search_entry.grid(row=0,column=1,pady=5,padx=5,sticky=W)

        name_label=Label(left_inside_frame,text="اسم الطالب: ",font=("comicsansns 11 bold"),bg="white",fg="darkgreen")
        name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=25,font=("comicsansns 10 bold"))
        name_entry.grid(row=1,column=1,pady=5,padx=5,sticky=W)

        course_label=Label(left_inside_frame,text="حالة الحضور: ",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        course_label.grid(row=2,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),width=12,state="read only")
        search_combo["values"]=( "حاضر","غائب")
        search_combo.current(0)
        search_combo.grid(row=2,column=1,padx=2,pady=10)

        #buttons frame

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=715,height=100)

        save_btn=Button(btn_frame,text="csv تحميل ملف", width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="csv رفع ملف", width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="تعديل", width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="حذف الكل", width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

         #right label frame 

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="قائمة الحضور", font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=10,width=720,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=660,height=400)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame,column=("ide","name","department","time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        #self.AttendaceReportTable.heading("dd",text="AttendanceID")
        self.AttendaceReportTable.heading("name",text="الاسم")

        self.AttendaceReportTable["show"]="headings"
        




        self.AttendaceReportTable.pack(fill=BOTH,expand=1)

       




    

if __name__ =='__main__':
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
    

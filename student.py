from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk

class Student:
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

        img3=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\bs.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

       # title_lbl=Label(bg_img,text="ادارة بيانات الطلاب",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
       # title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=1500,height=650)

        #left label frame 

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=580)

        img_left=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\add.png")
        img_left=img_left.resize((150,150),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=660,height=130)

        #current course 

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="ادارة بيانات الطالب", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=660,height=120)

        #department
       
        dep_label=Label(current_course_frame,text="القسم: ",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("اختار القسم", "علوم حاسب","نظم ومعلومات","هندسة","اعلام","ادارة ومحاسبه")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
       
        course_label=Label(current_course_frame,text="المواد: ",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("اختار المواد", "sdsa حاسب","نظم ومعلومات","هندسة","اعلام","ادارة ومحاسبه")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10)

         #department
       
        dep_label=Label(current_course_frame,text="السنة الدراسية: ",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        dep_label.grid(row=1,column=0,padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("الرابعة", "علوم حاسب","نظم ومعلومات","هندسة","اعلام","ادارة ومحاسبه")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10)

        #course
       
        course_label=Label(current_course_frame,text="الترم: ",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        course_label.grid(row=1,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("الثاني", "sdsa حاسب","نظم ومعلومات","هندسة","اعلام","ادارة ومحاسبه")
        course_combo.current(0)
        course_combo.grid(row=1,column=3,padx=2,pady=10)

        #class student information

        class_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class student infrormation",font=("times new roman",12,"bold"))
        class_frame.place(x=5,y=250,width=700,height=300)

        #first row

        studId_label=Label(class_frame,text="الكود الجامعي",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        studId_label.grid(row=0,column=0,padx=10,sticky=W)

        search_entry=ttk.Entry(class_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=1,pady=5,padx=10,sticky=W)

        studName_label=Label(class_frame,text="اسم الطالب",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        studName_label.grid(row=0,column=3,padx=10,sticky=W)

        search_entry=ttk.Entry(class_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=4,pady=5,padx=10,sticky=W)

        #second row

        gender_label=Label(class_frame,text="النوع",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        gender_label.grid(row=1,column=0,padx=10,sticky=W)

        search_entry=ttk.Entry(class_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=1,column=1,pady=5,padx=10,sticky=W)

        phone_label=Label(class_frame,text="رقم الهاتف",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        phone_label.grid(row=1,column=3,padx=10,sticky=W)

        search_entry=ttk.Entry(class_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=1,column=4,pady=5,padx=10,sticky=W)

        #third row 

        email_label=Label(class_frame,text="البريد الالكتروني",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        email_label.grid(row=2,column=0,padx=10,sticky=W)

        search_entry=ttk.Entry(class_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=2,column=1,pady=5,padx=10,sticky=W)

        address_label=Label(class_frame,text="العنوان",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        address_label.grid(row=2,column=3,padx=10,sticky=W)

        search_entry=ttk.Entry(class_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=2,column=4,pady=5,padx=10,sticky=W)

        #Radio Burrons 

        #radiobtn1=ttk.Radiobutton(class_frame,text="take photo",value="YES")
        #radiobtn1.grid(row=3,column=0)

       # radiobtn2=ttk.Radiobutton(class_frame,text="no photo",value="YES")
        #radiobtn2.grid(row=3,column=1)
        #btn frame
        btn_frame=Frame(class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=155,width=700,height=70)

        save_btn=Button(btn_frame,text="حفظ",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=4)

        edit_btn=Button(btn_frame,text="تعديل",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        edit_btn.grid(row=0,column=1,padx=4)

        delete_btn=Button(btn_frame,text="حذف",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=4)

        reset_btn=Button(btn_frame,text="حذف الكل",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=4)

        takePhoto_btn=Button(class_frame,text="تحميل صورة",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        takePhoto_btn.grid(row=3,column=0,padx=4,pady=5)

        updatePhoto_btn=Button(class_frame,text="تعديل صورة",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        updatePhoto_btn.grid(row=3,column=1,padx=4,pady=5)









        #right label frame 

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="", font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=10,width=660,height=580)

        img_right=Image.open(r"C:\Users\DELL\Desktop\face recognition system\images\search.png")
        img_right=img_right.resize((150,150),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=660,height=130)

        #search system frame

        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="بحث",font=("times new roman",12,"bold"),fg="darkgreen")
        Search_frame.place(x=5,y=135,width=660,height=70)

        search_label=Label(Search_frame,text="بحث بواسطة:",font=("times new roman",12,"bold"),bg="white",fg="red")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=12,state="read only")
        search_combo["values"]=("اختار ", "الرقم الجامعي","الاسم")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,pady=5,padx=10,sticky=W)

        search_btn=Button(Search_frame,text="بحث",width=12,font=("times new roman",12,"bold"),bg="blue", fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="اظهار الجميع",width=12,font=("times new roman",12,"bold"),bg="blue", fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        # ===========table frame ####################

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=650,height=250)

        #dep_label=Label(table_frame,text="Department",bg="black",fg="white")
       # dep_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem"))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview())
        scroll_y.config(command=self.student_table.yview())

        self.student_table.heading("dep",text="الاسم")
        self.student_table.heading("course",text="القسم")
        self.student_table.heading("year",text="الشعبة")
        self.student_table.heading("sem",text="نسبة الحضور")

        

        #self.student_table.heading("name",text="Name")
       
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)


        

        
       


if __name__ =="__main__":
    root =Tk()
    obj=Student(root)
    root.mainloop()
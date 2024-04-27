from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import backend

def mainwin():
    global window
    try:
        window.destroy()
    except:
        pass
    window = Tk()
    window.wm_title("بانکداری")
    window.geometry("1280x720")


    b1=ttk.Button(window,text="مدارک", width=12,command=doc_win)
    b1.grid(row=1,column=4)

    b2=ttk.Button(window,text="اسناد ضمانتی", width=12,command=wdoc_win)
    b2.grid(row=3,column=4)

    b3=ttk.Button(window,text="استعلام ها", width=12,command=inq_win)
    b3.grid(row=5,column=4)

    b4=ttk.Button(window,text="خروج", width=12 , command=window.destroy)
    b4.grid(row=7,column=4)

    window.mainloop()


def doc_win():
    global window
    try:
        window.destroy()
    except:
        pass
    window=Tk()
    window.title("مدارک")
    window.geometry("680x480")


    def doc_view_command():
        list1.delete(0,END)
        for row in backend.doc_view():
            list1.insert(END,row)



    def search_doc_command():
        list1.delete(0,END)
        for row in backend.search_doc(user_number_text.get(),password_text.get()):
            list1.insert(END,row)


    def add_doc_command():
        backend.insert_doc(user_number_text.get(),password_text.get(),l_agreement_text.get(),l_bcert_ncard_text.get(),l_pincome_text.get(),l_presidence_text.get(),l_avr_text.get(),g1_agreement_text.get(),g1_bcert_ncard_text.get(),g1_pincome_text.get(),g1_avr_text.get(),g2_agreement_text.get(),g2_bcert_ncard_text.get(),g2_pincome_text.get(),g2_avr_text.get())
        list1.delete(0,END)
        list1.insert(END,(user_number_text.get(),password_text.get(),l_agreement_text.get(),l_bcert_ncard_text.get(),l_pincome_text.get(),l_presidence_text.get(),l_avr_text.get(),g1_agreement_text.get(),g1_bcert_ncard_text.get(),g1_pincome_text.get(),g1_avr_text.get(),g2_agreement_text.get(),g2_bcert_ncard_text.get(),g2_pincome_text.get(),g2_avr_text.get()))


    def doc_delete_command():
        backend.delete_doc(selected_tuple[0])


    l1=Label(window,text="شماره حساب")
    l1.grid(row=0,column=0)

    l2=Label(window,text="پسورد")
    l2.grid(row=0,column=2)

    l3=Label(window,text="قرارداد وام گیرنده")
    l3.grid(row=0,column=4)

    l4=Label(window,text="کوپی شناسنامه و کارت ملی")
    l4.grid(row=1,column=0)

    l5=Label(window,text="مدرک احراز درآمد وام گیرنده")
    l5.grid(row=1,column=2)

    l6=Label(window,text="مدرک احراز سکونت وام گیرنده")
    l6.grid(row=1,column=4)

    l7=Label(window,text="میانگین سه ماهه")
    l7.grid(row=2,column=0)

    l8=Label(window,text="قرارداد ضامن اول")
    l8.grid(row=2,column=2)

    l9=Label(window,text="کوپی شناسنامه و کارت ملی ضامن اول")
    l9.grid(row=2,column=4)

    l10=Label(window,text="مدرک احراز درآمد ضامن اول")
    l10.grid(row=3,column=0)

    l11=Label(window,text="میانگین سه ماهه ضامن اول")
    l11.grid(row=3,column=2)

    l12=Label(window,text="قرارداد ضامن دوم")
    l12.grid(row=3,column=4)

    l13=Label(window,text="کوپی شناسنامه و کارت ملی ضامن دوم")
    l13.grid(row=4,column=0)

    l14=Label(window,text="مدرک احراز درآمد ضامن دوم")
    l14.grid(row=4,column=2)

    l15=Label(window,text="میانگین سه ماهه ضامن دوم")
    l15.grid(row=4,column=4)


    user_number_text=StringVar()
    e1=Entry(window,textvariable=user_number_text)
    e1.grid(row=0,column=1)

    password_text=StringVar()
    e2=Entry(window,textvariable=password_text)
    e2.grid(row=0,column=3)

    l_agreement_text=StringVar()
    e3=Entry(window,textvariable=l_agreement_text)
    e3.grid(row=0,column=5)

    l_bcert_ncard_text=StringVar()
    e4=Entry(window,textvariable=l_bcert_ncard_text)
    e4.grid(row=1,column=1)

    l_pincome_text=StringVar()
    e5=Entry(window,textvariable=l_pincome_text)
    e5.grid(row=1,column=3)

    l_presidence_text=StringVar()
    e6=Entry(window,textvariable=l_presidence_text)
    e6.grid(row=1,column=5)

    l_avr_text=StringVar()
    e7=Entry(window,textvariable=l_avr_text)
    e7.grid(row=2,column=1)

    g1_agreement_text=StringVar()
    e8=Entry(window,textvariable=g1_agreement_text)
    e8.grid(row=2,column=3)


    g1_bcert_ncard_text=StringVar()
    e9=Entry(window,textvariable=g1_bcert_ncard_text)
    e9.grid(row=2,column=5)

    g1_pincome_text=StringVar()
    e10=Entry(window,textvariable=g1_pincome_text)
    e10.grid(row=3,column=1)

    g1_avr_text=StringVar()
    e11=Entry(window,textvariable=g1_avr_text)
    e11.grid(row=3,column=3)

    g2_agreement_text=StringVar()
    e12=Entry(window,textvariable=g2_agreement_text)
    e12.grid(row=3,column=5)

    g2_bcert_ncard_text=StringVar()
    e13=Entry(window,textvariable=g2_bcert_ncard_text)
    e13.grid(row=4,column=1)


    g2_pincome_text=StringVar()
    e14=Entry(window,textvariable=g2_pincome_text)
    e14.grid(row=4,column=3)

    g2_avr_text=StringVar()
    e15=Entry(window,textvariable=g2_avr_text)
    e15.grid(row=4,column=5)


    list1=Listbox(window, height=30,width=100)
    list1.grid(row=5,column=0,rowspan=6,columnspan=3)

    sb1=Scrollbar(window)
    sb1.grid(row=5,column=3,rowspan=6)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>')


    b1=Button(window,text="نمایش", width=12,command=doc_view_command)
    b1.grid(row=5,column=5)

    b2=Button(window,text="جستجو", width=12,command=search_doc_command)
    b2.grid(row=6,column=5)

    b3=Button(window,text="اضافه کردن پرونده", width=12,command=add_doc_command)
    b3.grid(row=7,column=5)

    b4=Button(window,text="تغییر دادن پرونده", width=12)
    b4.grid(row=8,column=5)

    b5=Button(window,text="حذف پرونده", width=12,command=doc_delete_command)
    b5.grid(row=9,column=5)

    b6=Button(window,text="بازگشت", width=12,command=mainwin)
    b6.grid(row=10,column=5)

    window.mainloop()



def wdoc_win():
    global window
    try:
        window.destroy()
    except:
        pass
    window=Tk()
    window.title("اسناد ضمانتی")
    window.geometry("680x480")

    def wdoc_view_command():
        list1.delete(0,END)
        for row in backend.wdoc_view():
            list1.insert(END,row)

    def search_wdoc_command():
        list1.delete(0,END)
        for row in backend.search_wdoc(user_number_text.get(),password_text.get()):
            list1.insert(END,row)


    def add_wdoc_command():
        backend.insert_wdoc(user_number_text.get(),password_text.get(),l_wdtype_text.get(),l_wdamount_text.get(),l_confirm_text.get(),g1_wdtype_text.get(),g1_wdamount_text.get(),g1_confirm_text.get(),g2_wdamount_text.get(),g2_wdamount_text.get(),g2_confirm_text.get())
        list1.delete(0,END)
        list1.insert(END,(user_number_text.get(),password_text.get(),l_wdtype_text.get(),l_wdamount_text.get(),l_confirm_text.get(),g1_wdtype_text.get(),g1_wdamount_text.get(),g1_confirm_text.get(),g2_wdamount_text.get(),g2_wdamount_text.get(),g2_confirm_text.get()))



    l1=Label(window,text="شماره حساب")
    l1.grid(row=0,column=0)

    l2=Label(window,text="پسورد")
    l2.grid(row=0,column=2)

    l3=Label(window,text="نوع سند ضمانتی")
    l3.grid(row=0,column=4)

    l4=Label(window,text="مبلغ سند ضمانتی")
    l4.grid(row=1,column=0)

    l5=Label(window,text="تاییدیه کسر از حقوق")
    l5.grid(row=1,column=2)

    l6=Label(window,text="نوع سند ضمانتی ضامن اول")
    l6.grid(row=2,column=0)

    l7=Label(window,text="مبلغ سند ضمانتی ضامن اول")
    l7.grid(row=2,column=2)

    l8=Label(window,text="تاییده کسر از حقوق ضامن اول")
    l8.grid(row=2,column=4)

    l9=Label(window,text="نوع صند ضمانتی ضامن دوم")
    l9.grid(row=3,column=0)

    l10=Label(window,text="مبلغ سند ضمانتی ضامن دوم")
    l10.grid(row=3,column=2)

    l11=Label(window,text="تاییدیه کسر از حقوق ضامن دوم")
    l11.grid(row=3,column=4)


    user_number_text=StringVar()
    e1=Entry(window,textvariable=user_number_text)
    e1.grid(row=0,column=1)

    password_text=StringVar()
    e2=Entry(window,textvariable=password_text)
    e2.grid(row=0,column=3)

    l_wdtype_text=StringVar()
    e3=Entry(window,textvariable=l_wdtype_text)
    e3.grid(row=0,column=5)

    l_wdamount_text=StringVar()
    e4=Entry(window,textvariable=l_wdamount_text)
    e4.grid(row=1,column=1)

    l_confirm_text=StringVar()
    e5=Entry(window,textvariable=l_confirm_text)
    e5.grid(row=1,column=3)

    g1_wdtype_text=StringVar()
    e6=Entry(window,textvariable=g1_wdtype_text)
    e6.grid(row=2,column=1)

    g1_wdamount_text=StringVar()
    e7=Entry(window,textvariable=g1_wdamount_text)
    e7.grid(row=2,column=3)

    g1_confirm_text=StringVar()
    e8=Entry(window,textvariable=g1_confirm_text)
    e8.grid(row=2,column=5)


    g2_wdtype_text=StringVar()
    e9=Entry(window,textvariable=g2_wdtype_text)
    e9.grid(row=3,column=1)

    g2_wdamount_text=StringVar()
    e10=Entry(window,textvariable=g2_wdamount_text)
    e10.grid(row=3,column=3)

    g2_confirm_text=StringVar()
    e11=Entry(window,textvariable=g2_confirm_text)
    e11.grid(row=3,column=5)


    list1=Listbox(window, height=30,width=100)
    list1.grid(row=4,column=0,rowspan=6,columnspan=4)

    sb1=Scrollbar(window)
    sb1.grid(row=4,column=5,rowspan=6)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>')


    b1=Button(window,text="نمایش", width=20,command=wdoc_view_command)
    b1.grid(row=4,column=5)

    b2=Button(window,text="جستجو", width=20,command=search_wdoc_command)
    b2.grid(row=5,column=5)

    b3=Button(window,text="اضافه کردن سند ضمانتی", width=20,command=add_wdoc_command)
    b3.grid(row=6,column=5)

    b4=Button(window,text="تغییر دادن سند ضمانتی", width=20)
    b4.grid(row=7,column=5)

    b5=Button(window,text="حذف سند ضمانتی", width=20)
    b5.grid(row=8,column=5)

    b6=Button(window,text="بازگشت", width=20,command=mainwin)
    b6.grid(row=9,column=5)

    window.mainloop()



def inq_win():
    global window
    try:
        window.destroy()
    except:
        pass
    window=Tk()
    window.title("استعلام ها")
    window.geometry("680x480")

    def inq_view_command():
        list1.delete(0,END)
        for row in backend.inq_view():
            list1.insert(END,row)

    def search_inq_command():
        list1.delete(0,END)
        for row in backend.search_inq(user_number_text.get(),password_text.get()):
            list1.insert(END,row)

    def add_inq_command():
        backend.insert_inq(user_number_text.get(),password_text.get(),taken_text.get(),l_inquiry_text.get(),g1_inquiry_text.get(),g2_inquiry_text.get())
        list1.delete(0,END)
        list1.insert(END,(user_number_text.get(),password_text.get(),taken_text.get(),l_inquiry_text.get(),g1_inquiry_text.get(),g2_inquiry_text.get()))


    l1=Label(window,text="شماره حساب")
    l1.grid(row=0,column=0)

    l2=Label(window,text="پسورد")
    l2.grid(row=0,column=2)

    l3=Label(window,text="مبلغ گرفته شده")
    l3.grid(row=0,column=4)

    l4=Label(window,text="استعلام وام گیرنده")
    l4.grid(row=1,column=0)

    l5=Label(window,text="استعلام ضامن اول")
    l5.grid(row=1,column=2)

    l6=Label(window,text="استعلام ظامن دوم")
    l6.grid(row=1,column=4)


    user_number_text=StringVar()
    e1=Entry(window,textvariable=user_number_text)
    e1.grid(row=0,column=1)

    password_text=StringVar()
    e2=Entry(window,textvariable=password_text)
    e2.grid(row=0,column=3)

    taken_text=StringVar()
    e3=Entry(window,textvariable=taken_text)
    e3.grid(row=0,column=5)

    l_inquiry_text=StringVar()
    e4=Entry(window,textvariable=l_inquiry_text)
    e4.grid(row=1,column=1)

    g1_inquiry_text=StringVar()
    e5=Entry(window,textvariable=g1_inquiry_text)
    e5.grid(row=1,column=3)

    g2_inquiry_text=StringVar()
    e6=Entry(window,textvariable=g2_inquiry_text)
    e6.grid(row=1,column=5)

    list1=Listbox(window, height=30,width=100)
    list1.grid(row=2,column=0,rowspan=6,columnspan=4)

    sb1=Scrollbar(window)
    sb1.grid(row=4,column=5,rowspan=6)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>')


    b1=Button(window,text="نمایش", width=20,command=inq_view_command)
    b1.grid(row=2,column=5)

    b2=Button(window,text="جستجو", width=20,command=search_inq_command)
    b2.grid(row=3,column=5)

    b3=Button(window,text= "اضافه کردن استعلام", width=20,command=add_inq_command)
    b3.grid(row=4,column=5)

    b4=Button(window,text="تغییر دادن استعلام", width=20)
    b4.grid(row=5,column=5)

    b5=Button(window,text="حذف استعلام", width=20)
    b5.grid(row=6,column=5)

    b6=Button(window,text="بازگشت", width=20,command=mainwin)
    b6.grid(row=7,column=5)



    window.mainloop()

mainwin()

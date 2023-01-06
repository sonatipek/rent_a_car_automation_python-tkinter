from tkinter import *
from tkinter import ttk
from dbTransaction import dbTransactions

def kiralamaEkrani():
    dbIslemleri = dbTransactions("localhost", "root", "", "oto_kiralama")
    kiralamaEkranim = Tk()
    kiralamaEkranim.title("Bergama Araç Kiralama | Araç Kiralama Ekranı")
    kiralamaEkranim.geometry("720x480+100+100")
    kiralamaEkranim.resizable("false", "false")

    # Araç Yakıt Türü Girişi
    musteriler_var = StringVar()
    musteriler=dbIslemleri.getCustomers()
    Label(kiralamaEkranim, text="Müşteriler:", font="Arial 10").place(x=10, y=110)
    ttk.Combobox(kiralamaEkranim, textvariable=musteriler_var, values=musteriler,
        state="readonly",
        background="white",
        font="Arial 11",
        foreground="#0A2647",
        width=13).place(x=10, y=130)
    
    kiralamaEkranim.mainloop()

kiralamaEkrani()
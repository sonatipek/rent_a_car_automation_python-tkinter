from tkinter import *
from tkinter import ttk
from dbTransaction import dbTransactions

def kiralamaEkrani():
    dbIslemleri = dbTransactions("localhost", "root", "", "oto_kiralama")
    kiralamaEkranim = Tk()
    kiralamaEkranim.title("Bergama Araç Kiralama | Araç Kiralama Ekranı")
    kiralamaEkranim.geometry("720x480+100+100")
    kiralamaEkranim.resizable("false", "false")

    def dbKaydet_Kiralama():
        sonuc = araclar_var.get().split(" ")
        ucret = dbIslemleri.getFee(sonuc[1], sonuc[2], sonuc[3])
        ucret = ucret[0]    #sadeleştirme işlemi
        gun = gun_var.get()
        musteri_id = musteriler_var.get()[0]
        arac_id = araclar_var.get()[0]
        yolculuk = yolculuk_var.get()

        kiralamaUcret_var.set(f"{ucret[0] * gun} TL" )
        dbIslemleri.setRent(musteri_id, arac_id, gun, yolculuk)
        print(musteri_id, arac_id, gun, yolculuk)

    # Müşteri Seçimi
    musteriler_var = StringVar()
    musteriler=dbIslemleri.getCustomers()

    Label(kiralamaEkranim, text="Müşteriler:", font="Arial 10").place(x=10, y=10)
    ttk.Combobox(kiralamaEkranim, textvariable=musteriler_var, values=musteriler,
        state="readonly",
        background="white",
        font="Arial 11",
        foreground="#0A2647",
        width=20).place(x=10, y=30)

    # Araç Seçimi
    araclar_var = StringVar()
    araclar=dbIslemleri.getCars()
    Label(kiralamaEkranim, text="Araçlar:", font="Arial 10").place(x=10, y=60)
    ttk.Combobox(kiralamaEkranim, textvariable=araclar_var, values=araclar,
        state="readonly",
        background="white",
        font="Arial 11",
        foreground="#0A2647",
        width=20).place(x=10, y=80)

    # Kiralanacak Gün Seçimi
    gun_var = IntVar()
    Label(kiralamaEkranim, text="Kiralanacak Gün Sayısı:", font="Arial 10").place(x=10, y=110)
    Entry(kiralamaEkranim, textvariable=gun_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=24
        ).place(x=10, y=130)

    # Yolculuk Seçimi
    yolculuk_var = StringVar()
    Label(kiralamaEkranim, text="Kiralama Hedefi Neresi:", font="Arial 10").place(x=10, y=160)
    Entry(kiralamaEkranim, textvariable=yolculuk_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=24
        ).place(x=10, y=180)

    kiralamaUcret_var= StringVar()
    Label(kiralamaEkranim, text="Kiralama Ücreti:", font="Arial 10").place(x=250, y=30)
    kiralamaUcret=Label(kiralamaEkranim, text=" ", textvariable=kiralamaUcret_var, font="Arial 10").place(x=350, y=30)

        
    # Müşteri Kaydet Button
    Button(kiralamaEkranim, text="Kiralama Oluştur", command=dbKaydet_Kiralama, 
        bg="#0A2647", 
        border="0",
        fg="white",
        height=2, 
        width=20,
        font="Arial 12 bold",
        cursor="mouse").place(x=10, y=250)
    
    kiralamaEkranim.mainloop()
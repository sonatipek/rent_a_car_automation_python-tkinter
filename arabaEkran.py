from tkinter import *
from tkinter import ttk
from dbTransaction import dbTransactions

def arabaEkrani():
    dbIslemleri = dbTransactions("localhost", "root", "", "oto_kiralama")
    arabaEkranim = Tk()
    arabaEkranim.title("Araba Bilgileri Giriş Ekranı")
    arabaEkranim.geometry("360x680+50+50")
    arabaEkranim.resizable("false", "false")

    def dbKaydet_Araba():
        tur = aracTuru_var.get()
        marka = marka_var.get()
        model = aracModel_var.get()
        yil = uretimYili_var.get()
        yakit = yakit_var.get()
        vites = vites_var.get()
        guc = motorGucu_var.get()
        hacim = motorHacmi_var.get()
        kasa = kasaTipi_var.get()
        cekis = cekis_var.get()
        kapi = aracKapi_var.get()
        renk = renk_var.get()
        motorNo = motorNo_var.get()
        sasiNo = sasiNo_var.get()
        kira = kira_var.get()
        kullanim = kullanim_var.get()
        bedel = kiraBedeli_var.get()
        

        dbIslemleri.setCar(tur, marka, model, yil, yakit, vites, guc, kasa, hacim, cekis, kapi, renk, motorNo, sasiNo, bedel, kira, kullanim)

        print(tur, marka, model, yil, yakit, vites, guc, kasa, hacim, cekis, kapi, renk, motorNo, sasiNo, kira, kullanim, bedel)
    

    # Araç Türü Girişi
    aracTuru_var = StringVar()
    Label(arabaEkranim, text="Araç Türü:", font="Arial 10").place(x=10, y=10)
    Entry(arabaEkranim, textvariable=aracTuru_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15
        ).place(x=10, y=30)


    # Üretim Yılı Girişi
    uretimYili_var = StringVar()
    Label(arabaEkranim, text="Araç Üretim Yılı:", font="Arial 10").place(x=150, y=10)
    Entry(arabaEkranim, textvariable=uretimYili_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=30)


    # Araç Markası Girişi
    marka_var = StringVar()
    Label(arabaEkranim, text="Araç Markası:", font="Arial 10").place(x=10, y=60)
    Entry(arabaEkranim, textvariable=marka_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=10, y=80)

    
    # Araç Model Girişi
    aracModel_var = StringVar()
    Label(arabaEkranim, text="Araç Modeli:", font="Arial 10").place(x=150, y=60)
    Entry(arabaEkranim, textvariable=aracModel_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=80)


    # Araç Yakıt Türü Girişi
    yakit_var = StringVar()
    Label(arabaEkranim, text="Araç Yakıt Türü:", font="Arial 10").place(x=10, y=110)
    ttk.Combobox(arabaEkranim, textvariable=yakit_var, values=("Dizel", "Benzin", "LPG"),
        state="readonly",
        background="white",
        font="Arial 11",
        foreground="#0A2647",
        width=13).place(x=10, y=130)


    # Araç Vites Girişi
    vites_var = StringVar()
    Label(arabaEkranim, text="Araç Vites Türü:", font="Arial 10").place(x=150, y=110)
    ttk.Combobox(arabaEkranim, textvariable=vites_var, values=("Manuel", "Otomatik"),
        state="readonly",
        background="white",
        font="Arial 11",
        foreground="#0A2647",
        width=13).place(x=150, y=130)


    # Araç Motor Gücü Girişi
    motorGucu_var = StringVar()
    Label(arabaEkranim, text="Araç Motor Gücü:", font="Arial 10").place(x=10, y=160)
    Entry(arabaEkranim, textvariable=motorGucu_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=10, y=180)


    # Araç Motor Hacmi Girişi
    motorHacmi_var = StringVar()
    Label(arabaEkranim, text="Araç Motor Hacmi:", font="Arial 10").place(x=150, y=160)
    Entry(arabaEkranim, textvariable=motorHacmi_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=180)


    # Araç Kasa Tipi Girişi
    kasaTipi_var = StringVar()
    Label(arabaEkranim, text="Araç Kasa Tipi:", font="Arial 10").place(x=10, y=210)
    Entry(arabaEkranim, textvariable=kasaTipi_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=10, y=230)


    # Araç Çekiş Girişi
    cekis_var = StringVar()
    Label(arabaEkranim, text="Araç Çekiş:", font="Arial 10").place(x=150, y=210)
    Entry(arabaEkranim, textvariable=cekis_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=230)


    # Araç Kapı Sayısı Girişi
    aracKapi_var = StringVar()
    Label(arabaEkranim, text="Araç Kapı Sayısı:", font="Arial 10").place(x=10, y=260)
    Entry(arabaEkranim, textvariable=aracKapi_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=10, y=280)


    # Araç Renk Girişi
    renk_var = StringVar()
    Label(arabaEkranim, text="Araç Rengi:", font="Arial 10").place(x=150, y=260)
    Entry(arabaEkranim, textvariable=renk_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=280)


    # Araç Motor No Girişi
    motorNo_var = StringVar()
    Label(arabaEkranim, text="Araç Motor No:", font="Arial 10").place(x=10, y=310)
    Entry(arabaEkranim, textvariable=motorNo_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=10, y=330)


    # Araç Renk Girişi
    sasiNo_var = StringVar()
    Label(arabaEkranim, text="Araç Şasi No:", font="Arial 10").place(x=150, y=310)
    Entry(arabaEkranim, textvariable=sasiNo_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=330)


    # Araç Kira Bilgisi Girişi
    kira_var = StringVar()
    Label(arabaEkranim, text="Araç Kirada Mı:", font="Arial 10").place(x=10, y=400)
    ttk.Combobox(arabaEkranim, textvariable=kira_var, values=("Kirada", "Kirada Değil"),
        state="readonly",
        background="white",
        font="Arial 11",
        foreground="#0A2647",
        width=13).place(x=10, y=420)


    # Araç Kullanım Bilgisi Girişi
    kullanim_var = StringVar()
    Label(arabaEkranim, text="Araç Kullanım Dışı Mı:", font="Arial 10").place(x=150, y=400)
    ttk.Combobox(arabaEkranim, textvariable=kullanim_var, values=("Kullanılabilir", "Kullanım Dışı"),
        state="readonly",
        background="white",
        font="Arial 11",
        foreground="#0A2647",
        width=13).place(x=150, y=420)


    # Kira Bilgisi Girişi
    kiraBedeli_var = IntVar()
    Label(arabaEkranim, text="Aracın Günlük Kira Bedeli:", font="Arial 10").place(x=10, y=450)
    Entry(arabaEkranim, textvariable=kiraBedeli_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=33).place(x=10, y=470)


    # Müşteri Kaydet Button
    Button(arabaEkranim, text="Aracı Kaydet", command=dbKaydet_Araba, 
        bg="#0A2647", 
        border="0",
        fg="white",
        height=2, 
        width=26,
        font="Arial 12 bold",
        cursor="mouse").place(x=10, y=530)


    arabaEkranim.mainloop()
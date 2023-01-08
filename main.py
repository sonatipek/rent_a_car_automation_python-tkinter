from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import mysql.connector
from dbTransaction import dbTransactions


# *! Main Window 
mainWindow = Tk()
mainWindow.title("Bergama Araç Kiralama | Ana Menü")
mainWindow.resizable("false","false")
mainWindow.configure(background="white")

# Veritabanı bağlantısı
try:
        dbIslemleri = dbTransactions("localhost", "root", "", "oto_kiralama")
        # Veritabanı silme butonu
        dbSil = Button(mainWindow, text="Veritabanını sil (önerilmez!)", command=dbIslemleri.deleteDb, 
                bg="#0A2647", 
                border="0", 
                fg="white",
                height=3, 
                width=22).grid(padx=2, pady=2, row=1, column=4)
except:
        messagebox.showinfo(title="Veritabanına Bağlanılamadı", message="Veritabanı bağlantısı kurulamadı! Program arayüzü çalışacaktır fakat işlevler yerine GETİRİLMEYECEKTİR!")

# Font Tanımlaması
myFont = ("Arial", 12, "bold")


# *!Müşteri Ekranı
def musteriEkran():
    musteriEkranim = Toplevel()
    musteriEkranim.title("Bergama Araç Kiralama | Müşteri Kayıt Ekranı")
    musteriEkranim.geometry("720x240+150+150")
    musteriEkranim.resizable("false","false")

    def dbKaydet_Musteri():
        ad = ad_var.get()
        soyad = soyad_var.get()
        tcno = tcno_var.get()
        cepno = cepno_var.get()
        dogum = dogum_var.get()
        adres = adres_var.get()
        meslek = meslek_var.get()
        ehliyet = ehliyet_var.get()
        medeni = medeni_var.get()
        egitim = egitim_var.get()
        
        dbIslemleri.setCustomer(ad=ad, soyad=soyad, tcNo=tcno, dogumTarihi=dogum, adres=adres, cepNo=cepno, meslek=meslek, ehliyetSinifi=ehliyet, medeniDurum=medeni, egitimDurum=egitim)


    # Müşteri Ad Girişi
    ad_var = StringVar()
    Label(musteriEkranim, text="Müşteri Adı:", font="Arial 10").place(x=10, y=10)
    Entry(musteriEkranim, textvariable=ad_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15
        ).place(x=10, y=30)
   

    # Müşteri Soyad Girişi
    soyad_var = StringVar()
    Label(musteriEkranim, text="Müşteri Soyadı:", font="Arial 10").place(x=150, y=10)
    Entry(musteriEkranim, textvariable=soyad_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=30)

    # Müşteri TC NO Girişi
    tcno_var = StringVar()
    Label(musteriEkranim, text="*Müşteri T.C. No:", font="Arial 10").place(x=10, y=60)
    Entry(musteriEkranim, textvariable=tcno_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=10, y=80)


    # Müşteri Cep No Girişi
    cepno_var = StringVar()
    Label(musteriEkranim, text="*Müşteri Cep No:", font="Arial 10").place(x=150, y=60)
    Entry(musteriEkranim, textvariable=cepno_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=80)


    # Müşteri Doğum Tarihi Girişi
    dogum_var = StringVar()
    Label(musteriEkranim, text="Tarih Formatı (yyyy-gg-aa) olmalıdır. Ör:2023-01-01", font="Arial 7", fg='red').place(x=10, y=110)
    Label(musteriEkranim, text="Müşteri Doğum Tarihi:", font="Arial 10").place(x=10, y=125)
    Entry(musteriEkranim, textvariable=dogum_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=32).place(x=10, y=145)

    # Müşteri Adres Girişi
    adres_var = StringVar()
    musteriAdres_label = Label(musteriEkranim, text="Müşteri Adresi:", font="Arial 10").place(x=10, y=175)
    musteri_adres = Entry(musteriEkranim, textvariable=adres_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=32).place(x=10, y=195)

    # Müşteri Meslek Girişi
    meslek_var = StringVar()
    musteriMeslek_label = Label(musteriEkranim, text="Müşteri Meslek:", font="Arial 10").place(x=350, y=10)
    musteri_meslek = Entry(musteriEkranim, textvariable=meslek_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=350, y=30)

    # Müşteri Ehliyet Bilgisi Girişi
    ehliyet_var = StringVar()
    Label(musteriEkranim, text="Müşteri Ehliyet Bilgisi:", font="Arial 10").place(x=500, y=10)
    ttk.Combobox(musteriEkranim, textvariable=ehliyet_var, values=("M", "A1", "A2", "A", "B1", "B", "C1", "C", "D1", "D", "BE", "C1E", "CE", "D1E", "DE", "F", "G"),
        state="readonly",
        background="white",
        font="Arial 11",
        foreground="#0A2647",
        width=13).place(x=500, y=30)

    # Müşteri Medeni Durum Bilgisi
    medeni_var = StringVar()
    musteriMedeni_label = Label(musteriEkranim, text="Müşteri Medeni Durum:", font="Arial 10").place(x=350, y=60)
    ttk.Combobox(musteriEkranim, textvariable=medeni_var, values=("Evli", "Bekar"),
        state="readonly",
        background="white",
        font="Arial 11",
        foreground="#0A2647",
        width=13).place(x=350, y=80)

    # Müşteri Eğitim Bilgisi
    egitim_var = StringVar()
    musteriEgitim_label = Label(musteriEkranim, text="Müşteri Eğitim Bilgisi:", font="Arial 10").place(x=500, y=60)
    musteri_egitim = Entry(musteriEkranim, textvariable=egitim_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=500, y=80)

    Label(musteriEkranim, text="*: İşaretli veriler sistemde kayıtlı olan verilerden farklı olmalıdır.").place(x=350, y=105)
    

    # Müşteri Kaydet Button
    musteriKaydet  = Button(musteriEkranim, text="Müşteriyi Kaydet", command=dbKaydet_Musteri, 
        bg="#0A2647", 
        border="0",
        fg="white",
        height=3, 
        width=20,
        font="Arial 12 bold",
        cursor="mouse").place(x=350, y=135)
    musteriEkranim.mainloop()
# *! MÜŞTERİ EKRANI BİTİŞ


# *!Araba Ekranı
def arabaEkrani():
    arabaEkranim = Toplevel()
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
    ttk.Combobox(arabaEkranim, textvariable=kasaTipi_var, values=("Sedan", "Hatchback", "Station Wagon", "Cabrio", "Puck Up", "SUV"),
        state="readonly",
        background="white",
        font="Arial 11",
        foreground="#0A2647",
        width=13).place(x=10, y=230)


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
    ttk.Combobox(arabaEkranim, textvariable=aracKapi_var, values=("1", "2", "3", "4", "5", "6"),
        state="readonly",
        background="white",
        font="Arial 11",
        foreground="#0A2647",
        width=13).place(x=10, y=280)


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
    Label(arabaEkranim, text="*Araç Motor No:", font="Arial 10").place(x=10, y=310)
    Entry(arabaEkranim, textvariable=motorNo_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=10, y=330)


    # Araç Renk Girişi
    sasiNo_var = StringVar()
    Label(arabaEkranim, text="*Araç Şasi No:", font="Arial 10").place(x=150, y=310)
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

    Label(arabaEkranim, text="*: İşaretli veriler sistemde kayıtlı olan verilerden farklı olmalıdır.").place(x=10, y=490)


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
# *! Araba Ekranı Bitiş

# *! Kiralama Ekranı
def kiralamaEkrani():
    kiralamaEkranim = Toplevel()
    kiralamaEkranim.title("Bergama Araç Kiralama | Araç Kiralama Ekranı")
    kiralamaEkranim.geometry("720x480+100+100")
    kiralamaEkranim.resizable("false", "false")

    def dbKaydet_Kiralama():
        gun = gun_var.get()
        musteri_id = musteriler_var.get()[0]
        arac_id = araclar_var.get()[0]
        yolculuk = yolculuk_var.get()
        ucret = dbIslemleri.getFee(arac_id)
        ucret = ucret[0]
    

        kiralamaUcret_var.set(f"{ucret[0] * gun} TL" )
        dbIslemleri.setRent(musteri_id, arac_id, gun, yolculuk)
        dbIslemleri.updateRent(arac_id)

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
# *! Kiralama Ekranı Bitiş


# *! Listeleme Ekranı

def ListeEkrani():
    listeEkranim = Toplevel()
    listeEkranim.title("Bergama Araç Kiralama | Kiradaki Araçları Listele")
    listeEkranim.geometry("860x720+10+20")

    Label(listeEkranim, text="Kiradaki Araçlar", font=myFont).place(x=10, y=10)


    sonuc = dbIslemleri.getRent()
    for i in range(0,len(sonuc), 1):
        kiralananArac = f"{sonuc[i][0]} {sonuc[i][1]} {sonuc[i][2]}"
        kiralananMusteri = f"{sonuc[i][3]} {sonuc[i][4]}"
        kiralananGun = sonuc[i][5]
        kiraUcreti = sonuc[i][6]

        dirY = (i+1)*65
        Label(listeEkranim, font="Arial 11", text=f"{i+1}. {kiralananArac} aracı, {kiralananMusteri} adlı müşteriye, {kiralananGun} günlüğüne kiralanmıştır.").place(x=10, y=dirY)
        Label(listeEkranim, font="Arial 11 bold", text=f"\tKira bedeli: {kiraUcreti} ₺").place(x=10, y=dirY+20)

    
    listeEkranim.mainloop()

# *! Listeleme Ekranı Bitiş


# Müşteri Ekleme Butonu ile müşteri ekleme sayfasına yönlendirme
musteriEkle = Button(mainWindow, text="Müşteri Ekle", command=musteriEkran,
        bg="#0A2647", 
        bd="0", 
        fg="white",
        height=3, 
        width=20,
        font=myFont
        ).grid(padx=2, pady=200, row=0, column=0)

# Araba Ekleme Butonu ile araba ekleme sayfasına yönlendirme
arabaEkle = Button(mainWindow, text="Araba Ekle", command=arabaEkrani,
        bg="#0A2647", 
        bd="0", 
        fg="white",
        height=3, 
        width=20,
        font=myFont).grid(padx=2, pady=200, row=0, column=1)


# Araç Kirala Butonu ile araç kiralama sayfasına yönlendirme
aracKirala  = Button(mainWindow, text="Araç Kirala", command=kiralamaEkrani, 
        bg="#0A2647", 
        border="0",
        fg="white",
        height=3, 
        width=20,
        font=myFont).grid(padx=2, pady=200, row=0, column=2)

# Araç Listeleme Butonu ile araç listeleme sayfasına yönlendirme
aracListele = Button(mainWindow, text="Kiralanan Araçları Listele", command=ListeEkrani, 
        bg="#0A2647", 
        border="0", 
        fg="white",
        height=3, 
        width=20, 
        font=myFont).grid(padx=2, pady=200, row=0, column=3)

copyrightLabel = Label(mainWindow, text="© 2022 Sonat Saygın İpek | Bergama MYO Bilgisayar Programcılığı 2.Sınıf",
        bg="white").grid(row=1, column=0)


mainWindow.mainloop()
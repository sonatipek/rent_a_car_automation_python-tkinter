from tkinter import *
from windows.dbTransaction import dbTransactions


def musteriEkran():
    dbIslemleri = dbTransactions("localhost", "root", "", "oto_kiralama")
    musteriEkranim = Tk()
    musteriEkranim.title("Bergama Araç Kiralama | Müşteri Kayıt Ekranı")
    musteriEkranim.geometry("720x240+150+150")
    musteriEkranim.resizable("false","false")

    def ButtonClicked():
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
    musteriAd_label = Label(musteriEkranim, text="Müşteri Adı:", font="Arial 10").place(x=10, y=10)
    musteri_ad = Entry(musteriEkranim, textvariable=ad_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15
        ).place(x=10, y=30)
   

    # Müşteri Soyad Girişi
    soyad_var = StringVar()
    musteriSoyad_label = Label(musteriEkranim, text="Müşteri Soyadı:", font="Arial 10").place(x=150, y=10)
    musteri_soyad = Entry(musteriEkranim, textvariable=soyad_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=30)

    # Müşteri TC NO Girişi
    tcno_var = StringVar()
    musteriTC_label = Label(musteriEkranim, text="Müşteri T.C. No:", font="Arial 10").place(x=10, y=60)
    musteri_tc = Entry(musteriEkranim, textvariable=tcno_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=10, y=80)


    # Müşteri Cep No Girişi
    cepno_var = StringVar()
    musteriCep_label = Label(musteriEkranim, text="Müşteri Cep No:", font="Arial 10").place(x=150, y=60)
    musteri_cep = Entry(musteriEkranim, textvariable=cepno_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=80)


    # Müşteri Doğum Tarihi Girişi
    dogum_var = StringVar()
    musteriDogum_label = Label(musteriEkranim, text="Müşteri Doğum Tarihi:", font="Arial 10").place(x=10, y=110)
    musteri_dogum = Entry(musteriEkranim, textvariable=dogum_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=32).place(x=10, y=130)

    # Müşteri Adres Girişi
    adres_var = StringVar()
    musteriAdres_label = Label(musteriEkranim, text="Müşteri Adres Tarihi:", font="Arial 10").place(x=10, y=160)
    musteri_adres = Entry(musteriEkranim, textvariable=adres_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=32).place(x=10, y=180)

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
    musteriEhliyet_label = Label(musteriEkranim, text="Müşteri Ehliyet Bilgisi:", font="Arial 10").place(x=500, y=10)
    musteri_ehliyet = Entry(musteriEkranim,  textvariable=ehliyet_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=500, y=30)

    # Müşteri Medeni Durum Bilgisi
    medeni_var = StringVar()
    musteriMedeni_label = Label(musteriEkranim, text="Müşteri Medeni Durum:", font="Arial 10").place(x=350, y=60)
    musteri_medeni = Entry(musteriEkranim, textvariable=medeni_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=350, y=80)

    # Müşteri Eğitim Bilgisi
    egitim_var = StringVar()
    musteriEgitim_label = Label(musteriEkranim, text="Müşteri Eğitim Bilgisi:", font="Arial 10").place(x=500, y=60)
    musteri_egitim = Entry(musteriEkranim, textvariable=egitim_var,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=500, y=80)
    

    # Müşteri Kaydet Button
    musteriKaydet  = Button(musteriEkranim, text="Müşteriyi Kaydet", command=ButtonClicked, 
        bg="#0A2647", 
        border="0",
        fg="white",
        height=3, 
        width=20,
        font="Arial 12 bold",
        cursor="mouse").place(x=350, y=135)

    musteriEkranim.mainloop()
from tkinter import *

def musteriEkran():
    musteriEkranim = Tk()
    musteriEkranim.title("Bergama Araç Kiralama | Müşteri Kayıt Ekranı")
    musteriEkranim.geometry("720x240+150+150")
    musteriEkranim.resizable("false","false")

    # Müşteri Ad Girişi
    musteriAd_label = Label(musteriEkranim, text="Müşteri Adı:", font="Arial 10").place(x=10, y=10)
    musteri_ad = Entry(musteriEkranim,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15
        ).place(x=10, y=30)
   

    # Müşteri Soyad Girişi
    musteriSoyad_label = Label(musteriEkranim, text="Müşteri Soyadı:", font="Arial 10").place(x=150, y=10)
    musteri_soyad = Entry(musteriEkranim,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=30)

    # Müşteri TC NO Girişi
    musteriTC_label = Label(musteriEkranim, text="Müşteri T.C. No:", font="Arial 10").place(x=10, y=60)
    musteri_tc = Entry(musteriEkranim,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=10, y=80)


    # Müşteri Cep No Girişi
    musteriCep_label = Label(musteriEkranim, text="Müşteri Cep No:", font="Arial 10").place(x=150, y=60)
    musteri_cep = Entry(musteriEkranim,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=150, y=80)


    # Müşteri Doğum Tarihi Girişi
    musteriDogum_label = Label(musteriEkranim, text="Müşteri Doğum Tarihi:", font="Arial 10").place(x=10, y=110)
    musteri_dogum = Entry(musteriEkranim,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=32).place(x=10, y=130)

    # Müşteri Adres Girişi
    musteriAdres_label = Label(musteriEkranim, text="Müşteri Adres Tarihi:", font="Arial 10").place(x=10, y=160)
    musteri_adres = Entry(musteriEkranim,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=32).place(x=10, y=180)

    # Müşteri Meslek Girişi
    musteriMeslek_label = Label(musteriEkranim, text="Müşteri Meslek:", font="Arial 10").place(x=350, y=10)
    musteri_meslek = Entry(musteriEkranim,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=350, y=30)

    # Müşteri Ehliyet Bilgisi Girişi
    musteriEhliyet_label = Label(musteriEkranim, text="Müşteri Ehliyet Bilgisi:", font="Arial 10").place(x=500, y=10)
    musteri_ehliyet = Entry(musteriEkranim,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=500, y=30)

    # Müşteri Medeni Durum Bilgisi
    musteriMedeni_label = Label(musteriEkranim, text="Müşteri Medeni Durum:", font="Arial 10").place(x=350, y=60)
    musteri_medeni = Entry(musteriEkranim,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=350, y=80)

    # Müşteri Eğitim Bilgisi
    musteriEgitim_label = Label(musteriEkranim, text="Müşteri Doğum Tarihi:", font="Arial 10").place(x=500, y=60)
    musteri_egitim = Entry(musteriEkranim,
        bg="white",
        font="Arial 11",
        fg="#0A2647",
        relief="flat",
        width=15).place(x=500, y=80)
    

    # Müşteri Kaydet Button
    musteriKaydet  = Button(musteriEkranim, text="Müşteriyi Kaydet", command=None, 
        bg="#0A2647", 
        border="0",
        fg="white",
        height=3, 
        width=20,
        font="Arial 12 bold",
        cursor="mouse").place(x=350, y=135)
    musteriEkranim.mainloop()
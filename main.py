from tkinter import *
from tkinter import messagebox

# Windows
from windows.musteriEkran import musteriEkran
from windows.arabaEkran import arabaEkrani
from windows.kiralamaEkran import kiralamaEkrani
from windows.listeEkran import ListeEkrani

# Veritabanı işlemlerinin dahil edilmesi
from windows.dbTransaction import dbTransactions

mainWindow = Tk()
mainWindow.title("Bergama Araç Kiralama | Ana Menü")
mainWindow.resizable("false","false")
mainWindow.configure(background="white")

# Veritabanı bağlantısı
try:
        db1 = dbTransactions("localhost", "root", "", "oto_kiralama")
        # Veritabanı silme butonu
        dbSil = Button(mainWindow, text="Veritabanını sil (önerilmez!)", command=db1.deleteDb, 
                bg="#0A2647", 
                border="0", 
                fg="white",
                height=3, 
                width=22).grid(padx=2, pady=2, row=1, column=4)
except:
        messagebox.showinfo(title="Veritabanına Bağlanılamadı", message="Veritabanı bağlantısı kurulamadı! Program arayüzü çalışacaktır fakat işlevler yerine getirilmeyecektir.")


# Font Tanımlaması
myFont = ("Arial", 12, "bold")

# Müşteri Ekleme Butonu ile müşteri ekleme sayfasına yönlendirme
musteriEkle = Button(mainWindow, text="Müşteri Ekle", command=musteriEkran,
        bg="#0A2647", 
        bd="0", 
        fg="white",
        height=3, 
        width=20,
        font=myFont).grid(padx=2, pady=200, row=0, column=0)

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

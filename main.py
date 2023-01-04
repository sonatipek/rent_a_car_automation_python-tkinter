from tkinter import *
from tkinter import messagebox

# Windows
from windows.musteriEkran import musteriEkran
from windows.arabaEkran import arabaEkrani
from windows.kiralamaEkran import kiralamaEkrani
from windows.listeEkran import ListeEkrani

# Veritabanı işlemlerinin dahil edilmesi
from dbTransaction import dbTransactions

mainWindow = Tk()
mainWindow.title("Bergama Araç Kiralama | Ana Menü")
mainWindow.resizable("false","false")
mainWindow.configure(background="white")

# Font Tanımlaması
myFont = ("Arial", 12, "bold")

# Müşteri Ekleme Butonu ile müşteri ekleme sayfasına yönlendirme
musteriEkle = Button(mainWindow, text="Müşteri Ekle", command=musteriEkran,
        bg="#0A2647", 
        bd="0", 
        fg="white",
        height=3, 
        width=20,
        font=myFont).grid(padx=2, pady=200, row=0, column=4)

# Araba Ekleme Butonu ile araba ekleme sayfasına yönlendirme
arabaEkle = Button(mainWindow, text="Araba Ekle", command=arabaEkrani,
        bg="#0A2647", 
        border="0", 
        fg="white",
        height=3, 
        width=20,
        font=myFont).grid(padx=2, pady=200, row=0, column=3)

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
        font=myFont).grid(padx=2, pady=200, row=0, column=1)

# Veritabanı bağlantısı
db1 = dbTransactions("localhost", "root", "", "oto_kiralama")

mainWindow.mainloop()

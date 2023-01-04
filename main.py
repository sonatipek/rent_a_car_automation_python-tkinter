from tkinter import *
from tkinter import messagebox

# Windows
from windows.musteriEkran import musteriEkran
from windows.arabaEkran import arabaEkrani
from windows.kiralamaEkran import kiralamaEkrani
from windows.listeEkran import ListeEkrani

mainWindow = Tk()
mainWindow.title("Bergama Araç Kiralama | Ana Menü")
mainWindow.geometry("720x480+25+25")
mainWindow.configure(background="white")

# Font Tanımlaması
myFont = ("Arial", 12, "bold")

# !TODO: Veritabanı bağlantısı kurulduğunda başarılı mı değil mi kontrol et. Başarılıysa bunu göster.
# messagebox.showinfo(title="Veritabanı Bilgisi", message="Veritabanı bağlantısı kuruldu! İşlemlerinize başarıyla devam edebilirsiniz.")
# !TODO: Başarılı değilse bunu göster.
# messagebox.showerror("Veritabanı Bağlantısında Hata", "Veritabanı bağlantısı kurulamadı! Lütfen tekrar deneyin.")



# Müşteri Ekleme Butonu ile müşteri ekleme sayfasına yönlendirme
musteriEkle = Button(mainWindow, text="Müşteri Ekle", command=musteriEkran,
        bg="#0A2647", 
        bd="0", 
        fg="white",
        height=3, 
        width=20, 
        padx=2, 
        pady=3,
        font=myFont).grid(padx=2, pady=3)

# Araba Ekleme Butonu ile araba ekleme sayfasına yönlendirme
arabaEkle = Button(mainWindow, text="Araba Ekle", command=arabaEkrani,
        bg="#0A2647", 
        border="0", 
        fg="white",
        height=3, 
        width=20, 
        padx=2, 
        pady=3, 
        font=myFont).grid(padx=2, pady=3)

# Araç Kirala Butonu ile araç kiralama sayfasına yönlendirme
aracKirala  = Button(mainWindow, text="Araç Kirala", command=kiralamaEkrani, 
        bg="#0A2647", 
        border="0",
        fg="white",
        height=3, 
        width=20,
        padx=2, 
        pady=3, 
        font=myFont).grid(padx=2, pady=3)

# Araç Listeleme Butonu ile araç listeleme sayfasına yönlendirme
aracListele = Button(mainWindow, text="Kiralanan Araçları Listele", command=ListeEkrani, 
        bg="#0A2647", 
        border="0", 
        fg="white",
        height=3, 
        width=20, 
        font=myFont).grid(padx=2, pady=3)


mainWindow.mainloop()

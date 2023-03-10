import mysql.connector
from tkinter import *
from tkinter import messagebox

class dbTransactions:
    mydb=""
    hostname=""
    username=""
    mypassword=""

    def __init__(self, hostname, username, mypassword, dbName):
        self.hostname= hostname
        self.username= username
        self.mypassword= mypassword
        self.mydb = dbName
        self.baglanti = None

        self.dbCon()
        self.createTables()

    # MySQL'e bağlanıp, veritabanı oluşturmak
    def dbCon(self):
        try:
            db = mysql.connector.connect(host=self.hostname, user=self.username, password=self.mypassword)
            mycursor = db.cursor()

            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.mydb}")

            # İşlem başarılı bildirimi
            messagebox.showinfo(title="Veritabanı Bilgisi", message="Veritabanı bağlantısı kuruldu! İşlemlerinize devam edebilirsiniz.")

            return db

        except:
            # İşlem başarısız bildirimleri
            messagebox.showerror("Veritabanı Bağlantısında Hata", "Bir hata oluştu! XAMPP gibi uygulamalardan mysql'i başlattığınızdan emin olup programı tekrar çalıştırın. Aksi taktirde program düzgün çalışmayacaktır.")

            print("Bir hata oluştu! XAMPP gibi uygulamalardan mysql'i başlattığınızdan emin olup programı tekrar çalıştırın")

    # MySQL'de oluşturulan veritabanına bağlanıp, gerekli tabloları oluşturmak
    def createTables(self):
        db = mysql.connector.connect(host=self.hostname, user=self.username, password=self.mypassword, database=self.mydb)
        mycursor = db.cursor()
        self.baglanti = db

        # Müşteri Tablosu
        mycursor.execute("CREATE TABLE IF NOT EXISTS musteriler ( musteri_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ad VARCHAR(30) NOT NULL, soyad VARCHAR(30) NOT NULL, tc_no VARCHAR(11) NOT NULL UNIQUE, dogum_tarihi DATE NOT NULL, adres VARCHAR(255) NOT NULL, cep_no VARCHAR(11) NOT NULL UNIQUE, meslek VARCHAR(50) NOT NULL, ehliyet_sinifi VARCHAR(3) NOT NULL, medeni_durum VARCHAR(50) NOT NULL, egitim_durum VARCHAR(50) NOT NULL)")

        # Araç Tablosu
        mycursor.execute("CREATE TABLE IF NOT EXISTS araclar (arac_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, arac_tur VARCHAR(50) NOT NULL, arac_marka VARCHAR(50) NOT NULL, arac_model VARCHAR(50) NOT NULL, arac_uretim_yili YEAR NOT NULL, arac_yakit_tur VARCHAR(30) NOT NULL, arac_vites VARCHAR(10) NOT NULL, arac_motor_gucu VARCHAR(20) NOT NULL, arac_kasa_tip VARCHAR(20) NOT NULL, arac_motor_hacim VARCHAR(50) NOT NULL, arac_cekis VARCHAR(20) NOT NULL, arac_kapi VARCHAR(15) NOT NULL, arac_renk VARCHAR(50) NOT NULL, arac_motor_no VARCHAR(11) NOT NULL UNIQUE, arac_sasi_no VARCHAR(11) NOT NULL UNIQUE, arac_kiralama_bedeli_gunluk SMALLINT NOT NULL, arac_kira_durumu VARCHAR(15) NOT NULL, arac_kullanim_durumu VARCHAR(15) NOT NULL)")

        # Kiralama Tablosu
        mycursor.execute("CREATE TABLE IF NOT EXISTS kiralama_bilgileri (kiralama_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, musteri_id INT NOT NULL, arac_id INT NOT NULL, kiralama_gun SMALLINT NOT NULL, kiralama_hedef VARCHAR(50) NOT NULL, CONSTRAINT `FK__musteriler` FOREIGN KEY (`musteri_id`) REFERENCES `musteriler` (`musteri_id`) ON UPDATE NO ACTION ON DELETE NO ACTION, CONSTRAINT `FK__araclar` FOREIGN KEY (`arac_id`) REFERENCES `araclar` (`arac_id`) ON UPDATE NO ACTION ON DELETE NO ACTION)")


    def setCustomer(self, ad, soyad, tcNo, dogumTarihi, adres, cepNo, meslek, ehliyetSinifi, medeniDurum, egitimDurum):
        mycursor = self.baglanti.cursor()

        mycursor.execute(f"INSERT INTO musteriler (ad, soyad, tc_no, dogum_tarihi, adres, cep_no, meslek, ehliyet_sinifi, medeni_durum, egitim_durum) VALUES('{ad}','{soyad}','{tcNo}','{dogumTarihi}','{adres}','{cepNo}','{meslek}','{ehliyetSinifi}','{medeniDurum}','{egitimDurum}')")

        self.baglanti.commit()

    def getCustomers(self):
        mycursor = self.baglanti.cursor()


        mycursor.execute("SELECT musteri_id, ad, soyad FROM musteriler")
        sonuc = mycursor.fetchall()
        
        return sonuc

    def setCar(self, aracTur, aracMarka, aracModel, aracUretimYili, aracYakitTur, aracVites, aracMotorGucu, aracKasaTip, aracMotorHacim, aracCekis, aracKapi, aracRenk, aracMotorNo, aracSasiNo, aracKiralamaBedeliGunluk, aracKiraDurumu, aracKullanimDurumu):
        mycursor = self.baglanti.cursor()

        mycursor.execute(f"INSERT INTO araclar(arac_tur, arac_marka, arac_model, arac_uretim_yili, arac_yakit_tur, arac_vites, arac_motor_gucu, arac_kasa_tip, arac_motor_hacim, arac_cekis, arac_kapi, arac_renk, arac_motor_no, arac_sasi_no,arac_kiralama_bedeli_gunluk, arac_kira_durumu, arac_kullanim_durumu) VALUES('{aracTur}','{aracMarka}','{aracModel}','{aracUretimYili}','{aracYakitTur}','{aracVites}','{aracMotorGucu}','{aracKasaTip}','{aracMotorHacim}', '{aracCekis}','{aracKapi}','{aracRenk}', '{aracMotorNo}', '{aracSasiNo}', '{aracKiralamaBedeliGunluk}', '{aracKiraDurumu}', '{aracKullanimDurumu}')")

        self.baglanti.commit()

    def getCars(self):
        mycursor = self.baglanti.cursor()
        mycursor.execute("SELECT arac_id, arac_marka, arac_model, arac_uretim_yili FROM araclar  WHERE arac_kira_durumu = 'Kirada Değil' AND arac_kullanim_durumu = 'Kullanılabilir'")

        sonuc = mycursor.fetchall()
        
        return sonuc

    def getFee(self, aracID):
        mycursor = self.baglanti.cursor()
        mycursor.execute(f"SELECT arac_kiralama_bedeli_gunluk FROM araclar WHERE arac_id = '{aracID}'")

        sonuc = mycursor.fetchall()
        
        return sonuc

    def setRent(self, musteriID, aracID, kiralamaGun, kiralamaHedef):
        mycursor = self.baglanti.cursor()

        mycursor.execute(f"INSERT INTO kiralama_bilgileri(musteri_id, arac_id, kiralama_gun, kiralama_hedef) VALUES('{musteriID}', '{aracID}', '{kiralamaGun}', '{kiralamaHedef}')")

        self.baglanti.commit()

    def getRent(self):
        mycursor = self.baglanti.cursor()
        mycursor.execute("SELECT a.arac_marka, a.arac_model, a.arac_uretim_yili, m.ad, m.soyad, k.kiralama_gun, k.kiralama_gun * a.arac_kiralama_bedeli_gunluk FROM musteriler m INNER JOIN kiralama_bilgileri k ON m.musteri_id=k.musteri_id INNER JOIN araclar a ON k.arac_id=a.arac_id")

        sonuc = mycursor.fetchall()
        
        return sonuc

    def updateRent(self, aracID):
        mycursor = self.baglanti.cursor()
        mycursor.execute(f"UPDATE araclar SET arac_kira_durumu = 'Kirada' WHERE arac_id =  '{aracID}'")

        self.baglanti.commit()


    def deleteDb(self):
        mycursor = self.baglanti.cursor()

        mycursor.execute(f"DROP DATABASE {self.mydb}")

        self.baglanti.commit()

    def getSearch(self, value):
        mycursor = self.baglanti.cursor()
        mycursor.execute(f"SELECT ad, ehliyet_sinifi FROM musteriler WHERE ad LIKE '{value}%'")

        sonuc = mycursor.fetchall()
        
        return sonuc

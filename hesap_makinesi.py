"""Hesap Makinesi"""
import math

def hesapla(sayi1, sayi2, islem):
    if (islem == 1):
        return sayi1 + sayi2
    if(islem == 2):
        return sayi1 - sayi2
    if(islem == 3):
        return sayi1 * sayi2
    if(islem == 4):
        if sayi2 == 0:
            return "Hata: Sıfıra bölme yapılamaz."
        return sayi1 / sayi2
    if(islem == 5):
        return sayi1 ** sayi2
    if(islem == 6):
        if sayi1 < 0:
            return "Hata: Negatif sayının karekökü alınamaz."
        return math.sqrt(sayi1)

while True:
    try: 
        sayi1 = int(input("Lütfen İlk Sayıyı Girin: "))

        print("İşlemler:")
        print("1.Toplama")
        print("2.Çıkarma")
        print("3.Çarpma")
        print("4.Bölme")
        print("5.Üs Alma")
        print("6.Karekök")
        islem = int(input("Lütfen İşlem Seçin (1-6 arasında):"))

        if(islem <= 5): sayi2 = int(input("Lütfen 2. sayıyı girin:"))
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin.")
    
    if (islem >= 1) and (islem <= 5):
        sonuc = hesapla(sayi1, sayi2, islem)
        print(sayi1, "ile", sayi2, "islem no: ", islem, "sonuc: ", sonuc )
    if(islem == 6):
        sonuc = hesapla(sayi1, None, islem)
        print(sayi1, "işlem no: ", islem, "sonuc: ", sonuc )    
    else:
        print("Girdiğiniz işlem numarsı 1-6 arasında olmalı")
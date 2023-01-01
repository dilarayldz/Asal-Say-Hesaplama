print("""
Asal Sayı Bulma Programı
(Çıkmak için 'q' tuşuna basınız.)
""")

def asal_mı(deger):
    for i in range (2,sayi):
        if (sayi%i == 0):
            return False
        return True

while True:
    sayi = input ("Sayıyı Giriniz: ")
    if (sayi == "q"):
        print ("Program kapatıldı.")
        break
    
    else:
        sayi = int(sayi)
        if (sayi == 1):
            print (sayi, "Asal değildir.")
        
        elif (sayi == 2):
            print (sayi, "asal değildir.")
        
        else:
            sonuc = asal_mı(sayi)

            if (sonuc == True):
                print(sayi, "Asaldır.")
            
            else:
                print (sayi, "Asal değildir.")


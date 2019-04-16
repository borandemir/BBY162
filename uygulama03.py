_author_ = "Boran Demir"
print("******Asalım Bakalım Adamları******")

isim=input("Gir ismini biraderim: ")
print("Hoşgeldin oyuna", isim)
print("Bu Oyunda bitki isimlerini bulmaya çalışıcaksın", isim)
import random

Kelimeler= random.choice(["PATLICAN", "KIZILCIK", "KORUNGA", "KETEN", "KEKİK", "DEREOTU", "KİRAZ", "MARUL", "HARDAL",
                           "BİBERİYE", "KARANFİL", "MANOLYA", "KARNIBAHAR", "NOHUT", "SÜMBÜL", "FULYA", "BERGAMOT",
                           "KABAK", "HANIMELİ"])

Kelimeler = Kelimeler.upper()

ToplamCan = 5

Kelimehavuzu = []

harfSayisi = "_"


for word in Kelimeler:

    Kelimehavuzu.append(harfSayisi)


print(Kelimehavuzu)

while ToplamCan > 0:

    i = 0

    tahmin = input("\ngir harfini biraderim: ")
    tahmin = tahmin.upper()



    if tahmin in Kelimeler:
        for kontrol in Kelimeler:
            if Kelimeler[i] == tahmin:
                Kelimehavuzu[i] = tahmin
            i += 1


        print("")
        print(Kelimehavuzu)
        print("\n \"%s\" harfi " %tahmin)


    else:
        ToplamCan -= 1
        print("")
        print(Kelimehavuzu)
        print("\n\"%s\" yanlış harf biraderim, başka bi tane dene" % tahmin)
        print(ToplamCan, "Canın kaldı",isim)


    if ToplamCan == 0:
        print("Bilemedin!", isim)
        break



    if harfSayisi not in Kelimehavuzu:
        print("\nHelal olsun doğru cevap", isim)
        break

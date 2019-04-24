_author_ = "Boran Demir"

#1.soru
metin="Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin[0:20])

#2.soru

liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for i in liste:
    print(i)

#3. soru
sözlük =  {"Elma" :"Ağaçta yetişen bir tür meyve",
            "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze"}
meyve = input("merak ettiğin meyvenin adını gir: ")
meyve=meyve.capitalize()
if meyve in sözlük:
    cevap = "{} isimli meyvenin anlamı: {}"
    print(cevap.format(meyve,sözlük[meyve]))
else:
    print("aradığın meyve yok!")

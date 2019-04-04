_author_ ="Boran Demir"
print("*****Merhabalar efendim çizgi roman bilginizi sınamak isterseniz bu sınav tam olarak size göre****")
print("Sınavı başlatın ve Aşağıda bulunan soruları cevaplayınız")
print("---------------------------------------------------------------------------------------------------")

sorular = ['Marvel evreninde kafası kesilse dahi ölmeyen karakter kimdir?',
           'Thanosun eldiveninde toplam kaç adet sonsuzluk taşı bulunmaktadır',
           'Kaptan amerikanın baş düşmanı kimdir ?',
           'Batman\'ın gerçek ismi nedir ?',
           'Kaptan Amerika\'nın kalkanı hangi maddeden yapılmıştır ?']
cevaplar = ['B','D','A','C','B']
cevapA = ['Iron Man', '4', 'Red Skull', 'Martin', 'Çelik']
cevapB = ['Deadpool', '1', 'Wolverine', 'james', 'Vibranium']
cevapC = ['Venom', '8', 'Spiderman', 'Bruce', 'Krom']
cevapD = ['Daredevil', '6', 'Punisher', 'logan', 'aliminyum']

puan = 0
for i in range(len(sorular)):
    print("Soru" + str(i+1)+":"+sorular[i])
    print("A.) " + cevapA[i])
    print("B.) " + cevapB[i])
    print("C.) " + cevapC[i])
    print("D.) " + cevapD[i])
    cevap = input("GİR CEVABINI BİRADERİM: ")
    if cevaplar[i] == cevap.upper():
        puan +=1
print("SINAVI BİTİRMİŞ BULUNMAKTASIN")
print("ALDIĞIN NOT BUDUR KARDEŞİM:" +str(int((puan/len(sorular))*100)))
input()

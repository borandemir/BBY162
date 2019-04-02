_author_ =  "Boran Demir"
print("*** Tarih bilginizi sorgulamaya hazır mısınız? ***")
print("Aşağıda size sunulan sorulara doğru cevapları vermeye çalışınız ve kendinizi teste tabi tutunuz")
print("--------------------------------------------------------------------------------------------------")
sorular = ['Almanya ikinci dünya savaşından galip ayrılmıştır [D/Y]',\
           'Çin seddi hun akınlara karşı yapılmıştır [D/Y]',\
           'Çanakkale savaşı sırasında mayın döşeyen gemimizin adı nurhandır [D/Y]',\
           'kraliçe mary protestandır [D/Y]',\
           'Preveze deniz savaşı haçlılar tarafından kazanılmamıştır [D/Y]']
cevaplar = ['Y','D','Y','Y','D']
puan = 0
#soru 1
cevap = input((sorular[0]))
if cevaplar[0] == cevap.upper():
    print("helal olsun doğru yaptın!")
    puan += 1
else:
    print("cevabınız doğru değil biraderim!")
#soru2
cevap = input((sorular[1]))
if cevaplar[1] == cevap.upper():
    print("helal olsun doğru yaptın!")
    puan += 1
else:
    print("cevabınız doğru değil biraderim!")
    puan += 1
#soru 3
cevap = input((sorular[2]))
if cevaplar[2] == cevap.upper():
    print("helal olsun doğru yaptın!")
    puan += 1
else:
    print("cevabınız doğru değil biraderim!")
# soru 4
cevap = input((sorular[3]))
if cevaplar[3] == cevap.upper():
    print("helal olsun doğru yaptın!")
    puan += 1
else:
     print("cevabınız doğru değil biraderim!")
#soru 5
cevap = input((sorular[4]))
if cevaplar[4] == cevap.upper():
    print("helal olsun doğru yaptın!")
    puan += 1
else:
    print("cevabınız doğru değil biraderim!")
#Test Sonu
print("Sınav bitmiştir, aldığınız not: "+str(puan*20))

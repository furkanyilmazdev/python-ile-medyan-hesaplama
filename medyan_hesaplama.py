# medyan hesaplama uygulamasi

liste_uzunlugu = int(input("liste uzunlugu icin bir sayi giriniz"))
liste = []
for i in range(0,liste_uzunlugu):
    girdi = int(input("liste elemanlarini giriniz : "))
    liste.append(girdi)
if len(liste) % 2 == 0:  
    liste.sort()
    medyan = liste[int(len(liste)/2)]+liste[int((len(liste)/2)-1)]
    print(medyan/2)
else:
    liste.sort()
    medyan = liste[int(len(liste)/2)]
    print(medyan)

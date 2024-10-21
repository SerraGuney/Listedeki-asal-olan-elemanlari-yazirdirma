#region Kullanıcıdan 2 sayı alarak,
# bu sayılar arasından rastgele istenen değerde sayi seçerek bunları diziye atayan
# ve bu dizideki asal sayıları yazdıran program.
import random
liste=[]#iki sayı arasından rastgele elamanları tutan liste.
liste2=[]#liste de bulunan asal sayıları tutan liste.
sayi1=int(input("bir sayi giriniz:"))
sayi2=int(input("bir sayi giriniz:"))
deger=int(input("kac deger seçeceksiniz:"))
if sayi1<sayi2:
    kucuksayi=sayi1+1
    buyuksayi=sayi2-1
else:
    kucuksayi=sayi2+1
    buyuksayi=sayi1-1
if (buyuksayi+1)-(kucuksayi-1)>1:#iki değer arasında sayı olmasını değerlendiriyor.
    for k in range(deger):
        sayi=random.randint(kucuksayi,buyuksayi)
        liste.append(sayi)
    print("liste",liste)
    for a in range(deger):
        asal = True
        if liste[a]==1:
            continue
        elif liste[a]==2:
            liste2.append(liste[a])
        else:
             for j in range(2,liste[a]):
                if liste[a]%j==0:
                    asal=False#asal sayı false olmuşsa asal olmadığı anlamına gelir
             if  asal==True:#hala asal ise liste2'ye ekler.
                 if liste[a] not in liste2:#aynı elemanı listeye tekrar eklememeyi sağlıyor.
                    liste2.append(liste[a])
    print("asal sayılardan oluşan liste",liste2)
else:
    print("iki deger arasinda asal sayi yok")
#endregion


#region Kullanıcıdan 2 sayı alarak,
# bu sayılar arasından rastgele istenen değerde sayi seçerek bunları diziye atayan
# bu sayıların asal olup olmadığını kontrol eden bir program yazın.
# Eğer sayı asal ise "Asaldır", değilse "Asal değildir" mesajı verin.
# import random
# liste=[]
# liste2=[]
# sayi1=int(input("bir sayi giriniz:"))
# sayi2=int(input("bir sayi giriniz:"))
# deger=int(input("kac deger seçeceksiniz:"))
# if sayi1<sayi2:
#     kucuksayi=sayi1+1
#     buyuksayi=sayi2-1
# else:
#     kucuksayi=sayi2+1
#     buyuksayi=sayi1-1
# if (buyuksayi+1)-(kucuksayi-1)>1:
#     for k in range(deger):
#         sayi=random.randint(kucuksayi,buyuksayi)
#         liste.append(sayi)
#     print("liste",liste)
#     for a in range(deger):
#         asal = True
#         if liste[a]==1:
#             continue
#         elif liste[a]==2:
#             liste2.append(liste[a])
#         else:
#              for j in range(2,liste[a]):
#                 if liste[a]%j==0:
#                     asal=False
#              if  asal==True:
#                 liste2.append(liste[a])
#     print("asal sayılardan oluşan liste",liste2)
#endregion
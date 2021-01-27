

# değişkenler arası değer ataması
# a=3
# b=5
# a,b= b,a
# print(a)

# bir değişkene bir sayı eklemenin kısa yolu
# a=5
# a+=1
# a*=2
# print(a)

# operatörler
# // tam sayı bölmesi yapar
# print(4//3)
# % kalanı bulma operatörü
# print(5%3)
# ** üs almaya yarar
# print(2**6)
# print(8**(1/3))
# a=-4
# print(-a)

# \ ters slaş kaçış dizisi
# print("rıdvanın\"n dswd")

# indeks hesabı
# a="rıdvan"
# print(a[2])
# print(a[-1])

# string parçalama
# a="rıdvandikmen"
# print(a[4:9]) #4 ve 9 indeks arasındaki karakterleri alır (9 dahil değil)
# print(a[:9]) # 0.indeksden seçilen indekse kadar alır
# print(a[2:-3])
# print(a[::2]) # [ilk indeks:ikinci indeks:kaç atlayarak yazacağı alan]
# print(a[::-2])
# print(a[1:10:2])

# string özellikleri
#a="rıdvandikmen "
# b="niğde "
# c="ankara"
# print(len(a)) #string karakter sayısı bulma
# print(a+b+c) # stringler bu şekilde yan yana eklenebilir
# print(a*3) #string bu şekilde tekrarlanabilir
# d= a + "ankara" # bu şekilde stringler değişiklik yapılabilir !!! önemli mülakatlarda sorulu
# print(d)
# a= a + "1544"
# print(a)

# veri tipi dönüşümleri
# a=45
# print(float(a)) # tam sayıyı ondalıklı sayıya çevirme
# print(float(-13))
# print(str(a))
# print(len(str(a)))# 45 sayısını stringe dönüştürdü uzunluk olarak her bir sayıyı bir karakter olarak aldı
# print(len(str(3.45)))
# b="456465465"
# print(b)
# print(int(b))
# c=12.45445
# print(float(c))

# print(12,"asd\tasd",6556,"na\ndsa")#virgül ayırır \n alt satıra yazdırır \t tab kadar boşluk bırakır
# type verinin türünü söyler
# print(type(45))
# print(type(45.45))
# print(type("dfsfd"))

# a=454484
# b= "sadasda"
# c = 98.98
# d=78
# print(a,b,c,sep="rıdvan")#sep parametresi yazılan değerler arasında boşluk bırakmak yerine kullanırlır
# print(a,b,c,sep="\t")
# print(*b) #* işareti string değerlerde arasına boşluk koyar
# print(*b,sep="8")
# print("{} {} {}".format(a,d,a+d))# bu format metodu çok fazla kullanım alanı var http://pyformat.info/
# print("{2} {1} {0}".format("dfgdfg",58,"52514511"))

#listeler/diziler
#listelerde stringlerdeki gibi parçalama işlemi yapılabilir
# liste=["a",96,"b",3.54] #lisete oluşturma yöntemi
# liste1= list()#lisete oluşturma yöntemi
# liste2=list("rıdvan")
# print(len(liste))
# print(liste2)
# print(liste2[4])#listede indeks bulunabilir
# print(liste2[len(liste2)-1])
# print(liste2[::-1])
# liste3=liste+liste2
# print(liste3)
# print(liste2*5)
# liste4=[1,2,3,4,5,6,4,5,5,5,]
# liste4[5]=100 # listelerde stringlerin aksine eleman değişikliği yapılır
# liste4[:2]=[99.98]
# print(liste4)
# a=[52,48,100,4,12]
# a.append(0)# append listeye ekleme yapar
# print(a)
# a.pop(2)#pop metodu listeden atma işlemi yapar () içine girdiğimiz indeksi atar
# print(a)
# a.sort()#indeksleri sıralar
# print(a)
# a.sort(reverse=True)#tersden sıralamayı sağlar
# print(a)
# b=[[1,2],[1],[7,8]]#iç içe listeler

# Demetler/Tuple
#Demetlerle diziler arasındaki fark değiştirilemez oluşu
# demet= (1,2,3,4,5,6,7,8,9)
# print(type(demet))
# print(demet[-3])
# print(demet[::-1])#listedeki gibi parçalama özelliklerini içerir burda ters çeviriyoruz
# demet2=(1,1,1,1,2,5,8,9,6,3)
# print(demet2.count(1))# Count metodu demetin içinde bir değerin kaç tane geçtiğini hesaplar
# demet3=("rd","ed","as")
# print(demet3.index("rd"))# indeks metodu demetin içindeki verinin kaçıncı indeks olduğuna bakar
# demet3[2]=5 # demetlerde elamanlar listelerdeki gibi değişmez
# print(demet3)

#sözlük oluşturma
# sözlük={"bir":1,"iki":2,"üç":3}  #sözlük oluşturma
# print(type(sözlük))
# print(sözlük["bir"])
# sözlük["rıdvan"]="rd" # sözlüğe eleman ekleme
# print(sözlük)
# sözlük["bir"]=8 #sözlükde deper değiştirme
# print(sözlük)
# # sözlükde fonksiyonlar
# print(sözlük.keys())#sözlükdeki anahtar değerleri verir
# print(sözlük.values())#sözlükdeki değerleri verir
# print(sözlük.items())#verileri ayrı ayrı gösterir

# kullanıcıdan girdi alma
# a=input("bir sayı giriniz")#kullanıcıdan veri alır eğer türünü belirlemezsek string alır
# print(a)
# b = int(input("bir sayı giriniz")) #girdiyi integer sayıya çevirdik
# print(b)

# mantıksal değerler
# Mantıksal değerler boolean olarak isimlendirilir ve 0 dışındaki bütün değerler True dur
# a= True
# print(type(a))
# b=False
# print(type(b))

# None
# none bir değişken oluşturup ama içine daha sonra değer atıcaksak eğer none yazılabilir
# a=None
# print(a)

#karşılaştırma operatörleri
# == iki değer birbirine eşitmi eşitse true verir
# != değerler eşit değilmiyi kontrol eder eşit değilse true verir
# <  soldaki sayı sağdakinden küçükmü ona bakar
# > soldaki sayı sağdakinden büyük mü ona bakar
# <= soldaki sayı sağdakinden küçük eşitmi diye kontrol eder
# >= soldaki sayı sağdakinden büyük eşitmi diye konttrom eder
# print("rıd"=="rıd")
# print(2==3)
# print("rıd"!="rıd")
# print("rıd"!="rd")
# print(1<2)
# print(5<2)
# print("araba">"bebek")#a harfi önce geldiği için küçük sayılıyo
# print(1>2)
# print(10>5)
# print(10<=5)
# print(5<=10)
# print(40>=30)
# print(30>=40)

#Mantıksal bağlaçlar
# and iki işlemdede doğruluk aranır
# print(1<2 and "rıdvan">"dikmen")
# or herhangi bir işlemin sonucu true olsa yeter
# print(10<2 or "rıdvan">"dikmen")
# not not operatörü bi işlemin sonucu true ise false false ise true yapıyor
# print(not 1<2)

# koşullu durumlar
# if ler yukardaki durumu kontrol etmez bu yüzden elif kullanılır
# vize=int(input("vize notunuzu giriniz"))
# final=int(input("final notunuzu giriniz"))
# sınıfort=float(input("sınıf ortalamasını giriniz"))
# ortalama =(vize*40)/100+(final*60)/100
# print(ortalama)
# if ortalama>=60:
#     print("dersi geçtiniz")
# elif (ortalama-sınıfort)==10:
#     print("dersi geçtiniz")
# else:
#     print("dersden kaldınız")

#döngüler
# in operatörü bir elemanın başka bir listede demette yada string de olup olmadığını kontrol eder
# liste=[1,2,3,4,5]
# print(5 in liste)
# print(not "asd" in liste)
# print("d"in "rıdvan")

# for listelerin demetlerin stringlerin yada sözlüklerin üzerinde dolaşmayı sağlayan döndü türüdür
# liste=[1,2,3,4,5,6]
# for i in liste:
#     if i%2==0:
#         print(i)

# rd="rıdvandikmen"
# for i in rd:
#     print(i*6)

# liste=[(1,2),(3,4),(5,6)]
# for i,j in liste: # Bu şekilde listelerin içindeki demetlere de ulaşabildik
#     print(i,j)

# sözlük={"bir":1,"iki":2,"üç":3}
# for i in sözlük.keys():
#     print(i)

# sözlük={"bir":1,"iki":2,"üç":3}
# for i,j in sözlük.items():
#     print(i,j)

# toplam=0
# liste=[7,8,9,4,5,6]
# for i in liste:
#     toplam=toplam+i
#     print(toplam) # burda yazdırırsak her adımda yazdırırı
# print(toplam) # burada yazdırırsak son sonucu verir

#while döngüsü
# while döngüsü koşul sağlandığı sürece devam eder
# while döngüsünde koşullar sıralı sağlanır
# i=0
# while(i<10):
#     i+=1# ilk işlem i yi bir arttırmak olduğu için ilk ekrana 1 yazdırılıyor i 9 olduğunda 1 ekleyip yazdırdı
#     print(i)
#
# i=0
# while(i<10):
#     print(i)# ilk işlem i yi yazdırmak olduğu için 0 dan başlayıp 9 da bitti.
#     i+=1

# liste=[1,2,3,4,5,6]
# indeks=0
# while(indeks < len(liste)):
#     print(liste[indeks])
#     indeks+=1 #indeksi arttırmazsak eğer sonsuz döngüye girer

#Sonsuz döngü while döngüsünün koşulu sonsuza kadar true olursa sonsuz döngü olur
# i=10
# while(i<20):
#     print(i)

# döngülerde kullanılan range() fonksiyonu
# listelere benzeyen bir sayı dizisi oluşturu range(1,10) 10 dahil değil

# print(*range(0,10,2))# * olmadan çalışmaz

# liste=list(range(0,10)) # liste oluşturmanın kolay yolu
# print(liste)

# print(*range(10,0,-1))# geri saydırmak istersek yazım şekli

# for i in range(0,10):
#     print(i*"*")

# break continue
# breakda döngüde break görüldüğü yerde döngü durdurulur. İçinde bulunuğu döngüde işe yarar

# i=0
# while(i<10):
#     if i==5:
#         break
#     print(i)
#     i += 1

# for i in range(10):
#     if i==7:
#         break
#     print(i)

# while True: # döngü true olduğu sürece döngü devam eder
#     isim=input("isminizi giriniz çıkış için * a basın")
#     if isim=="*":
#         break
#     print(isim)

# bunu yeniden yap!!!!!!!!!!!!!!!!!!!!!!!!!
# isim = input("isminizi giriniz çıkış için * a basın")
# liste = [isim]
# for i in liste:
#     if liste=="*":
#         break
#     print(i)

#continue bunda döngüde raslandığında kalan işlemleri tamamlamadan en başa döner

# liste=list(range(20))
# for i in liste:
#     if i==10 or i==14: # i 10 ve 14 olunca birek alta inmeden başa dönüyo
#         continue
#     print(i)

# i=0
# while (i<10):
#     if (i==2):
#         continue # sonsuz döngüye girdi artamadığı için sürekli iki de döndü
#     print(i)
#     i+=1

# i=0
# while (i<10):
#     if (i==2):
#         i+=1
#         continue
#     print(i)
#     i+=1

# list comprehension liste oluşturmak,üretmek için kullanılan pratik bir yöntem

# liste1=[1,2,3,4]
# liste2=[]
# for i in liste1:
#     liste2.append(i)
# liste2.append(5)
# print(liste2)

# liste1=[1,2,3,4]
# liste2=[i for i in liste1] #list comprehension
# print(liste2)
# liste3=[i*2 for i in liste1]
# print(liste3)

# liste=[(1,2),(3,4),(5,6)]
# liste1=[i*j for i,j in liste]
# print(liste1)

# r="rıdvan"
# liste=[i*2 for i in r]
# print(liste)

# liste=[[1,2,3,10,50,54],[4,5,6,7],[8,9,10]]
# liste1=list()
# for i in liste:
#     for a in i:
#         liste1.append(a)
# print(liste1)

# liste=[[1,2,3,10,50,54],[4,5,6,7],[8,9,10]]
# liste1=[x for i in liste for x in i]
# print(liste1)
# ***************************************************************************************************************************
# Kullanıcı giriş sistemi
# isim="rıdvan"
# soyisim="dikmen"
# hak=3
# while True:
#     girisim=input("isminizi giriniz")
#     girsoyisim=input("soyisminizi giriniz")
#     if (isim==girisim and soyisim==girsoyisim):
#         print("hoşgeldiniz")
#         break
#     elif hak==1:
#         print("hakkınız bitti")
#         break
#     else:
#         print("hatalı işlem yaptınız")
#         hak-=1
#         continue

# isim="rıdvan"
# soyisim="dikmen"
# hak=3
# while True:
#     girisim = input("isminizi giriniz")
#     girsoyisim=input("soyisminizi giriniz")
#     if isim!=girisim and soyisim==girsoyisim:
#         print("isim yanlış")
#         hak-=1
#     elif isim==girisim and soyisim!=girsoyisim:
#         print("soyisim yanlış")
#         hak-=1
#     elif isim!=girisim and soyisim!=girsoyisim:
#         print("ikiside yanlış")
#         hak-=1
#     else:
#         print("sisteme giriş yapıldı")
#         break
#     if hak==0:
#         print("hakkınız bitti")
#         break

#faktöriyel bulma
# sayı=int(input("faktöriyelini almak istediğiniz sayıyı giriniz"))
# sayı1=1
# for i in range(1,sayı+1):
#     sayı1=sayı1*i
#     i+=1
# print(sayı1)

#fibonacci sayısı
# a=1
# b=1
# fibonacci=[a,b]
# for i in range(20):
#     a,b=b,a+b
#     fibonacci.append(b)
# print(fibonacci)

# sayı = int(input("bulmak istediğiniz mükemmel sayıyı yazınız"))
# toplam = 0
# i = 1
# while (i<sayı):
#     if (sayı % i == 0):
#         toplam += i
#     i += 1
# if (toplam == sayı):
#     print("mükemmel sayı")
# else:
#     print("mükemmel sayı değil")

# sayı = input("sayıyı giriniz")
# uzunluk=len(sayı)
# sayı=int(sayı)
# toplam=0
# gecici_sayı = sayı
#
# while (gecici_sayı > 0):
#     basamak = gecici_sayı % 10
#
#     toplam += basamak ** uzunluk
#
#     gecici_sayı //= 10
#
# if (toplam == sayı):
#     print(sayı, "bir armstrong sayısıdır.")
# else:
#     print(sayı, "bir armstrong sayısı değildir.")
# ***************************************************************************************************************************

# metodlar/fonksiyonlar
# metodlar
# a = [1,2,3,4,5]
# a.insert(1,"rd")
# a.append("dik")
# a.pop()
# print(a)
# help(a.insert) # bırda metodun ne yaptığını öğrenmemizi sağlar

#fonksiyonlar
#programlama belli işlemleri olan ve tekrar tekrar kullanılan yapılardır
# fonksiyonların tanımlanma şekli
# def fonk_adı(parametre1,parametre2....(opsiyonel))
#     fonk. bloğu
#     yapılacak işlemler
#     dönüş değerleri - opsiyonel

# type(selamla)
# def selamla():
#     print("merhaba")
#     print("nasılsınız")
# print(type(selamla))
# selamla()

# def selamla(isim): # isim paremetre denir
#     print("isminiz",isim)
# selamla("rıdvan")  # rıdvan buna argüman denir

# def topla(sayı1,sayı2,sayı3):
#     print(sayı1+sayı2+sayı3)
# topla(5,8,9)

# def faktoriyel(sayı):
#     fak=1
#     if (sayı == 0 or sayı == 1):
#         print(fak)
#     else:
#         while (sayı>1):
#             fak*=sayı
#             sayı-=1
#         print(fak)
# faktoriyel(6)

#fonksiyonlarda return
# return fonksiyon sonucu elde edilen değerleri çağrıldığı yere döndürür yani değişkende depolar

# def topla(a,b,c):
#     return a+b+c
# def çarp(a,b):
#     return a*b
#
# toplam=topla(1,2,3)
# print(çarp(4,toplam))

# def topla(a,b,c):
#     return a+b+c
#     print(a+b+c) # return ün altındaki hiçbir işlem çalıştırlmaz
# print(topla(5,6,4))

# fonksiyonlarda çağırıldıklara yere değer döndürmeyen fonksiyonlara(return kullamayan) void fonksiton denir

# def topla(a,b,c):
# print(a+b+c)


































































































































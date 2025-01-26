# 1) Kullanicidan isim, yas ve egitim bilgileri isteyip ehliyet alabilme durumunu kontrol et. Ehliyet alma kosulu en az 18 yas 
# ve egitim durumu lise veya uni olmalidir.

isim = input('isminiz: ')
yas = int(input('yasiniz: '))
egitim = input('egitim: ')

if (yas>18):
    if(egitim=='lise' or egitim=='universite'):
        print(f'{isim} ehliyet alabilirsin.')
    else:
        print(f'{isim} ehliyet alamazsin!egitim durumun yetersiz.')
else:
    print('{isim} ehliyet alamazsin!yasin tutmuyor')

# 2) Bir ogrencinin 2 yazili 1 sozlu notunu alip hesaplanan ortalamaya gore not araligina karsilik gelen not bilgisini yazdir.
# 0-24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5


yazili1 = float(input('1.yazili: '))
yazili2 = float(input('2.yazili: '))
sozlu = float(input('sozlu: '))

ortalama = (yazili1+yazili2+sozlu)/3

if (ortalama>=0) and (ortalama<25):
    print(f'ortalamaniz: {ortalama} notunuz: 0')
elif (ortalama >=25) and (ortalama<45):
    print(f'ortalamaniz: {ortalama} notunuz: 1')
elif (ortalama >=45) and (ortalama<54):
    print(f'ortalamaniz: {ortalama} notunuz: 2')
elif (ortalama >=55) and (ortalama<69):
    print(f'ortalamaniz: {ortalama} notunuz: 3')
elif (ortalama >=70) and (ortalama<84):
    print(f'ortalamaniz: {ortalama} notunuz: 4')
elif (ortalama >=85) and (ortalama<100):
    print(f'ortalamaniz: {ortalama} notunuz: 5')
else:
    print(f'ortalamaniz: {ortalama} notunuz: gecersiz!')


# 3) Trafige cikis tarihi alinan bir aracin servis zamanini asagidaki bilgilere gore hesapla.
# 1.Bakim => 1.yil
# 2.Bakim => 2.yil
# 3.Bakim => 3.yil
# **Sure hesabini alinan gun, ay, yil bilgisine gore gun bazli hesapla.
# ***datetime modulunu kullanmak gerekli.
# (simdi) - (2022/10/29) => gun

import datetime
tarih = input('araciniz hangi tarihte trafige cikti(yyyy/aa/gg): ')
tarih = tarih.split('/')
#tarih[0] yil bilgisi
#tarih[1] ay bilgisi
#tarih[2] gun bilgisi

trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2])) #trafigeCikis adinda bir obje olusturduk ki onu datetime degiskeninden cikarabilmek icin
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if (days<=365):
    print('1.servis araligi')
elif (days>365) and (days<=365*2):
    print('2.servis araligi')
elif (days>365*2) and (days<=365*3):
    print('3.servis araligi')
else:
    print('hatali sure!')
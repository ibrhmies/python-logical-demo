#-> girilen sayının 50-100 arasında olup olmadığını kontrol ediniz.

x = int(input("X: "))

sonuc = (x > 50) and (100>x)

print(sonuc)


#-> girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.

x = int(input("X: "))

sonuc = (x > 0) and (x % 2 == 1)

print(sonuc) 


#username ve parola bilgileri ile giriş kontrolü yapınız.

username = "ibrhms"
password = 12345 

y = str(input("Username giriniz: "))
x = int(input("Parola giriniz: "))

sonuc = (username == y) and (password == x)

print(sonuc)


#-> Girilen 3 sayıyı büyüklük sıralamasına göre sıralayınız.

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

sonuc = (x > y) and (x > z) 
print(f"X en büyük sayı: {sonuc}")

sonuc = (y > x) and (y > z) 
print(f"Y en büyük sayı: {sonuc}")

sonuc = (z > x) and (z > y) 
print(f"Z en büyük sayı: {sonuc}")


#-> kullanıcıdan vize(%40) ve final (%60) notlarını alıp ortalamasını hesaplayınız
#          eğer ortalaması 55 üstüyse geçti değilse kaldı yazınız
#          a) ortalama 55 olsa bile final notu en az 55 olmalıdır.
#          b) finalden 70 alınırsa ortalama önemli değildir.

vize = float(input("vize notunu giriniz: "))
final = float(input("final notunu giriniz: "))

ortalama = vize*0.4 + final*0.6

sonuc = ((ortalama >= 55) and (final >= 55)) or ((ortalama >= 55) or( final >= 70))

print(f"öğrencinin ortalaması {ortalama} ve sınavdan geçti: {sonuc}")


#-> kişinin ad , boy ve kilo değerlerini alıp kilo indeksini hesaplayınız.
#   Formül:(kilo/boy uzunluğunun karesi)
#   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#   0-18.4       => zayıf
#   18.5-24.9    => normal
#   25.0-29.9    => fazla kilolu
#   30.0-34.9    => şişman(obez)

kisininAdi = str(input("Adınızı giriniz: "))
kisininBoyu = float(input("Boyunuzu giriniz: "))
kisininKilosu = float(input("Kilonuzu giriniz: "))

vki = ( kisininKilosu / kisininBoyu**2 )

sonuc = (vki > 0) and (vki <= 18.4)
print(f"Vücut kitle indeksi {vki} Zayıf: {sonuc}")

sonuc = (vki >= 18.5) and (vki <= 24.9)
print(f"Vücut kitle indeksi {vki} Normal: {sonuc}")

sonuc = (vki >= 25.0) and (vki <= 29.9)
print(f"Vücut kitle indeksi {vki} Fazla Kilolu: {sonuc}")

sonuc = (vki >= 30.0) and (vki <= 34.9)
print(f"Vücut kitle indeksi {vki} Şişman(obez): {sonuc}")





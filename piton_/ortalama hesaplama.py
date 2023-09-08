def boşluk(a):
    while a != 0:
        print("")
        a -= 1

class Ortalama:
    def __init__(self, Ders, Sınav1= 0, Sınav2 = 0, Performans1 = 0, Performans2 = 0, Proje = 0, Ders_sayısı= 0, Ortalama = 0 ):
        self.Ders = Ders
        self.Sınav1 = Sınav1
        self.Sınav2 = Sınav2
        self.Performans1 = Performans1
        self.Performans2 = Performans2
        self.Proje = Proje
        self.Ders_sayısı = Ders_sayısı
        self.Ortalama = Ortalama
                                
#kişi sayısı girme
while True:
    cevap = "2"
    try:
        d_sayısı = int(input("Ders sayısını girin : "))
    except ValueError:
        d_sayısı = -1
    boşluk(1)        

    if d_sayısı >= 1:
        while True:
            print("{} ders sayısına emin misiniz?".format(d_sayısı))
            print("(1) Evet     (2) Hayır")
            
            cevap = str(input())
            if cevap == "1":
                boşluk(1)
                break
            elif cevap == "2":
                break
            else:
                pass
    else:
        pass

    if cevap == "1":
        break
    else:
        pass

# listeye ders atmaca
liste = []
olay_s = 1
for n in range(1, d_sayısı + 1):
    liste.append(str(n))
    olay_s += 1

# liste2
liste2 = list(liste)
for n in range(0, olay_s - 1):
    liste2[n] += "a"

# Ders girişleri
for n in range(0, olay_s - 1):
    liste[n] = Ortalama(str(input("{0}. dersin adını girin : ".format(n+1)))) 
    liste2[n] = Ortalama(liste[n].Ders)
boşluk(1)
    
# Ders sayısı girişleri
for n in range(0, olay_s - 1):
    while True:
        try:
            liste[n].Ders_sayısı = int(input("{} dersinin ders sayısını girin : ".format(liste[n].Ders)))
        except ValueError:
            liste[n].Ders_sayısı = -1
        if liste[n].Ders_sayısı >= 1:
            break
        else:
            print("1 veya daha fazla sayı yazın.")
            pass        
    liste2[n].Ders_sayısı = liste[n].Ders_sayısı
        
# dönem1 not girişleri ve ortalama hesaplama
for n in range(0, olay_s - 1):
    boşluk(1)
    t = 0
    
    while True:# Sınav1 giriş
        try:
            liste[n].Sınav1 += int(input("{} dersinin 1. sınav giriş: : ".format(liste[n].Ders)))
        except ValueError:
            liste[n].Sınav1 = -1
            
        if liste[n].Sınav1 > -1:
            if liste[n].Sınav1 < 101:
                break
            else:
                liste[n].Sınav1 = 0
                pass
        else:
            liste[n].Sınav1 = 0
            pass
        
    while True: # Sınav2 giriş
        try:                        
            liste[n].Sınav2 += int(input("{} dersinin 2. sınav giriş : ".format(liste[n].Ders)))
        except ValueError:
            liste[n].Sınav2 = -1
        if liste[n].Sınav2 > -1:
            if liste[n].Sınav2 < 101:
                break
            else:
                liste[n].Sınav2 = 0
                pass
        else:
            liste[n].Sınav2 = 0
            pass
            
    while True: # Performans1 giriş
        try:                                      
            liste[n].Performans1 += int(input("{} dersinin 1. performans giriş : ".format(liste[n].Ders)))
        except ValueError:
            liste[n].Performans1 = -1
        if liste[n].Performans1 > -1:
            if liste[n].Performans1 < 101:
                break
            else:
                liste[n].Performans1 = 0
                pass
        else:
            liste[n].Performans1 = 0
            pass
            
    while True: #Performans2 giriş
        try:                         
            liste[n].Performans2 += int(input("{} dersinin 2. performasn giriş : ".format(liste[n].Ders)))
        except ValueError:
            liste[n].Performans2 = -1
        
        if liste[n].Performans2 > -1:
            if liste[n].Performans2 < 101:
                break
            else:
                liste[n].Performans2 = 0
                pass
        else:
            liste[n].Performans2 = 0
            pass
        
    print("{} dersinin Projesi var mı ".format(liste[n].Ders))
    print("(1) EVET        (2) HAYIR")
    cevap = str(input(""))
    
    if cevap == "1":
        t += 1
        while True:
             try:
                liste[n].Proje += int(input("{} dersinin proje giriş : ".format(liste[n].Ders)))
             except ValueError:
                liste[n].Proje = -1
                
             if liste[n].Proje > -1:
                 if liste[n].Proje < 101:
                     break
                 else:
                     liste[n].Proje = 0
                     pass
             else:
                 liste[n].Proje = 0
                 pass
        else:
            pass
    
    liste[n].ortalama = (liste[n].Sınav1 + liste[n].Sınav2 + liste[n].Performans1 + liste[n].Performans2 + liste[n].Proje) / (t + 4)
0

# derslerin ortalaması alma
ders_top = 0
ders_sayısı_top = 0    
for n in range(0, olay_s - 1):
    ders_top += (liste[n].ortalama) * (liste[n].Ders_sayısı)
    ders_sayısı_top += liste[n].Ders_sayısı

dönem1_ortalama = ders_top / ders_sayısı_top
print(dönem1_ortalama)   

# ------------------------ Tablo ----------------------- #

# çizgi
çizgi = ""
for n in range(80):
    çizgi += "-"

# ders isim düzenleyici
for n in range(0, olay_s):
    kelime = list(liste[n].Ders)
    for b in kelime:
         
# tablonun başlangıcı
def başlangıç():
    boşluk(1)
    print(çizgi)
    print("|  DERS  | 1.SINAV | 2.SINAV | 1.PERFORMANS | 2.PERFORMANS | PROJE | ORTALAMA  |")
    print(çizgi)   
            

def tablo():
    başlangıç()
    for n in range(0, olay_s):
        print("| {} ")
        print(çizgi)
tablo()
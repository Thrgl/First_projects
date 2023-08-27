class ortalama:
    def __init__(self, Ders, Ders_sayısı, Proje = 0):
        self.Ders = Ders
        self.Ders_sayısı = Ders_sayısı
        self.Proje = Proje

#kişi sayısı girme
while True:
    try:
        d_sayısı = int(input("Ders sayısını girin : "))
    except ValueError:
        d_sayısı = -1

    if d_sayısı >= 1:
        while True:
            print("{} ders sayısına eminmisiniz?".format(d_sayısı))
            print("(1) Evet     (2) Hayır")
            
            cevap = str(input())
            if cevap == "1":
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

# ders girişleri
for z in range(0, olay_s):
    liste[z] = ortalama(str(input()), int(input()), int(input()))
    
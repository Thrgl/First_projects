import random
import time

ismi = ["Çamaşır sodası", "Tuz ruhu", "Zaç yağı", "Kezzap", "Krom", "Kobalt", "Çinko", "Kalay", "Altın", "Demir", "Bakır", "Gümüş", "Baryum", "Kurşun", "Mangan", "Nikel", "Brom", "İyot", "Cıva", "Platin", "Sirke asiti", "Kireç Taşı", "Yemek sodası", "Amonyak", "Sönmüş kireç", "Sud kostik", "Potas kostik", "Sönmemiş Kireç", "Yemek tuzu", "Hidrojen", "Helyum", "Lityum", "Berilyum", "Bor", "Karbon", "Azot", "Oksijen", "Neon", "Sodyum", "Magnezyum", "Alüminyum", "Silisyum", "Fosfor", "Klor", "Argon", "Potasyum", "Kalsiyum"]
birleşikler = ["NaClO", "HCl", "H2SO4", "HNO3", "Cr", "Co", "Zn", "Sn", "Au", "Fe", "Cu", "Ag", "Ba", "Pb", "Mn", "Ni", "Br", "I", "Hg", "Pt", "CH3COOH", "CaCO3", "NaHCO3", "NH2", "Ca(OH)2", "NaOH", "KOH", "CaO", "NaCl", "H", "He", "Li", "Be", "B", "C", "N",  "O", "Ne", "Na", "Mg", "Al", "Si", "P", "Cl", "Ar", "K", "Ca"]

#Boş menu
def menu():
    print("           kimya isim oyunu")
    print("10 soru karışık element ismi ve formül sorma")
    print("   başlamak için (ENTER) tuşuna basın")
    
    cevap = input("            ")

def soru1():
    global m
    element = random.randint(0, len(birleşikler) - 1)
    print("{} formülünün adı ne?".format(birleşikler[element]))

    A1 = str(ismi[random.randint(0, len(birleşikler) - 1)])
    A2 = str(ismi[random.randint(0, len(birleşikler) - 1)])
    A3 = str(ismi[random.randint(0, len(birleşikler) - 1)])
    A4 = ismi[element] 
    
    cevaplar = [A1, A2, A3, A4]
    cevaplar2 = ["0", "1", "2", "3"]
    başı = 0
    başı2 = ["A", "B", "C", "D"]

    while len(cevaplar2) != 0:

        a = random.choice(cevaplar2)

        print("({0}) {1:4}".format(başı2[başı], cevaplar[int(a)]))
        başı += 1

        if a == "3":
            başı2[başı-1] = A4

        del cevaplar2[cevaplar2.index(a)]


    şık = input(str())
    if şık == "A" or şık == "a":
        if başı2[0] == A4: 
            print("Doğru cavap\nDiğer soruya geçiliyor\n")
            m -= 1
        else:
            print("cevabınız yanlış\nDoğru cevap {}\nDiğer soruya geçiliyor\n".format(A4))
    
    elif şık == "B" or şık == "b":
        if başı2[1] == A4: 
            print("Doğru cavap\nDiğer soruya geçiliyor\n")
            m -= 1
        else:
            print("cevabınız yanlış\nDoğru cevap {}\nDiğer soruya geçiliyor\n".format(A4))
    
    elif şık == "C" or şık == "c":
        if başı2[2] == A4: 
            print("Doğru cavap\nDiğer soruya geçiliyor\n")
            m -= 1
        else:
            print("cevabınız yanlış\nDoğru cevap {}\nDiğer soruya geçiliyor\n".format(A4))
           
    elif şık == "D" or şık == "d":
        if başı2[3] == A4: 
            print("Doğru cavap\nDiğer soruya geçiliyor\n")
            m -= 1
        else:
            print("cevabınız yanlış\nDoğru cevap {}\nDiğer soruya geçiliyor\n".format(A4))    
    else:
        print("Şıklardan birini seçin\nDoğru cevap {}\nDiğer soruya geçiliyor\n".format(A4))



def soru2():
    global m

    element = random.randint(0, len(birleşikler) - 1)
    print("{} maddesinin formülü ne?".format(ismi[element]))

    A1 = str(birleşikler[random.randint(0, len(birleşikler) - 1)])
    A2 = str(birleşikler[random.randint(0, len(birleşikler) - 1)])
    A3 = str(birleşikler[random.randint(0, len(birleşikler) - 1)])
    A4 = birleşikler[element] 
    
    cevaplar = [A1, A2, A3, A4]
    cevaplar2 = ["0", "1", "2", "3"]
    başı = 0
    başı2 = ["A", "B", "C", "D"]

    while len(cevaplar2) != 0:

        a = random.choice(cevaplar2)

        print("({0}) {1:4}".format(başı2[başı], cevaplar[int(a)]))
        başı += 1

        if a == "3":
            başı2[başı-1] = A4

        del cevaplar2[cevaplar2.index(a)]


    şık = input(str())

    if şık == "A" or şık == "a":
        if başı2[0] == A4: 
            if t == 9:    
                print("Doğru cavap\n")
            else:
                print("Doğru cavap\nDiğer soruya geçiliyor\n")
            m -= 1

        else:
            if t == 9:
                print("cevabınız yanlış\nDoğru cevap {}\n".format(A4))
            else:
                print("cevabınız yanlış\nDoğru cevap {}\nDiğer soruya geçiliyor\n".format(A4))

    elif şık == "B" or şık == "b":
        if başı2[1] == A4: 
            if t == 9:    
                print("Doğru cavap\n")
            else:
                print("Doğru cavap\nDiğer soruya geçiliyor\n")
            m -= 1

        else:
            if t == 9:
                print("cevabınız yanlış\nDoğru cevap {}\n".format(A4))
            else:
                print("cevabınız yanlış\nDoğru cevap {}\nDiğer soruya geçiliyor\n".format(A4))
    
    elif şık == "C" or şık == "c":
        if başı2[2] == A4: 
            if t == 9:    
                print("Doğru cavap\n")
            else:
                print("Doğru cavap\nDiğer soruya geçiliyor\n")
            m -= 1

        else:
            if t == 9:
                print("cevabınız yanlış\nDoğru cevap {}\n".format(A4))
            else:
                print("cevabınız yanlış\nDoğru cevap {}\nDiğer soruya geçiliyor\n".format(A4))
           
    elif şık == "D" or şık =="d":
        if başı2[3] == A4: 
            if t == 9:    
                print("Doğru cavap\n")
            else:
                print("Doğru cavap\nDiğer soruya geçiliyor\n")
            m -= 1

        else:
            if t == 9:
                print("cevabınız yanlış\nDoğru cevap {}\n".format(A4))
            else:
                print("cevabınız yanlış\nDoğru cevap {}\nDiğer soruya geçiliyor\n".format(A4))    
    else:
        if t == 9:
            print("Lütfen Şıklardan birini seçin\nDoğru cevap {}\n".format(A4))
        else:
            print("Lütfen Şıklardan birini seçin\nDoğru cevap {}\nDiğer soruya geçiliyor\n".format(A4))

def on_soru():
    global m
    global t
    n = 100
    m = 10
    başlangıç = time.time()
    for t in range(0, 10):
        if t // 2 == 0:
            soru1()
        else:
            soru2()
    
    bitiş = time.time()

    süre = bitiş - başlangıç

    print(f"toplam puanın 100 üzerinden {n-(m*10)} puan\nbunu {süre:.2f} dürede bitirdiniz")


while True:
    menu()
    on_soru()
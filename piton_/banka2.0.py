import time

class Banka:
    def __init__(self, İsim, bakiye):
        self.İsim = İsim
        self.bakiye = bakiye

#cizgi sadece
t = 0
cizgi = "-"
while t != 60:
    cizgi += "-"
    t += 1

#30 boşluk
def b30():
    a = 30
    while a != 0:
        print(" ", end= " ")
        a -= 1

#30 boşluk
def b26():
    a = 24
    while a != 0:
        print(" ", end= " ")
        a -= 1

#boşluk sayısı ayarlayacı
def boşluk(n):
    while True: 
        if n != 0:
            print("\n", end="")
            n -= 1
        else :
            break

#orta ayarlayacı
def ba(cevap):
	boşluk_sayısı = 62
	d = 0
	
	ayrık = []
	yazı = [cevap]
	
	for b in yazı:
		harf = list(b)
		ayrık.append(harf)	
	
	liste = ayrık[0]
	for k in liste:
		d = d + 1
		if d%2 == 0:
			pass
		else:
			boşluk_sayısı -=1	  
	
	while boşluk_sayısı >= 0:
		print(" ", end="")
		boşluk_sayısı -= 1
	print(cevap)        
    
#oyuncu sayısı girme bölgesi
boşluk(1)
ba("𝗠 𝗢 𝗡 𝗢 𝗣 𝗢 𝗟 𝗬")
boşluk(1)
while True:
    ba("Oyuncu sayısını giriniz ( En az 2 kişi )")
    boşluk(1)
    b30()
    try:
        oyuncu_sayısı = int(input())
    except ValueError:
        oyuncu_sayısı = 0
        pass
    if oyuncu_sayısı >= 2:
        break
    else:
        ba("2 veya daha fazla sayı yazın")
        boşluk(1)
        pass
          
#kişi sayısı belirleme
olay_sayısı = 0
liste = []
for n in range(1, oyuncu_sayısı + 1):
    n = [str(n)]
    liste += n
    olay_sayısı += 1
    

#kişilerin isim ve para girişi
boşluk(6)
for n in range(0, olay_sayısı):
    b = ("{0}. Oyuncu adınız".format(n+1))
    ba(b)
    b30()
    liste[n] = Banka(str(n + 1) + "." + str(input()), 15000)
    boşluk(1)
boşluk(2)

#sorgulama bölgesi
def sorgulama():
    boşluk(2)
    
    for m in liste:
        h = ""
        ğ = 30
        s = 0

        a = [str(m.İsim) + str(m.bakiye) + "K"]
        
        köl = []
        for d in a:
            harf = list(d)
            köl.append(harf)

        tmm = köl[0]

        for sd in tmm:
            s += 1
        ğ -= s
				    
        for k in range(0, (ğ - 1)):
            h += " "    
        
        w = str(m.İsim) + str(h) + str(m.bakiye) + "K"
        b26()
        print(w) 
    
    time.sleep(1)

#sorgulama 2 bölgesi
def sorgulama2(yan_sayı):
    boşluk(1)
    eksi_liste = list(liste) 
    del eksi_liste[yan_sayı - 1]  
    for m in eksi_liste:
        h = ""
        ğ = 30
        s = 0

        a = [str(m.İsim) + str(m.bakiye) + "K"]
        
        köl = []
        for d in a:
            harf = list(d)
            köl.append(harf)

        tmm = köl[0]

        for sd in tmm:
            s += 1
        ğ -= s
				    
        for k in range(0, (ğ - 1)):
            h += " "    
        
        w = str(m.İsim) + str(h) + str(m.bakiye) + "K"
        b26()
        print(w) 
    time.sleep(1)


#para gönder kısmı
def para_gönder():
    while True:
        sorgulama()
        boşluk(1)
        ba("Parayı göderecek kişinin numarasını giriniz ")
        boşluk(1)
        b30()
        try:    
            p1 = int(input())
            yan_sayı = p1
        except ValueError:
            p1 = 0
        if p1 >= 1:
            if p1 <= oyuncu_sayısı:
                ba(cizgi)
                break
            else:
                ba("Kişi numarası giriniz")
                time.sleep(2)
                ba(cizgi)
                boşluk(2)
                pass
        else:
            ba("Kişi numarası giriniz")
            time.sleep(2)
            ba(cizgi)
            boşluk(2)
            pass

    while True:
        boşluk(2)
        sorgulama2(yan_sayı)
        boşluk(1)
        ba("Parayı alacak kişinin numarasını yazınız")
        boşluk(1)
        b30() 
        try:    
            p2 = int(input())
        except ValueError:
            p2 = 0
        if p2 >= 1:
            if p2 <= oyuncu_sayısı:
                if p2 != yan_sayı:
                    ba(cizgi)
                    break
                else:
                    ba("Önceki kişiyi seçemezsiniz, başka kişi seçin")
                    time.sleep(2)
                    ba(cizgi)
                    boşluk(2)
                    pass
            else:
                ba("Kişi numarası giriniz")
                time.sleep(2)
                ba(cizgi)
                boşluk(2)
                pass
        else:
            ba("Kişi numarası giriniz")
            time.sleep(2)
            ba(cizgi)
            boşluk(2)
            pass

    while True:
        boşluk(1)
        ba("Para miktarını giriniz")
        boşluk(1)
        b30()
        try:
            para_miktarı = int(input())
        except ValueError:
            para_miktarı = -1
        if para_miktarı >= 0:
            break
        else:
            ba("0 veya daha fazla rakam yazınız")
            time.sleep(2)
            ba(cizgi)
            boşluk(2)
            pass

    liste[(p1 - 1)].bakiye -= para_miktarı
    liste[(p2 -1)].bakiye += para_miktarı

#para arttırma bölgesi    
def para_artırma():
    while True:
        sorgulama()
        boşluk(1)
        ba("Para artıracak kişinin isminin başındaki numarayı yazın")
        boşluk(1)
        b30()
        try:    
            p1 = int(input())
        except ValueError:
            p1 = 0
        if p1 >= 1:
            if p1 <= oyuncu_sayısı:
                ba(cizgi)
                break
            else:
                ba("alttaki isminlerden birinin yanındaki başındaki yazın")
                time.sleep(2)
                ba(cizgi)
                boşluk(2)
                pass
        else:
            ba("alttaki isminlerden birinin yanındaki başındaki yazın")
            time.sleep(2)
            ba(cizgi)
            boşluk(2)
            pass
    
    while True:
        boşluk(1)
        ba("Para miktarını girin")
        boşluk(1)
        b30()
        try:
            para_miktarı = int(input())
        except ValueError:
            para_miktarı = -1
        if para_miktarı >= 0:
            break
        else:
            ba("0 veya daha fazla rakam yazın")
            time.sleep(2)
            ba(cizgi)
            boşluk(1)
            pass

    liste[(p1 - 1)].bakiye += para_miktarı

#para azaltma bölgesi
def para_azaltma():
    while True:
        sorgulama()
        boşluk(1)
        ba("Para azaltılacak kişinin isminin başındaki numarayı yazın")
        boşluk(1)
        b30()
        try:    
            p1 = int(input())
        except ValueError:
            p1 = 0
        if p1 >= 1:
            if p1 <= oyuncu_sayısı:
                ba(cizgi)
                break
            else:
                ba("alttaki isminlerden birinin yanındaki başındaki yazın")
                time.sleep(2)
                ba(cizgi)
                boşluk(2)
                pass
        else:
            ba("alttaki isminlerden birinin yanındaki başındaki yazın")
            time.sleep(2)
            ba(cizgi)
            boşluk(2)
            pass

    while True:
        boşluk(1)    
        ba("Para miktarını girin") 
        boşluk(1)   
        b30()
        try:
            para_miktarı = int(input())
        except ValueError:
            para_miktarı = -1
        if para_miktarı >= 0:
            break
        else:
            ba("0 veya daha fazla rakam yazın")
            time.sleep(2)
            boşluk(1)
            pass
    liste[(p1 - 1)].bakiye -= para_miktarı
    
#100 kağıt verme
def v100k():
    k = 0
    while True:
        sorgulama()
        boşluk(1)
        ba("100k verilecek kişinin isminin başındaki numarayı yazın")
        boşluk(1)
        b30()
        try:    
            p1 = int(input())
        except ValueError:
            p1 = 0
        if p1 >= 1:
            if p1 <= oyuncu_sayısı:
                ba(cizgi)
                break
            else:
                ba("alttaki isminlerden birinin yanındaki başındaki yazın")
                time.sleep(2)
                ba(cizgi)
                boşluk(2)
                pass
        else:
            ba("alttaki isminlerden birinin yanındaki başındaki yazın")
            time.sleep(2)
            ba(cizgi)
            boşluk(2)
            pass
        
    while True:
        ba("bu işlemi yapmak istiyormusunuz")
        ba("(yanındaki numarayı yazın)")
        boşluk(1)
        ba("1 | EVET |                     2 | HAYIR |")
        boşluk(1)
        b30()  
        a = str(input())
        if a == "1":
            p1 -= 1
            eksi_liste = list(liste)
            del eksi_liste[p1]
            for a in eksi_liste:
                a.bakiye -= 100
                k += 1
            liste[p1].bakiye += k * 100    
            ba(cizgi)
            break            
        elif a == "2":
            break
        else:
            ba("'EVET' yada 'HAYIR' seçin")
            ba(cizgi)
            pass
                    
#motor bölgesi
while True:
    boşluk(2)
    ba("🅼 🅴 🅽 🆄")
    boşluk(1)
    b26()
    print("(1) Para trasnferleri")
    b26()
    print("(2) Bankadan Para çekme")
    b26()
    print("(3) Bankaya Para verme")
    b26()
    print("(4) Oyuncu cüzdan sorgulama")
    boşluk(1)
    b26()
    print("(5) Şans kartı ( Oyumculardan 100K alma )")
    boşluk(1)
    b26()
    print("(BİTİR) Oyunu bitir")
    boşluk(1)
    ba("Sayı girişi")
    boşluk(1)
    b30()
    cevap =str(input())
    if cevap == "1":
        boşluk(6)
        para_gönder()
        sorgulama()
        boşluk(6)
    elif cevap == "2":
        boşluk(6)
        para_artırma()
        sorgulama()
        boşluk(6)
    elif cevap == "3":
        boşluk(6)
        para_azaltma()
        sorgulama()
        boşluk(6)
    elif cevap == "4":
        boşluk(6)
        ba("BAKİYELER")
        sorgulama()
        boşluk(6)
    elif cevap == "5":
        boşluk(6)
        v100k()
        sorgulama()
        boşluk(6)
    elif cevap == "BİTİR":
        break
    else:
        ba("alttaki sayılardan birini yazın !!!")
import re

paragraf = str(input("Pagrafınızı girin : "))

kelime = str(input("\nAramak istediğiniz kelimeyi yazınız : "))

b = 0
for a in re.finditer(kelime, paragraf):
    print(a.span(), a.group())
    b += 1

print( "\nYazdığnız paragrafta, '{0}' kelimsinden {1} kere geçmektedir".format(kelime, b))
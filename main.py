# class Araba:
#     marka = ""
#     cikis_yili = 0
#     km = 0
#     lpg = True
#
# araba1 = Araba()
# araba1.marka = "Renault"
# araba1.cikis_yili = 2009
# araba1.km = 32000
# araba1.lpg = False
#
# print(araba1.marka)
# print(araba1.cikis_yili)
# print(araba1.km)
# print(araba1.lpg)

# class Muzisyen:
#     def __init__(self,isim,tur):
#         self.isim = isim
#         self.tur = tur
#
# muzisyen1 = Muzisyen("Beethoven","Klasik")
# muzisyen2 = Muzisyen("Ajdar","Pop")
# muzisyen3 = Muzisyen("Ceza","Rap")
# muzisyen4 = Muzisyen("Lars","Rock")
#
# print(muzisyen1.isim)
# print(muzisyen1.tur)
# print("----------------------------------")
# print(muzisyen2.isim)
# print(muzisyen2.tur)
# print("----------------------------------")
# print(muzisyen3.isim)
# print(muzisyen3.tur)
# print("----------------------------------")
# print(muzisyen4.isim)
# print(muzisyen4.tur)

class Sinif1:
    def yazdir(self):
        print("Yazdırıldı")

class Sinif2(Sinif1):
    def yazdir_iki(self):
        print("Yazdıracak mısın?")

sinif2 = Sinif2()
sinif2.yazdir_iki()
sinif2.yazdir()

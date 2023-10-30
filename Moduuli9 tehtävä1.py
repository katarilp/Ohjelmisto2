# "Auto"-luokka, jonka ominaisuudet ovat
# rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
# joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton
# (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, reknum, huippu):
        self.reknum = reknum
        self.huippu = huippu
    nopeus = 0
    matka = 0

    def printtaa_auto(self):
        (print(f"Rekisteröidyn auton tiedot: \nrekisteritunnus {self.reknum},\nhuippunopeus: {self.huippu} km/h,\n"
               f"tämänhetkinen nopeus: {self.nopeus}\nja kuljettu matka: {self.matka}."))

auto1 = Auto("ABC-123", 142)

auto1.printtaa_auto()





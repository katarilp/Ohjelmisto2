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

auto1 = Auto("ABC-123", 142)

print(f"Rekisteröidyn auton tiedot: "
      f"rekisteritunnus {auto1.reknum}, "
      f"huippunopeus: {auto1.huippu} km/h, "
      f"tämänhetkinen nopeus: {auto1.nopeus} "
      f"ja kuljettu matka: {auto1.matka}.")




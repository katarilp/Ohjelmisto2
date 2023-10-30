# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti
# "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random

class Auto:
    def __init__(self, reknum, huippu):
        self.reknum = reknum
        self.huippu = huippu
    nopeus = 0
    matka = 0
    def printtaa_auto(self):
        (print(f"Rekisteröidyn auton tiedot: \nrekisteritunnus {self.reknum},\nhuippunopeus: {self.huippu} km/h,\n"
               f"tämänhetkinen nopeus: {self.nopeus}\nja kuljettu matka: {self.matka}."))
    def kiihdytä(self, nopeudenmuutos):
        self.nopeus = self.nopeus + nopeudenmuutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippu:
            self.nopeus = self.huippu
        print(f"Auton {self.reknum} nopeus on nyt {self.nopeus} km/h.")

    def kulje(self, aika):
        if self.nopeus == 0:
            pass
        else:
            self.matka = self.matka + self.nopeus * aika
        print(f"Autolla {self.reknum} on kuljettu {self.matka} kilometriä.")

kilpailijat = []

num = 1
for num in range (1, 11):
    str(num)
    vauhti = random.randint(100, 200)
    num = Auto(f"ABC-{num}", vauhti)
    #num.printtaa_auto()
    kilpailijat.append(num)

while num.matka < 10000:
    for kaara in kilpailijat:
        nopmuutos = random.randint(-10, 15)
        kaara.kiihdytä(nopmuutos)
        kaara.kulje(1)



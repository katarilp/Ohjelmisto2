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

class Auto:
    def __init__(self, reknum, huippu):
        self.reknum = reknum
        self.huippu = huippu
    nopeus = 0
    matka = 0

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

auto1 = Auto("ABC-123", 142)

print(f"Rekisteröidyn auton tiedot: "
      f"rekisteritunnus {auto1.reknum}, "
      f"huippunopeus: {auto1.huippu} km/h, "
      f"tämänhetkinen nopeus: {auto1.nopeus} "
      f"ja kuljettu matka: {auto1.matka}.")
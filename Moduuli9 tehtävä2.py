# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja
# tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

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

auto1 = Auto("ABC-123", 142)

print(f"Rekisteröidyn auton tiedot: "
      f"rekisteritunnus {auto1.reknum}, "
      f"huippunopeus: {auto1.huippu} km/h, "
      f"tämänhetkinen nopeus: {auto1.nopeus} "
      f"ja kuljettu matka: {auto1.matka}.")

auto1.kiihdytä(30)

auto1.kiihdytä(70)

auto1.kiihdytä(50)

auto1.kiihdytä(-200)
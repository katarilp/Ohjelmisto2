# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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

auto1.kiihdytä(60)
auto1.kulje(1.5)
auto1.kiihdytä(40)
auto1.kulje(24)
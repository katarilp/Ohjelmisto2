# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman
# ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin
# numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Talo:
    def __init__(self, talon_ylin_kerros, talon_alin_kerros, hissit):
        self.talon_ylin_kerros = talon_ylin_kerros
        self.talon_alin_kerros = talon_alin_kerros
    hissilista = []
    for i in range(hissit):
        uusihissi = Hissi("i", self.talon_ylin_kerros, self.talon_alin_kerros)
        hissilista.append(uusihissi)


class Hissi:
    def __init__(self, ylin, alin):
        self.ylin = ylin
        self.alin = alin
        self.lokaatio = alin

    def kerros_ylös(self):
        if self.lokaatio == self.ylin:
            print(f"Hissi on jo ylimmässä kerroksessa {self.lokaatio}.")
        else:
            self.lokaatio = self.lokaatio + 1
            print(f"Hissi on nyt kerroksessa {self.lokaatio}")

    def kerros_alas(self):
        if self.lokaatio == self.alin:
            print(f"Hissi on jo alimmassa kerroksessa {self.lokaatio}.")
        else:
            self.lokaatio = self.lokaatio - 1
            print(f"Hissi on nyt kerroksessa {self.lokaatio}.")

    def siirry_kerrokseen(self, kerros):
        if kerros < self.lokaatio:
            while self.lokaatio > kerros:
                self.kerros_alas()

        if kerros > self.lokaatio:
            while self.lokaatio < kerros:
                self.kerros_ylös()
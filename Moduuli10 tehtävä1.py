# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit
# siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko
# kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi
# sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen
# ja sen jälkeen takaisin alimpaan kerrokseen.

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





h = Hissi(5,1)
h.siirry_kerrokseen(2)
h.kerros_alas()
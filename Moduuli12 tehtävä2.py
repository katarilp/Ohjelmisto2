# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan
# säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
import requests
#paikka = input("Anna paikkakunta: ")

haku = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={e95331e2b95e29980906f883749c400e}"
tulos = requests.get(haku).json()

print(tulos)
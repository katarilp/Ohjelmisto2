import numpy
# 1. Muunna asteiksi a) 2,493 rad b) 0,911 rad
# 2. Muunna asteet radiaaneiksi a) 137,7 astetta b) 62,3 astetta
# 3. Laadi taulukko, josta esittää seuraavat kulmat radiaaneina
kulmat = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]

print("(1)")
a = 2.493
print(numpy.degrees(a))
b = 0.911
print(numpy.degrees(b))

print("(2)")
c = 137.7
print(numpy.radians(c))
d = 62.3
print(numpy.radians(d))

print("(3)")
array1 = []
for i in kulmat:
    array1.append(numpy.radians(i))
print(numpy.array(array1))

print("Laske t.2 suorakulmaisen kolmion(kateetit 1,6m ja 2,3m) hypotenuusan pituus käyttäen sopivaa numpyn funktiota.")
print(numpy.hypot(1.6, 2.3))
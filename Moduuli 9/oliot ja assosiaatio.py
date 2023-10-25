# 23.10.2023 Oliot ja luokat(Matti)
# Ullan kanssa laajennettiin student-luokaa, jotta kukin opiskelija voi kuulua kurssille ja kurssi koululle.
''' Ulla: Kolme opiskelijaa. Luodaan kolme kurssia. Kursseille 1 ja 2 lisätään opiskelijoita.
Luodaan kaksi koulua(Metropolia ja Laurea), joilla molemmilla on yksi kurssi.

Kurssi toimii omana luokkanaan. Kurssilla on nimi ja lista opiskelijoista. '''

class Course:
    def __init__(self, name):
        self.name = name
        self.students = [] # kurssikohtainen studentlista, kun se on luokan sisällä, ei mainissa
    def check_coursename(self):
        print(f"Kurssin nimi on {self.name}.")

    def check_students_on_course(self):
        print(f"Kurssin {self.name} opiskelijat:")
        for student in self.students:
            print(student.name)
    def add_student(self, student):
        self.students.append(student)

    def drop_student(self, student):
        self.students.remove(student)
class Student:

    count = 0

    def __init__(self, name, age=15):  # age oletusarvo 15, jossei määritelty kutsussa
        self.name = name
        self.age = age
        self.credits = 0
        Student.count += 1
        print(f"Uusi opiskelija luotu. Opiskelijoita on nyt yhteensä {Student.count}.")

    def say_hello(self):
        print(f"Tervehdys! Olen {self.name}, {self.age} vuotta. "
              f"Minulla on {self.credits} opintopistettä.")

    def change_name(self, new_name):
        self.name = new_name

    def add_credits(self, credits):
        # estä opintopisteiden meneminen negaativiseksi
        if self.credits + credits < 0:
            self.credits = 0
        else:
            self.credits = self.credits + credits


st1 = Student("Mikko Mallikas", 38)
st1.say_hello()
#st1.change_name("Uusi nimi")
#st1.say_hello()
st2 = Student("Iines Ankka", 21)
#st2.say_hello()
st3 = Student("Elli Esimerkki")
#st3.say_hello()

st1.add_credits(6)
st2.add_credits(3)
# st2.add_credits(-10) vähentäminenkin toimii, kunhan laittaa miinuksen
st1.add_credits(15)
st3.add_credits(5)

st1.say_hello()
st2.say_hello()
st3.say_hello()

print("*==========*")
# Luodaan 10 uutta opiskelijaa lisää ja tallennetaan viittaukset listaan
'''
students = []
for i in range(10):
    new_student = Student("Opiskelija " + str(i))
    new_student.add_credits(30)
    students.append(new_student)
# lisätään myös aiemmin luotujen kahden opiskelijaolion viittaukset listalle
students.append(st1)
students.append(st2)
# Käydään kaikki listalla olevat opiskelijat läpi
for student in students:
    student.say_hello()
    '''
# 25.10.2023 Assosiaatio(Ulla)
print(f"Oppilaita on yhteensä {Student.count}.")

course1 = Course("Ohjelmisto1")
course1.check_coursename()
course2 = Course("Ohjelmisto2")
course2.check_coursename()

# lisätään oppilaista kursseille
course1.students.append(st1)
course1.students.append(st2)
course1.check_students_on_course()
# on parempi käyttää metodia, kuin appendata yksitellen kökösti
# student-olio(tai oikeastaan viittaus siihen) annetaan metodikutsuun parametrina
course2.add_student(st2)
course2.add_student(st3)
course2.check_students_on_course()
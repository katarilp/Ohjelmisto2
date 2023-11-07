import mysql.connector

def yhdistaDB():
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password="00520",
        autocommit=True
    )
    return yhteys

def haeICAO(koodi):
    yhteys = yhdistaDB()
    sql = "SELECT name, municipality FROM airport"
    sql += "WHERE ident='" + koodi + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    print(tulos)


icao = input("Anna icao> ")
haeICAO(icao)


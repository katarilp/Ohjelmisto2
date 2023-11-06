from flask import Flask
app = Flask()
# tuottaa olion, jolla on palvelinominaisuudet
# @ sitoo reitin(kuorruttaa funktion) sen perässä olevaan toimintaan
@app.route('/')
def get_root():



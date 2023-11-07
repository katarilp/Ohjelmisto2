from flask import Flask, request, Response
import json

# request on eri asia kuin moduuli12 requests-kirjasto (tulee flask-paketista)
app = Flask(__name__)
# tuottaa olion, jolla on palvelinominaisuudet
# jos on käynnistetty tästä, nimi on __main__(materiaalin if-lauseessa käytetään nimeä määrittelyyn)

# @ sitoo reitin(kuorruttaa funktion) sen perässä olevaan toimintaan
@app.route('/') # dekoraattori eli reitti
def get_root():
    return 'Moro' # jos tässä kohtaa kirjoittaa selaimeen 'localhost:5000' aukeaa html-sivu, jossa lukee Moro
# 5000 on flaskin oletusportti, mutta sen voi muuttaa. 5000 voi olla varattu jollekin muulle ohjelmalle

''' Old-school tapa
@app.route(')/kukkuu') #kun lisätään uutta, pitää aina sulkea ja avata yhteys uudelleen, että ne latautuvat
def get_kukkuu():
    print(request.args) # hakee selaimen http-pyyntöön annetun parametrin (esim localhost:3000/kukkuu?name=Matti)
    name = request.args.get("name")
    return f"No kukkuu vaan, {name}!"'''

@app.route('/kukkuu/<name>/<age>') # http://localhost:3000/kukkuu/Matti
def get_kukkuu_v2(name, age):
    return f"No kukkuu vaan, {name} {age}!"

# parametrit lisätään pötköön &-merkillä (?name=Matti&age=25&country=China) jo skäytetään get.args
# toisessa versiossa ne laitetaan /-merkillä (...kukkuu/Matti/25)

# esim. http://localhost:3000/multiply/5
# response jasoniksi '{num: 5, result: 25}'
# rajoitetaan num 0-100
@app.route('/multiply/<num>')
def multiply(num): # https://flask.palletsprojects.com/en/3.0.x/errorhandling/#error-handlers
    try:
        num = int(num)
    except ValueError:
        response_data = {
            "msg": "Input in not a number",
            "input_num": num
        }
        status_code = 400
    else:
        if 0 < num < 100:
            result = num * num
            response_data = {
            "msg": "Calculation done",
            "input_num": num,
            "result": result
            }
            status_code = 200
        else:
            response_data = {
            "msg": "Input is out of bounds",
            "input_num": num
            }
            status_code = 400

    response_data = json.dumps(response_data)
    response = Response(response=response_data, status=status_code, mimetype="application/json")
    return response


app.run(use_reloader=True, port=3000)
# reloader lataa lisäykset ilman yhteyden uudelleenkäynnistystä, kun tiedoston tallentaa

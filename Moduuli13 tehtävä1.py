'''Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.'''

from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/')
def get_root():
    return '1. tehtävä'


@app.route('/alkuluku/<number>')
def get_alkuluku(number):
    number = int(number)
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            response_data = {
                f"Number: {number}, isPrime: {is_prime} ."
            }
            response_data = str(response_data)
            return response_data
    if is_prime == True:
        response_data = {
            f"Number: {number}, isPrime: {is_prime}"
            }
        response_data = str(response_data)
        return response_data
    response_data = json.dumps(response_data)
    response = Response(response=response_data, status=200, mimetype="application/json")
    return response


app.run(use_reloader=True, port=3000)
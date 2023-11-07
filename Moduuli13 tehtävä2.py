from flask import Flask, request, Response
import json
import tietokantahaku13

app = Flask(__name__)

@app.route('/') # dekoraattori eli reitti
def get_root():
    return 'Moro'

@app.route('/kentta/<icao>')
def haku(icao):
    try:
        kentta, kaupunki = tietokantahaku13.haeICAO(icao)
        status_code = 200
        response_data = {
            "ICAO": icao,
            "Name": kentta,
            "Municipality": kaupunki
        }

    except ValueError:
        response_data = {
            "msg": "Virheellinen ICAO-koodi."
        }
        status_code = 400

        response_data = json.dumps(response_data)
        response = Response(response=response_data, status=status_code, mimetype="application/json")
        return response

    app.run(use_reloader=True, port=3000)
@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")
from datetime import datetime
import requests
from . import coinApi_periodos, config

class APIError(Exception):
    pass


class CryptExchangeModel():
    def __init__(self, origin='BTC', dest="EUR"):
        self.origin = origin
        self.dest = dest
        self.data = {}

    def obtener(self):
        endpoint = "exchangerate/{}/{}"
        authHeader = {"X-CoinAPI-Key": config['API_KEY']}

        url = config["URL_PROVIDER"] + endpoint.format(self.origin, self.dest)
        print(url)
        respuesta = requests.get(url, headers=authHeader)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            datos.pop('src_side_base')
            datos.pop('src_side_quote')
            self.data = datos
        elif respuesta.status_code < 500:
            self.data = respuesta.json()
            raise APIError(f"Se ha producido un error {respuesta.status.code} en la consulta de la API")
        else:
            raise APIError(f"Se ha producido un error {respuesta.status.code} en la consulta de la API")


class CryptHistoryModel():
    def __init__(self, fini=None, ffin=None, cripto='BTC', base='EUR', intervalo='1SEC'):
        if not ffin:
            self.ffin = datetime.utcnow()

        if not fini:
            self.fini = datetime.utcnow()

        self.cripto = cripto
        self.base = base
        self.intervalo = intervalo
        self.data = {}

    def obtener(self):
        endpoint = "exchangerate/{}/{}/history?time_start={}&time_end={}&period_id={}"
        authHeader = {"X-CoinAPI-Key": config['API_KEY']}

        url = config['URL_PROVIDER'] + endpoint.format(self.cripto, 
                                                       self.base, 
                                                       self.fini.strftime("%Y%m%dT000000"),
                                                       self.ffin.strftime("%Y%m%dT%H%M%S"),
                                                       self.intervalo)
        print(url)
        respuesta = requests.get(url, headers=authHeader)
        if respuesta.status_code == 200:
            self.data = respuesta.json()
        elif respuesta.status_code < 500:
            self.data = respuesta.json()
            raise APIError("Se ha producido un error 400 en la consulta de la API")
        else:
            raise APIError(f"Se ha producido un error {respuesta.status.code} en la consulta de la API")
        




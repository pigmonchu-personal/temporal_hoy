import configparser
from os import environ

coinApi_periodos = ['SEC', ('segundos', [1 ,2, 3, 4, 5, 6, 10, 15, 20 , 30]),
               'MIN', ('minutos', [1 ,2, 3, 4, 5, 6, 10, 15, 20 , 30]),
               'HRS', ('horas', [1 ,2, 3, 4, 6, 8, 12]),
               'DAY', ('días', [1 ,2, 3, 5, 7, 10])
    ]


api = environ['API']
config = configparser.ConfigParser()
config.read('config.ini')
config = config[api]

import requests
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def esmoneda(cripto):
    criptos = ["BTC", "LTC", "ETH"]
    if cripto.upper() in criptos:
        return True
    else:
        return False

    


def micodigo(codigo):
    return codigo == "2t4y22arty"


def precio(moneda):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '50153e7b-d211-4eff-8c58-04e710fb790f',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        pass

    monedas_dict={}
    for cripto in data["data"]:
        if moneda == cripto["symbol"]:
            return cripto["quote"]["USD"]["price"]

def obtener_cantidad_cripto(nombre_archivo,crypto):
    
    archivo = open(nombre_archivo,"r")    
    texto = archivo.read()
    archivo.close()
    
    lineas = texto.splitlines()    
    
    diccionario={}
    for linea in lineas:
        termino = linea.split(":")        
        diccionario[termino[0]]=termino[1]
      
    return diccionario.get(crypto)

def actualizar_dato(archivo,buscar,reemplazar):
	"""
	Función cambia una linea entera de un archivo
	Tiene que recibir el nombre del archivo, la cadena a buscar,
    y la cadena a reemplazar si la linea coincide con buscar
	"""

	with open(archivo, "r") as f:
		lines = (line.rstrip() for line in f)

		altered_lines = [reemplazar if line==buscar else line for line in lines]

	with open(archivo, "w") as f:
		f.write('\n'.join(altered_lines) + '\n')

def insertar_transaccion(cripto, operacion, codigo_user, cantCripto, cotiUSD):

    nombre_archivo = "Transacciones.txt"

    archivo = open(nombre_archivo,"a")
    archivo.write("\n" + "Fecha: " + time.strftime("%c") + " ! Moneda: " + cripto + " ! Operación: " + operacion + " ! Código de usuario: " + codigo_user + " ! Cantidad: " + str(cantCripto) + " ! Monto en USD: " + str(cotiUSD) + " !" )
    archivo.close()

def obtener_cantidad_cripto(nombre_archivo,moneda):

    archivo = open(nombre_archivo,"r")
    texto = archivo.read()
    archivo.close()

    lineas = texto.splitlines()

    diccionario={}
    for linea in lineas:
        termino = linea.split(":")
        diccionario[termino[0]]=termino[1]
    print(diccionario)
    return diccionario[moneda]

def obtener_balance_cripto(nombre_archivo,moneda):

    archivo = open(nombre_archivo,"r")
    texto = archivo.read()
    archivo.close()

    lineas = texto.splitlines()

    diccionario={}
    for linea in lineas:
        termino = linea.split(":")
        diccionario[termino[0]]=termino[1]
    return diccionario[moneda]




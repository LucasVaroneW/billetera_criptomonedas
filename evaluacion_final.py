from symtable import Symbol
from funciones import *
import requests


moneda= ""
headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  '50153e7b-d211-4eff-8c58-04e710fb790f'}
parametros = {'symbol': moneda}
requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros)

saldo=800
monedaDigital=["BTC", "LTC", "ETH"]
nombre_archivo = "criptomonedas.txt"

print("\t.:MENU:.")
print("1. Recibir dinero")
print("2. Transferir")
print("3. Balance de moneda")
print("4. Balance general")
print("5. Historial de transferencia")
print("6. Salir del programa")
opcion = int(input("Que desea Hacer (Ingrese una opción valida): "))
print()

# ------------------------------------------------- RECIBIR CANTIDAD -------------------------------------------------

def getCant(moneda):
    cantidad = str(input("Ingrese la cantidad de " + moneda.upper() + ": "))
    while not (cantidad.isdigit() and int(cantidad) >= 0):
        cantidad = input("ERROR! Ingrese la cantidad de " + moneda.upper() + ": ")
    return cantidad

def obtenerMoneda():
    moneda = input("Ingrese la moneda Digital (Ej: BTC): ")
    while not esmoneda(moneda):
        moneda = input("ERROR! Ingrese una correcta la moneda Digital (Ej: BTC): ")
    return moneda.upper()

if opcion==1:
    moneda = obtenerMoneda()
    cantidad = getCant(moneda)


    codigo = input("Ingrese su código: ")
    if not micodigo(codigo):
        print('Codigo validado')

        cantidad_original = obtener_cantidad_cripto("criptomonedas.txt", moneda)
        print(cantidad_original)

        cotiUSD = precio(moneda)
        total = float(cantidad) * float(cotiUSD)

        print("Moneda: " + moneda)
        print("Cantidad a recibir: " + cantidad)
        print("El precio de la moneda " + moneda + " en dólares es: USD " + str(cotiUSD))
        print("Total a recibir en: USD " + str(total))

        nuevo_monto = float(cantidad_original) + float(cantidad)

        actualizar_dato(nombre_archivo, moneda + ':' + cantidad_original, moneda + ':' + str(nuevo_monto))

        insertar_transaccion(moneda, 'Recibir Criptomoneda',codigo, cantidad, cotiUSD)

        input("\nPresione una tecla para volver al menú principal")


    else:
        print("El código utilizado es igual al código de la billetera personal, función inválida")
        opcion==1

# ------------------------------------------------- TRANSFERIR MONTO -------------------------------------------------
if opcion==2:
    moneda = obtenerMoneda()
    cantidad = getCant(moneda)


    codigo = input("Ingrese su código: ")
    if not micodigo(codigo):
        print('Codigo validado')

        cantidad_original = obtener_cantidad_cripto("criptomonedas.txt", moneda)
        print(cantidad_original)

        cotiUSD = precio(moneda)
        total = float(cantidad) * float(cotiUSD)

        print("Moneda: " + moneda)
        print("Cantidad a transferir: " + cantidad)
        print("El precio de la moneda " + moneda + " en dólares es: USD " + str(cotiUSD))
        print("Total a transferir en: USD " + str(total))

        nuevo_monto = float(cantidad_original) - float(cantidad)

        actualizar_dato(nombre_archivo, moneda + ':' + cantidad_original, moneda + ':' + str(nuevo_monto))

        insertar_transaccion(moneda, 'Transferir Criptomoneda',codigo, cantidad, cotiUSD)

        input("\nPresione una tecla para volver al menú principal")


    else:
        print("El código utilizado es igual al código de la billetera personal, función inválida")
        opcion==2
# ------------------------------------------------- BALANCE MONEDA -------------------------------------------------
if opcion==3:
    moneda = obtenerMoneda()

    cantidad_original = obtener_cantidad_cripto("criptomonedas.txt", moneda)
    print(cantidad_original)

    cotiUSD = precio(moneda)
    total = float(cantidad_original) * float(cotiUSD)

    print("Moneda: " + moneda)
    print("El precio de la moneda " + moneda + " en dólares es: USD " + str(cotiUSD))
    print("La cantidad de " + moneda +" es "+ cantidad_original)


    input("\nPresione una tecla para volver al menú principal")

# ------------------------------------------------- BALANCE GENERAL -------------------------------------------------
if opcion==4:
    monedaBTC="BTC"
    monedaLTC="LTC"
    monedaETH="ETH"

    cantidad_originalBTC = obtener_balance_cripto("criptomonedas.txt", monedaBTC)
    cotiUSD = precio(monedaBTC)
    total = float(cantidad_originalBTC) * float(cotiUSD)
    print("Moneda: " + monedaBTC)
    print("El precio de la moneda " + monedaBTC + " en dólares es: USD " + str(cotiUSD))
    print("La cantidad de " + monedaBTC + " es " + cantidad_originalBTC)

    cantidad_originalLTC = obtener_balance_cripto("criptomonedas.txt", monedaLTC)
    cotiUSD = precio(monedaLTC)
    total = float(cantidad_originalLTC) * float(cotiUSD)
    print("Moneda: " + monedaLTC)
    print("El precio de la moneda " + monedaLTC + " en dólares es: USD " + str(cotiUSD))
    print("La cantidad de " + monedaLTC + " es " + cantidad_originalLTC)

    cantidad_originalETH = obtener_balance_cripto("criptomonedas.txt", monedaETH)
    cotiUSD = precio(monedaETH)
    total = float(cantidad_originalETH) * float(cotiUSD)
    print("Moneda: " + monedaETH)
    print("El precio de la moneda " + monedaETH + " en dólares es: USD " + str(cotiUSD))
    print("La cantidad de " + monedaETH + " es " + cantidad_originalETH)

    input("\nPresione una tecla para volver al menú principal")

# ------------------------------------------------- HISTORIAL -------------------------------------------------
if opcion==5:
    nombre_archivo1 = "transacciones.txt"

    mensaje = "Resumen de transacciones efectuadas a la fecha:"

    print('-' * len(mensaje))
    print(mensaje)
    print('-' * len(mensaje))

    archivo = open(nombre_archivo1,"r")
    texto = archivo.read()

    print ("\n" + texto.replace("!","\n"))
    archivo.close()

    input("\nPresione una tecla para volver al menú principal")


import pymongo
import json

MONGO_TIME_OUT = 1000
MONGO_USER = "" # Usuario
MONGO_KEY = "" # Contraseña
MONGO_URL = f"mongodb+srv://{MONGO_USER}:{MONGO_KEY}@cluster0.do5eava.mongodb.net/test"

#Creamos la conexión con MongoDB
#Anticipamos errores de ejecución usando 'TRY y EXCEPT'
try:
    #Variable cliente que se va a conectar al cliente de Mongo
    cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS = MONGO_TIME_OUT)
    #Pedimos la información de conexión
    cliente.server_info()
    #mostramos mensaje de conexión correcta
    print("Conexion con mongo exitosa")
    #cerramos conexión
    cliente.close()
#Vamos a recoger los posibles errores que pudiéramos tener, en este caso, exceso de tiempo de respuesta
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    #mostramos mensaje en tal caso
    print("Tiempo excedido de carga")
#también recogemos el posible error de conexión
except pymongo.errors.ConnectionFailure as errorConexion:
    #mostramos un m ensaje en tal caso
    print("Fallo al conectarse a mongodb: "+errorConexion)

MONGO_BASEDATOS = "EstadosUnidos"
MONGO_COLECCION = "Estados"

try:
    cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS = MONGO_TIME_OUT)
    base_datos = cliente[MONGO_BASEDATOS]
    coleccion = base_datos[MONGO_COLECCION]

    coleccion.insert_one(
        {
        "Estado": "SouthCarolina", 
        "Poblacion_2000" : 4012012, 
        "Poblacion_2001": 4023438, 
        "Residentes_menores65_2000": 3535770, 
        "Residentes_menores65_2001": 3567172, 
        "Muertes_2000": 8581, "Muertes_2001": 9500, 
        "Latitud" : 33.687439, 
        "Longitud": -80.436374, 
        "Anio_fundacion" : "26-03-1776" 
    })

    cliente.close()

except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga")
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb" + errorConexion)
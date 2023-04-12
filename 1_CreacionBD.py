import pymongo

MONGO_TIME_OUT = 1000
MONGO_USER = "marqos_neo" #Poner tu Usuario
MONGO_KEY = "123456marcos" #Poner tu Contraseña
MONGO_URL = f"mongodb+srv://{MONGO_USER}:{MONGO_KEY}@cluster0.do5eava.mongodb.net/test"

# Partimos de una lista de estados con sus datos, lo mismo que se plateó en el Reto Grupal 1
EstadosUnidos = [
    {
        "Estado": "Alabama", 
        "Poblacion_2000" : 4447100, 
        "Poblacion_2001": 4451493, 
        "Residentes_menores65_2000": 3870598, 
        "Residentes_menores65_2001": 3880476, 
        "Muertes_2000": 10622, 
        "Muertes_2001": 15912, 
        "Latitud" : 33.258882, 
        "Longitud" : -86.829534, 
        "Anio_fundacion" : "14-12-1819"
    },
    {
        "Estado": "Florida", 
        "Poblacion_2000" : 15982378, 
        "Poblacion_2001": 17054000, 
        "Residentes_menores65_2000": 13237167, 
        "Residentes_menores65_2001": 13548077, 
        "Muertes_2000": 38103, 
        "Muertes_2001": 166069, 
        "Latitud" : 27.756767, 
        "Longitud" :-81.463983, 
        "Anio_fundacion": "03-03-1845"
    },
    {
        "Estado": "Georgia", 
        "Poblacion_2000" : 8186453, 
        "Poblacion_2001": 8229823, 
        "Residentes_menores65_2000": 7440877, 
        "Residentes_menores65_2001": 7582146, 
        "Muertes_2000": 14804, "Muertes_2001": 15000, 
        "Latitud" : 32.329381, 
        "Longitud" : -83.113737, 
        "Anio_fundacion": "12-02-1733"
    }
]

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
# Vamos a recoger los posibles errores que pudiéramos tener.
# En este caso, exceso de tiempo de respuesta.
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

    for estado in EstadosUnidos:
        coleccion.insert_one(estado)

    cliente.close()

except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga")
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb" + errorConexion)

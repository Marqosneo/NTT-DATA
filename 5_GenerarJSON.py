import pymongo
import json

MONGO_TIME_OUT = 1000
MONGO_USER = "marqos_neo" #Usuario
MONGO_KEY = "123456marcos"  #Contraseña
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
    
    # Obtenemos todos los documentos de la colección y los guardamos en un archivo json
    with open('EstadosUnidos.json', 'w') as file:
        estados = list(coleccion.find())
        #El atributo que se genera automáticamente id_, nos da problemas con el formato JSON, por eso lo eliminamos
        # Eliminación del campo ObjectId
        for estado in estados:
            estado.pop('_id', None)
        # Creamos JSON    
        json.dump(estados, file)

    cliente.close()

except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga")
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb" + errorConexion)

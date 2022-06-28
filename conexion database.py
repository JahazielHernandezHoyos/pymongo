from pymongo import MongoClient
from pymongo.collation import Collation

#uri = "mongodb://localhost:27017"
basedatos = MongoClient(
    "mongodb://localhost:27017"
)

# imprime las colecciones creadas
print(basedatos.list_database_names())

# conecta con la coleccion especificada en este caso raspberry
collection = basedatos.invernadero.raspberry

# insertar un registro
collection.insert_one({'"temperatura"': '1',
                      '"luz"': '1', '"humedad"': '1', '"one"': '1'})

# Traer todos los registros encontrados
for registro in collection.find():
    print(registro)

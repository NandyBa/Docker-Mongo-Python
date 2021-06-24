from pymongo import MongoClient #Module nécessaire pour intéragir avec la base de donnée MongoDB

#Etape 1: Connection au serveur MongoDB
client = MongoClient('mongodb:27017')
db=client.collection

#Etape 2: Insertion dans la base de données 
cours = {
    'id' : 1,
    'type': "Maths"
}
result=db.collection.insert_one(cours)
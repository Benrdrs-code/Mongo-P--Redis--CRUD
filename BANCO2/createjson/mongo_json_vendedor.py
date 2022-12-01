from pymongo import MongoClient
import pandas
import json
import time

def create_json():
  mongo_client = MongoClient('localhost', 27017)
  db = mongo_client.bancoNAME
  col = db.vendedor

  start_time = time.time()

  #  faça uma chamada de API para o servidor MongoDB
  cursor = col.find()

  # extrair a lista de documentos do cursor obj
  mongo_docs = list(cursor)

  # restringir o número de documentos para exportar
  mongo_docs = mongo_docs[:999]

  # cria um DataFrame vazio para armazenar documentos
  docs = pandas.DataFrame(columns=[])

  
  for num, doc in enumerate(mongo_docs):
    doc["_id"] = str(doc["_id"])
    doc_id = doc["_id"]
    series_obj = pandas.Series( doc, name=doc_id )
    docs = docs.append(series_obj)
    if num % 10 == 0:
      print (type(doc))
      print (type(doc["_id"]))
      print (num, "--", doc, "\n")
  docs.to_json("Vendedor.json")
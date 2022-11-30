from pymongo import MongoClient
import pprint  # Mesmo resultado do `pretty()`

client = MongoClient('localhost', 27017)  # Conectando ao banco
db = client['bancoNAME']  # selecionando o banco de dados
collection = db['produtos']  # selecionando a collection

query = collection.find()

for n in query:  # iterando os dados
    print(n)
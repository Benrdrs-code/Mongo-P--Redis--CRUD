import redis
import pymongo
from direct_redis import DirectRedis

cliente =  pymongo.MongoClient('mongodb://localhost:27017')

clienteRedis = DirectRedis(host='localhost', port=6379, db=0)
if(clienteRedis):
  print(1)
else:
  print(0)


bancoRedis = cliente.MercadoLivre
minhaColuna = bancoRedis.Usuario
minhaBusca = {'nome': ''}
x = minhaColuna.find_one(minhaBusca)

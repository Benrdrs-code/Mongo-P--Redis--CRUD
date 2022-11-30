from bson.objectid import ObjectId
import Vendedor.buscarVendedor as buscar

def deletarVendedor (bancoRedis):
    minhaColuna = bancoRedis.vendedor
    buscar.procurarTodesVendedor(bancoRedis)

    id = input(str('Qual o ID do Vendedor você quer deletar? '))
    minhaColuna.delete_one({'_id':ObjectId(id)})
    print('Vendedor deletado')


from bson.objectid import ObjectId
import Produto.buscarProduto as buscar

def deletarProduto (meuBanco):
    minhaColuna = meuBanco.produtos
    buscar.procurarTodesProduto(meuBanco)

    id = input(str('Qual o Id do Produto você quer deletar? '))
    minhaColuna.delete_one({'_id':ObjectId(id)})
    print('Produto deletado')


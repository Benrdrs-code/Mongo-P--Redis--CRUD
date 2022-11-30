from bson.objectid import ObjectId
import Usuario.buscarUsuario as buscar

def deletarUsuario (meuBanco):
    minhaColuna = meuBanco.Usuario
    buscar.procurarTodesUsuario(meuBanco)

    id = input(str('Qual o ID você quer deletar? '))
    minhaColuna.delete_one({'_id':ObjectId(id)})
    print('Usuario deletado')


from multiprocessing.spawn import import_main_path
import pymongo
import Usuario.atualizarUsuarior as atualizarUsuario
import Usuario.buscarUsuario as buscarUsuario
import Usuario.cadastrarUsuario as cadastrarUsuario
import Usuario.deletarUsuario as deletarUsuario
import Produto.atualizarProduto as atualizarProduto
import Produto.buscarProduto as buscarProduto
import Produto.cadastrarProduto as cadastrarProduto
import Produto.deletarProduto as deletarProduto
import Vendedor.cadastrarVendedor as cadastrarVendedor
import Vendedor.buscarVendedor as buscarVendedor
import Vendedor.atualizarVendedor as atualizarVendedor
import Vendedor.deletarVendedor as deletarVendedor
import Compra.cadastrarCompra as cadastrarCompra
import Compra.buscarCompra as buscarCompra
import Compra.atualizarCompra as atualizarCompra
import Compra.deletarCompra as deletarCompra
import redis
from direct_redis import DirectRedis


cliente =  pymongo.MongoClient('mongodb://localhost:27017')
meuBanco = DirectRedis(host='localhost', port=6379, db=0)

meuBanco = cliente.bancoNAME
loop = True
while loop:
    print('''  
    1 - CRUD Usuario \n 
    2 - CRUD Produto\n
    3 - CRUD Vendedor\n
    4 - CRUD Compra\n
    ''')
    opcao = input(str("Escolha uma opção para fazer o crud: "))
    match opcao:
        case '1':
            print('''  
                1 - Cadastrar Usuario \n 
                2 - Atualizar Usuario \n
                3 - Buscar Usuario \n
                4 - Buscar todos Usuarios \n
                5 - Deletar Usuario \n
                0 - Sair \n ''')
            opcaoUsuario = input(str("Escolha uma opção: "))
        
            match opcaoUsuario:
                case '1':
                    cadastrarUsuario.cadastrarUsuario(meuBanco)
                case '2':
                    atualizarUsuario.atualizarUsuario(meuBanco)
                case '3':
                    buscarUsuario.procurarUsuario(meuBanco)
                case '4':
                    buscarUsuario.procurarTodesUsuario(meuBanco)
                case '5':
                    deletarUsuario.deletarUsuario(meuBanco)
                case '0':
                    loop = False

        case '2':
            print('''  
                1 - Cadastrar Produto \n 
                2 - Atualizar Produto \n
                3 - Buscar Produto \n
                4 - Buscar todos os Produtos \n
                5 - Deletar Produtos \n
                0 - Sair \n ''')
            opcaoProduto = input(str("Escolha uma opção: "))
        
            match opcaoProduto:
                case '1':
                    cadastrarProduto.cadastrarProduto(meuBanco)
                case '2':
                    atualizarProduto.atualizarProduto(meuBanco)
                case '3':
                    buscarProduto.procurarProduto(meuBanco)
                case '4':
                    buscarProduto.procurarTodesProduto(meuBanco)
                case '5':
                    deletarProduto.deletarProduto(meuBanco)
                case '0':
                    loop = False
                
        case '3':
            print('''  
                1 - Cadastrar Vendedor \n 
                2 - Atualizar Vendedor \n
                3 - Buscar Vendedor \n
                4 - Buscar todos os Vendedor \n
                5 - Deletar Vendedor \n
                0 - Sair \n ''')
            opcaoVendedor = input(str("Escolha uma opção: "))
        
            match opcaoVendedor:
                case '1':
                    cadastrarVendedor.cadastrarVendedor(meuBanco)
                case '2':
                    atualizarVendedor.atualizarVendedor(meuBanco)
                case '3':
                    buscarVendedor.procurarVendedor(meuBanco)
                case '4':
                    buscarVendedor.procurarTodesVendedor(meuBanco)
                case '5':
                    deletarVendedor.deletarVendedor(meuBanco)
                case '0':
                    loop = False
        

        case '4':
            print('''  
                1 - Cadastrar Compra \n 
                2 - Atualizar Compra \n
                3 - Buscar Compra \n
                4 - Buscar todas as Compra \n
                5 - Deletar Compra \n
                0 - Sair \n ''')
            opcaoCompra = input(str("Escolha uma opção: "))
        
            match opcaoCompra:
                case '1':
                    cadastrarCompra.cadastrarCompra(meuBanco)
                case '2':
                    atualizarCompra.atualizarCompra(meuBanco)
                case '3':
                    buscarCompra.procurarCompra(meuBanco)
                case '4':
                    buscarCompra.procurarTodesCompra(meuBanco)
                case '5':
                    deletarCompra.deletarCompra(meuBanco)
                case '0':
                    loop = False
        
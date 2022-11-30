def procurarProduto(meuBanco):
    minhaColuna = meuBanco.produtos
    minhaBusca = {'nomeProduto': 'gin'}
    x = minhaColuna.find(minhaBusca)

    for a in x:
        print(a)

def procurarTodesProduto (meuBanco):
    minhaColuna = meuBanco.produtos

    for x in minhaColuna.find():
        print(x)
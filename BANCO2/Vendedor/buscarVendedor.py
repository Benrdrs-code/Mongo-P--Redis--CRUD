def procurarVendedor (bancoRedis ) :
    minhaColuna = bancoRedis.vendedor
    minhaBusca = {'nome': 'Natalia'}
    x = minhaColuna.find(minhaBusca)

    for a in x :
        print(a)

def procurarTodesVendedor (bancoRedis):
    minhaColuna = bancoRedis.vendedor

    for x in minhaColuna.find ():
        print(x)
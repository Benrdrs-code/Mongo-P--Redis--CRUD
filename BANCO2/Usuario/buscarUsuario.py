def procurarUsuario (meuBanco ) :
    minhaColuna = meuBanco.Usuario
    minhaBusca = {'nome': 'Lira'}
    x = minhaColuna.find(minhaBusca)

    for a in x :
        print(a)

def procurarTodesUsuario (meuBanco):
    minhaColuna = meuBanco.Usuario

    for x in minhaColuna.find ():
        print(x)
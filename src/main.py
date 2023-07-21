from views import view

if __name__ == '__main__':
    mensagem = '!rank engibee'
    comando = mensagem.split(' ')[0]

    argu = mensagem.split(' ')[1:]
    view.do_something(comando, argu)
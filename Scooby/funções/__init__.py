from time import sleep

def selecionar_opção(msg):
    while True:
        try:
            txt = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mErro! Digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[0;31mEntrada de dados interrompida pelo usuário!\033[m")
            return 0
        else:
            return txt

def avaliar_experiencia(msg):
    while True:
        if msg > 5 or 1 > msg:
            print("Opção inválida. Tente novamente")
        else:
            print("\nObrigado! Sua sessão foi encerrada. Volte sempre!")
            break

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastrar(arq, avaliar):
        a = open(arq, 'at') # append text
        a.close()

def criarArquivo(nome):
        a = open(nome, 'wt+')  # write text
        a.close()

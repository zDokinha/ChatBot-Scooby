from Scooby.funções import *
from time import sleep
import webbrowser


nome = str(input("Digite seu nome: ")).lower().capitalize()
idade = selecionar_opção("Digite sua idade: ")

while True:
    print(f"O que gostaria de saber hoje? {nome}")
    print("[1] - Banho e tosa")
    print("[2] - Pets que oferecemos serviços e produtos.")
    print("[3] - Horário de funcionamento.")
    print('[4] - Blog Petz')
    print("[5] - Tipos de Ração.")
    print("[6] - Encerrar ChatBot.")
    resposta = selecionar_opção(">>> ")
    if resposta == 1:
        print("\n\033[33mPetz Estética\033[m"
              "\nTemos uma equipe altamente qualificada e apaixonada por animais pronta para atender "
              "todas as suas necessidades."
              "\nAlém disso, os nossos processos foram definidos pelos melhores profissionais da área, "
              "tornando o banho do seu pet um momento tranquilo, agradável e seguro.\n")
    elif resposta == 2:
        print("\nSão eles:"
              "\n\nCachorros  \nGatos  \nPassáros \nCoelhos \nFurão \nTartarugas \nLagartos "
              "\nPeixes \nHamsters \nPorquinhos da índia\n"
              "Chincilas\n")
    elif resposta == 3:
        print(f"\nLojas Físicas\nSegunda a Domingo - 09:00 ás 20:00.\n"
              f"Feriado - 09:00 ás 18:00. \n\nServiço Online - 24/7.\n")
    elif resposta == 4:
        print("\nNosso blog oferece diversas curisidades sobre seus bichinhos, "
              "vai de opções ideais de nomes para gatos, cachorros,\naté "
              "informações importantes, por exemplo, prevenção de doenças como a cinomose.")
        print('Te redicionaremos para o site...')
        sleep(3)
        webbrowser.open("https://www.petz.com.br/blog/")
    elif resposta == 5:
        print("\nNão sabe qual o tipo de ração ideal para o seu pet? \n"
              "\nFalaremos algumas características sobre cada uma delas para que essa escolha se torne mais fácil: \n"
              # RAÇÃO SECA
              "\n\033[33mRação seca\033[m\nA ração seca é mais prática, dura mais e é mais fácil de ser armazenada,"
              "podendo ficar por mais tempo no pote de comida para o cachorro. "
              "\nOutro ponto muito positivo da ração seca é limpar os dentes do animal no momento da "
              "mastigação é mais prática,\n"
              "dura mais e é mais fácil de ser armazenada, "
              "podendo ficar por mais tempo no pote de comida para o cachorro.\n"
              # RAÇÃO ÚMIDA
              "\n\033[33mRação úmida\033[m\nAs rações úmidas trazem o benefício de possuírem concentração de "
              "80% de líquido, "
              "ajudando a hidratar o animal relutante em beber água. \nPor conta disso, "
              "problemas renais e hepáticos acabam sendo prevenidos."
              " \nE Oferecem todos os nutrientes e balanço hídrico necessários aos animais de estimação.\n"
              # RAÇÃO NATURAL
              "\n\033[33mRação natural\033[m\nA ração natural contém ingredientes de maior valor nutricional. "
              "\nPor esse motivo, a quantidade de vitaminas, fibras, minerais e similares é "
              "bem mais alta do que a ração comum. "
              "\nElas também oferecem um volume adequado de proteína animal, algo "
              "indispensável para a saúde dos pets.\n")
    elif resposta == 6:
        print("Avalie sua experiência:\n[1]Péssima\n[2]Ruim\n[3]OK\n[4]Boa\n[5]Excelente:")
        option = selecionar_opção(">>> ")
        quit()

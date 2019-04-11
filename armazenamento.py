import time  # importa biblioteca para receber a hora do sistema
import playsound  # importa biblioteca para tocar a música
import random  # importa biblioteca para escolher randomicamente a música

lista_alarmes_seg = []  # lista de alarmes convertidos em segundos
lista_alarmes = []  # lista de alarmes na forma original


def mensagem_entrada():  # mensagem que irá recepcionar o usuário
    print("-----------------------------")
    print("\nBem vindo ao DesPHYtador!\n")
    print("-----------------------------")


def exibir_opcoes():  # exibe o menu de opções para o usuário escolher o que deseja executar
    print('1 - Cadastrar alarme')
    print('2 - Lista de alarmes')
    print('3 - Remover alarme')
    print('4 - Sair')


def ler_opcao():  # ler do usuário a opção que deseja executar do menu
    try:
        opcao = int(input('\nQual operação deseja executar?: '))
        return opcao  # retorna a opção do usuário
    except:
        print("Erro de entrada!")  # caso o usuário digite um valor diferente dos que estão do menu
        ler_opcao()  # e depois pede novamente a opção que o usuário deseja executar


def musica():  # função para tocar uma música de acordo com a o item da lista que é escolhido de forma aleatória
    lista = [0, 1, 2]

    resultado_musica = random.choice(lista)
    print('Tocando música: ', resultado_musica)

    if resultado_musica == 0:
        playsound.playsound('musica1.mp3')
    elif resultado_musica == 1:
        playsound.playsound('musica2.mp3')
    elif resultado_musica == 2:
        playsound.playsound('musica3.mp3')


def cadastrar(alarm, lista):  # função que cadastra o alarme em um das listas
    if not alarme_existe(alarm, lista):  # testando a existência
        lista.append(alarm)  # adicionando a entrada do usuário na lista
    return lista  # retornando lista


def ler_alarme():  # função que recebe do usuário a hora do alarme
    try:
        alarm = int(input('Insira a hora (HHMMSS; formato 12h): '))
        while True:  # esse while serve para tratar erro do formato de entrada do cadastro do alarme, já que o
            # formato é de 12 hrs
            if 10000 <= alarm <= 125959:
                break
            else:
                alarm = int(input('Hora errada! Insira o formato correto (HHMMSS em 12h): '))
                break
        return alarm
    except:
        ler_alarme()


def formato(alarm):  # função que recebe o formato e a partir disso transforma a hora em segundos
    forma = int(input('Insira o formato da hora (0 para am ou 1 para pm): '))

    while True:  # esse while serve para tratar o erro de entrada do formato da hora escolhida pelo usuário

        if forma != 1 and forma != 0:
            print('Formato incorreto!')
            forma = int(input('Insira o formato da hora (0 para am ou 1 para pm): '))
        else:

            alarm = conversao(alarm)  # chamando a função de conversão em segundos
            if forma == 1:
                alarm += 43200  # adicionando mais 12 horas em segundos para transformar em pm
            return alarm


def hora_atual():  # função que recebe a hora atual do sistema
    hora = int((time.strftime('%H%M%S')))
    return hora


def conversao(h):  # função que converte a hora de entrada em segundos
    hr = int(h / 10000)
    m = int((h % 10000) / 100)
    s = int((h % 10000) % 100)

    hr_seg = (hr * 3600) + (m * 60) + s
    return hr_seg


def alarme_tocar(alarmseg, atualseg):  # função que calcula a diferença da hora atual para a hora de toque do alarme
    tocar = alarmseg - atualseg
    if tocar < 0:  # se a diferença for negativa, a diferença será de um dia a mais
        tocar += 86400  # um dia em segundos
    return tocar


def alarme_existe(alarm, lista):  # testa a existência do alarme
    return alarm in lista


def remover_alarme(alarm, lista):  # remove um alarme original da lista pelo índice
    indice = lista.index(alarm)
    del lista[indice]


def funcao_operacao_1(alarm):  # função que converte a hora e a cadastra em suas respectivas listas
    alarmseg = formato(alarm)
    cadastrar(alarm, lista_alarmes)
    cadastrar(alarmseg, lista_alarmes_seg)


def funcao_operacao_2(alarm):  # função que converte a hora e a remove das respectivas listas
    alarmseg = formato(alarm)
    remover_alarme(alarm, lista_alarmes)
    remover_alarme(alarmseg, lista_alarmes_seg)


def existencia1(alarm):  # função que irá conferir se a hora que o usuário deseja remover está cadastrada
    for existencia in lista_alarmes:  # esse for irá pecorrer toda lista de alarmes
        if existencia == alarm:  # se algum dos valores que existencia assumiu da lista for igual ao alarme, a função
            #  retornará verdadeiro
            return True
    return False  # caso não exista
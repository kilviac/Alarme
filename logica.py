import armazenamento as f


def operacoes():  # essa função irá executar as operações que o menu oferta para o usuário, utilizando as funções
    # presentes no armazenamento.
    while True:
        entrada = f.ler_opcao()  # chamando a função pra ler a entrada através da variável 'entrada'
        if 0 < entrada < 5:
            if entrada == 1:
                alarme = f.ler_alarme()  # chama a função de leitura e a operação 1
                f.funcao_operacao_1(alarme)
                print('Alarme cadastrado com sucesso!\n')
                print("Lista de alarmes: ", f.lista_alarmes)

            elif entrada == 2:  # printa a lista de alarmes originais e chama a função operação 2
                print("\nLista de alarmes: ", f.lista_alarmes)

            elif entrada == 3:  # printa a lista de alarmes originais e chama a função operação 2

                print("\nLista de alarmes: ", f.lista_alarmes)
                alarme = int(input("Qual alarme deseja remover? "))

                existencia = f.existencia1(alarme)

                while not existencia:
                    print('Alarme não existente!')
                    alarme = int(input("Qual alarme deseja remover? "))
                    existencia = f.existencia1(alarme)

                f.funcao_operacao_2(alarme)
                print("Lista de alarmes: ", f.lista_alarmes)  # printa a lista com as remoções
                print('Alarme removido com sucesso!')
                print("Lista de alarmes: ", f.lista_alarmes)

            elif entrada == 4:
                print('Obrigada por utilizar nosso sistema de alarme! Aguardando hora do alarme...')
                tocar_musica()
                break
        else:
            print("Opcao incorreta")
            f.exibir_opcoes()


def tocar_musica():  # essa função é responsável por atualizar a hora do sistema (no caso, do meu computador),
    # até que chegue no horário que o usuário cadastrou para tocar o alarme, e então ele tocará.
    while True:
        hora_atual = f.hora_atual()  # chama a função que recebe a hora atual
        hora_atual_seg = f.conversao(hora_atual)  # converte a hora atual em segundos
        for a in f.lista_alarmes_seg:  # para cada elemento da lista de alarmes em segundos, calcula a diferença
            diferenca = f.alarme_tocar(a, hora_atual_seg)
            if hora_atual_seg == a + diferenca:  # se a hora atual for igual a hora do alarme + a diferença
                print('ACORDA!')

                f.musica()  # chama a função de toque do alarme

                print('APERTE O BOTÃO STOP DO CONSOLE PARA PARAR O ALARME')

                break
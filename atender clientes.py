def main():
    opc = int(input(
        "Digite opc: \n1-Incluir cliente na fila\n2-Atender prox cliente\n3-Consultar pos. de um cliente\n4-Imprimir clientes\n5-Sair "))
    fila = []
    clienteatual = 0    #inicializa variável clienteatual como 0
    cont = 0            #inicializa variável cont como 0
    while (opc != 5):   #A estrutura repete até que a opc seja = 5
        if (opc == 1):
            nome = input("Digite o nome do cliente: ")
            aux = [nome, 0]     #insere o nome do cliente e um valor numérico que considerei como -> foi atendido =1, não foi atendido = 0
            fila.append(aux)    #insere a lista aux dentro de fila [[nome, foi atendido]]
        elif (opc == 2):
            if (clienteatual < (len(fila))): #só atende o cliente se tiver clientes para atender, por isso, pergunta se clienteatual < tamanho da fila
                fila[clienteatual][1] = 1    #diz que o valor foi atendido para o clienteatual é igual a 1
                print("O cliente foi atendido com sucesso\n")
                clienteatual += 1            #pula para o próximo cliente
            else:
                print("Não é possível antender porque não tem cliente para antender")
        elif (opc == 3):
            nome = input("Digite o nome do indivíduo que deseja pesquisar a posição: ")
            achou = False               #inicializa a variável achou
            for i in range(0, len(fila)):   #para cada i em (0 até tamanho da lista)
                if (fila[i][0] == nome):    #o elemento [i][0] corresponde a string nome?
                    achou = True            #Se sim, achou = True
                elif (fila[i][0] != nome and achou == False):  #se não corresponder e não tiver achado ainda
                    cont += 1                                  #então soma o contador de posição
            if (achou):                                        #se achou = true
                print("A posição do indivíduo é: ", cont)      #imprime a posição do elemento
                cont = 0                                       #zera o contador
        elif (opc == 4):
            print(fila)
        elif (opc == 5):
            break
        #pergunta as opções novamente para continuar a repetição
        opc = int(input(
            "Digite opc: \n1-Incluir cliente na fila\n2-Atender prox cliente\n3-Consultar pos. de um cliente\n4-Imprimir clientes\n5-Sair "))

if __name__ == "__main__":
    main()

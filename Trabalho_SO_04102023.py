'''O escalonamento Round Robin é um método de gerenciamento de processos em que há um quantum, ou seja, um período de 
tempo fixo durante o qual um processo é permitido a executar na CPU antes de dar lugar ao próximo processo na fila. 
Os processos possuem um tempo de uso total, e são executados pela ordem de chegada, um de cada vez, e quando um 
processo excede seu quantum, ele vai para o final da fila com seu tempo de uso restante e o próximo é executado. 
O processo continua até que todos os tempos de uso dos processos sejam esgotados, ou seja, até todos os processos
serem concluídos. Isso garante uma distribuição justa do tempo de CPU entre os processos.'''

#FEITO EM PYTHON NO VISUAL STUDIO CODE

processos = []  #Cria uma lista para guardar os processos
processos_prontos = [] #Cria outra lista para guardar os processos que estão prontos

print("\n------------------------SEJA BEM-VINDO!------------------------\n-------SISTEMA DE ESCALONAMENTO DE PROCESSOS ROUND-ROBIN-------\n")

while True: #Loop para solicitar as entradas manuais ao usuário até que sejam válidas
    numProcessos = int(input("\nDigite o número de processos (máx. 15): \n")) #Solicita o número de processos ao usuário

    if 1 <= numProcessos <= 15: #Laço de repetição para conferir se o número de processos informado é válido
        break #Se o número for válido (entre 1 e 15) o programa sai do laço e continua
    else:
        print("Quantidade inválida. Digite um valor entre 1 e 15.\n") #Se o número for inválido ele solicita que digite novamente e exibe a mensagem

quantum = int(input("Digite o tempo de quantum: \n"))#Solicita ao usuário que informe o tempo de quantum.
print("---------------------------------------------------------------")

#Faz a leitura dos nomes, tempos de uso e tempos de chegada dos processos
for i in range(numProcessos): #Faz a leitura dos nomes, tempos de uso e tempos de chegada dos processos
    #Executa uma vez para cada processo.
    nome = input(f"Digite o nome do processo {i + 1}: \n")#Solicita o nome do processo.
    tpUso = int(input(f"Digite o tempo de uso do processo {nome}: \n"))#Solicita o tempo de uso desse processo
    tpChegada = int(input(f"Digite o tempo de chegada do processo {nome}: \n"))#Solicita o tempo de chegada do processo.
    print("---------------------------------------------------------------")

    processo = {"nome": nome, "tpUso": tpUso, "tpChegada": tpChegada} #processo = variável usada para armazenar os 3 dados de um processo juntos, 
    #para que na lista os processos sejam dicionários de dados(agrupados de 3 em 3 termos)
    processos.append(processo) #Pega o processo, juntamente com seu tempo de uso e chegada, e adiciona na lista

# Ordena os processos por tempo de chegada
processos.sort(key=lambda x: x["tpChegada"]) #A função lambda retorna a chave tpChegada dos elementos da lista de processos
#A função sort utiliza os valores que a lambda fornece para ordenar os processos por tempo de chegada

# Simulação do escalonamento Round Robin
tempo_atual = 0 #Armazena o tempo de execução atual da CPU
while processos or processos_prontos: #Loop que continua executando até que as listas processos e processos_prontos estejam vazias
    while processos and processos[0]["tpChegada"] <= tempo_atual: #Continua o loop enquanto houver processos na lista que estão prontos para serem executados
        processos_prontos.append(processos.pop(0)) #Adiciona o processo pronto na lista de processos prontos e o remove da lista de processos inicial, 
        #para que ele não seja "executado duas vezes"
        print("Processos prontos: ") #Exibe os processos prontos e o tempo restante deles
        for p in processos_prontos:
            if (p["tpChegada"]<=tempo_atual):
                nome_processo = p["nome"]
                tempo_restante = p["tpUso"]
                print(f"Processo {nome_processo}")
                print(f"Tempo restante: {tempo_restante}")
                print("---------------------------------------------------------------")

    if processos_prontos: #Confere se há processos na lista de prontos
        processo_atual = processos_prontos.pop(0) #Armazena o primeiro processo da lista de prontos em processo_atual e o remove da lista
        nome = processo_atual["nome"] #Coleta o nome do processo
        tpUso = processo_atual["tpUso"] #Coleta o tempo de uso do processo
        tpChegada = processo_atual["tpChegada"] #Coleta o tempo de chegada do processo

        if tpUso <= quantum: #Confere se o tempo de uso restante do processo é menor ou igual ao quantum
            for i in range (tpUso): #Se for, termina de executá-lo pelo tempo de uso restante
                print(f"Tempo {tempo_atual}: Executando {nome}")
                print("---------------------------------------------------------------")
                tempo_atual += 1
                tpUso -= 1
        else: #Se não for, executa ele pelo tempo do quantum
            for i in range (quantum):
                print(f"Tempo {tempo_atual}: Executando {nome}")
                print("---------------------------------------------------------------")
                tempo_atual += 1
                tpUso -= 1

        processo_atual["tpUso"] = tpUso #Coleta o tempo restante do processo
        if processo_atual["tpUso"] > 0: #Verifica se o tempo restante é maior que 0
            processos_prontos.append(processo_atual) #Se for, recoloca o processo no final da fila de prontos

        if processos_prontos: #Trecho para exibir os processos em estado pronto, se houver
            print("Processos prontos: ")
            for p in processos_prontos:
                if (p["tpChegada"]<=tempo_atual):
                        nome_processo = p["nome"]
                        print(f"Processo {nome_processo}")
                        print(f"Tempo restante: {tpUso}")
                        print("---------------------------------------------------------------")
        else: #Se não encontrar processos prontos na linha 80, exibe a mensagem abaixo
            print("Não há processos na fila.")
            print("---------------------------------------------------------------")


    else: #Se na linha 57 o programa não encontra nenhum processo na lista de prontos, exibe a mensagem abaixo
        print(f"Tempo {tempo_atual}: Nenhum processo em execução.")
        print("---------------------------------------------------------------")
        tempo_atual +=1

print("Todos os processos foram concluídos!") #Ao final da execução notifica a conclusão da simulação

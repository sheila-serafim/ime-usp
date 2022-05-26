nomeEntrada = input("Escreva o nome do arquivo de entrada (com .txt no final): ")  
entrada = open(nomeEntrada, "r")

nomeSaida = input("Escreva o nome do arquivo de saída (com .txt no final): ")  
saida = open(nomeSaida, "w", newline="")


def main():
    """ () -> NoneType
    Programa gera um labirinto a partir de arquivo texto e 
    verifica se existe caminho possível, se existir, 
    mostra o caminho mais curto.
    """
    
    matrizL, lin_origem, col_origem, lin_destino, col_destino = le_cria_labirinto()    
    
    print("\nOrigem:\t\t(%d,%d)" %(lin_origem, col_origem))
    print("Destino:\t(%d,%d)\n" %(lin_destino, col_destino))    
    print("Matriz com zeros e uns:")
    
    imprime_labirinto_numericamente(matrizL)
    saida.write("Matriz com zeros e uns:\r\n")
    escreve_labirinto_numerica_arquivo(matrizL)
    saida.write('\r\n')
    print()
    
    if (matrizL[lin_destino][col_destino] != -1):
        matrizL = marca_labirinto(matrizL, lin_destino, col_destino)
        print("Matriz já marcada:")
        saida.write('Matriz já marcada:' + '\n')
        imprime_labirinto_numericamente(matrizL)
        escreve_labirinto_numerica_arquivo(matrizL)
        saida.write('\r\n')
        print()
    else:
        print("Destino está na parede, portanto não consigo marcar a matriz.\n")
        saida.write("Destino está na parede, portanto não consigo marcar a matriz.\r\n")
    
    #vejo se existe caminho antes de chamar a função
    if (matrizL[lin_origem][col_origem] != 0 and matrizL[lin_origem][col_origem] != -1):
        matriz, caminho = determina_um_caminho(matrizL, lin_origem, col_origem)
        print("Matriz com caminho possível:")
        saida.write("Matriz com caminho:\r\n")
        imprime_labirinto_simbolicamente(matriz)
        escreve_labirinto_simbolica_arquivo(matriz)
        saida.write('\r\n')
        print()
        imprime_caminho(caminho)
        escreve_caminho_arquivo(caminho)
    else:
        print("Para este labirinto, não existe caminho possível.")
        saida.write("Para este labirinto, não existe caminho possível.")    
    
    saida.close()
    
        
def le_cria_labirinto():
    """ () ->  matriz, int, int, int int
    Esta função lê todos os dados de um arquivo cujo nome deve ser 
    fornecido pelo usuário (conforme descrito no item (a)). 
    Ela cria uma matriz (com  moldura) com as informações lidas, e retorna 
    essa matriz, os índices de linha e de coluna da posição da origem e os 
    índices de linha e de coluna da posição do destino.
    """    
    
    primeiraLinha = entrada.readline()
    tupla1 = primeiraLinha.split()
    qtdLinhas = int(tupla1[0])
    qtdColunas = int(tupla1[1])
    
    segundaLinha = entrada.readline()
    tupla2 = segundaLinha.split()
    linhaOrigem = int(tupla2[0])
    colunOrigem = int(tupla2[1])
    
    terceiraLinha = entrada.readline()
    tupla3 = terceiraLinha.split()
    linhaDestino = int(tupla3[0])
    colunDestino = int(tupla3[1])
    
    matriz = [[-1]*(qtdColunas+1)] #primeira linha de moldura
    
    #montando a matriz linha a linha
    for i in range(0, qtdLinhas):
        lista = entrada.readline().split()
        linha = [-1] + list(map(int, lista)) + [-1]        
        matriz = matriz + [linha]
    
    entrada.close()
    matriz = matriz + [[-1]*(qtdColunas+1)]    
    
    return matriz, linhaOrigem, colunOrigem, linhaDestino, colunDestino

    
def marca_labirinto(matrizL, lin_destino, col_destino):
    """ (matriz, int, int) -> matriz
    Recebe uma matriz de inteiros (com moldura) matrizL, representando um 
    labirinto, e dois inteiros lin_destino e col_destino que são os índices 
    de linha e de colunada posição do destino nesse labirinto. Efetua a 
    marcação da matrizL, conforme o algoritmo que foi descrito.
    """
    
    pareslinhacoluna = []
    i = lin_destino
    j = col_destino
    
    matrizL[i][j] = 1
    pareslinhacoluna.append([i,j])
    
    inicio = 0
    fim = 0
    
    while(inicio <= fim):
        
        k = matrizL[i][j]
        inicio = inicio + 1
        
        #para a esquerda
        if matrizL[i][j-1] == 0:
            matrizL[i][j-1] = k + 1
            pareslinhacoluna.append([i,j-1])    
            fim = fim + 1
        
        #para a direita
        if matrizL[i][j+1] == 0:
            matrizL[i][j+1] = k + 1
            pareslinhacoluna.append([i,j+1])
            fim = fim + 1
            
        #para cima
        if matrizL[i-1][j] == 0:
            matrizL[i-1][j] = k + 1
            pareslinhacoluna.append([i-1,j])
            fim = fim + 1
            
        #para baixo
        if matrizL[i+1][j] == 0:
            matrizL[i+1][j] = k + 1
            pareslinhacoluna.append([i+1,j])
            fim = fim + 1
    
        if (inicio < len(pareslinhacoluna)):
            i = pareslinhacoluna[inicio][0]
            j = pareslinhacoluna[inicio][1]            
        
    return matrizL

    
def determina_um_caminho(matrizL, lin_origem, col_origem):
    """ (matriz, int, int) -> matriz, list
    Recebe uma matriz de inteiros (com moldura) matrizL, representando um 
    labirinto já marcado, e dois inteiros lin_origem e col_origem que são
    os índices de linha e de coluna da posição da origem nesse labirinto.
    A função supõe que existe um caminho da origem para o destino e determina 
    um tal caminho de comprimento mínimo (fazendo uso do algoritmo descrito). 
    [Ou seja, esta função só deve ser chamada quando se sabe que existe um 
    tal caminho.] 
    A função cria uma matriz de caracteres (como mostrada no exemplo),
    diferenciando as posições livres das posições que representam paredes, 
    e indicando nessa matrizas posições da origem, do destino e do caminho 
    encontrado.(Para facilitar, pode criar essa matriz com moldura.)
    Esta função cria também uma lista, onde cada elemento é um par 
    representando os índices de linha e de coluna de uma posição do caminho
    encontrado. A função retorna a matriz e a lista criadas.
    """
    
    i = lin_origem
    j = col_origem
    k = matrizL[i][j]
    
    caminho = []
    caminho.append([i,j])
    matriz = []
    
    #criando a lista com o caminho    
    while (matrizL[i][j] > 1):
        
        k = matrizL[i][j]
        
        #para a esquerda
        if matrizL[i][j-1] == k-1:
            caminho.append([i,j-1])
            j = j-1
        
        #para a direita
        elif matrizL[i][j+1] == k-1:
            caminho.append([i,j+1])
            j = j+1
            
        #para cima
        elif matrizL[i-1][j] == k-1:
            caminho.append([i-1,j])
            i = i-1
            
        #para baixo
        elif matrizL[i+1][j] == k-1:
            caminho.append([i+1,j])
            i = i+1
            
    #criando matriz com origem, destino e paredes
    k = matrizL[lin_origem][col_origem]
    linhaNova = []
    
    for linha in matrizL:
        for item in linha:
            if item == 1:
                linhaNova.append('D')
            elif item == -1:
                linhaNova.append('H')
            else:
                linhaNova.append(' ')
        matriz = matriz + [linhaNova]
        linhaNova = []
    
    #adicionando o caminho na nova matriz criada
    nó = 1
    tamanho = len(caminho)
    while nó < tamanho-1:
        i = caminho[nó][0]
        j = caminho[nó][1]
        matriz[i][j] = '*'   
        nó = nó + 1
        
    matriz[lin_origem][col_origem] = 'O'  
            
    return matriz, caminho
    
    
def imprime_labirinto_numericamente(matrizL):
    """ (matriz) -> NoneType
    Recebe uma matriz de inteiros (com moldura) matrizL, representando 
    um labirinto (antes ou depois da marcação). Imprime o labirinto 
    (sem a moldura), no formato de matriz e ajustada nas colunas 
    (exibindo também os índices das linhas e das colunas).
    """
    
    i = 1
    j = 1
    qtdLinhas = len(matrizL)
    qtdColunas = len(matrizL[0])
    
    for coluna in range(0, qtdColunas):
        if (coluna == 0):
            print('   ', end = ' ')
        else:
            print('%3s' %coluna, end=' ')
    print()
        
    while i < qtdLinhas-1:
        j = 1
        while j < qtdColunas:
            if (j == 1):
                print('%3d' %i, end = ' ')              
            print('%3d' %matrizL[i][j], end=' ')
            j = j + 1
        i = i + 1
        print()        
    
    
def imprime_labirinto_simbolicamente(matrizC):
    """ (matriz) -> NoneType
    Recebe uma matriz de caracteres (com moldura) matrizC, representando 
    um labirinto já com um caminho de comprimento mínimo. Imprime o 
    labirinto (sem a moldura), no formato de matriz e ajustada nas colunas 
    (exibindo também os índices das linhas e das colunas).
    """
    
    i = 1
    j = 1
    qtdLinhas = len(matrizC)
    qtdColunas = len(matrizC[0])
    
    for coluna in range(0, qtdColunas):
        if (coluna == 0):
            print('   ', end = ' ')
        else:
            print('%3d' %coluna, end=' ')
    print()
        
    while i < qtdLinhas-1:
        j = 1
        while j < qtdColunas:
            if (j == 1):
                print('%3d' %i, end = ' ')
            print('%3s' %matrizC[i][j], end=' ')
            j = j + 1
        i = i + 1
        print()
        
    print("\nLengenda:")
    print("O - Origem")
    print("D - Destino")
    print("H - Parede") 
    print("* - Caminho") 
    
    
def imprime_caminho(lin_col_caminho):
    """ (list) -> NoneType
    Recebe uma lista lin_col_caminho, onde cada elemento é um par 
    representando os índices de linha e de coluna de uma posição do 
    caminho encontrado. Imprime os índices das posições do caminho 
    encontrado (conforme o exemplo dado).
    """    
    
    print("Caminho:")
    
    for i in range(0, len(lin_col_caminho)):
        linha = lin_col_caminho[i][0]
        coluna = lin_col_caminho[i][1]
        print('(%s, %s)\t' %(linha,coluna), end='')
        if (i+1)%6 == 0:
            print()

            
def escreve_labirinto_numerica_arquivo(matrizL):
    """ (matriz) -> NoneType
    Recebe uma matriz de inteiros (com moldura) matrizL, representando 
    um labirinto (antes ou depois da marcação). Escreve o labirinto 
    (sem a moldura), no formato de matriz e ajustada nas colunas 
    (exibindo também os índices das linhas e das colunas).
    """
    
    i = 1
    j = 1
    qtdLinhas = len(matrizL)
    qtdColunas = len(matrizL[0])
    
    for coluna in range(0, qtdColunas):
        if (coluna == 0):
            saida.write('    ')
        else:
            saida.write('%3s ' %coluna)
    saida.write("\r\n")
        
    while i < qtdLinhas-1:
        j = 1
        while j < qtdColunas:
            if (j == 1):
                saida.write('%3d ' %i)                
            saida.write('%3d ' %matrizL[i][j])
            j = j + 1
        i = i + 1       
        saida.write("\r\n")
        
        
def escreve_labirinto_simbolica_arquivo(matrizC):
    """ (matriz) -> NoneType
    Recebe uma matriz de caracteres (com moldura) matrizC, representando 
    um labirinto já com um caminho de comprimento mínimo. Escreve o 
    labirinto (sem a moldura), no formato de matriz e ajustada nas colunas 
    (exibindo também os índices das linhas e das colunas).
    """
    
    i = 1
    j = 1
    qtdLinhas = len(matrizC)
    qtdColunas = len(matrizC[0])
    
    for coluna in range(0, qtdColunas):
        if (coluna == 0):
            saida.write('    ')
        else:
            saida.write('%3d ' %coluna)
    saida.write('\r\n')
        
    while i < qtdLinhas-1:
        j = 1
        while j < qtdColunas:
            if (j == 1):
                saida.write('%3d ' %i)
            saida.write('%3s ' %matrizC[i][j])
            j = j + 1
        i = i + 1
        saida.write('\r\n')
        
    saida.write("\nLengenda:\r\n")
    saida.write("O - Origem\r\n")
    saida.write("D - Destino\r\n")
    saida.write("H - Parede\r\n")   
    saida.write("* - Caminho") 
        
        
def escreve_caminho_arquivo(lin_col_caminho):
    """ (list) -> NoneType
    Recebe uma lista lin_col_caminho, onde cada elemento é um par 
    representando os índices de linha e de coluna de uma posição do 
    caminho encontrado. Escreve os índices das posições do caminho
    encontrado (conforme o exemplo dado).
    """
    
    saida.write("\r\nCaminho:\r\n")
    
    for i in range(0, len(lin_col_caminho)):
        linha = lin_col_caminho[i][0]
        coluna = lin_col_caminho[i][1]
        saida.write('(%s, %s)\t' %(linha,coluna))
        if (i+1)%6 == 0:
            saida.write('\r\n')
            
#-------------------------------------------------------------------------------
    
main()

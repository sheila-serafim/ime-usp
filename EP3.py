# -*- coding: utf-8 -*-
"""
    Nome do aluno: Sheila Serafim Neves
    Número USP: 5448120
    Curso: Licenciatura em Matemática
    Disciplina: MAC0110 Introdução à Computação
    Turma: 47
    Exercício-Programa EP3

    DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
    TODAS AS PARTES ORIGINAIS DESTE EXERCÍCIO-PROGRAMA FORAM
    DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
    DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
    OU PLÁGIO.
    DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
    PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
    ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA
    SERÃO TRATADOS SEGUNDO OS CRITÉRIOS DIVULGADOS NA PÁGINA DA
    DISCIPLINA.
  
    A seguir você pode descrever alguma ajuda que você recebeu para fazer
    este EP.  Com exceção do material didático de MAC0110, pode incluir
    qualquer ajuda recebida de outra pessoa ou de trecho de código (indicando
    a página ou a fonte) para que o seu programa não seja considerado plágio
    ou irregular.

"""
# ----------------------------------------------------------------------------

def main():
    """ 
    ( ) -> NoneType...
    
    Chama os 3 problemas relacionados a este Exercício Programa.
    """
    print("=============================================================================")
    print("\nPROBLEMA 1")
    print("\nDeterminar todos os números primos menores ou iguais a n.")
    resolverProblema1()
    
    print()
    print("\n===========================================================================")
    print("\nPROBLEMA 2")
    print("\nDeterminar dois números primos r e s tais que 2 <= r < s <= n,")
    print("o valor de s−r é máximo e não existem números primos entre r e s.")
    resolverProblema2()
    
    print("\n===========================================================================")
    print("\nPROBLEMA 3")
    print("\nTestar a Conjetura de Goldbach para todo inteiro par menor do que k.")
    resolverProblema3()  
    print("\n===========================================================================")
    

def resolverProblema1():
    """ 
    ( ) -> NoneType...
    
    Imprime a quantidade de primos até um n dado e também os números
    primos encontrados.
    """
    
    n = int(input("Digite um inteiro >= 2 para n:  "))
    
    while n < 2:
        print("\nEntrada inválida.", end="")
        n = int(input("\nDigite um inteiro >= 2 para n:  "))
    
    crivo = criaListaCrivoEratostenes(n)
    primos = criaListaPrimos(crivo)
    qtd = len(primos)    
    
    print()
    print("\nExistem %d números primos menores ou iguais a %d. São eles:  " %(qtd, n))
    imprimeNumerosInteirosLista(primos)    
    
    
def resolverProblema2():
    """ 
    ( ) -> NoneType...
    
    Encontra o maior intervalo sem números primos e mostra o primo 
    exatamente anterior e posterior ao intervalo.
    """
    
    n = int(input("Digite um inteiro > 2 para n:  "))
    
    while n <= 2:
        print("\nEntrada inválida.")
        n = int(input("Digite um inteiro > 2 para n:  "))
    
    r, s = maiorIntervaloSemPrimos(n)
    
    print("\nUma sequência consecutiva mais longa de inteiros menores do que %d," %n)
    print("sem nenhum número primo, é formada por %d inteiros que estão entre " %(s-r-1))
    print("o par de números primos %d e %d." %(r,s) )
    
    
def resolverProblema3():
    """ 
    ( ) -> NoneType...
    
    Testa a Conjectura de Goldbach e exibe a lista de soma de primos 
    encontrada, caso a conjectura funcione, ou imprime uma mensagem
    de erro, caso contrário.
    """
    
    n = int(input("Digite um inteiro > 4 para k:  "))
    
    while n < 5:
        print("\nEntrada inválida.", end="")
        n = int(input("\nDigite um inteiro > 4 para k:  "))
        
    lista, afirmacao = testaConjecturaGoldbach(n)
    
    print("\nPara todo n par tal que 2 < n < %d, os pares p e q tais que n = p + q são: " %n)
    print()
    
    if (afirmacao):
        for x in range(2, n//2):
            print("%4d = %4d + %4d" %(2*x,lista[x],2*x-lista[x]))
    else:
        print("A Conjectura não foi válida.")
    
        
def criaListaCrivoEratostenes(n):
    """ 
    (int) -> list
    Recebe um inteiro positivo n e cria uma lista crivo[0...n] com 
    zeros e uns, tal que para cada i, 0 <= i <= n, crivo[i] é 1 se i 
    é primo e crivo[i] é 0 se i não é primo.A lista crivo é criada 
    implementando o algoritmo do Crivo de Eratóstenes. Esta função 
    retorna a lista crivo.
    """
    
    crivo = [1] * (n+1)
    
    for i in range(2, n):  
        if crivo[i] == 1:
           for j in range(2, n//i + 1):
               crivo[i * j] = 0
               
    return crivo
    
def criaListaPrimos(crivo):
    """ (list) -> list
    Recebe uma lista crivo que foi criada utilizando o algoritmo do 
    Crivo de Eratóstenes. A partir da lista crivo, esta função 
    cria e retorna uma lista chamada primos, contendo todos os 
    números primos, em ordem crescente.
    """    
    
    n = len(crivo)
    primos = []
          
    for i in range(2, n):
        if crivo[i] == 1:
            primos.append(i)
            
    return primos
    
def imprimeNumerosInteirosLista(a):
    """ 
    (list) -> NoneType
    Recebe uma lista a de números inteiros e imprime todos os 
    números da lista, escrevendo no máximo dez números em cada 
    linha e de modo que fiquem ajustados nas colunas.
    """

    n = len(a)
    linha = 1
    coluna = 1
    item = 0
    totalLinhas = (n//10)+2
    
    while (linha < totalLinhas):
        while (coluna < 11 and item < n):
            print("%5d" %(a[item]), end='')
            coluna += 1
            item = item + 1
        print()
        linha += 1
        coluna = 1
    
    
def maiorIntervaloSemPrimos(n):
    """ 
    (int) -> int, int
    Recebe um inteiro positivo n e determina um par de números 
    primos r e s, tais que 2 <= r < s < n, o valor s-r é máximo e 
    para todo i tal que r < i < s, tem-se que i não é primo 
    (ou seja, entre r e s não há nenhum primo). Esta função retorna 
    os primos r e s.
    """
    
    crivo = criaListaCrivoEratostenes(n)
    primos = criaListaPrimos(crivo)
    maiorDistancia = 0
    qtdPrimos = len(primos)-1
    
    for i in range(0,qtdPrimos):
        distancia = primos[i+1]-primos[i]
        if distancia > maiorDistancia:
            maiorDistancia = distancia
            r = primos[i]
            s = primos[i+1]    
    return r, s

    
def testaConjecturaGoldbach(k):
    """ 
    (int) -> list, bool
    Recebe um inteiro k > 2 e verifica se a Conjectura de Goldbach é 
    verdadeira para todo inteiro n par, 2 < n < k. Para isto, para 
    cada tal inteiro n, esta função tenta encontrar dois números 
    primos p e q tais que n = p + q. Se existir mais do que um tal 
    par, escolha o par com o menor p (e tal que p <= q).
    Obs.: Para alguns números pode existir mais de um par de primos.
    Por exemplo, 40 = 3 + 37 = 11 + 29 = 17 + 23. Neste caso, o par 
    escolhido deve ser p, q, com p = 3 e q = 37.
    Para dar um certificado da validade da conjectura para os números
    pares n entre 2 e k, o programa constrói uma lista chamada lista
    pares_primos que tem a seguinte propriedade:
    Como n é par, n >= 4, então n = 2 * i, onde i >= 2. Para cada i, 
    i >= 2, pares_primos[i] armazena o primo p tal que n = p + q,
    onde p <= q  e  q = n - p é primo. Apenas o valor de p é 
    armazenado já que o valor de q é precisamente n - p. A função 
    testaConjecturaGoldbach retorna a lista pares_primos e retorna 
    também True ou False dependendo se a conjectura for válida ou
    não para todo n par, 2 < n < k.
    """
    
    crivo = criaListaCrivoEratostenes(k)
    pares_primos = [0,0]
    éVálida = True
    achei = False
    
    for n in range(4,k,2):        
        for p in range(2,k):
            if (crivo[p] == 1 and crivo[n-p] == 1):
                pares_primos.append(p)
                achei = True
                break
        if not achei:
            éVálida = False
                    
    return pares_primos, éVálida

main()



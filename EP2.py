# -*- coding: utf-8 -*-
"""
    Nome do aluno: Sheila Serafim Neves
    Número USP: 5448120
    Curso: Licenciatura em Matemática
    Disciplina: MAC0110 Introdução à Computação
    Turma: 47
    Exercício-Programa EP2

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
# ---------------------------------------------------------------------------------------

import math
# para usar as funções sqrt e fabs, e a constante pi
# ---------------------------------------------------------------------------------------

def main():
    """
        Este programa calcula várias estimativas para o número pi
        a partir de diferentes formas.
    """
       
    print("----------------------------------------------------------------------------")
    print("                ALGUMAS APROXIMAÇÕES PARA O VALOR DE PI:                    ")
    print("              (utilizamos math.pi que é 3.141592653589793)                  ")
    print("----------------------------------------------------------------------------")
    
    pi = math.pi
    a = 0.0
    b = 1.0
    i = 0
    k = 2**i
    piAproxRetangulos = 0.0
    
    print("\nMétodo 1 - Valor aproximado para PI utilizando o Método dos Retângulos")
    eps = float(input("Digite um número (> 0 e < 1) para epsilon: "))
    
    while (math.fabs(piAproxRetangulos - pi) >= eps):
        
        piAproxRetangulos = 4*areaMetodoRetangulos(a, b, k)
        k = 2**i
        i = i + 1    
    
    print("\nNúmero de retângulos considerados para o cálculo da última área: ", k//2)
    print("\nValor aproximado para PI: ", piAproxRetangulos)
    print("\n--------------------------------------------------------------------------")
    
#---------------------------------------------------------------------------------------
    
    i = 0
    k = 2**i
    piAproxTrapezios = 0.0
    
    print("\nMétodo 2 - Valor aproximado para PI utilizando o Método dos Trapézios")
    eps = float(input("Digite um número (> 0 e < 1) para epsilon: "))
    
    while (math.fabs(piAproxTrapezios - pi) >= eps):
        
        piAproxTrapezios = 4*areaMetodoTrapezios(a, b, k)
        k = 2**i
        i = i + 1  
    
    print("\nNúmero de trapézios considerados para o cálculo da última área: ", k//2)
    print("\nValor aproximado para PI: ", piAproxTrapezios)
    print("\n--------------------------------------------------------------------------")
    
#---------------------------------------------------------------------------------------
    
    print("\nMétodo 3 - Valor aproximado para PI utilizando a série de Wallis")
    eps = float(input("Digite um número (> 0 e < 1) para epsilon: "))
    k, piAproxWallis = piSerieWallis(eps)
    print("\nNúmero de termos da série incluídos no cálculo: ", k)
    print("\nValor aproximado para PI: ", 2*piAproxWallis)
    print("\n--------------------------------------------------------------------------")
    
#---------------------------------------------------------------------------------------    
    
    print("\nMétodo 4 - Valor aproximado para PI utilizando a série de Nilakantha")
    eps = float(input("Digite um número (> 0 e < 1) para epsilon: "))
    k, piAproxNilakantha = piSerieNilakantha(eps)
    print("\nNúmero de termos da série incluídos no cálculo: ", k)
    print("\nValor aproximado para PI: ", piAproxNilakantha)
    print("\n--------------------------------------------------------------------------")

# ---------------------------------------------------------------------------------------

def f(x):
    """ (float) -> float

    Recebe um número real x e se (1.0-x*x) for positivo, retorna  
    a raiz quadrada de (1.0-x*x); em caso contrário, retorna 0.
    Obs.: para determinar a raiz quadrada é utilizada a função sqrt do
    módulo math.
    """
    
    if ((1.0-x*x) > 0):
        y = math.sqrt(1.0-x*x)
    else:
        y = 0.0
    return y
    
# ---------------------------------------------------------------------------------------

def areaMetodoRetangulos(a, b, k):
    """ (float, float, int) -> float

    Recebe dois números reais a e b, com a < b, e um inteiro positivo k.
    Esta função retorna um valor aproximado para a área sob a função f(x),
    no intervalo [a, b], calculada pelo método dos retângulos, utilizando
    k retângulos.
    """  
    
    soma = 0.0
    delta = (b-a)/k
    
    for i in range(1,k+1):
        soma = soma + f(a + i*delta)*delta
        
    return soma
    
# ---------------------------------------------------------------------------------------

def areaMetodoTrapezios(a, b, k):
    """ (float, float, int) -> float

    Recebe dois números reais a e b, com a < b, e um inteiro positivo k.
    Esta função retorna um valor aproximado para a área sob a função f(x),
    no intervalo [a, b], calculada pelo método dos trapézios, utilizando
    k trapézios.
    """
        
    soma = 0.0
    delta = (b-a)/k     

    for i in range(0,k):
        termo1 = f(a + i*delta)
        termo2 = f(a + (i+1)*delta)
        soma = soma + ((termo1 + termo2)*delta)/2          
    
    return soma
    
# ---------------------------------------------------------------------------------------

def piSerieWallis(eps):
    """ (float) -> int, float

    Recebe um número real eps, com 0 < eps < 1. 
    Esta função calcula um valor aproximado para pi, piAproxWallis, 
    através da série de Wallis, incluindo os primeiros termos até
    que o valor absoluto da diferença entre o valor calculado 
    piAproxWallis e o valor da constante math.pi seja menor do que 
    eps. A função retorna o número de termos considerados e o valor
    calculado piAproxWallis.
    Obs.: para determinar o valor absoluto é utilizada a função fabs
    do módulo math.
    """
            
    piAproxWallis = 2 #primeiro termo
    numerador = 2
    denominador = 3     
    pi = math.pi
    k = 1
    
    while (math.fabs(2*piAproxWallis - pi) >= eps):
        
        piAproxWallis = piAproxWallis*numerador/denominador
        
        incrementoNum = (denominador//numerador)*2
        incrementoDen = (numerador//denominador)*2
        
        numerador = numerador + incrementoNum
        denominador = denominador + incrementoDen   
            
        k = k + 1
        
    return k, piAproxWallis
    
# ---------------------------------------------------------------------------------------

def piSerieNilakantha(eps):
    """ (float) -> int, float

    Recebe um número real eps, com 0 < eps < 1. 
    Esta função calcula um valor aproximado para pi, piAproxNilakantha,
    através da série de Nilakantha, incluindo os primeiros termos até 
    que o valor absoluto da diferença entre o valor calculado 
    piAproxNilakantha e o valor da constante math.pi seja menor do que
    eps. A função retorna o número de termos considerados e o valor 
    calculado piAproxNilakantha.
    Obs.: para determinar o valor absoluto é utilizada a função fabs 
    do módulo math.
    """
  
    pi = math.pi
    piAproxNilakantha = 3 #primeiro termo
    numerador = 4
    denominador = 2
    sinal = 1
    k = 1
    
    while (math.fabs(piAproxNilakantha - pi) >= eps):
              
        multiplicacao = denominador*(denominador+1)*(denominador+2)
        termo = sinal*(numerador/multiplicacao)
        piAproxNilakantha = piAproxNilakantha + termo
        
        denominador = denominador + 2
        sinal = -sinal
        k = k + 1
        
    return k, piAproxNilakantha
    
# ---------------------------------------------------------------------------------------

main()
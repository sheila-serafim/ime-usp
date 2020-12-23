def buscarProximoPrimo(n3):
    """
    (int)-->int 
    
    Recebe o último primo da minha sequência, encontra o próximo número 
    primo e retorna este valor.    
    """
    
    divisivel = False
    acheiPrimo = False
    divisor = 3 
    candidato = n3 + 2
    
    # Aqui vamos testando os candidatos a primo até encontrar o próximo primo.
    while (acheiPrimo == False):        
        
        # Aqui vamos aumentando os divisores para testar um candidato a primo.
        while (divisor*divisor <= candidato and divisivel == False):
            if candidato % divisor == 0:
                divisivel = True
            divisor = divisor + 1
            
        if divisivel == False:
            acheiPrimo = True
            primo = candidato
        else:
            candidato = candidato + 2
            divisor = 3
            divisivel = False

    return primo
#-----------------------------------------------------------------------------

def main():
    
    print("Este programa verifica se n é soma de três números primos consecutivos.")
    k = int(input("Digite um inteiro positivo para n: "))
    print()
    
    n1 = 2  #Primeiro Primo
    n2 = 3  #Segundo Primo
    n3 = 5  #Terceiro Primo     
    
    while (k > n1 + n2 + n3):        
        n = buscarProximoPrimo(n3)
        n1 = n2
        n2 = n3
        n3 = n        
        
    if (k == n1 + n2 + n3):
        print ("%d é soma de três números primos consecutivos:" %(k))
        print ("%d = %d + %d + %d" %(k, n1, n2, n3))
    else:
        print ("%d não é soma de três números primos consecutivos." %(k))
    
#-----------------------------------------------------------------------------
main()

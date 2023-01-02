# Torre de Hanoi - 4 Torres
# Solucao Recursiva


def towerOfHanoi(n, torre_inicial, torre_final, torre_aux1, torre_aux2):
    if (n == 0):
        return 0
    if (n == 1):
        print("Movendo o disco", n, "da torre", torre_inicial, "para a torre", torre_final)
        return 1
    cont1 = towerOfHanoi(n-2, torre_inicial, torre_aux1, torre_aux2, torre_final)
    print("Movendo o disco", n-1, "da torre", torre_inicial, "para a torre", torre_aux2)
    print("Movendo o disco", n, "da torre", torre_inicial, "para a torre", torre_final)
    print("Movendo o disco", n-1, "da torre", torre_aux2, "para a torre", torre_final)
    cont2 = towerOfHanoi(n-2, torre_aux1, torre_final, torre_inicial, torre_aux2)
    return cont1 + cont2 + 3

# Numero de discos
n = int(input("Digite o numero de discos: "))
print("")

# A, B, C e D sao os nomes das torres
contador = towerOfHanoi(n, 'A', 'D', 'B', 'C')
print("\nNúmero de movimentos = ", contador)
print(("Solucao finalizada! =)"))
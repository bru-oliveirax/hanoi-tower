# Torre de Hanoi - 3 Torres
# Solucao Recursiva


def TowerOfHanoi(n, torre_inicial, torre_final, torre_aux):
    if n == 0:
        return
    TowerOfHanoi(n - 1, torre_inicial, torre_aux, torre_final)
    print("Movendo o disco", n, "da torre", torre_inicial, "para o torre", torre_final)
    TowerOfHanoi(n - 1, torre_aux, torre_final, torre_inicial)

# Numero de discos
n = int(input("Digite o numero de discos: "))
print("")

# A, B, C e D sao os nomes das torres
TowerOfHanoi(n, 'A', 'C', 'B')
print(("Solucao finalizada! =)"))
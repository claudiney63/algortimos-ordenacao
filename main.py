import random
import time
import saida as saida
import entradas as en
import bubble_sort


def algoritimo_label():
    print('Escolha um algoritimo:')
    print('1. ordenacao pelo metodo da bolha (bublesort);\n2. ordenacao por insercao (insertionsort);\n3. ordenacao por intercalacao (mergesort);\n4. ordenacao por Heap (heapsort);\n5. ordenacao rapida (quicksort).')

    escolha = int(input('Escolha: '))
    return escolha


def entradas_label():
    print('Quantidade de Entradas: ')
    print('1. 100;\n2. 1.000;\n3. 5.000;\n4. 30.000;\n5. 50.000;\n6. 100.000;\n7. 150.000;\n8. 200.000.')

    entrada = int(input('Escolha: '))
    saida_da_entrada = en.entrada_100

    if (entrada == 1):
        saida_da_entrada = [random.randrange(1, 100) for i in range(100)]
        return saida_da_entrada
    elif(escolha == 2):
        saida_da_entrada = [random.randrange(1, 1000) for i in range(1000)]
        return saida_da_entrada
    elif(escolha == 3):
        saida_da_entrada = [random.randrange(1, 5000) for i in range(5000)]
        return saida_da_entrada
    elif(escolha == 4):
        saida_da_entrada = [random.randrange(1, 30000) for i in range(30000)]
        return saida_da_entrada
    elif(escolha == 5):
        saida_da_entrada = [random.randrange(1, 50000) for i in range(50000)]
        return saida_da_entrada
    elif(escolha == 6):
        saida_da_entrada = [random.randrange(1, 100000) for i in range(100000)]
        return saida_da_entrada
    elif(escolha == 7):
        saida_da_entrada = [random.randrange(1, 150000) for i in range(150000)]
        return saida_da_entrada
    elif(escolha == 8):
        saida_da_entrada = [random.randrange(1, 200000) for i in range(200000)]
        return saida_da_entrada

    return None


if __name__ == '__main__':

    escolha = algoritimo_label()

    if (escolha == 1):  # Bubble Sort
        escolha_ord = entradas_label()
        inicio = time.time()
        print(f'Entradas: N = {len(escolha_ord)}')
        print("Array NAO ordenado: ", escolha_ord)
        # Chama da função para ordenar
        print("\nArray Ordenado: ", bubble_sort.bubble_sort(escolha_ord))

        fim = time.time() - inicio

        print(f"Tempo Execucao: {fim:.5f} ms")

    elif (escolha == 2):  # Insertionsort
        saida.saida_ordenada()

    elif (escolha == 3):  # Mergesort
        saida.saida_ordenada()

    elif (escolha == 4):  # Heapsort
        saida.saida_ordenada()

    elif (escolha == 5):  # Quicksort
        saida.saida_ordenada()

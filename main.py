import time
import bubble_sort
import insertion_sort
import algoritimo_label
import entradas_label

if __name__ == '__main__':

    escolha = algoritimo_label.algoritimo_label()

    if (escolha == 1):  # Bubble Sort
        escolha_ord = entradas_label.entradas_label()
        inicio = time.time()
        print("Array NAO ordenado: ", escolha_ord)
        # Chama da função para ordenar

        soma_tempo = 0
        for i in range(0, 3):
            print("\nArray Ordenado: ", bubble_sort.bubble_sort(escolha_ord))
            fim = time.time() - inicio
            soma_tempo += fim

        print('\nAlgoritimo Bubble Sort:')
        print(f'Entradas: N = {len(escolha_ord)}')
        print(f"Tempo Execucao: {(soma_tempo/3):.5f} ms")

    elif (escolha == 2):  # Insertionsort
        escolha_ord = entradas_label.entradas_label()
        inicio = time.time()
        print("Array NAO ordenado: ", escolha_ord)
        # Chama da função para ordenar
        soma_tempo = 0
        for i in range(0, 3):
            print("\nArray Ordenado: ", insertion_sort.insertion_sort(escolha_ord))

            fim = time.time() - inicio
            soma_tempo += fim

        print('\nAlgoritimo Insertion Sort:')
        print(f'Entradas: N = {len(escolha_ord)}')
        print(f"Tempo Execucao: {(soma_tempo/3):.5f} ms")

    elif (escolha == 3):  # Mergesort
        None

    elif (escolha == 4):  # Heapsort
        None

    elif (escolha == 5):  # Quicksort
        None

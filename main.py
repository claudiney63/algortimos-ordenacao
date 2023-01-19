import time
import bubble_sort
import insertion_sort
import algoritimo_label
import entradas_label
import merge_sort

if __name__ == '__main__':

    escolha = algoritimo_label.algoritimo_label()

    if (escolha == 1):  # Bubble Sort
        escolha_ord = entradas_label.entradas_label()
        inicio = time.time()
        print("Array NAO ordenado: ", escolha_ord)
        # Chamada função para ordenar

        soma_tempo = 0
        for i in range(0, 3):
            escolha_aux = escolha_ord.copy()
            print("\nArray Ordenado: ", bubble_sort.bubble_sort(escolha_aux))
            fim = time.time() - inicio
            soma_tempo += fim

        print('\nAlgoritimo Bubble Sort:')
        print(f'Entradas: N = {len(escolha_aux)}')
        print(f"Tempo Execucao: {(soma_tempo/3):.5f} ms")

    elif (escolha == 2):  # Insertionsort
        escolha_ord = entradas_label.entradas_label()
        inicio = time.time()
        print("Array NAO ordenado: ", escolha_ord)
        # Chamada função para ordenar
        soma_tempo = 0
        for i in range(0, 3):
            escolha_aux = escolha_ord.copy()
            print("\nArray Ordenado: ", insertion_sort.insertion_sort(escolha_aux))

            fim = time.time() - inicio
            soma_tempo += fim

        print('\nAlgoritimo Insertion Sort:')
        print(f'Entradas: N = {len(escolha_aux)}')
        print(f"Tempo Execucao: {(soma_tempo/3):.5f} ms")

    elif (escolha == 3):  # Mergesort
        escolha_ord = entradas_label.entradas_label()
        inicio = time.time()
        print("Array NAO ordenado: ", escolha_ord)
        # Chamada função para ordenar
        soma_tempo = 0
        
        for i in range(0, 3):
            
            escolha_aux = escolha_ord.copy()
            merge_sort.merge_sort(escolha_aux, 0, len(escolha_aux) - 1)
            
            print("\nArray Ordenado: ", escolha_aux)

            fim = time.time() - inicio
            soma_tempo += fim

        print('\nAlgoritimo Merge Sort:')
        print(f'Entradas: N = {len(escolha_aux)}')
        print(f"Tempo Execucao: {(soma_tempo/3):.5f} ms")

    elif (escolha == 4):  # Heapsort
        None

    elif (escolha == 5):  # Quicksort
        None

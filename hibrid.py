# Algoritimo de ordenação hibrido tratando como principal o merge sort
# e segundario o insert sort

#  função para dividir as listas nas duas sublistas
def hibrid_merge_insertion_sort(list1, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    hibrid_merge_insertion_sort(list1, left_index, middle)
    hibrid_merge_insertion_sort(list1, middle + 1, right_index)
    hibrid_merge(list1, left_index, right_index, middle)

#  Definindo uma função para mesclar a lista


def hibrid_merge(list1, left_index, right_index, middle):

    #  Criando subpartes de uma lista
    left_sublist = list1[left_index:middle + 1]
    right_sublist = list1[middle:right_index+1]

    #  Valores iniciais para variáveis que usamos para manter
    #  faixa de onde estamos em cada list1
    left_sublist_index = 0
    right_sublist_index = 0
    sorted_index = left_index

    #  atravessar ambas as cópias até  excedermos um elemento
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):

        #  atravessar ambas as cópias até  excedermos um elemento
        # # parte e em seguida avançar na sublista_esquerda (aumentando o ponteiro)
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
            list1[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index = left_sublist_index + 1
        #  Caso contrário, adicione na sublista correta
        else:
            list1[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index = right_sublist_index + 1

        #  avançar na parte classificada
        sorted_index = sorted_index + 1

   # Laço externo para atravessar através de 1 para len(list1)
    for i in range(1, len(list1)):

        value = list1[i]

        #  Move elementos da lista1[0..i-1], que são
        #  maior que valor, para uma posição à frente
        #  da sua posição atual
        j = i - 1
        while j >= 0 and value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = value

# lista1 = [100-i for i in range(100)]

# print(lista1)

# hibrid_merge_insertion_sort(lista1, 0, len(lista1))

# print(lista1)

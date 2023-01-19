# Criando uma função de classificação em bolhas
def bubble_sort(list1):  
    # Loop externo para percorrer toda a lista 
    for i in range(len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  

    return list1
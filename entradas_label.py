import random

def entradas_label():
    print('Quantidade de Entradas: ')
    print('1. 100;\n2. 1.000;\n3. 5.000;\n4. 30.000;\n5. 50.000;\n6. 100.000;\n7. 150.000;\n8. 200.000.')

    escolha = int(input('Escolha: '))

    if (escolha == 1):
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
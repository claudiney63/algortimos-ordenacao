import random
import numpy as np

# N = 100
entrada_100 = [random.randrange(1, 100) for i in range(100)]
file = open("entrada_100.txt", "w+")
content = str([random.randrange(1, 100) for i in range(100)])
file.write(content)
file.close()
# file = open("entrada_100.txt", "r")
# entrada_100 = file.read()

# N = 1000
file = open("entrada_1000.txt", "w+")
content = str([random.randrange(1, 1000) for i in range(1000)])
file.write(content)
file.close()
file = open("entrada_1000.txt", "r")
entrada_1000 = file.read()

# N = 5000
file = open("entrada_5000.txt", "w+")
content = str([random.randrange(1, 5000) for i in range(5000)])
file.write(content)
file.close()
file = open("entrada_5000.txt", "r")
entrada_5000 = file.read()

# N = 30000
file = open("entrada_30000.txt", "w+")
content = str([random.randrange(1, 30000) for i in range(30000)])
file.write(content)
file.close()
file = open("entrada_30000.txt", "r")
entrada_30000 = file.read()
 
# N = 50000
file = open("entrada_50000.txt", "w+")
content = str([random.randrange(1, 30000) for i in range(30000)])
file.write(content)
file.close()
file = open("entrada_50000.txt", "r")
entrada_50000 = file.read()

# entrada_100000 = np.random.randint(1,100000, (100000))

# file = open("entrada_100000.txt", "w+")
# content = str(entrada_100000)
# file.write(content)
# file.close()

# entrada_150000 = np.random.randint(1,150000, (150000))

# file = open("entrada_150000.txt", "w+")
# content = str(entrada_150000)
# file.write(content)
# file.close()

# entrada_200000 = np.random.randint(1,200000, (200000))

# file = open("entrada_200000.txt", "w+")
# content = str(entrada_200000)
# file.write(content)
# file.close()
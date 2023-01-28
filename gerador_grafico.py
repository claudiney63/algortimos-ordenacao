import matplotlib.pyplot as plt
import numpy as np

# RANDOM
entrada = [100, 250, 500, 1000, 5000, 30000, 50000, 100000, 150000, 200000]

# plt.figure(figsize=(8, 6))
# plt.xlabel("Entradas (n)")
# plt.ylabel("Tempo (s)")
# plt.plot(entrada, [0.02776, 0.05436, 0.13420, 0.13619, 2.17398, 73.11906, 200.36972,
#          806.12331, 1861.45981, 3425.50603], label='Bubble Sort')
# plt.plot(entrada, [0.02400,	0.05179,	0.12059,	0.03456,	0.85830,
#          20.92266,	55.11189,	217.95049,	494.65314,	913.33515], label="Insertion Sort")
# plt.title('Random')
# plt.legend(ncol=2)
# plt.show()

# plt.figure(figsize=(8, 6))
# plt.xlabel("Entradas (n)")
# plt.ylabel("Tempo (s)")
# plt.plot(entrada, [0.02383,	0.05426,	0.11379,	0.01624,	0.39975,	3.10160,
#          5.10434,	10.58470,	16.81018,	23.14874], label="Merge Sort")
# plt.plot(entrada, [0.02607,	0.05164,	0.11807,	0.01543,	0.37820,	3.04833,
#                    5.72867,	10.81921,	17.04173,	23.48254], label="Heap Sort")
# plt.plot(entrada, [0.02445,	0.04998,	0.11515,	0.01352,	0.38769,
#          3.01375,	5.16947,	10.59459,	16.65683,	22.86695], label="Quick Sort")
# plt.title('Random')
# plt.legend(ncol=2)
# plt.show()


# ORDENADO

# plt.figure(figsize=(8, 6))
# plt.xlabel("Entradas (n)")
# plt.ylabel("Tempo (s)")
# plt.plot(entrada, [0.02630,	0.05543,	0.13095,	0.06319,	1.71428,	51.27958,	141.02246,	551.12577,	1356.02392,	2274.31846], label='Bubble Sort')
# plt.plot(entrada, [0.02489,	0.05839,	0.12393,	0.05542,	1.48654,	41.61818,	112.56013,	438.25997,	985.30289,	1755.57727], label="Quick Sort")
# plt.title('ORDENADO')
# plt.legend(ncol=2)
# plt.show()

# plt.figure(figsize=(8, 6))
# plt.xlabel("Entradas (n)")
# plt.ylabel("Tempo (s)")
# plt.plot(entrada, [0.02411,	0.05473,	0.11545,	0.01215,	0.37062,	2.94991,	4.98632,	10.41644,	16.30052,	22.49595], label="Insertion Sort")
# plt.plot(entrada, [0.02542,	0.05234,	0.11536,	0.01480,	0.37103,	3.04966,	5.17810,	10.64903,	16.72835,	22.98797], label="Merge Sort")
# plt.plot(entrada, [0.02447,	0.05292,	0.11538,	0.1591,	0.39218,	3.02214,	5.30448,	10.77895,	16.97464,	23.32704], label="Heap Sort")
# plt.title('ORDENADO')
# plt.legend(ncol=2)
# plt.show()


# INVERSO

# plt.figure(figsize=(8, 6))
# plt.xlabel("Entradas (n)")
# plt.ylabel("Tempo (s)")
# plt.plot(entrada, [0.02401,	0.05375,	0.13346,	0.13119,	2.62884,	82.58733,	228.74460,	905.46673,	2070.13404,	3614.16102], label='Bubble Sort')
# plt.plot(entrada, [0.02492,	0.04941,	0.11870,	0.04996,	1.36411,	38.52397,	105.01331,	393.55445,	912.04753,	1611.85542], label="Insertion Sort")
# plt.plot(entrada, [0.02183,	0.05086,	0.11613,	0.04495,	1.11297,	30.12976,	79.87377,	469.76799,	1055.42570,	1912.00803], label="Quick Sort")
# plt.title('INVERSO')
# plt.legend(ncol=2)
# plt.show()

# plt.figure(figsize=(8, 6))
# plt.xlabel("Entradas (n)")
# plt.ylabel("Tempo (s)")
# plt.plot(entrada, [0.02556,	0.04767,	0.10956,	0.01608,	0.37769,	3.05544,	5.17581,	10.64271,	17.02616,	22.99188], label="Merge Sort")
# plt.plot(entrada, [0.02332,	0.04903,	0.11554,	0.01515,	0.39488,	3.08138,	5.22473,	10.78365,	16.99319,	23.25239], label="Heap Sort")
# plt.title('INVERSO')
# plt.legend(ncol=2)
# plt.show()


# COMPARAÇÕES (RANDOM)

# plt.figure(figsize=(8, 6))
# plt.xlabel("Entradas (n)")
# plt.ylabel("Comparações")
# plt.plot(entrada, [9801,	62001,	249001,	998001,	24990001,	899940001,
#          2499900001,	9999800001,	22499700001,	39999600001], label='Bubble Sort')
# plt.plot(entrada, [4229,	27721,	118223,	508235,	12509989,	451075327,
#          1245917655,	5003180389,	11256097981,	20012981075], label="Insertion Sort")
# plt.title('COMPARAÇÕES (RANDOM)')
# plt.legend(ncol=2)
# plt.show()

# plt.figure(figsize=(8, 6))
# plt.xlabel("Entradas (n)")
# plt.ylabel("Comparações")
# plt.plot(entrada, [1963,	5855,	13189,	29367,	182219,	1324485,
#          2321003,	4942189,	7672003,	10483327], label="Merge Sort")
# plt.plot(entrada, [2036,	6080,	13700,	30125,	185963,	1349729,
#          2363045,	5024765,	7793627,	10648673], label="Heap Sort")
# plt.plot(entrada, [1737,	4035,	11137,	24935,	173221,	1157663,
#          1917201,	4108927,	6389987,	8571693], label="Quick Sort")
# plt.title('COMPARAÇÕES (RANDOM)')
# plt.legend(ncol=2)
# plt.show()


# RANDOM HYBRID

# plt.figure(figsize=(8, 6))
# plt.xlabel("Entradas (n)")
# plt.ylabel("Tempo (s)")
# plt.plot(entrada, [0.03200,	0.05663,	0.11252,	0.01692,	0.38311,	2.88603,
#          5.06278,	10.53470,	16.79818,	23.01261], label='HYBRID MERGE + QUICK')
# plt.title('Inverso')
# plt.legend(ncol=2)
# plt.show()

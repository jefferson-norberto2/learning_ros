from itertools import permutations, product
#Definindo programadores e artistas
prog = ['L' , 'M']
art_g = ['R', 'S', 'T', 'V']
proj = ['C', 'D', 'F']

#Criando os possíveis times de 2 artistas e um programador
times = product(art_g, prog, art_g, proj)
times_C = []
times_D = []
times_F = []

#definindo time C
for time in times:
    if 'S' and 'C' in times:
        times_C.append(time)

for time in times:
    print(time)
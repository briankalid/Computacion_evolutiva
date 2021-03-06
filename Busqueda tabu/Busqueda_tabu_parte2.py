
import random
import numpy as np


def min_st(tar, lim):
    do = float('inf')
    do_i = float('inf')

    for key, value in tar.items():
        if value <= do:
            if key not in lim:
                do = value
                do_i = key

    return [do_i, do]



def sol_ini(n, dic):
    res = []
    c_actual = '0'
    lim = [c_actual]

    for i in range(n-1):

        aux = min_st(dic[c_actual], lim)

        res.append(aux)
        lim.append(aux[0])
        c_actual = aux[0]

 
    res.append(["0", dic[c_actual]['0']])

    sum_res = 0

    for i, e in res:
        sum_res += e


    return(lim,sum_res) 




def better_cost(dic,neighborhood):

    better_way=[]
    better_cost=float('inf')


    for i, neigh in enumerate(neighborhood):
        city_actual='0'


        suma=0
        for j,city in enumerate(neigh):
            if j>0:     
                suma+=dic[city_actual][city]
                city_actual=city
        suma+=dic[city_actual]['0']


        if suma<better_cost:
            better_way=neigh
            better_cost=suma

    
    return better_way,better_cost



def gen_neighborhood(sol,l_tabu):
    neighborhood=[]

    sel_city=random.randint(1,9)

    while str(sel_city) in l_tabu:
        #print('sista')
        sel_city=random.randint(1,9)


    for i in range(len(sol)):
        if (not i==sel_city) and (i!=0) :


            aux=sol[:]

            aux[sel_city],aux[i]=aux[i],aux[sel_city]

            neighborhood.append(aux)
        

    return neighborhood,str(sel_city)


def input_file():

    file_name=input('file name: ')

    file = open(file_name,'r') 
    
    lista=[i for i in file.read().split('\n')]
    
    while '' in lista:
        lista.remove('')
    
    n=int(lista[0])

    i_max=int(lista[1])

    lista=lista[2:]

    city_bri = {}


    for i in range(n-1):

        aux = [int(j) for j in lista[i].split()]

        if str(i) not in city_bri:
            city_bri[str(i)] = {}

        for j, w in enumerate(aux):
            city_bri[str(i)][str(i+j+1)] = w

            if str(i+j+1) not in city_bri:
                city_bri[str(i+j+1)] = {}

            city_bri[str(i+j+1)][str(i)] = w

    return n,i_max,city_bri





if __name__ == "__main__":



    n,i_max,city_bri=input_file()

    m=int(input('M: '))



    b_sol=[]
    b_cost=float('inf')

    w_sol=[]
    w_cost=-float('inf')


    to_med=[]
    aux_sol_mediana=[]

    for M in range(m):

        solucion,cost=sol_ini(n, city_bri)

        psol=[]
        pcost=-float('inf')

        lista_tabu={}


        for i in range(i_max):


            neighborhood,sel_city=gen_neighborhood(solucion,lista_tabu)


            lista_aux={}
            for key in lista_tabu:
                lista_tabu[key]=lista_tabu[key]-1

                if lista_tabu[key] != 0:
                    lista_aux[key] = lista_tabu[key]

            lista_tabu=lista_aux

            lista_tabu[sel_city]=n//2


            way_aux,cost_aux=better_cost(city_bri,neighborhood)


            if cost_aux<cost:
                solucion=way_aux
                cost=cost_aux
            

        
        if cost<b_cost:
            b_cost=cost
            b_sol=solucion

        if cost>w_cost:
            w_cost=cost
            w_sol=solucion

        to_med.append(cost)

        aux_sol_mediana.append([solucion,cost])
        

    
    to_med.sort()

    if len(to_med)%2==0:
        i_mediana=to_med[(len(to_med)//2)-1]
        i_mediana=i_mediana+to_med[len(to_med)//2]
        i_mediana=i_mediana/2

    else:
        i_mediana=to_med[len(to_med)//2]


    withot_rep=[]

    for item in aux_sol_mediana:
        if item not in withot_rep:
            withot_rep.append(item)


    print("Solucion inicial",solucion,cost)
   

    print('Peor solucion:',w_sol,w_cost)
    print("Mejor solucion:",b_sol,b_cost)


    print('\nLas siguientes soluciones corresponden a la mediana:')

    for elemento in withot_rep:
        if elemento[1]==i_mediana:
            print(elemento)

    print('\n')

    print("Media:",np.mean(to_med))

    print("Desviacion estandar:",np.std(to_med))
 

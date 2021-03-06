
import random

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
        sel_city=random.randint(1,9)


    for i in range(len(sol)):
        if (not i==sel_city) and (i!=0) :


            aux=sol[:]

            aux[sel_city],aux[i]=aux[i],aux[sel_city]

            neighborhood.append(aux)
        

    return neighborhood,str(sel_city)


def input_man(n):

    city_bri = {}


    for i in range(n-1):

        aux = [int(i) for i in input().split()]

        if str(i) not in city_bri:
            city_bri[str(i)] = {}

        for j, w in enumerate(aux):
            city_bri[str(i)][str(i+j+1)] = w

            if str(i+j+1) not in city_bri:
                city_bri[str(i+j+1)] = {}

            city_bri[str(i+j+1)][str(i)] = w

    return city_bri





if __name__ == "__main__":

    n = int(input())
    i_max = int(input())


    city_bri=input_man(n)


    solucion,cost=sol_ini(n, city_bri)

    lista_tabu={}

    print("Solucion inicial",solucion,cost)
   

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
    
    print("Solucion busqueda tabu:",solucion,cost)

    

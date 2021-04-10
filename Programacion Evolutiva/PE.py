import math
import numpy as np


def f(x,n):
    s1=sum([i**2 for i in x])

    s2=sum([math.cos(2*math.pi*i) for i in x])

    return (-20*math.exp(-0.2*math.sqrt( (1/n)*s1 ))) - (math.exp( (1/n)*s2 )) + (20) + (math.e)

def fitness(x,n):
    return -f(x,n)




def sol_init(mu,n):

    population=[]

    for i in range(mu):
        var = np.random.uniform(-30,30,n)
        fact = np.random.uniform(0,1,n)


        child = [var,fact,fitness(var,n)]

        population.append(child)


    return population



def mutation(var,fact,n,alpha,epsilon):
    
    mutation_sigma = fact * (1+(alpha*np.random.normal(0,1,n)))

    mutation_sigma[mutation_sigma < epsilon] = epsilon

    mutation_x = var + (mutation_sigma*np.random.normal(0,1,n))

    mutation_x[mutation_x < -30] = -30
    mutation_x[mutation_x > 30] = 30

    return [mutation_x,mutation_sigma,fitness(mutation_x,n)]


if __name__ == '__main__':
    #input
    #n=int(input())
    #mu,G = [int(i) for i in input().split()]
    #alpha,epsilon = [float(i) for i in input().split()]

    ##


    n=2
    mu = 100
    G = 200
    alpha = 2.0
    epsilon = 0.0001

    parents = sol_init(mu,n)
    
    

    for i in range(G):
        new_gen = parents.copy()

        for p in parents:
            child = mutation(p[0],p[1],n,alpha,epsilon)

            new_gen.append(child)

        new_gen = sorted(new_gen, key=lambda child: child[-1])

        new_gen = new_gen[mu:]

        parents = new_gen.copy()

    print(parents[-1])
    
    print(round(parents[-1][-1],3))

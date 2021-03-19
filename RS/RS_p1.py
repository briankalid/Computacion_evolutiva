import random
import math


def sol_ini(n,c,ps,ws):
    
    sol=[]
    lim=[]


    continuar = True

    while continuar:
        continuar=False
        aux=c-sum(sol)

        for i,elemento in enumerate(ws):
            if (elemento<=aux) and (i not in lim):
                continuar=True


        if continuar:

            select=random.randint(0,n-1)

        
            while (select in lim) or (ws[select]>aux):
                select=random.randint(0,n-1)

            lim.append(select)
            sol.append(ws[select])
    


    aux=[0 for elemento in ps]

    for elemento in lim:
        aux[int(elemento)]=1



    return sol,[ps[i] for i in lim],aux

def bin_to_element(x,ps,ws):
    a=[p for i,p in enumerate(ps) if x[i]==1]
    b=[w for i,w in enumerate(ws) if x[i]==1]
    return a,b

def available(x,ps,ws,c):
    ps_tmp,ws_tmp=bin_to_element(x,ps,ws)
    if sum(ws_tmp)>c:
        return False
    return True



def neighborhood(s,ps,ws,c):
    res_neighborhood=[]
    
    for i in range(len(s)):
        aux=s[:]

        if aux[i]==0:
            aux[i]=1
            if available(aux,ps,ws,c):
                res_neighborhood.append(aux)

        else:
            aux[i]=0
            if available(aux,ps,ws,c):
                res_neighborhood.append(aux)

    return res_neighborhood


if __name__ == '__main__':
    T0,Tf = [float(i) for i in input().split()]
    n=int(input())
    c=float(input())

    ps=[]
    ws=[]

    for i in range(n):
        p,w=[float(i) for i in input().split()]
        ps.append(p)
        ws.append(w)


    w_inicial,p_inicial,i_sol_in=sol_ini(n,c,ps,ws)

    print('Solucion inicial',w_inicial,p_inicial,i_sol_in,sum(p_inicial))


    T=[T0]
    X=[i_sol_in]
    
    x_best=i_sol_in
    f_best=sum(p_inicial)


    t=0

    while T[t] >= Tf:
        y=random.choice(neighborhood(X[t],ps,ws,c))
        #print(y,bin_to_element(y,ps,ws))
        f_aux=sum(bin_to_element(y,ps,ws)[0])
        #print(f_aux)
        if f_aux > f_best:
            x_best=y
            f_best=f_aux


        comp = math.e**( (-1*(f_aux) - sum(bin_to_element(X[t],ps,ws)[0])) /T[t]  )


        if (f_aux <= sum(bin_to_element(X[t],ps,ws)[0])) or (random.uniform(0,1)<comp):
            X.append(y)

        else:
            X.append(X[t])

        T.append(0.99*T[t])
        t+=1


    print(bin_to_element(x_best,ps,ws),x_best,f_best)



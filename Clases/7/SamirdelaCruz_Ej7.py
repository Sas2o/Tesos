import random

#1.1

def direct_pi(N):
    Nhits=0
    for i in range(N):
        x=(random.random()-0.5)*2
        y=(random.random()-0.5)*2
        if x**2+y**2<1:
            Nhits+=1
    return Nhits
N=4000
print(direct_pi(N)/1000)

#1.2

def markov_pi(N,r):
    Nhits=0
    x,y=(random.random()-0.5)*r,(random.random()-0.5)*r
    for i in range(N):
        dx=(random.random()-0.5)*r
        dy=(random.random()-0.5)*r
        if abs(x+dx)<1 and abs(y+dy)<1:
            x+=dx
            y+=dy
        if x**2+y**2<1:
            Nhits+=1
    return Nhits
N=4000
r=0.3
print(markov_pi(N,r)/1000)

#1.8

def markov_two_site(k):
    pesoP=[1,1]
    if k==0:
        l=1
        pesoP[0]+=1
    elif k==1:
        l=0
        pesoP[1]+=1
    Upsilon=pesoP[l]/pesoP[k]
    if random.random()<Upsilon:
        k=l
    return k
site=[int(random.random()*2)]
for i in range(100):
    site.append((markov_two_site(site[-1])))
print(site)

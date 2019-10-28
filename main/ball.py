from vpython import *
from random import *

#ball = sphere(pos=(-5, 0,0), radius =0.5)

lado=4.0
espessura=0.3

parede = box(pos=vector(6, 0,0), size = vector(0.2, 12, 12), opacity=0.2)
parede2 = box(pos= vector(-6,0,0), size = vector(0.2, 12, 12), opacity=0.2)
parede3 = box(pos= vector(0,6,0), size = vector(12, 0.2, 12), opacity=0.2)
parede4 = box(pos= vector(0,-6,0), size = vector(12, 0.2, 12), opacity=0.2)
parede5 = box(pos= vector(0,0,-6), size = vector(12, 12, 0.2), opacity=0.2)
parede6 = box(pos= vector(0,0,6), size = vector(12, 12, 0.2), opacity=0.2)

#cria um conjunto de partículas com posições aleatórias
no_particulas= int(input("no_particulas.: "))
raio=0.4

maxv=10.0
x = 2
esferas=[] 
for i in range(no_particulas): 
    ball = sphere(pos=vector(-5, 0,0), radius=raio)
    ball.pos=vector(uniform(-1-x,1+x),uniform(-1-x,1+x),uniform(-1-x,1+x)) 
    ball.velocidade=maxv*vector(uniform(-1,1),uniform(-1,1),uniform(-1,1)) 
    esferas.append(ball)
    x = x + 2 
dt = 0.005
scene.autoscale = False

#ball.trail = curve()

while True:
    rate(100)
    x = randint(1,6)
    y = randint(-10,10)
    z = randint(-6,6)
    for ball in esferas: #repete sobre a lista de partículas 
        #ball.trail.append(pos = ball.pos)   
        if ball.pos.x + raio>= parede.pos.x:
            ball.velocidade = vector(25, y, z)
            ball.velocidade = -ball.velocidade
        elif ball.pos.x - raio <= parede2.pos.x:
            ball.velocidade = vector(25, y, z)
            ball.velocidade = ball.velocidade
        elif ball.pos.y + raio >= parede3.pos.y:
            ball.velocidade = vector(x, -25, z)
            #ball.velocidade = ball.velocidade
        elif ball.pos.y - raio <= parede4.pos.y:
            ball.velocidade = vector(x, 25, z)
        elif ball.pos.z - raio<= parede5.pos.z:
            ball.velocidade = vector(x,y,25)
        elif ball.pos.z + raio >= parede6.pos.z:
            ball.velocidade = vector(x,y,-25)
       # elif x.pos == esferas[x+1].pos:
        #    ball.
        ball.pos = ball.pos + ball.velocidade*dt

    for i in range(no_particulas):
        for j in range(i+1,no_particulas):
            distancia = mag(esferas[i].pos - esferas[j].pos)
            if distancia <= 2*raio:
                esferas[i].velocidade, esferas[j].velocidade = esferas[j].velocidade, esferas[i].velocidade

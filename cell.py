import pygame
import GlobalVar
from Vector2 import Vector2
import random
import math
import chunk

class Cell:
    def __init__(self,pos) -> None:
        self.vita0 = random.randint(10,30) # vita iniziale
        self.vitaRimanente = self.vita0
        self.dim = 2   
        self.raggio = random.randint(100,120) # raggio di visione

        self.pos = Vector2(pos[0],pos[1])
        self.vel = random.randrange(1,3)
        self.dir = Vector2(random.randrange(0,GlobalVar.resolution[0]),random.randrange(0,GlobalVar.resolution[1]))

        self.ciboTrovato=False

        self.reprProb = random.randint(30,70) # probabilità che una cellula si riproduca quando mangia
        self.chunkIndex = [0,0]

    def vivo(self):
        if self.vitaRimanente>0: return True
        else: return False

    def muoviversodir(self):
        self.pos = self.pos + (self.dir.Sub(self.pos)).normalized()*(self.vel)

    def cambiaDir(self,var):
        '''
        cambia la direzione in un range di var pixel
        '''
        rand = (random.randint(self.dir.x-var,self.dir.x+var),random.randint(self.dir.y-var,self.dir.y+var))
        if rand[0]>0 and rand[0]<GlobalVar.resolution[0] and rand[1]>0 and rand[1]<GlobalVar.resolution[1]:
            self.dir.Set(rand[0],rand[1])

    def renderizza(self):
        # disegna i raggi di visione
        #pygame.draw.circle(GlobalVar.MainWindow,(100,100,100),self.pos.tuple(),self.raggio,1)

        # disegna le cellule
        pygame.draw.circle(GlobalVar.MainWindow,GlobalVar.white,self.pos.tuple(),self.dim)
        
        # disegna le dir
        #pygame.draw.circle(GlobalVar.MainWindow,GlobalVar.white,self.dir.tuple(),self.dim)
    
    def generaFigli(self,numfigli,arr):
        '''
        genera figli in base alla dimensione => in base a quanti pellet ha mangiato.
        Ereditano determinati tratti dal genitore
        '''
        numfigli *= 2
        for i in range(numfigli):
            newcell = Cell(self.pos.tuple())
            newcell.vita0 = self.vita0
            newcell.vel = self.vel
            arr.append(newcell)


    def calcolaDistanze(self,ciboArray):
        '''
        calcola il pellet più vicino e cambia la direzione della cellula se è interno al raggio
        '''
        if ciboArray:               # se l'array non è vuoto
            vicino = ciboArray[0]
            distmin = self.pos.Sub(vicino.pos).sqrMag()
            for c in ciboArray:     # calcola le distanze da ogni pellet nello stesso chunk
                if self.chunkIndex == c.chunkIndex:
                    d=self.pos.Sub(c.pos).sqrMag()
                    if distmin > d:
                        distmin = d
                        vicino = c      # restituisce il pellet più vicino
            if math.sqrt(distmin)<=self.raggio: # se il pellet più vicino è nel raggio di visione
                self.ciboTrovato = True
                self.dir = vicino.pos   # imposta la direzione su quel pellet

    def mangia(self,arr):
        '''
        decide se ingrandirsi o riprodursi
        '''
        if random.randint(0,100) >= self.reprProb:
            self.dim += 1
            self.vitaRimanente += 10
        else:
            self.generaFigli(self.dim-1,arr)
            arr.remove(self)

    def update(self,cibo,arrcell):
        if self.vivo():
            chunk.assegnaIndice(self,GlobalVar.chunkArr)
            self.muoviversodir()

            if not self.ciboTrovato:
                self.calcolaDistanze(cibo)
                if random.choice([0,1]) and not self.ciboTrovato: # 50%
                    self.cambiaDir(random.randrange(10,50))

            self.renderizza()
            self.vitaRimanente -= 1/GlobalVar.fps
        
        else:
            arrcell.remove(self)
            del self

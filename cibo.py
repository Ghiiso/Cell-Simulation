import pygame
import GlobalVar
import random
from Vector2 import Vector2

class Cibo:
    def __init__(self,pos) -> None:
        self.pos = Vector2(pos[0],pos[1])
        self.color = GlobalVar.red

    def renderizza(self):
        pygame.draw.circle(GlobalVar.MainWindow,self.color,self.pos.tuple(),2)
    def update(self):
        self.renderizza()

    def generaGriglia(arr,chunk):
        '''
        genera una griglia di pellet e li aggiunge all'array ciboArray
        '''
        chunkleght = [int(GlobalVar.resolution[0]/chunk),int(GlobalVar.resolution[1]/chunk)] # divide la larghezza dello schermo in tot chunk

        for i in range(1,chunk+1):
            #pygame.draw.line(GlobalVar.MainWindow,GlobalVar.white,(chunkleght[0]*i,0),(chunkleght[0]*i,GlobalVar.resolution[1]))
            #pygame.draw.line(GlobalVar.MainWindow,GlobalVar.white,(0,chunkleght[1]*i),(GlobalVar.resolution[0],chunkleght[1]*i))
            for j in range(1,chunk+1):
                # genera una coppia di numeri all'interno di ogni chunk
                rand = ( random.randrange(chunkleght[0]*(i-1),chunkleght[0]*i), random.randrange(chunkleght[1]*(j-1),chunkleght[1]*j) )
                arr.append(Cibo(rand))


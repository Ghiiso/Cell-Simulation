import pygame
import matplotlib.pyplot as plt
import graph
import math
import GlobalVar
from Vector2 import Vector2
from Input import Input
from cell import Cell
from cibo import Cibo
import random

pygame.init()
GlobalVar.init()
runGame=True
FPS = pygame.time.Clock()

startcellule = 5
startpellet = 5

i=0
sec=0
time = []
ciboLen = []
cellLen = []

ciboArr = []
cellArr = []
for i in range(startcellule): # genera le cellule
    rand = (random.randrange(30,GlobalVar.resolution[0]-30),random.randrange(30,GlobalVar.resolution[1]-30))

    cellArr.append(Cell(rand))


while runGame:
    pygame.display.update()
    GlobalVar.MainWindow.fill(GlobalVar.black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Cibo.generaGriglia(ciboArr,startpellet)

    if Input.Check(pygame.K_ESCAPE):
        runGame = False

    for cell in cellArr:
        cell.update(ciboArr,cellArr)
        if cell.ciboTrovato:
            for cibo in ciboArr:
                if cibo.pos.Sub(cell.pos).magnitude()<1:
                    ciboArr.remove(cibo)
                    cell.mangia(cellArr)
            cell.ciboTrovato=False

    for cibo in ciboArr:        
        cibo.update()
    
    
    if(i!=GlobalVar.fps):
        i += 1
    else:
        i=0
        time.append(sec)
        sec += 1
        ciboLen.append( len(ciboArr))
        cellLen.append(len(cellArr))


    FPS.tick(GlobalVar.fps)
pygame.quit()

graph.mostraGrafici(cellLen,ciboLen,time)
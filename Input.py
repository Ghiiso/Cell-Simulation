import pygame

class Input:
    def __init__(self) -> None:
        pass
    
    def Check(key) -> bool:
        '''
        ritorna True se "key" è premuto
        '''
        keys = pygame.key.get_pressed()
        return keys[key]
    
    def GetAxisRaw(keys) -> int:
        '''
        ritorna un valore tra -1,0,1:
        il primo valore passato è l'asse positivo
        '''
        return int(Input.Check(keys[0]))-int(Input.Check(keys[1]))


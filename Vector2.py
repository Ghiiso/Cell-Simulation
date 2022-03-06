import math

class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def tuple(self) -> tuple:
        '''
        tupla di coordinate (read only)
        '''
        return self.x,self.y

    def sqrMag(self) -> float:
        return self.x**2+self.y**2

    def magnitude(self) -> float:
        '''
        modulo (read only)
        '''
        return math.sqrt(self.sqrMag())

    def normalized(self):
        '''
        nuovo vettore normalizzato
        '''
        mag = self.magnitude()
        if mag!=0:
            return Vector2(self.x/mag,self.y/mag)
        else: return Vector2(0,0)

    def changeMag(self,newmag):
        newmag = newmag/self.magnitude()
        return Vector2(self.x*newmag,self.y*newmag)

    def Equals(self,vettore) -> bool:
        return self.x == vettore.x and self.y == vettore.y
    
    def Add(self,vettore):
        return Vector2(self.x+vettore.x,self.y+vettore.y)

    def Sub(self,vettore):
        return Vector2(self.x-vettore.x,self.y-vettore.y)

    def Mult(self,fac):
        return Vector2(self.normalized().x*fac,self.normalized().y*fac)

    def Div(self,fac):
        return Vector2(self.normalized().x/fac,self.normalized().y/fac)
    def Set(self,newx,newy):
        '''
        cambia il valore del vettore
        '''
        self.x = newx
        self.y = newy

    # operator overloading = bellissimi
    # le funzioni vengono chiamate quando la corrispondente operazione viene eseguita

    def __add__(self,v):
        return Vector2.Add(self,v)

    def __mul__(self,factor):
        return Vector2.Mult(self,factor)

    def __sub__(self,v):
        return Vector2.Sub(self,v)

    def __eq__(self,v):
        return Vector2.Equals(self,v)

    #vettorini semplicini

    def zero():
        '''
        crea un oggetto vettore nullo
        '''
        return Vector2(0,0)

    def up():
        '''
        crea un oggetto vettore che punta in alto
        '''
        return Vector2(0,-1)
    def down():
        '''
        crea un oggetto vettore che punta in basso
        '''
        return Vector2(0,1)
    def left():
        '''
        crea un oggetto vettore che punta a sinistra
        '''
        return Vector2(-1,0)
    def right():
        '''
        crea un oggetto vettore che punta a destra
        '''
        return Vector2(1,0)
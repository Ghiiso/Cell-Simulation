
class Chunk:

    def __init__(self,index,limX,limY):
        self.index = index
        self.x_dx = limX[0]
        self.x_sx = limX[1]
        self.y_sup = limY[0]
        self.y_inf = limY[1]

def init(res,div):
    '''
    ritorna un array formato da div^2 Chunk, assegnando un indice e i bordi dx sx sup e inf
    '''
    xl = res[0]/div
    yl = res[1]/div
    arrGriglia = []
    for i in range(div):
        for j in range(div):
            arrGriglia.append(Chunk( (i,j), (xl*i,xl*(i+1)), (yl*j,yl*(j+1)) ))

    return arrGriglia

def assegnaIndice(obj,arrGriglia):
    '''
    data un oggetto, assegna l'indice del chunk in cui si trova
    '''
    for chunk in arrGriglia:
        if obj.pos.x >= chunk.x_dx and obj.pos.x < chunk.x_sx:
            if obj.pos.y >= chunk.y_sup and obj.pos.y < chunk.y_inf:
                obj.chunkIndex = chunk.index
                return
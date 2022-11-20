import math
class Coordenada:
    def __init__(self,coords=(0,0),extra ="-1"):
        if extra != "-1":
            raise Exception('Numero de argumentos errado: 2')
        if type(coords) is not tuple:
            raise Exception("Parâmetro não é uma tupla")
        if len(coords) != 2:
            raise Exception(f"Numero de coordenadas inválido: {len(coords)}")
        if not (all(isinstance(x, (int, float)) for x in coords)):
            raise Exception("Elemento da tupla não é int or float")

        self.x=coords[0]
        self.y=coords[1]
    
    def distancia(self, other):
        return math.sqrt( math.pow(self.x-other.x,2) +  math.pow(self.y-other.y,2))

    def asTuple(self):
        return (self.x, self.y)

    def asList(self):
        return [self.x, self.y]

    def __str__(self):
        return f"({self.x}, {self.y})"
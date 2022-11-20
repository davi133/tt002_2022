from Coordenada import Coordenada
from copy import deepcopy
import random
import time
from PIL import  Image, ImageDraw

class Rota:
    def __init__(self):
        self.pontos =[]
        self.tudo = False

    def addCoord(self, coordenada):
        self.pontos.append(coordenada)

    def __str__(self):
        txt =""
        for i in self.pontos:
            txt += f"{i}->"
        txt += str(self.pontos[0])
        return txt

    def comprimento(self):
        compr =0
        for i in reversed(range(len(self.pontos))):
            compr += self.pontos[i].distancia(self.pontos[i-1])
        return compr

    def copy(self):
        return deepcopy(self)

    def shuffle(self):
        if self.tudo:
            random.shuffle(self.pontos)
        else:
            aux= self.pontos[1:]
            random.shuffle(aux)
            self.pontos = [self.pontos[0]] +aux

    def __popClosestPointTo(self, coord):
        closest = self.pontos[0]
        menor_dist = coord.distancia(closest)
        menor_i=0
        for i in range(len(self.pontos)):
            if coord.distancia(self.pontos[i]) < menor_dist:
                closest = self.pontos[i]
                menor_dist = coord.distancia(self.pontos[i])
                menor_i=i

        self.pontos.pop(menor_i)
        return closest


    def otimiza(self):
        otimizado = Rota()
        copia = self.copy()
        copia.pontos.pop(0)
        otimizado.addCoord(self.pontos[0])
        for i in range(len(self.pontos[1:])):
            otimizado.addCoord(copia.__popClosestPointTo(otimizado.pontos[-1]))
        self.pontos = otimizado.pontos

    def espera(self,t):
        tin = time.time()
        delta = time.time() - tin
        segundos_contados=0;
        while delta < t:
            delta = time.time() - tin
            while delta > segundos_contados:
                print(f"Esperando : {segundos_contados*1000}")
                segundos_contados +=1

    def randomCoords(self,  n, max_coord):
        self.pontos = []
        for i in range(n):
            x = random.randint(1, max_coord)
            y = random.randint(1, max_coord)
            self.pontos.append(Coordenada((x, y)))

    def maximo(self):
        max_x = -99999
        max_y = -99999
        for ponto in self.pontos:
            if ponto.x > max_x:
                max_x = ponto.x
            if ponto.y > max_y:
                max_y = ponto.y
        return (max_x, max_y)

    def desenha(self, pathname):
        maxs = self.maximo()
        maxs = (maxs[0]+30,maxs[1]+50)
        img = Image.new('P',maxs,"#fff")
        draw = ImageDraw.Draw(img)

        for i in range(len(self.pontos)-1):
            A = self.pontos[i].asList()
            A[0] += 15
            B = self.pontos[i+1].asList()
            B[0] += 15
            draw.line((tuple(A), tuple(B)), fill="#000", width=3)
        draw.line((self.pontos[-1].asTuple(), self.pontos[0].asTuple()), fill="#000", width=3)

        coord = (20, maxs[1]-25)
        draw.text(coord, f"Custo: {self.comprimento()}",fill="#000")

        start = self.pontos[0].asTuple()
        draw.ellipse( (tuple([start[0]-5,start[1]-5]),tuple([start[0]+5,start[1]+5])), outline="#00f", width=3)
        img.save(pathname)
        return  img











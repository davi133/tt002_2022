import random
from Rota import Rota
import time
from matplotlib import pyplot

# Ainda não é para entregar. Em grupo de 3 pessoas.
# Vai ser pedido para entregar futuramente, junto
# com o conteúdo da aula 11.


class Otimizador:
    # Este é o construtor do otimizador. Você pode adicionar código aqui
    # se julgar necessário.
    def __init__(self):
        self.plt = pyplot
        self.fig, self.ax = self.plt.subplots()
        self.plt.xlabel("Tempo(ms)")
        self.plt.ylabel("Comprimento (pixel)")
        self.plt.title("Comprimento versus tempo(ms)")

    # Este método de otimização já está implementado.
    # Toda vez que o comprimento for atualizado para um valor menor, é
    # necessário salvar o comprimento e o tempo gasto na função
    # para fazer o gráfico.
    # Ao final da execução, é necessário usar o matplotlib (pyplot)
    # para gerar o gráfico (comprimento X tempo).
    # Deve ser feito o mesmo para a função de otimização 'aleatório'
    # e 'otimizadorGrupo1'
    # As três séries temporais devem ser salvas em um mesmo gráfico,
    # conforme figuras 'Resultado_10x.py'
    # Seu grupo pode adicionar código nesta função se julgar necessário.
    # O mesmo para os outros dois otimizadores.
    # A linha do gráfico referente ao 'SingleSwap' deve estar em preto.
    # A linha do gráfico referente ao 'Aleatório' deve estar em verde.
    # A linha do gráfico referente ao 'otimizadorGrupo1' deve estar em azul
    # e deve ser mais grossa que a linha dos outros algoritmos.
    # Todas as linhas devem iniciar no tempo zero e terminar no tempo final.
    def singleSwap(self, rota: Rota, time_ms: int):
        tempo_x = []
        compr_y = []
        # Inicia a partir de uma rota não otimizada
        rota.shuffle()
        # Tempo de entrada na função.
        tin = round(time.time() * 1000)
        # Tempo gasto na função.
        delta_ms = round(time.time() * 1000) - tin
        minComprimento = rota.comprimento()
        while delta_ms < time_ms:
            # atualiza delta
            delta_ms = round(time.time() * 1000) - tin
            size_rota = len(rota.pontos)
            pos1 = random.randrange(0, size_rota)
            pos2 = random.randrange(0, size_rota)
            swap(rota, pos1, pos2)
            if rota.comprimento() < minComprimento:
                minComprimento = rota.comprimento()
            else:
                # desfaz o swap
                swap(rota, pos1, pos2)
            tempo_x += [delta_ms]
            compr_y += [minComprimento]
        self.plt.plot(tempo_x, compr_y, color='#000000', label="SingleSwap")

    def aleatorio(self, rota: Rota, time_ms: int):
        tempo_x = []
        compr_y = []
        # inicia a partir de uma rota não otimizada
        rota.shuffle()
        tin = round(time.time() * 1000)
        delta_ms = round(time.time() * 1000) - tin
        minComprimento = rota.comprimento()
        while delta_ms < time_ms:
            delta_ms = round(time.time() * 1000) - tin
            rotaAux = rota.copy()
            rotaAux.shuffle()
            if rotaAux.comprimento() < minComprimento:
                rota.pontos = rotaAux.pontos
                minComprimento = rota.comprimento()
            tempo_x += [delta_ms]
            compr_y += [minComprimento]
        self.plt.plot(tempo_x, compr_y, color='#0A0', label="Random")

    # Aqui você deve usar sua criatividade e propor um algoritmo de
    # otimização. O algoritmo deixado é apenas um exemplo.
    # Ao fixar um label para o seu grupo
    # dê um nome para o seu grupo que o diferencie dos demais.
    # Veja a Figura Resultado_10x.png. No lugar de 'Algoritmo do Grupo 1'
    # deve estar um nome curto que identifique o seu grupo. O nome deve
    # ser composto de um nome dos integrantes. Exemplo:
    # Rodrigo_Ivan_Celso
    def otimizadorGrupo1(self, rota: Rota, time_ms: int):
        tempo_x = []
        compr_y = []
        # inicia a partir de uma rota não otimizada
        rota.shuffle()
        tin = round(time.time() * 1000)
        delta_ms = round(time.time() * 1000) - tin
        minComprimento = rota.comprimento()
        size_rota = len(rota.pontos)
        candidates_qtd = max(round(size_rota * .01), 3)
        pointer=0
        while delta_ms < time_ms:
            delta_ms = round(time.time() * 1000) - tin
            candidates = [random.randrange(0, size_rota) for a in range(3)]
            menor =-1
            menor_dist=9000000
            for i in candidates:
                dist = rota.pontos[pointer].distancia(rota.pontos[i])
                if dist < menor_dist:
                    menor_dist = dist
                    menor = i

            pos1 = pointer
            pos2 = menor
            swap(rota, pos1, pos2)

            pointer+=1
            pointer= pointer % (len(rota.pontos))
            if rota.comprimento() < minComprimento:
                minComprimento = rota.comprimento()
            else:
                swap(rota, pos1, pos2)
            tempo_x += [delta_ms]
            compr_y += [minComprimento]
        self.plt.plot(tempo_x,compr_y, linewidth=3, color='#00A', label="otimizadorGrupo1")

    def cleanGraph(self):
        self.plt.clf()
    # Esta função deve salvar o gráfico. A função não deve ser alterada.
    # O objetivo final é colocar vários algoritmos vindos de grupos diferentes
    # num mesmo gráfico e depois esta função irá salvar a solução com todos os gráficos.
    def salvaFigura(self, filename):
        self.plt.tight_layout()
        self.plt.legend()
        self.plt.savefig(filename)


def swap(rota: Rota, pos1: int, pos2: int):
    aux = rota.pontos[pos1]
    rota.pontos[pos1] = rota.pontos[pos2]
    rota.pontos[pos2] = aux


# Cria uma rota Vazia.
r = Rota()
# Número de coordenadas da rota
size = int(input("Digite o número de vértices:"))
# valor máximo x e y para a coordenada
r.randomCoords(size, 400)
# Cria o otimizador
opt = Otimizador()
# Tempo de otimização em ms
time_ms = int(input("Digite o tempo em ms:"))
# Otimiza por single swap
opt.singleSwap(r, time_ms)
# Otimização aleatório
opt.aleatorio(r, time_ms)
# Otimização feita por seu grupo
opt.otimizadorGrupo1(r, time_ms)
opt.salvaFigura("Resultado_" + str(size) + ".png")

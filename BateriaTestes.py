from OtimizadorBase import Otimizador
import matplotlib.pyplot as plt
from Rota import Rota
import numpy as np
from Rota import Rota

class BateriaTestes:
    funcoes = []

    def addFuncao(self, funcao, nome):
        self.funcoes.append((funcao, nome))


    ''''
    Em grupo de 3 pessoas. Apenas uma envia o arquivo no moodle. Nome dos 
    três integrantes dentro do arquivo. Esta tarefa não pode ser adiada.
    Veja o prazo no moodle.
    Você deve fazer primeiro a tarefa descrita na Aula 10 e depois resolver esta
    tarefa (aula 11).
    
    Primeiramente deve ser cadastrado um conjunto de funções de otimização na classe
    BateriaTestes, através do método addFunção. Esta função, chamada 'executa', recebe
    o número de repetições que pode ser 3, 5 ou 10 por exemplo. O tempo, em ms, e uma 
    lista de tamanhos. Por exemplo, se a lista de tamanhos for [10,100,100], deve-se executar
    as funções para rotas de tamanho 10, 1000 e 1000. Deve ser criada uma única instância (rota) 
    para ser otimizada para cada valor distinto em sizeList. No caso de sizeList for [10,100,1000],
    devem ser criadas 3 rotas, uma com 10, uma com 100 e uma com 1000 coordenadas.
    A rota deve ser otimizada por cada uma das funções. Além disso, deve-se repetir a otimização
    'n_repeticoes' vezes. Por exemplo se n_repeticoes=10, deve-se executar a função de otimização
    10 vezes e calcular a média e o desvio padrão. Uma vez que todos estes dados foram calculados,
    deve ser criado um gráfico igual ao disponível em 'Bateria.png'. 
    A média é o comprimento da barra e o desvio padrão é o erro que está no topo da barra.
    Note que, se sizeList for 
    alterado para mais ou para menos valores, o gráfico deve ser criado automaticamente para o 
    novo conjunto sizeList. Também se forem adicionadas ou removidas funções em self.funções, o 
    gráfico deve continuar executando de maneira automática.
    A bateria de testes executa 'n_repeticoes' vezes para cada par funcao X size.
    Deve ser criado um gráfico para cada size em sizeList. Por exemplo, se sizeList for [10,100,1000]
    deve ser criado um gráfico Otimizacao_10.png, Otimizaca_100.png e Otimizacao_1000.png. No gráfico
    Otimização_10.png deve ficar a primeira execução de cada função em instâncias de tamanho 10. 
    O mesmo para size 100 e 1000. Veja Os gráficos Otimização_X.png para ter um exemplo. 
    
    No lugar de 'Grupo 1'
    # deve estar um nome curto que identifique o seu grupo. O nome deve
    # ser composto de um nome dos integrantes. Exemplo:
    # Rodrigo_Ivan_Celso. Além disso, o arquivo Phyton deve seguir o mesmo padrão.
    # BateriaTestes_Rodrigo_Ivan_Celso.py.
    '''

    def executa(self, n_repeticoes: int, tempo_ms, sizeList):
        labels = []
        rotas = dict()
        for size in sizeList:
            print(f"Criando Rota_"+str(size))# e labels
            labels += [size]
            rota_original = Rota()
            rota_original.randomCoords(size, 400)
            rotas[size] = rota_original.copy()
            opt = Otimizador()
            for otimizador in self.funcoes:
                otimizador[0](rota_original, tempo_ms)
            opt.salvaFigura(f"Otimizacao_{size}.png")
            opt.cleanGraph()

        todas_medias = dict()
        todos_desvios = dict()
        for size in sizeList:
            rota = rotas[size]
            for otimizador in self.funcoes:
                total = 0
                all_results = []
                for rep in range(n_repeticoes):
                    print(f"Repetição {rep} da função {otimizador[1]} com "+str(size)+" vertices")
                    rota_c = rota.copy()
                    otimizador[0](rota_c, tempo_ms)
                    total += rota_c.comprimento()
                    all_results += [rota_c.comprimento()]
                todas_medias[otimizador[1]] = todas_medias.get(otimizador[1],[]) +[total/n_repeticoes]
                todos_desvios[otimizador[1]] = todos_desvios.get(otimizador[1], []) + [np.std(all_results)]
        #print(json.dumps(todas_medias))
        self.__makeGraph(todas_medias,todos_desvios,labels)



    def __makeGraph(self,medias,desvios,labels):
        plt.clf()
        fig, ax = plt.subplots()
        ax.set_ylabel('Custo')

        x = np.arange(len(labels))
        ax.set_xticks(x, labels)

        width = 0.5  # the width of the bars
        total_width = width / len(medias)
        i = 0
        for key in medias:
            print(f"label is ={key}")
            ax.bar(x - total_width / 2 + (i * total_width), medias[key], total_width,yerr=desvios[key], label=key, error_kw=dict(lw=1, capsize=5, capthick=1))
            #ax.bar(x - total_width / 2 + (i * total_width), medias[key], total_width, label=key, )
            i += 1


        fig.tight_layout()
        ax.legend()
        fig.savefig("BateriaTestes_Davi_Guilherme_Pedro.png")


'''
Esta parte do código cria uma bateria de teste, cadastra as funções
e executa a bateria de testes. Esta parte não deve ser alterada.
Note que ao adicionar uma função também é passado um nome (rótulo) 
para a funcão. Todo o resto deve acontecer dentro da função executa.
'''
bt = BateriaTestes()
otimizador = Otimizador()
bt.addFuncao(otimizador.singleSwap, "singleSwap")
bt.addFuncao(otimizador.aleatorio, "aleatorio")
bt.addFuncao(otimizador.otimizadorGrupo1, "Davi_Guilherme_Pedro")

# tempo_ms = 300
# repeticoes = 5
# size = [10,100,500,1000]
# bt.executa(repeticoes, tempo_ms, size)

tempo_ms = 3000 #TODO: voltar pro orignal, que é 3000
repeticoes = 10
size = [10, 100, 250, 500, 750, 1000]
bt.executa(repeticoes, tempo_ms, size)

import networkx
from database import DAO

class Model:
    def __init__(self):
        self._grafo = networkx.DiGraph()
        self._listaNodi=[]
        self._listaArchi=[]




    def aggiungiNodi(self):
        """self._listaGeni=DAO.DAO.getGeni()
        for gene in self._listaGeni:
            if gene.Chromosome not in self._listaNodi and gene.Chromosome!=0:
                self._listaNodi.append(gene.Chromosome)
        self._grafo.add_nodes_from(self._listaNodi)
        """
        self._listaNodi = DAO.DAO.getNodi()
        print(len(self._listaNodi))
        self._grafo.add_nodes_from(self._listaNodi)



    def aggiungiArchiAListaArchi(self):
        self._listaArchi = DAO.DAO.getArchi()


    def aggiungiArchiPesati(self):
        print()
        print(self._listaArchi)
        for arco in self._listaArchi:
            print()
            print(arco)
            arcoPesato = DAO.DAO.getArcoPesato(arco)[0]
            self._grafo.add_edge(arcoPesato[0],arcoPesato[1], weight=arcoPesato[2])

    def getPesiMinMax(self): #grafo è dizionario di dizionari
        min=13214134
        max=-4313424
        for i in self._grafo:
            for j in self._grafo[i]:
                if self._grafo[i][j]["weight"]>max:
                    max=self._grafo[i][j]["weight"]
                if self._grafo[i][j]["weight"]<min:
                    min=self._grafo[i][j]["weight"]
        return min,max #ritorna tupla con min e max come valori

    def creaGrafo(self):
        #preparo a nuovo utilizzo
        self._listaNodi.clear()
        self._listaArchi.clear()
        self._grafo.clear()

        self.aggiungiNodi()
        self.aggiungiArchiAListaArchi()
        self.aggiungiArchiPesati()



    def getNumeroNodi(self):
        return len(self._grafo.nodes())

    def getNumeroArchi(self):
        return len(self._grafo.edges())

    def getNumeroArchiMinoriMaggioriSoglia(self, soglia):
        numeroArchiConPesoMinoreSoglia= 0
        numeroArchiConPesoMaggioreSoglia = 0
        for i in self._grafo:
            for j in self._grafo[i]:
                if self._grafo[i][j]["weight"]<soglia:
                    numeroArchiConPesoMinoreSoglia+=1
                if self._grafo[i][j]["weight"]>soglia:
                    numeroArchiConPesoMaggioreSoglia+=1
        return numeroArchiConPesoMinoreSoglia,numeroArchiConPesoMaggioreSoglia #ritorna tupla con sti due valori
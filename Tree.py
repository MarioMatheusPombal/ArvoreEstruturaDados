class Tree:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
    
    def buscaAlturaNo(self, valor):
        if self.raiz == None:
            return 0
        else:
            return self.raiz.buscaAlturaNo(valor)
    
    def buscaAlgo(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.buscaAlgo(valor)

    def alturaMaxArvore(self):
        if self.raiz != None:
            return self.raiz.alturaMaxArvore()
    
    def NivelDeterminadoNo(self, valor):
        if self.raiz != None:
            return self.raiz.NivelDeterminadoNo(valor)

    def herdeiroMaisDir(self):
        if self.raiz != None:
            return self.raiz.herdeiroMaisDir()
    
    def herdeiroMaisEsq(self):
        if self.raiz != None:
            return self.raiz.herdeiroMaisEsq()
    
    def printCaminho(self, valor):
        if self.raiz != None:
            return self.raiz.printCaminho(valor) - 1
    
    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()
            
    def somaTudo(self):
        if self.raiz != None:
            return self.raiz.somaTudo()
    
    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()

    def inOrdem(self):
        if self.raiz != None:
            return self.raiz.inOrdem()
    
    def printCaminhoAteMenor(self):
        if self.raiz != None:
            return self.raiz.printCaminhoAteMenor()
    
    def calculaMedia(self):
        return (self.raiz.herdeiroMaisEsq() + self.raiz.herdeiroMaisDir())/2

    def printDescendentes(self,valor):
        if self.raiz != None:
            return self.raiz.printDescendentes(valor)

class No:

    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)                
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)

    def buscaAlturaNo(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.buscaAlturaNo(valor)
                if aux == 0:
                    return 0
                else:
                    return aux +1
        else:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.buscaAlturaNo(valor)
                if aux == 0:
                    return 0
                else:
                    return aux +1
    
    def buscaAlgo(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                return 1 + self.esq.buscaAlgo(valor)
        else:
            if self.dir == None:
                return 0
            else:
                return 1 + self.dir.buscaAlgo(valor)

    def max(self, a, b):
        if a>b:
            return a
        return b
    
    def alturaMaxArvore(self):
        hesq=hdir=0
        if self.esq!=None:
            hesq=self.esq.alturaMaxArvore()
        if self.dir!=None:
            hdir=self.dir.alturaMaxArvore()
        return 1 + max(hesq,hdir)
    
    def NivelDeterminadoNo(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info: 
            if self.esq == None:
                return 0
            else:
                aux = self.esq.NivelDeterminadoNo(valor)
                if aux != 0:
                    return 1+aux
                else:
                    return False
        else:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.NivelDeterminadoNo(valor)
                if aux != 0:
                    return 1+aux
                else:
                    return 0
    
    def herdeiroMaisDir(self):
        if self.dir!=None:
            return self.dir.herdeiroMaisDir()
        else:
            return self.info
    
    def herdeiroMaisEsq(self):
        if self.esq!=None:
            return self.esq.herdeiroMaisEsq()
        else:
            return self.info
    
    def printCaminho(self, valor):
        if valor == self.info:
            print(self.info)
            return 1 
            
        elif valor < self.info:
            if self.info != None:
                print(self.info)
            if self.esq == None:
                return 0
            else:
                aux = self.esq.printCaminho(valor)
                if aux != 0 :
                    return 1 + aux
                else:
                    return False
        else:
            if self.info != None:
                print(self.info)
            if self.dir == None:
                return 0 
            else:
                aux = self.dir.printCaminho(valor)
                if aux != 0:
                    return 1 + aux 
                else:
                    return 0
    
    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq==None and self.dir == None:
            print(self.info,end=" ")
        if self.dir != None:
            self.dir.printFolhas()
            
    def somaTudo(self):
        total = self.info
        if self.esq != None:
            total += self.esq.somaTudo()
        if self.dir != None:
            total += self.dir.somaTudo()
        return total
    
    def somaFolhas(self):
        total = 0
        if self.esq==None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total

    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        
        print(self.info,end=" ")
        
        if self.dir != None:
            self.dir.inOrdem()

    def printCaminhoAteMenor(self):
        if self.info != None:
            print(self.info)
        if self.esq != None:
            self.esq.printCaminhoAteMenor()

    def printDescendentes(self,valor):
        if self.info == valor:
            if self.esq != None:
                self.esq.inOrdem()
            if self.dir != None:
                self.dir.inOrdem()

        elif valor < self.info:
            if self.esq != None:
                self.esq.printDescendentes(valor)
            
        else:
            if self.dir != None:
                self.dir.printDescendentes(valor)

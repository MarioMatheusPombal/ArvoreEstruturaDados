import Tree

t1 = Tree.Tree()
t1.insere(4)

t1.insere(2)
t1.insere(6)
t1.insere(7)

t1.insere(1)
t1.insere(5)
t1.insere(3)

t1.insere(8)
t1.insere(10)
t1.insere(9)

t1.insere(12)
t1.insere(11)


print('\n------')
print('printCaminho')
print(t1.printCaminho(7))
print('\n------')
print('printFolhas')
t1.printFolhas()
print('\n------')
print('inOrdem')
t1.inOrdem()
print('\n------')
print('CaminhoAteMenor')
t1.printCaminhoAteMenor()
print('\n------')
print('Herdeiro + a Esquerda e + a Direita')
print(t1.herdeiroMaisEsq(),t1.herdeiroMaisDir())
print('\n------')
print('calculaMedia')
print(t1.calculaMedia())
print('\n------')
print('printDescendentes')
t1.printDescendentes(10)
print('\n------')
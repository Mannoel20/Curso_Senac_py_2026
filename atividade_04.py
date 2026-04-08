ListaNomes = [ ]
listaFamilias = [ ]
qtdNomes = 3
qtdFamilias = 2
for familia in range(qtdFamilias):
 for nome in range(qtdNomes):
  nome = input( "Informe um nome de sua familia: " )
ListaNomes.append( nome )
listaFamilias.append(ListaNomes)
listaNomes = []
for item in listaFamilias:
 print( item )
print()
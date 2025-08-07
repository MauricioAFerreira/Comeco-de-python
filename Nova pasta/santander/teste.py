from funcionalidades import *

tv = Televisor('Sony', 'Sony-123')

controle = ControleRemoto(tv)

controle.sintonizarCanal('SBT')
controle.trocarCanal('SBT')

print(tv.canal_atual)
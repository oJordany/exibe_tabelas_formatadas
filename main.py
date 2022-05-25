# DEMONSTRAÇÕES
from util import printaBancoEmFormatoTabela
from util import printaListaEmFormatoTabela
from util import printaDicioEmFormatoTabela

printaBancoEmFormatoTabela('example.db', 'stocks', 'date')

print()

# Criando uma lista qualquer:
lista = [
  ['nome', 'idade', 'cpf', 'senha'],
  ['Catarina', 18, '077.666.752-19', 'JsSP_DT12'],
  ['Rubens', 19, '007.616.252-11', 'JsSP_DTHTTO123'],
  ['Rose', 20, '077.000.702-09', 'JsSP_DT12Pil'],
  ['Sonia', 24, '011.666.123-45', '@_DT12'],
]

printaListaEmFormatoTabela(lista)

print()

# Criando um dicionario qualquer: 
dicio = {
  'nome' : ['Catarina', 'Rubens', 'Rose', 'Sonia'],
  'idade' : [18, 19, 20, 24],
  'cpf' : ['077.666.752-19', '007.616.252-11', '077.000.702-09', '011.666.123-45'],
  'senha' : ['JsSP_DT12', 'JsSP_DTHTTO123', 'JsSP_DT12Pil', '@_DT12']
}

printaDicioEmFormatoTabela(dicio)
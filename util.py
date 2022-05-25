# EXEMPLO DE UM BANCO CRIADO
# import sqlite3
# con = sqlite3.connect('example.db')
# cur = con.cursor()
# cur.execute('''CREATE TABLE stocks
#                 (date text, trans text, symbol text, qty real, price real)''')
# datasList = [
#   ('2006/01/01', 'SELL', 'R$', 90.0, 20.0),
#   ('2006/01/05', 'BUY', 'R$', 100.0, 15.5),
#   ('2006/05/05', 'SELL', 'R$', 50.0, 30.25),
#   ('2006/05/05', 'SELL', 'R$', 50.0, 30.25),
# ]
# cur.executemany('INSERT INTO stocks VALUES (?, ?, ?, ?, ?)', datasList)

# con.commit()

# con.close()

def printaBancoEmFormatoTabela(baseDeDados, nomeTabela, order=''):
  # Trantando o order
  if order != '':
    order = f'ORDER BY {order}'
  # Usando o sqlite 3
  import sqlite3
  con = sqlite3.connect(f'{baseDeDados}')
  
  con.row_factory = sqlite3.Row
  cur = con.cursor()
  cur.execute(f'SELECT * FROM {nomeTabela}')
  r = cur.fetchone()
  # Encontrando o maior membro da tabela
  biggestMember= 0;
  
  for key in r.keys():
    if len(key) > biggestMember:
      biggestMember = len(str(key))

  
  for row in cur.execute(f'SELECT * FROM {nomeTabela}'):
    for data in row:
      if len(str(data)) > biggestMember:
        biggestMember = len(str(data))
        
  biggestMember += 3;

  # Table Header
  for i, key in enumerate(r.keys()):
    if i != len(r.keys()) - 1:
      print(f'{key}{" "*(biggestMember-len(key))}|', end='')
    else:
      print(f'{key}{" "*(biggestMember-len(key))}', end='')
  
  print()
  print('-'*biggestMember*len(r.keys()))

  # Table Body
  for row in cur.execute(f'SELECT * FROM {nomeTabela} {order}'):
    for i in range(0, len(row)):
      if i != len(row) - 1:
        print(f'{row[i]}{" "*(biggestMember-len(str(row[i])))}|', end='')
      else:
        print(f'{row[i]}{" "*(biggestMember-len(str(row[i])))}')
  
  con.close()

def printaListaEmFormatoTabela(lista):
  #Encontrando o maior membro da tabela
  biggestMember= 0;
  
  for row in lista:
    for data in row:
      if len(str(data)) > biggestMember:
        biggestMember = len(str(data))
         
  biggestMember += 3;

  # Table Header e Table Body
  for l, row in enumerate(lista):
    for i, data in enumerate(row):
      if i != len(row) - 1:
        print(f'{data}{" "*(biggestMember-len(str(data)))}|', end='')
      else:
        print(f'{data}{" "*(biggestMember-len(str(data)))}')
    if l == 0:
      print('-'*biggestMember*len(row))

def printaDicioEmFormatoTabela(dicionario):
  # Encontrando o maior membro da tabela
  biggestMember= 0;
  
  for key in dicionario.keys():
    if len(str(key)) > biggestMember:
      biggestMember = len(str(key))
  
  for row in dicionario.values():
    for data in row:
      if len(str(data)) > biggestMember:
        biggestMember = len(str(data))
        
  biggestMember += 3;

  # Table Header
  aux = 0
  for key in dicionario.keys():
    if aux != len(dicionario) - 1:
      print(f'{key}{" "*(biggestMember-len(str(key)))}|', end='')
    else:
      print(f'{key}{" "*(biggestMember-len(str(key)))}')
    aux += 1
      
  print('-'*biggestMember*len(dicionario))
  
  # Table Body
  aux = 0
  for lista in dicionario.values():
    aux2 = 0
    for key in dicionario.keys():
      data = dicionario[f'{key}'][aux]
      if aux2 != len(dicionario) - 1:
        print(f'{data}{" "*(biggestMember-len(str(data)))}|', end='')
      else:
        print(f'{row[aux]}{" "*(biggestMember-len(str(data)))}')
      aux2 += 1
    aux += 1
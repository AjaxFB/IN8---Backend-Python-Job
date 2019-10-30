# Bruno Henrique Moraes D'Amato
# https://www.linkedin.com/in/brunodamato/

""" Arrays
Tendo os arrays ['ES', 'MG', 'RJ', 'SP'] e ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo'], 
percorra os vetores dados e crie um outro com a seguinte estrutura: 
['ES'=>'Espírito Santo', 'MG'=>'Minas Gerais', 'RJ'=>'Rio de Janeiro', 'SP'=>'São Paulo']. 
Depois de criado terceiro vetor, leia-o e imprima em cada linha a chave de cada posição e 
seu respectivo valor separados por "-".
"""

import doctest

def find_when_start(char=None,list=[]):
  """ find first element in list that start with a char
  >>> find_when_start('a',['abc','bcd','cde'])
  'abc'
  >>> find_when_start(char='a',list=['abc','bcd','cde'])
  'abc'
  >>> find_when_start()
  """
  element = None
  try:
    for object in list:
      if char == object[0]:
        element = object
        break
  except Exception as e:
    element = None
    print(str(e))
  return element

def run(uf_list=[],uf_extensive_list=[]):
  """ print your correspondents
  >>> uf_list = ['ES', 'MG', 'RJ', 'SP']
  >>> uf_extensive_list = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo']
  >>> run(uf_list,uf_extensive_list)
  ES-Espírito Santo
  MG-Minas Gerais
  RJ-Rio de Janeiro
  SP-São Paulo
  >>> run(uf_list=uf_list,uf_extensive_list=uf_extensive_list)
  ES-Espírito Santo
  MG-Minas Gerais
  RJ-Rio de Janeiro
  SP-São Paulo
  >>> run()
  """
  try:
    uf_dict = {}
    for uf in uf_list:
      uf_extensive_finded = find_when_start(char=uf[0],list=uf_extensive_list)
      uf_dict[uf] = uf_extensive_finded
    for uf in uf_dict:
      print(uf + '-' + uf_dict[uf])
  except Exception as e:
    print(str(e))

if __name__ == "__main__":
  test = doctest.testmod()
  if test.failed == 0:
    uf_list = ['ES', 'MG', 'RJ', 'SP']
    uf_extensive_list = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo']
    run(uf_list=uf_list,uf_extensive_list=uf_extensive_list)


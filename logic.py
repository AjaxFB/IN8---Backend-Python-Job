# Bruno Henrique Moraes D'Amato
# https://www.linkedin.com/in/brunodamato/

""" Logic
Pensando em todos os números naturais inferiores a 10 que são múltiplos de 3 ou 5, temos 3, 5, 6 e 9. 
Somando esses múltiplos obtemos o valor 23. 
Utilize um algorítimo para calcular a soma de todos os múltiplos de 3 ou 5 abaixo de 1000
"""

import doctest

def sum_list(list=[]):
  """ Sum elements in a list
  >>> sum_list([0,1,2])
  3
  >>> sum_list()
  """
  element = None
  if list:
    element = 0
    for object in list:
      element += object
  return element

def run(multiple_list=[],max=0):
  """ Sum of multiples in range(0,max)
  >>> multiple_list = [3,5]
  >>> max = 1000
  >>> run(multiple_list=multiple_list,max=max)
  233168
  >>> run()
  None
  """
  multiple_max_list = []
  for number in range(0,max):
    multiple_count = 0
    for multiple in multiple_list:
      if not (number/multiple)%1:
        multiple_count += 1
    if multiple_count > 0: 
      multiple_max_list.append(number)
  print(sum_list(multiple_max_list))

if __name__ == "__main__":
  test = doctest.testmod()
  if test.failed == 0:
    multiple_list = [3,5]
    max = 1000
    run(multiple_list=multiple_list,max=max)
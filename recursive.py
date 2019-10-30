# Bruno Henrique Moraes D'Amato
# https://www.linkedin.com/in/brunodamato/

""" Recursive function
Crie uma função recursiva para descobrir o menor número inteiro divisível por 2, 3 e 10 ao mesmo tempo.
Quando encontrá-lo, imprima-o na tela.

* Por definição, zero é divisível por qualquer número, então será buscado o menor número inteiro positivo maior que 0.
"""

import doctest

def run(divisible_list=[],start=1):
  """ find divisible by a list
  >>> divisible_list = [2,3,10]
  >>> run(divisible_list=divisible_list)
  30
  >>> run(divisible_list)
  30
  >>> run()
  1
  """
  divisible_count = 0
  for divisible in divisible_list:
    if not (start/divisible)%1:
      divisible_count += 1
  if len(divisible_list) == divisible_count: 
    print(start) 
  else: 
    run(divisible_list=divisible_list,start=start+1)

if __name__ == "__main__":
  test = doctest.testmod()
  if test.failed == 0:
    divisible_list = [2,3,10]
    run(divisible_list=divisible_list)


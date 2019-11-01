# Bruno Henrique Moraes D'Amato
# https://www.linkedin.com/in/brunodamato/

""" API
Imagine que você ficou responsável por desenvolver o backend do sistema de uma biblioteca. 
Crie uma API RESTful para o cadastro, edição, listagem e exclusão dos livros (título, autor, edição) e 
o controle de entradas e saídas. 

Como o controle de entradas e saídas não ficou claro, pois poderia ser um controle de logs, controle de emprestimo,
controle de acesso a api. Estarei criando um controle de estoque mesmo.

Não utilizei, mas deveria utilizar SQLAlchemy para persistir num SGDB, mas estou colocando em memória mesmo.
Poderia melhorar a aplicação com métodos de validação de integridade do livro pré emprestimo e pré devolução.
Realizar tratamento de tipos para quantidade de livros.
Poderia utilizar um sistema de busca próprio em vez do dict do python.. etc..
"""

import doctest
from flask import Flask
from flask import jsonify
from flask import request

class Biblioteca:
  livros = {}
  def __init__(self,livros=[]):
    for livro in livros:
      self.livros[livro.getId()] = livro

  def getLivro(self):
    temp_livros = {}
    for livro in self.livros:
      temp_livros[self.livros[livro].getId()] = self.livros[livro].getDict()
    return temp_livros

  def postLivro(self,livro):
    if not livro.getId() in self.livros:
      self.livros[livro.getId()] = livro
    return {'Livro inserido':livro.getDict()}

#  def patchLivro(self,livro):
#    print('Livro atualizado')
#    return {}

  def putLivro(self,livro):
    if livro.getId() in self.livros:
      self.livros[livro.getId()] = livro
    return {'Livro substituído':livro.getDict()}

  def deleteLivro(self,livro):
    livro_deletado = self.livros[livro.getId()].getDict()
    self.livros.pop(livro.getId())
    return {'Livro Deletado':livro_deletado}

  def emprestarLivro(self,livro):
    self.livros[livro.getId()].setQuantidade(int(self.livros[livro.getId()].getQuantidade()) - 1)
    return {'Livro Emprestado':self.livros[livro.getId()].getDict()}

  def devolverLivro(self,livro):
    self.livros[livro.getId()].setQuantidade(int(self.livros[livro.getId()].getQuantidade()) + 1)
    return {'Livro Devolvido':self.livros[livro.getId()].getDict()}

biblioteca_temp = Biblioteca()

class Livro:
  id = None
  titulo = None
  autor = None
  edicao = None
  quantidade = None

  def __init__(self,id=None,titulo=None,autor=None,edicao=None,quantidade=None):
    self.id = id
    self.titulo = titulo
    self.autor = autor
    self.edicao = edicao
    self.quantidade = quantidade

  def getId(self):
      temp_id = self.id
      return temp_id
  def setId(self,id=None):
      self.id = id

  def getTitulo(self):
      temp_titulo = self.titulo
      return temp_titulo
  def setTitulo(self,titulo=None):
      self.titulo = titulo

  def getAutor(self):
      temp_autor = self.autor
      return temp_autor
  def setAutor(self,autor=None):
      self.autor = autor

  def getEdicao(self):
      temp_edicao = self.edicao
      return temp_edicao
  def setEdicao(self,edicao=None):
      self.edicao = edicao

  def getQuantidade(self):
      temp_quantidade = self.quantidade
      return temp_quantidade
  def setQuantidade(self,quantidade=None):
      self.quantidade = quantidade

  def getDict(self):
    livro = {}
    livro['titulo'] = self.titulo
    livro['autor'] = self.autor
    livro['edicao'] = self.edicao
    livro['quantidade'] = self.quantidade
    return livro

def getLivro():
  """ Busca todos os livros
  """
  return biblioteca_temp.getLivro()

def postLivro(livro):
  """ Cadastro do livro
  """
  return biblioteca_temp.postLivro(livro)

#def patchLivro():
#  """ Atualização parcial do livro
#  """
#  return biblioteca_temp.patchLivro()

def putLivro(livro):
  """ Substituição do livro
  """
  return biblioteca_temp.putLivro(livro)

def deleteLivro(livro):
  """ Remoção do livro
  """
  return biblioteca_temp.deleteLivro(livro)

def emprestarLivro(livro):
  """ Emprestimo do livro
  """
  return biblioteca_temp.emprestarLivro(livro)
def devolverLivro(livro):
  """ Devolução do livro
  """
  return biblioteca_temp.devolverLivro(livro)


app = Flask(__name__)
@app.route('/livro', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def livro():
  if request.method == 'GET':
    return jsonify(getLivro())

  elif request.method == 'POST':
    input = request.get_json(force=True)
    if 'id' in input and 'titulo' in input and 'autor' in input and 'edicao' in input and 'quantidade' in input:
      livro = Livro( \
        id=input['id'], \
        titulo=input['titulo'], \
        autor=input['autor'], \
        edicao=input['edicao'], \
        quantidade=input['quantidade'] \
      )
    return jsonify(postLivro(livro))

#  elif request.method == 'PATCH':
#    return jsonify(patchLivro())

  elif request.method == 'PUT':
    input = request.get_json(force=True)
    if 'id' in input and 'titulo' in input and 'autor' in input and 'edicao' in input and 'quantidade' in input:
      livro = Livro( \
        id=input['id'], \
        titulo=input['titulo'], \
        autor=input['autor'], \
        edicao=input['edicao'], \
        quantidade=input['quantidade'] \
      )
    return jsonify(putLivro(livro))

  elif request.method == 'DELETE':
    livro = Livro(id=request.args.get('id'))
    return jsonify(deleteLivro(livro))

@app.route('/emprestar', methods = ['POST'])
def emprestar():
  livro = Livro(id=request.args.get('id'))
  return jsonify(emprestarLivro(livro))

@app.route('/devolver', methods = ['POST'])
def devolver():
  livro = Livro(id=request.args.get('id'))
  return jsonify(devolverLivro(livro))

if __name__ == "__main__":
  test = doctest.testmod()
  if test.failed == 0:
    app.run(host='0.0.0.0', port=80)
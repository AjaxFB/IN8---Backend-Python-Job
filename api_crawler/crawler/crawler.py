# Bruno Henrique Moraes D'Amato
# https://www.linkedin.com/in/brunodamato/

""" Crawler
Crie um crawler (aplicação de busca de informação na web) que leia as 3 primeiras notícias do site g1.globo.com e 
organize em um JSON contendo o título, subtitulo (se tiver) e url da imagem de destaque (se tiver).

Como os dados solicitados são obtidos via GET da página, mas são escolhidos via javascript, será utilizado webdriver.
Não estou considerando notícias relacionadas e nem jogos de futebol como subtítulo. ('bstn-related')
"""

import doctest
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

def isJson(var=''):
  """ Check json
  >>> isJson(var='')
  False
  >>> isJson('')
  False
  >>> isJson('{}')
  True
  """
  result = True
  try:
    json.loads(var)
  except Exception as e:
    result = False
  return result

def get_json_by_webdriver():
  result = []
  try:
    # Start webdriver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-setuid-sandbox")
    w = webdriver.Chrome(chrome_options=chrome_options)
    w.get("https://g1.globo.com/")
    # Running JS
    time.sleep(5)
    # Finding news
    news = w.find_elements_by_class_name('bstn-hl-wrapper')
    if len(news) == 3:
      for new in news:
        new_json = {}
        # Getting title
        temp_title = new.find_elements_by_class_name('bstn-hl-mainitem')
        if len(temp_title) == 1:
          title = temp_title[0].find_elements_by_class_name('bstn-hl-title')
          if len(title) == 1:
            new_json['title'] = title[0].text
        # Getting summary
        summary = new.find_elements_by_class_name('bstn-hl-summary')
        if len(summary) == 1:
          new_json['summary'] = summary[0].text
        # Getting url of photo
        photo = new.find_elements_by_class_name('with-photo')
        if len(photo) == 1:
          string_list = photo[0].get_attribute('style').split('"')
          for string in string_list:
            if 'http' in string: 
              new_json['photo'] = string
        result.append(new_json)
    w.quit()
  except Exception as e:
    print(str(e))
    result = {}
  return result

def run():
  news_json = get_json_by_webdriver()
  print(json.dumps(news_json,indent=4))
  
if __name__ == "__main__":
  test = doctest.testmod()
  if test.failed == 0:
    run()

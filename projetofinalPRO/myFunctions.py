import streamlit as st
from bs4 import BeautifulSoup
from multiprocessing import Queue
from urllib.request import Request, urlopen
import random
import re
import pytest

class Gustavo:
  def Function(list_url):
    try:
      for url in list_url:
        try:
          req = Request(url)
          html_page = urlopen(req)
          soup = BeautifulSoup(html_page, "html.parser")
        except:
          continue
        else:
          links = []
          for link in soup.findAll('a'):
            links.append(link.get('href'))
        final = []
        for link in links:
          try:
            if re.findall("^https", link):
              final.append(link)
          except:
            continue
        return final
    except:
      return []
    else:
      return []
          
  def Recomendacao(lista):
    lista_final = random.choices(lista, k=20)
    fila = Queue()
    [fila.put(n) for n in lista_final] 
    while not fila.empty():
      try:
        req = Request(fila.get())
        page_request = urlopen(req)
        pg = BeautifulSoup(page_request, "html.parser").find('title')
        st.write(f'Titulo da Pagina : {pg.text}')
        st.write(f'Link da Pagina : {fila.get()}')
        st.write('---'*9)
      except:
        st.write('Nao foi encontrado o Titulo da Página!!')
        st.write(f'Link da Pagina : {fila.get()}')
        st.write('---'*9)
        pass

  def DescricaoProjeto():
    st.markdown('# Sherlock Links 🔭')
    st.write('  ')
    st.markdown("### Projeto Final do Curso de Python PRO - Mentorama")
    st.write('  ')
    st.markdown('**Descrição do Projeto:**')
    st.markdown(""" Este projeto realiza a busca de todas as urls na pagina web desejada.
Assim, obtendo mais urls dentro da lista de urls já obtidas, tendo essa operação repetida em 5 vezes.
Com isso, é obtido uma lista final onde é recomendada 10 links de forma aleatoria.

**Projeto no GitHub:** https://github.com/gustavo-duarte-silva/ProjetoFinalPythonPRO
""")


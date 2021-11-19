from requests import get, post
from bs4 import BeautifulSoup
import time

def filtro_concurso_valido(data):
    data_atual_texto = time.strftime('%d/%m/%Y', time.localtime())
    dia_atual, mes_atual, ano_atual = data_atual_texto.split('/')
    dia, mes, ano = data.split('/')
    ano_igual_ou_maior = int(ano) >= int(ano_atual)
    data_prox_mes_e_valida = ano_igual_ou_maior and int(mes) > int(mes_atual)
    data_mes_atual_e_valida = ano_igual_ou_maior and int(mes) == int(mes_atual) and int(dia) >= int(dia_atual)
    if data_prox_mes_e_valida or data_mes_atual_e_valida:
        return True
    return False

def get_data_pci(d):
    data_quebrada = d.find("div", {"class": "ce"}).br
    if data_quebrada is not None:
        data = data_quebrada.text
    else:
        data = d.find("div", {"class": "ce"}).text
    return data

def get_concursos_pci():
    response = get("https://www.pciconcursos.com.br/concursos/norte/")
    texto = response.text
    soup = BeautifulSoup(texto, 'html.parser')
    concursos = soup.find_all("div", {"class": "ca"})
    concursos_pa = [c for c in concursos if "PA" in c.text]
    concursos_pa_medio = [c for c in concursos_pa if "Médio" in c.span.text]
    concursos_pa_medio_validos = [c for c in concursos_pa_medio if filtro_concurso_valido(get_data_pci(c))]
    return concursos_pa_medio_validos
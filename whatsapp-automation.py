from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.keys import Keys

# url whatsapp >> wa.me/Contact
# Iniciar conversa no whatsapp >> _advp _aeam
# escrever a mensagem no whatsapp >> selectable-text copyable-text iq0m558w g0rxnol2

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com/')
time.sleep(30)

contatos = ['Bel', 'Bel']
mensagem = 'Teste'

def buscar_contatos(contatos):
    campo_pesquisa = driver.find_element('//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
    time.sleep(3)
    campo_pesquisa.click
    campo_pesquisa.send_keys(contatos)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
    time.sleep(3)
    campo_mensagem.click
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contatos(contatos)
    time.sleep(10)
    enviar_mensagem(mensagem)

# contact = 5581985691269
# time.sleep



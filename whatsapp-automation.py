from random import *
import pyautogui
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import urllib


# Capturando as informações da planilha através do import do pandas.
contatos = pd.read_excel('contatos.xlsx', engine='openpyxl')

# Chama o brownser
driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com/')
time.sleep(30)


while len(driver.find_elements(By.ID, 'pane-side')) <1:
    time.sleep(3)


for i, mensagem in enumerate(contatos['Mensagem']):
    pessoa = contatos.loc[i, 'Nome']
    number = contatos.loc[i, 'Contatos']
    text = urllib.parse.quote(f"Olá {pessoa}! {mensagem}")
    link = f"http://web.whatsapp.com/send?phone={number}&text={text}"
    driver.get(link)
    while len(driver.find_elements(By.ID, 'pane-side')) <1:
        time.sleep(3)
    time.sleep(15)
    # eviar = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
    driver.find_elements(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(randrange(15, 60))




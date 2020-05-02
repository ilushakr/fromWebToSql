import sqlite3
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from requests import get
import lxml
from lxml import html
import codecs
from selenium import webdriver
import time

############################################################3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Item:
    def __init__(self, kanji, meaning, hiragana, yarksi):
        self.kanji = kanji
        self.meaning = meaning
        self.hiragana = hiragana
        self.yarksi = yarksi


#                        level JLPT
################################################################################################################################
# url = "https://akanji.ru/JLPT/N5"

# url = "https://akanji.ru/JLPT/N4"
# driver = webdriver.Chrome('C:\\silenium\\chromedriver.exe')
# driver.get(url)
#
# content = driver.page_source
# # print(content)
# # time.sleep(2)
# #
# #
# content_html_scroll = driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# # driver.implicitly_wait(5)
# # WebDriverWait(driver, 5).until(driver.execute_script("window.scrollTo(0, document.body.scrollHeight)"))
# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "charRow180")))
#
# content_element = driver.find_element_by_class_name("charList")
# content_html = content_element.get_attribute("innerHTML")
#
# soup = BeautifulSoup(content_html, "html.parser")
# p_tags = soup.find_all("tr")
# p_tags.pop(0)
# allItems = []
#
# for x in p_tags:
#     allItems.append(Item(x.find("td").find("div").text, x.find_all("td")[1].text, x.find_all("td")[3].text, x.find_all("td")[7].find('a')['href']))
#
# for x in allItems:
#     print(x.kanji)
#
#
# print(len(allItems))
#
# driver.close()
################################################################################################################################

#                        Yarksi
################################################################################################################################
# url = "https://yarxi.ru/?u=19978"
#
# driver = webdriver.Chrome('C:\\silenium\\chromedriver.exe')
# driver.get(url)
#
# content = driver.page_source
# # print(content)
#
#
# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "onyomi")))
# content_element = driver.find_element_by_class_name("onyomi")
# content_html = content_element.get_attribute("innerHTML")
#
# soup = BeautifulSoup(content_html, "html.parser")
#
# print(soup.text)
# driver.close()

################################################################################################################################


#                             DATABASE
#############################################################################################################

# conn = sqlite3.connect("data.db")  # или :memory: чтобы сохранить в RAM
# cursor = conn.cursor()
#
# # Создание таблицы
# cursor.execute('CREATE TABLE IF NOT EXISTS core_fes (Well TEXT, '
#                'Sample TEXT, '
#                'Svr FLOAT)')
#
# # Вставляем данные в таблицу
# cursor.execute('INSERT INTO  core_fes VALUES ("yellow", "red", 25.6)')
#
# # Сохраняем изменения
# conn.commit()
# cursor.close()
# conn.close()
#
# conn = sqlite3.connect("data.db")
# # conn.row_factory = sqlite3.Row
# cursor = conn.cursor()
#
# sql = "SELECT * FROM core_fes"
# cursor.execute(sql)
# print(cursor.fetchall())  # or use fetchone()

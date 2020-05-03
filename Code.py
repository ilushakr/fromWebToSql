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
from selenium.webdriver.chrome.options import Options


class Item:
    def __init__(self, kanji, meaning, hiragana, yarksi):
        self.kanji = kanji
        self.meaning = meaning
        self.hiragana = hiragana
        self.yarksi = yarksi


def get_yarksi(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('C:\\silenium\\chromedriver.exe', options=options)
    driver.get(url)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "onyomi")))

    content_element = driver.find_element_by_class_name("kun")
    content_html = content_element.get_attribute("innerHTML")

    soup = BeautifulSoup(content_html, "html.parser")

    driver.close()

    return soup.find("span").text[1: -1]


def get_lvl_jptl(url, before_str):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('C:\\silenium\\chromedriver.exe', options=options)
    # driver = webdriver.Chrome('C:\\silenium\\chromedriver.exe')
    driver.get(url)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, before_str)))

    content_element = driver.find_element_by_class_name("charList")
    content_html = content_element.get_attribute("innerHTML")

    soup = BeautifulSoup(content_html, "html.parser")
    p_tags = soup.find_all("tr")
    p_tags.pop(0)
    all_items = []
    i = 0
    for x in p_tags:
        try:
            all_items.append(Item(x.find("td").find("div").text, x.find_all("td")[1].text, x.find_all("td")[3].text,
                                  x.find_all("td")[7].find('a')['href']))
        except Exception:
            all_items.append(Item(i, i, i, i))
        i = i + 1
    driver.close()

    return all_items


# for x in get_lvl_jptl("https://akanji.ru/JLPT/N5", "charRow102"):
#     print(x.kanji + ' - ' + x.hiragana + ' - ' + x.meaning + ' - ' + x.yarksi)


#                             DATABASE
#############################################################################################################



conn = sqlite3.connect("data.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
cursor.execute('CREATE TABLE IF NOT EXISTS N5 (kanji TEXT, '
               'hiragana TEXT, '
               'meaning TEXT, '
               'yarksi TEXT)')

sql = 'DELETE FROM N5'
cur = conn.cursor()
cur.execute(sql)
conn.commit()

# Вставляем данные в таблицу
for x in get_lvl_jptl("https://akanji.ru/JLPT/N5", "charRow102"):
    try:
        a = get_yarksi(x.yarksi)
    except Exception:
        a = "null"
    cursor.execute('INSERT INTO  N5 VALUES (?, ?, ?, ?)', [x.kanji, x.hiragana, x.meaning, a])
    print(a)

# Сохраняем изменения
conn.commit()
cursor.close()
conn.close()

# conn = sqlite3.connect("data.db")
# # conn.row_factory = sqlite3.Row
# cursor = conn.cursor()
#
# sql = "SELECT yarksi FROM N5"
# cursor.execute(sql)
#
# yr = []
# for i in cursor.fetchall():
#     # a = cursor.fetchall()[i]
#      yr.append(i[0])
#
#
# for x in yr:
#     print(get_yarksi(x))

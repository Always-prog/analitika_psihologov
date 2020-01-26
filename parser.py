# -*- coding: utf-8 -*-
import requests as rq
import driver 
from bs4 import BeautifulSoup as BS
from selenium import webdriver
import time



pov = int(input("установите повторения: "))
pov_plus = 0
driver = webdriver.Chrome("C:/Users/ludol/Desktop/stepan/chrome_driver/chromedriver")
driver.get("https://www.b17.ru")
while pov_plus < pov:
    try:
        driver.find_element_by_id("index_list_next").click()
    except(BaseException):
        pass
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1.5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    last_height = new_height
    pov_plus += 1
print("парсинг закончен, страница сохраняется")
html_source = driver.page_source



def obrabotka(obr):
    OnOff = False  
    output = []
    for i in range(len(obr)):
        list_names = list(obr[i])
        for j in range(len(list_names)):
            if list_names[j] == "<":
                list_names.pop(j)
                OnOff = True
            if OnOff == True:
                list_names.pop(j)
            if list_names[j] == ">":
                list_names.pop(j)
                OnOff = False
        output.append("".join(list_names[0]))
    return output  

def FillFile(name_file,filling_list,filling):
    name_file = name_file
    filling_list = filling_list
    filling = filling

    file = open(name_file,"w", encoding='utf-8')
    file.close()
    file = open(name_file,"a", encoding='utf-8')
    for i in range(len(filling_list)):
        file.write(filling_list[i])
        file.write(filling)
    file.close()

#работа над html:
print("получаю страницу, нахожу в ней фрагменты для базы данных")
soup         = BS(html_source,"html.parser")
names_zag    = soup.findAll("a",class_="name")
names_small  = soup.findAll("div",class_="small small_text")
print("удяляю все теги из фрагментов")
result_zag   = obrabotka(names_zag)
result_small = obrabotka(names_small)
print("очистка памяти")
del names_small
del names_zag

#работа над записю файлов
#заголовки:
print("запись в файл заголовков")
FillFile("b17_zag.txt",result_zag,"\n")
FillFile("b17_mini_text.txt",result_small,"\n")
del result_zag
del result_small
print("готово!")











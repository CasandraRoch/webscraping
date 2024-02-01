import requests #hacer peticion a la pagina
from bs4 import BeautifulSoup as bs #permite extraer el html
import random 
import time #para hacer pausas
import pandas as pd
from selenium import webdriver #permite ser web scraping
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc #permite que las paginas no detecten que es un ordenador
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import pyodbc
from sqlalchemy import create_engine
import urllib
browser = webdriver.Chrome()

url= "https://twitter.com/i/flow/login"

browser.get(url)

time.sleep(10)

#browser.implicitly_wait(10)

user = "ec.roch11@gmail.com"
password= "340248346"
username= "@peerico34"
input_user=browser.find_element(By.XPATH,'//input[@name="text"]')
input_user.send_keys(user)
input_user.send_keys(Keys.ENTER)
time.sleep(5)
input_username=browser.find_element(By.XPATH, '//input[@name="text" and @data-testid="ocfEnterTextTextInput"]')
input_username.send_keys(username)
input_username.send_keys(Keys.ENTER)
time.sleep(5)
campo_password= browser.find_element(By.XPATH, '//input[@name="password"]')
campo_password.send_keys(password)
campo_password.send_keys(Keys.ENTER)
time.sleep(5)

subject="Camila Cabello"
search_box = browser.find_element(By.XPATH,'//input[@data-testid="SearchBox_Search_Input"]')
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)
time.sleep(4)

people=browser.find_element(By.XPATH,"//span[contains(text(),'Personas')]")
people.click()
time.sleep(3)

profile= browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
profile.click()
time.sleep(5)



Tweet=browser.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
#Like=browser.find_element(By.XPATH,"//div[@data-testid='like']").text
Tweets=[]
#Likes=[]

while True:
    articles = browser.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    
    for article in articles:
        Tweet = article.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)

        #Like = browser.find_element(By.XPATH,".//div[@data-testid='like']").text
        #Likes.append(Like)

    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    # Esperar a que cargue la página después de desplazar
    time.sleep(4)

    articles = browser.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    Tweets2 = list(set(Tweets))
    
    if len(Tweets2) >= 10:
        break

print(len(Tweets))
print(Tweets)


df= pd.DataFrame(Tweets)
print(df)
print(df.head(2))

df.to_excel("tweets.xlsx",index=False)



# Obtiene y muestra la ruta del directorio actual
current_directory = os.getcwd()
print("Directorio actual de trabajo:", current_directory)

# Construye la ruta completa al archivo "tweets.xlsx"
ruta_completa = os.path.join(current_directory, "tweets.xlsx")
print("Ruta completa del archivo tweets.xlsx:", ruta_completa)



params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=LAPTOP-KR77677J\SQLEXPRESS;DATABASE=TAREA_DOS;UID=sa;PWD=Casycas340248346!")
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

df.to_sql('tweeter', engine, if_exists='replace', index=False)








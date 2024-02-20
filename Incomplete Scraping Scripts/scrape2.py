from bs4 import BeautifulSoup
# from googlesearch import search
import requests
# from selenium import webdriver 
# from selenium.webdriver.common.by import By
# import time
import csv
def scraper(q):
    response=requests.get(f'https://www.google.com/search?q={q}')
    soup = BeautifulSoup(response.content, 'html.parser')
    for item in soup.find_all('div'):
        print(item.text)
        break

scraper('canoo roi')
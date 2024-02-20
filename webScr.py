from bs4 import BeautifulSoup
# from googlesearch import search
import requests
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import csv


driver=webdriver.Chrome()

def writeFunc(key ,val):
    with open('canoo.csv', 'a', newline='') as file:
                writer=csv.writer(file)
                a=[key,val]
                writer.writerow(a)

def scraper(q):
    driver.get(f'https://www.google.com/search?q={q}')
    # ele = driver.find_element(By.TAG_NAME,'b')
    # if(ele):
    #      return ele
    # else: 
    time.sleep(2)
    div_elements = driver.find_elements(By.XPATH,"//div[@aria-expanded='false']")
        # rgba_color = 'rgba(66, 133, 244, 0.3 )'
    for div in div_elements[5:]:
            div.click()
            # element = driver.find_element(By.XPATH, f"//b[.//style[contains(., 'background-color: rgba({rgba_color}'))]]")
            time.sleep(2)
            ele = driver.find_element(By.TAG_NAME,'b')
    return ele    
      
def func1():

    query=input("Main Query: ")
    element=scraper(query)
    if(element):
        var=(element.text)
        writeFunc(query,var)
        subq=' '
        while(subq!='.'):
            subq=input("Sub Query: (Press . to stop) ")
            element2=scraper(f'{subq} of {var}')
            if(element2):
                var2=(element2.text)
                writeFunc(subq,var2)
                 
                 
def func4():
        subq=' '
        while(subq!='.'):
            subq=input("Sub Query: (Press . to stop) ")
            element2=scraper(subq)
            if(element2):
                var2=(element2.text)
                writeFunc(subq,var2) 
    
func1()

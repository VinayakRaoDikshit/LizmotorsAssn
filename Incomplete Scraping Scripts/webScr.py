from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv

driver = webdriver.Chrome()

def writeFunc(key ,val):
    with open('canoo.csv', 'a', newline='') as file:
                writer=csv.writer(file)
                a=[key,val]
                writer.writerow(a)

def writeCSV(query,result):

    # Open the CSV file in append mode
    with open('canoo.csv', 'a', newline='') as csvfile:
        # Define the headers
        fieldnames = ['Query', 'Result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the headers if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        result_str = ', '.join(result)
        writer.writerow({'Query': query, 'Result': result_str})

def clean(l,q):
     j=0
     for i in l:
          if(i==''):
               del l[j]
          j+=1
     writeCSV(q,l)
               
            
def scraper(q):
    driver.get(f'https://www.google.com/search?q={q}')
    # ele = driver.find_element(By.TAG_NAME,'b')
    # if(ele):
    #      return ele
    # else: 
    time.sleep(2)
    div_elements = driver.find_elements(By.XPATH,"//div[@aria-expanded='false']")
        # rgba_color = 'rgba(66, 133, 244, 0.3 )'
    # for div in div_elements[5:]:
    #         div.click()
    #         time.sleep(1)
            # element = driver.find_element(By.XPATH, f"//b[.//style[contains(., 'background-color: rgba({rgba_color}'))]]")
    for div in div_elements[5:]:
            li=[]
            div.click()
            try:
                ele = driver.find_elements(By.TAG_NAME,'b')
                for someEle in ele:
                    var2=(someEle.text)
                    # writeFunc(q,var2) 
                    li.append(someEle.text)

            except NoSuchElementException:
                 continue
    clean(li,q)
            
    # return ele    
def newScrape(q):
      driver.get(f'https://www.google.com/search?q={q}')
      time.sleep(2)
      ele = driver.find_element(By.TAG_NAME,'mark')
      var2=(ele.text)
      writeFunc(q,var2) 
      
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
        while(subq):
            subq=input("Query: (Press . to stop) ")
            if(subq=='.'):
                  break
            scraper(subq)
func4()

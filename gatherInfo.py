from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv


driver = webdriver.Chrome()

# Function to append the Query and its result to a csv file.
# It accepts 2 arguments query, which is the query made by user and result, which is a list containing output of the webscraped data 
def writeCSV(query,result):

    # Open a CSV file named canoo.csv in append mode
    with open('canoo.csv', 'a', newline='') as csvfile:
        # Define the headers
        headings = ['Query', 'Result']

        #initialize object of DictWriter class 
        writer = csv.DictWriter(csvfile, fieldnames=headings)
        
        # Write the headers if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Join the elements of the result list into one single string enclosed by " " and separated with ,
        result_str = ', '.join(result)

        # Append to the csv file
        writer.writerow({'Query': query, 'Result': result_str})

#Function to remove ' ' (blank spaces) from the list obtained by scraping  
def clean(l,q):
     j=0
     for i in l:
          if(i=='' or i=='  '):
               del l[j]
          j+=1

     # Call the function which writes data to csv with user's query and the cleaned list
     writeCSV(q,l)


# Function to retrieve relevant results from the web as per the query 'q' 
# q is the query made by the user and it is passed on to this function by the driver function mentioned below
     
def scraper(q):
    #Concatenate google search URL with user's target query 'q'
    driver.get(f'https://www.google.com/search?q={q}')

    #wait for the page to be loaded, increase this time in case of low internet bandwidth
    time.sleep(2)

    #find all the <div> elements which are associated with all those accordion /collapsible menus which are currently not expanded.
    div_elements = driver.find_elements(By.XPATH,"//div[@aria-expanded='false']")
    
    #Expand all the menus by iterating over the div_elements list. Start from 6th element because on a google search results page, the first 5 collapsible menus include irrelevant menus such as "All filters", "Safe search" etc. 
    for div in div_elements[5:]:
            #this list will store the raw, scraped results
            li=[]

            #simulate click using selenium to expand each of the collapsible menus
            div.click()
    
            #try block
            try:
                #search for all the <b> elements on the page, upon expansion of menus 
                ele = driver.find_elements(By.TAG_NAME,'b')

                #iterate over the list and extract text from the <b> 
                for someEle in ele:
                    var2=(someEle.text)
                    li.append(someEle.text)
            #except block
            except NoSuchElementException:
                 continue
    
    clean(li,q)

#Driver function to take input from user
def driverFunc():
        quer=' '
        while(quer):
            #Take queries as input from the user
            quer=input("Query (Press . to stop): ")
            if(quer=='.'):
                  break
        
            #call the scraper function with user's query
            scraper(quer)

driverFunc()
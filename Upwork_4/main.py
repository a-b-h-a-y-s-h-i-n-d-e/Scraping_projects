
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlsplit
from openpyxl import load_workbook

import pandas as pd 
import time


options = Options()
#options.add_experimental_option("detach", True)
options.add_argument("--enable-javascript")



def saveToexcel(i, price, profit, link):                                         
    fileName = urlsplit(link).hostname.split('.')[0]                             
    fileName = fileName + ".xlsx"                                                
                                                                                 
    priceCol = "price" + str(i)  # Convert i to string
    profitCol = "profit" + str(i)  # Convert i to string
                                                                                 
    data = {'Dataname': [priceCol, profitCol], 'Data': [price, profit]}        
    df = pd.DataFrame(data)                                                      
                                                                                 
    with pd.ExcelWriter(fileName, engine='xlsxwriter') as writer:              
        df.to_excel(writer, sheet_name='Sheet1', index=False, header=False)



def scrapeLink(link):

    driver = webdriver.Chrome(service= Service("./chromedriver"), options = options)
    driver.set_window_size(1500,1000)
    actions = ActionChains(driver)

    try:
        driver.get(link)

        # waiting for page to be loaded
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        #cookiesButton = driver.find_element(By.ID, "")
        #cookiesButton.click()

        #blogMenu = driver.find_element(By.XPATH, "//a[@href='# blog-menu']//span")
        blogMenu = driver.find_element(By.XPATH, "//span[@id='currentTab']")
        actions.click(blogMenu).perform()
        archieveButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='list-group-item'][2]")))
        actions.click(archieveButton).perform()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "_blogInnerContent")))

        boxes = driver.find_elements(By.XPATH, "//li[@class='block media _feedPick feed-pick']")


        for i, box in enumerate(boxes, start = 1):

            driver.execute_script("arguments[0].scrollIntoView();", box)

            price = box.find_element(By.XPATH, ".//div[@class='pick-line']//span").text
            print(price)
            
            
            divProfit = box.find_element(By.XPATH, ".//div[@class='labels']")
            text = divProfit.text.split()   
            profit = text[3]
            print(profit)

            saveToexcel(i, price, profit, link)

            
            





    except KeyboardInterrupt as e:
        print("you stopped the program!!")
    except Exception as e:
        print(e)
        










def iterateThroughExcel():
    df = pd.read_excel("Updated_blogabet links.xlsx", header = None)
    links = df[0].tolist()

    for link in links:
        scrapeLink(link)
        print(link)
    


iterateThroughExcel()
#scrapeLink("https://m2picks.blogabet.com/")




"""

--> First things first 
     we have to understand first workflow

     1. function that will iterate through each link in excel file
     2. then calling another function for each link



"""

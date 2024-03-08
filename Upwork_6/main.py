# https://understat.com/league/Ligue_1/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys

import time

def scrapeHome():
    driver = webdriver.Chrome(service=Service("./chromedriver"), options= options)
    driver.set_window_size(1500, 1000)
    actions = ActionChains(driver)
    try:                                                   
        driver.get("https://understat.com/league/Ligue_1/")
                                                           
        time.sleep(20)                                     
                                                           
    except Exception as e:                                 
        raise

def scrapeAway():
    pass

def run():
                                                  
    print("Enter data of Start date -:")
    while True:
        startMonth = input("Enter month -> (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec) -> ")
        if(len(startMonth) == 3):
            break
        else:
            print("Please Enter valid Month :)")
    
    while True:
        startDay = input("Enter date -> (from 1 to 31)")
        if(len(startDay) > 0 and len(startDay) < 3):
            break
        else:
            print("Please Enter valid Date :)")

    while True:
        startYear = input("Enter year -> (e.g = 2024)")
        if(len(startYear) == 4):
            break
        else:
            print("Please Enter valid Year :)")
    
    startDate = startMonth + " " +startDay + ", " + startYear
    print(startDate)
    

    print("Enter data of End date -:")                                                                     
    while True:                                                                                              
        endMonth = input("Enter month -> (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec) -> ")
        if(len(endMonth) == 3):                                                                            
            break                                                                                            
        else:                                                                                                
            print("Please Enter valid Month :)")                                                             
                                                                                                             
    while True:                                                                                              
        endDay = input("Enter date -> (from 1 to 31)")                                                     
        if(len(endDay) > 0 and len(endDay) < 3):                                                         
            break                                                                                            
        else:                                                                                                
            print("Please Enter valid Date :)")                                                              
                                                                                                             
    while True:                                                                                              
        endYear = input("Enter year -> (e.g = 2024)")                                                      
        if(len(endYear) == 4):                                                                             
            break                                                                                            
        else:                                                                                                
            print("Please Enter valid Year :)")                                                                                                
    endDate = endMonth + " " + endDay + ", " + endYear                                                     
    print(endDate)



if __name__ == "__main__":
    options = Options()
    options.add_argument("--enable-javascript")
    run()







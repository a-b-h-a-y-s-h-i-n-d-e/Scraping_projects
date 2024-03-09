# https://understat.com/league/Ligue_1/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time
import threading
import csv

def cancelAdd(driver):
    print("Threading start to check incoming adds")
    try:
        
        iframe = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='aswift_2']")))
        print("Iframe found")
        driver.switch_to.frame(iframe)
        
        card = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='card']")))
        cancelButton = card.find_element(By.XPATH, ".//div[id='dismiss-button']")
        driver.execute_script("arguments[0].click();", cancelButton)
        driver.switch_to.default_content()
    except Exception as e:
        print(e)


def createCSV(fileName, headers, data):
    try:
        with open(fileName, mode = 'w', newline = '') as file:
            writer = csv.writer(file)

            # writing headers first
            writer.writerow(headers)

            # now writing remaining data 
            writer.writerows(data)
    except Exception as e:
        raise

def scrapeHome(startDate, endDate):
    driver = webdriver.Chrome(service=Service("./chromedriver"), options= options)
    driver.set_window_size(1500, 1000)
    actions = ActionChains(driver)
    try:                                                   
        driver.get("https://understat.com/league/Ligue_1/")
                                                           
                                                           
    except Exception as e:                                 
        raise


    #threading.Thread(target=cancelAdd, args=(driver, )).start()
    # Entering startDate and endDate 
    try:
        leagueChart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='league-chemp']"))) 
        driver.execute_script("arguments[0].scrollIntoView(true);", leagueChart)

        # clicking on home button
        homeButtonID = driver.find_element(By.XPATH, "//input[@id='home-away2']")
        labelElement = homeButtonID.find_element(By.XPATH, "following-sibling::label") 
        driver.execute_script("arguments[0].scrollIntoView(true);", labelElement)
        #labelElement.click()
        driver.execute_script("arguments[0].click();", labelElement)
        
        #startDateInput = leagueChart.find_element(By.XPATH, ".//input[@id='dp1709963814828']")
        #print(startDateInput)
        #print("Element found")
        #startDateInput.click()
        #startDateInput.send_keys(startDate)

        headers = ['No.', 'Team', 'M', 'W', 'D', 'L', 'G', 'GA', 'PTS', 'xG', 'xGA', 'xPTS']
        data = []
        rows = leagueChart.find_elements(By.XPATH, ".//table//tbody//tr")
        for row in rows:
            number = row.find_element(By.XPATH, ".//td[@class='align-right']").text 
            team = row.find_element(By.XPATH, ".//td//a").text
            matches = row.find_element(By.XPATH, ".//td[@class='align-right'][2]").text 
            wins = row.find_element(By.XPATH, ".//td[@class='align-right'][3]").text 
            draw = row.find_element(By.XPATH, ".//td[@class='align-right'][4]").text  
            loose = row.find_element(By.XPATH, ".//td[@class='align-right'][5]").text 
            games = row.find_element(By.XPATH, ".//td[@class='align-right'][6]").text
            ga = row.find_element(By.XPATH, ".//td[@class='align-right'][7]").text 
            pts = row.find_element(By.XPATH, ".//td[@class='align-right'][8]").text 
            #try:
            #    xg = row.find_elements(By.TAG_NAME, "td")[9].text
            #except Exception as e:
            #    print(e)
            
            xg = row.find_elements(By.TAG_NAME, "td")[9].text
            xga = row.find_elements(By.TAG_NAME, "td")[10].text
            xpts = row.find_element(By.XPATH, ".//td[@class='align-right nowrap'][2]").text
            tempList = [number, team, matches, wins, draw, loose, games, ga, pts, xg, xga, xpts]
            data.append(tempList)
        print(data)



    except NoSuchElementException:
        print('Element not found!!')
    except Exception as e:
        print(e)

    fileName = 'homeData.csv'
    createCSV(fileName, headers, data)


def scrapeAway():
    pass

def run():
                                                  
    #print("Enter data of Start date -:")
    #while True:
    #    startMonth = input("Enter month -> (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec) -> ")
    #    if(len(startMonth) == 31) -> ")
    #    if(len(startDay) > 0 and len(startDay) < 3):
    #        break
    #    else:
    #        print("Please Enter valid Date :)")

    #while True:
    #    startYear = input("Enter year -> (e.g = 2024) -> ")
    #    if(len(startYear) == 4):
    #        break
    #    else:
    #        print("Please Enter valid Year :)")
    #
    #startDate = startMonth + " " +startDay + ", " + startYear
    #print(startDate)
    

    #print("Enter data of End date -:")                                                                     
    #while True:                                                                                              
    #    endMonth = input("Enter month -> (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec) -> ")
    #    if(len(endMonth) == 3):                                                                            
    #        break                                                                                            
    #    else:                                                                                                
    #        print("Please Enter valid Month :)")                                                             
    #                                                                                                         
    #while True:                                                                                              
    #    endDay = input("Enter date -> (from 1 to 31) -> ")                                                     
    #    if(len(endDay) > 0 and len(endDay) < 3):                                                         
    #        break                                                                                            
    #    else:                                                                                                
    #        print("Please Enter valid Date :)")                                                              
    #                                                                                                         
    #while True:                                                                                              
    #    endYear = input("Enter year -> (e.g = 2024) -> ")                                                      
    #    if(len(endYear) == 4):                                                                             
    #        break                                                                                            
    #    else:                                                                                                
    #        print("Please Enter valid Year :)")                                                                                                
    #endDate = endMonth + " " + endDay + ", " + endYear                                                     
    #print(endDate)
    startDate = "Mar 1, 2023"
    endDate = "Oct 1, 2023"

    scrapeHome(startDate, endDate)

if __name__ == "__main__":
    options = Options()
    options.add_argument("--enable-javascript")
    run()







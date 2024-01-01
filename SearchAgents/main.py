# https://www.kw.com/agent/search/ca/san%20jose
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchWindowException

def askForValue():
    # value = input("Enter the value ! -> ")
    value = "ca/san%20jose"
    return value


def loading_full_page(driver, agentsPage, wait):
    try:
        agentsPage.find_elements(By.XPATH, "//div[@class='FindAgentRoute__row']")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='FindAgentRoute__row']")))

    except Exception as e:
        print(e)

    



# def iterateEachCard(driver, agentsPage, wait):
#     # now iterating through each card
    
#     pass
    
    
    
value = askForValue()
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service("chromedriver"), options=options)
driver.set_window_size(1500,1000)

link = "https://www.kw.com/agent/search/" + value
driver.get(link)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)


try:
    agentsPage = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='infinite-scroll-component KWInfiniteScroll row']"))
    )
    
    # print(agentsPage)

except Exception as e:
    print(e)


loading_full_page(driver, agentsPage, wait)





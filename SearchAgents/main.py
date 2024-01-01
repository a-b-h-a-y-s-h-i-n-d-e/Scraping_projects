# https://www.kw.com/agent/search/ca/san%20jose
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchWindowException



def askForValue():
    # value = input("Enter the value ! -> ")
    value = "ca/san%20jose"
    return value

def fetchNumberOfResults(driver, agentsPage):
    string = driver.find_element(By.XPATH, "//div[@class='col-6 col-md-4 col-l-4 col-xl-4']")
    print(string.text)
    number_match = re.search(r'\b\d+\b', string.text)

    # Check if a match is found
    if number_match:
        number_of_agents = int(number_match.group())
        print(f"Number of agents: {number_of_agents}")
        return number_of_agents
    else:
        print("No match found.")




def loading_full_page(driver, agentsPage, wait, searchResults):
    while True:
        try:
            agents = agentsPage.find_elements(By.XPATH, "//div[@class='FindAgentRoute__row']")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            if len(agents) == searchResults:
                break

            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='FindAgentRoute__row']")))


        except Exception as e:
            print(e)
    print(len(agents))
    iterateEachCard(driver, agentsPage, wait, agents)



def iterateEachCard(driver, agentsPage, wait, agents):
    # now iterating through each card
    
    for agent in agents:
        pass

    
    
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

searchResults= fetchNumberOfResults(driver, agentsPage)
print(searchResults)

# loading_full_page(driver, agentsPage, wait, searchResults)





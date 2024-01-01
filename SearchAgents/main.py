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
import csv
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchWindowException, NoSuchElementException



def askForValue():
    # value = input("Enter the value ! -> ")
    value = "ca/san%20jose"
    return value

def fetchNumberOfResults(driver, agentsPage):
    string = driver.find_element(By.XPATH, "//div[@class='col-6 col-md-4 col-l-4 col-xl-4']")
    number_match = re.search(r'\b\d+\b', string.text)

    # Check if a match is found
    if number_match:
        number_of_agents = int(number_match.group())
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

    
    iterateEachCard(driver, wait, agents)



def iterateEachCard(driver, wait, agentsPage):
    # now iterating through each card
    agents = driver.find_elements(By.XPATH, "//div[@class='FindAgentRoute__row']")
    

    # with open('agents_data.csv', 'w', newline='', encoding='utf-8') as csvfile:

    #     # now defining header
    #     fieldnames = ['Link', 'FirstName', 'LastName', 'Email', 'Phone', 'OfficePhone',
    #                   'Website', 'Bio', 'Area', 'Language', 'Center']
        
    #     writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    #     writer.writeheader()


    try:


        for agent in agents:
        # Clicking individual agent
            agent.click()

            agentProfileRoute = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='AgentProfileRoute']")))
            


            # first <section> where contact info is present
            agentContact = agentProfileRoute.find_element(By.XPATH, "//section[@class='AgentContent__contacts']")

            # link
            agentLink = driver.current_url

            # name
            fullName= agentContact.find_element(By.CLASS_NAME, 'AgentContent__name').text
            name_parts = fullName.split(' ')
            if len(name_parts) >= 2:
                FirstName = name_parts[0]
                LastName = ' '.join(name_parts[1:])
                
            # email
            email = agentContact.find_element(By.XPATH, "//a[@class='AgentInformation__factBody']").text
            
            # phone numbers
            mobilePhone= agentContact.find_element(By.XPATH, "//div[@class='AgentInformation__phoneMobileNumber']//a").text
            officePhone = agentContact.find_element(By.XPATH, "//div[@class='AgentInformation__phoneOfficeNumber']//a").text
            
            # website
            website = agentContact.find_element(By.XPATH, "//div[@class='icon icon-border-website icon-blue-2-solid']/following-sibling::a").text
            


            # second <section> where bio and all is present
            agentInfo = agentProfileRoute.find_element(By.XPATH, "//section[@class='AgentContent__info']")

            # bio
            bio = agentInfo.find_element(By.XPATH, "//div[@class='AgentContent__sectionText AgentContent__bio']").text
            
            # Area
            area = agentInfo.find_element(By.XPATH, "//div[@class='AgentContent__sectionText AgentContent__serviceAreas']").text
            
            # Language
            elements = agentInfo.find_elements(By.XPATH, "//div[@class='AgentContent__section']")
            language_element = elements[2]
            language = language_element.find_element(By.XPATH, "./div[@class='AgentContent__sectionText']").text
            print(language)

            # # center
            # elements = agentInfo.find_elements(By.XPATH, "//div[@class='AgentContent__section']")
            # center_element = elements[4]
            # center = center_element.find_element(By.XPATH, "./div[@class='AgentContent__sectionText']").text
            # print(center)
            


            

            

            

            # Go back to the agents list page
            driver.back()

        
    except StaleElementReferenceException as e:
        
        pass
    driver.quit()
        
        


    
    
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

# loading_full_page(driver, agentsPage, wait, searchResults)

iterateEachCard(driver, wait, agentsPage)




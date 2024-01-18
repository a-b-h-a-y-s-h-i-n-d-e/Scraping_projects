"https://shop.parmigianoreggiano.com/it/shop.html"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException,TimeoutException, NoSuchWindowException, NoSuchElementException
import threading


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service("chromedriver"), options=options)
driver.set_window_size(1500,1000)
driver.get("https://shop.parmigianoreggiano.com/it/shop.html")
actions = ActionChains(driver)


def acceptCookies():
    try:
        acceptButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@id='onetrust-accept-btn-handler']")))
        acceptButton.click()

    except Exception as e:
        raise


"""
    things to find for this project ->

    -> price per KG
    -> company name
    -> product name
    -> price in €
    -> weight in kg
"""

def fetchData():
    index = 1
    productsDataPage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ol[@class='products list items product-items']")))

    products = productsDataPage.find_elements(By.XPATH, "//li[@class='item product product-item']")

    numberOfItemsDiv = driver.find_element(By.XPATH, "//p[@id='toolbar-amount']")
    numberOfItemsText = numberOfItemsDiv.text

    last_digit = int(numberOfItemsText.split()[-1])

    print("Last digit:", last_digit)

    for i in range(1, last_digit + 1):
        try:
            product = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f"//li[@class='item product product-item'][{index}]")))
            index = index + 1
            title = product.find_element(By.XPATH, ".//a[@class='nome-caseificio']//span")
            print(title.text)






            moreProduct = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//div[@class='amscroll-load-button']")))
            # print(moreProduct)
            if moreProduct:
                ActionChains(driver).move_to_element(moreProduct).click().perform()
                # print("button clicked")

        except TimeoutException as e:
            pass

        except NoSuchElementException as e:
            pass

        except Exception as e:
            raise
    

threading.Thread(target=acceptCookies).start()
fetchData()



# now also we need to do some shit for accept cookies


from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def getWebDriver(urlFonte: str) -> webdriver:
    
    driver: webdriver = webdriver.Chrome()
    # driver: webdriver = webdriver.Chrome(executable_path='/home/tadeu/Documents/chromedriver/chromedriver')
    # driver = webdriver.Chrome(executable_path='C:/Users/tsegura/Documents/Pacotes/chromedriver.exe')
    
    driver.get(urlFonte)

    return driver
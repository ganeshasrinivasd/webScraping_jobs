import pandas as pd
import numpy as np
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException

def get_naukri(keywords):
    driver = webdriver.Chrome()
    driver.get("https://naukri.com/")
    searchBar = driver.find_element(By.CLASS_NAME,"suggestor-input ")
    e=""
    for i in keywords:
        e=e+i+" "
    # e = "'"+e+"'"
    searchBar.send_keys(e)
    searchBar.send_keys(Keys.ENTER)
    
    jobsite = driver.current_url
    jobsite="'"+jobsite+"'"
    driver.quit()
    return jobsite

def scraping_jobs(keyword, location):
    
    jobs=[]
    driver = webdriver.Chrome()
    url = "https://www.glassdoor.co.in/Job/index.htm"
    driver.get(url)
    
    search_job = driver.find_element("xpath",'//input[@class="keyword"]')
    search_job.send_keys([keyword])
    driver.implicitly_wait(2)
    search_location = driver.find_element("xpath",'//input[@class="loc"]')
    search_location.clear()
    search_location.send_keys([location])
    search_button = driver.find_element("xpath",'//button[@id="HeroSearchButton"]')
    search_button.click()
    time.sleep(1)
    z=driver.current_url
    return str(z)


a=input()
keywords = a

df = scraping_jobs(keywords, 'hyderabad')
df2 = get_naukri([keywords])
print("Glasdoor: "+ str(df))
print("Naukri: "+ str(df2))


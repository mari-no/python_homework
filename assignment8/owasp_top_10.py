## Task 6: Scraping Structured Data
import json
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

top10_URL = "https://owasp.org/Top10/2025/"

try:
    
    driver.get(top10_URL)
    top10_header = driver.find_element(By.CSS_SELECTOR, '#top-102025-list')
    top10_list = top10_header.find_elements(By.XPATH, './following-sibling::ol/li')
    top_list =[]
    for item in top10_list:
        risk_text = item.text
        link = item.find_element(By.CSS_SELECTOR,'a[href]').get_attribute('href')
        top_list.append({"Vulnerability title": risk_text,
                         "Href link":link})
    print(top_list)
    top_list_df = pd.DataFrame(top_list)
    top_list_df.to_csv('assignment8/owasp_top_10.csv', index = False)

except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")


finally:
    driver.quit()


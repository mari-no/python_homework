import json
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


###### Task 1
robots_URL = 'https://durhamcountylibrary.org/robots.txt'
try:
    driver.get(robots_URL)
    print(driver.page_source)
except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")


## Conclusion:
# It's not allowed for all user-agents to scrape under/staff

#   >User-agent: * 
#     Disallow: /staff/


##Task 2
li_class = "row cp-search-result-item"
title_class = "title-content"
title_tag = "span"
author_class="author-link"
author_tag = "a"
info_div_class = "cp-format-info"
info_class = 'display-info-primary'
info_tag = 'span'
###Task 3

search_URL = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
try:
    driver.get(search_URL)
    # all the li elements in that page for the search list results
    search_results = driver.find_elements(By.CSS_SELECTOR,'li.row.cp-search-result-item') # all li elements
    print("Length of li items scraped:",len(search_results))
    #empty list called results. add dict values to this list, one for each search result.
    results = []
    for result in search_results:
        title = result.find_element(By.CSS_SELECTOR, 'span.title-content').text
        authors = result.find_elements(By.CSS_SELECTOR, 'a.author-link')
        info = result.find_element(By.CSS_SELECTOR,'div.cp-format-info span.display-info-primary').text
        author_names=[]
        for author in authors:
            author_names.append(author.text)
        author_names = ";".join(author_names)
        print(title)
        results.append({"Title": title, 
                        "Author": author_names,
                        "Format-Year": info})
    

    results_dataframe = pd.DataFrame(results)
    print(results_dataframe)

# Task 4

    results_dataframe.to_csv('assignment8/get_books.csv', index = False)
    with open('assignment8/get_books.json', 'w') as file:
        json.dump(results, file, indent =4)
except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")


finally:

    driver.quit()



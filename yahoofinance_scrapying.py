from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

options = Options()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://finance.yahoo.com/quote/TSM/news/"

driver.get(url)
actions = ActionChains(driver)
for _ in range(100):  
    actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(5)  

WebDriverWait(driver, 25)

rendered_html = driver.execute_script("return document.documentElement.outerHTML;")

soup = BeautifulSoup(rendered_html, "html.parser")

news_items = soup.select("li.js-stream-content")

import pandas as pd

soup = BeautifulSoup(rendered_html, "html.parser")
data = []  

for item in soup.select("div.content"):  
    
    title_element = item.select_one("h3.clamp")
    title = title_element.get_text(strip=True) if title_element else "no_title"

    
    link_element = item.select_one("a")
    link = link_element["href"] if link_element and link_element.has_attr("href") else "no_link"

    
    time_element = item.select_one("div.publishing")
    published_time = time_element.get_text(strip=True) if time_element else "no_time"

    
    summary_element = item.select_one("p.clamp")
    summary = summary_element.get_text(strip=True) if summary_element else "no_summary"


    data.append([title, link, published_time, summary])
df = pd.DataFrame(data, columns=["title", "link", "published_time", "summary"])

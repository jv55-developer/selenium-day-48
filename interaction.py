from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

english_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# print(english_articles.text)
# english_articles.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
#
# print(f"{price_dollar}.{price_cents}")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("class"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# documentation = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation.text)

# footer_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(footer_link.get_attribute("href"))

event_dictionary = {}

event_links = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li")
for event in event_links:
    time = event.find_element(By.TAG_NAME, value="time").text
    event_name = event.find_element(By.TAG_NAME, value="a").text
    index = event_links.index(event)
    event_dictionary[index] = {"time": time, "name": event_name}

print(event_dictionary)
driver.quit()

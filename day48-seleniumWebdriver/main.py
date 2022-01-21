from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/jpascoato/Documents/development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com.br/dp/B08SMJTTNF/ref=cm_gf_aaeu_iaaa_d_p0_e0_qd0_oTCdMzO6yFQPobYZa4a4")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

# search_bar = driver.find_element(By.NAME, "field-keywords")
# print(search_bar.get_attribute("tabindex"))

# logo = driver.find_element(By.CLASS_NAME, "nav-logo-link")
#
# print(logo.size)

# find_css = driver.find_element(By.CSS_SELECTOR, ".a-spacing-small span")
# print(find_css.text)
#
# xpath = driver.find_element(By.XPATH, '//*[@id="universal-hero-quick-promo"]/div/div/div/div[2]/div[1]/span')
# print(xpath.text)

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_titles[n].text
    }
print(events)

# driver.close()
driver.quit()

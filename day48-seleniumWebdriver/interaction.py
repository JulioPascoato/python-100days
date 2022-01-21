from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "/home/jpascoato/Documents/development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")


# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

# article_count.click()

# print(article_count.text)

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Julio")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Pascoato")

email = driver.find_element(By.NAME, "email")
email.send_keys("jpascoato@gmail.com")

email.send_keys(Keys.ENTER)


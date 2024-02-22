from selenium import webdriver

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

searchInput = driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)

driver.close()

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()    # açıldıktan 2 sn sonra ekran tam ekran olur.
# driver.save_screenshot("github.com-homepage.png")    # ekran görüntüsü alarak dizine kaydeder.

print(driver.title)

url = "http://github.com/sadikturan"
driver.get(url)

if "sadikturan" in driver.title:
    driver.save_screenshot("github-sadikturan.png")

time.sleep(2)
driver.back()  # bir önceki sayfaya gider.
# driver.forward()  # bir sonraki sayfaya gider.

time.sleep(2)
driver.close()
from selenium import webdriver
import time
driver = webdriver.Edge(executable_path="C:\\Users\\aritr\\PycharmProjects\\WebDrivers\\edgedriver_win64"
                                        "\\msedgedriver.exe")
driver.get("https://www.cowin.gov.in/home")
driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath("//input[@appinputchar=\"pincode\"]").send_keys("700054")
time.sleep(3)

driver.find_element_by_xpath("//button[@class=\"pin-search-btn\"]").click()
time.sleep(3)

driver.find_element_by_xpath("//a[@class=\"know-more-link accessibility-plugin-ac\"]").click()
time.sleep(3)

driver.quit()

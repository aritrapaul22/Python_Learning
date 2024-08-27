import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")

    service = Service(executable_path='C:\\Users\\aritr\\PycharmProjects\\WebDrivers\\chromedriver\\chromedriver'
                                      '-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.demoblaze.com/index.html")
    return driver


def main():
    # Launch Website
    driver = get_driver()
    time.sleep(2)

    # Login
    driver.find_element(by=By.ID, value="login2").click()
    time.sleep(1)
    driver.find_element(by=By.ID, value="loginusername").send_keys("test")
    time.sleep(1)
    driver.find_element(by=By.ID, value="loginpassword").send_keys("test")
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//*[@id=\"logInModal\"]/div/div/div[3]/button[2]").click()
    time.sleep(3)

    # Scrape Items and Price and Write to a text file
    filename = "PhonePrice.txt"
    with open(filename, 'w') as file:
        for item in range(1, 5):
            product = driver.find_element(by=By.XPATH, value=f"//*[@id=\"tbodyid\"]/div[{item}]/div/div/h4/a").text
            price = driver.find_element(by=By.XPATH, value=f"//*[@id=\"tbodyid\"]/div[{item}]/div/div/h5").text
            file.write(f"{product},{price}\n")

    # Logout
    driver.find_element(by=By.ID, value="logout2").click()
    time.sleep(2)
    driver.quit()


main()

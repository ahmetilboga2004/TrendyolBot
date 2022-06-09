#! /usr/bin/python3
import time
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
options.add_argument("--headless")
options.add_argument("--window-size=%s" % WINDOW_SIZE)


driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)

loginPage = "https://www.trendyol.com/giris?cb=https%3A%2F%2Fwww.trendyol.com%2F"
driver.get(loginPage)
time.sleep(1)

inputEmail = driver.find_element_by_name("login email")
inputPassword = driver.find_element_by_name("login-password")

inputEmail.send_keys("email@gmail.com")
inputPassword.send_keys("password123")

loginButon = driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[1]/form/button")
loginButon.click()
time.sleep(1)

if driver.find_elements_by_css_selector("#error-box-wrapper"):
    print("KULLANICI ADI VEYA ŞİFRE HATALIDIR...")
    driver.close()
else:
    time.sleep(2)
    couponsPage = "https://www.trendyol.com/Hesabim/IndirimKuponlari"
    driver.get(couponsPage)

    if driver.find_elements_by_css_selector(".coupon"):
        print("KUPON VAR")
        exitButton = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[2]/div/a[9]")
        driver.execute_script("arguments[0].click();", exitButton)
    else:
        print("KUPON BULUNMAMAKTA")
        exitButton = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[2]/div/a[9]")
        driver.execute_script("arguments[0].click();", exitButton)

import datetime
import re
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
email_true = 'admin@phptravels.com'
password_true = 'demoadmin'
url = 'https://phptravels.net/admin'
login_page = '//strong[text()=\"Login\"]'
email_input = '//*[@name="email" and @type="text"]'
password_input = '//*[@name="password" and @type="password"]'
remember_pw_checked = '//*[@class="icheckbox_square-grey checked"]'
remember_pw_hover_checked = '//*[@class="icheckbox_square-grey hover checked"]'
remember_pw = '//*[@class="icheckbox_square-grey"]'
login_button = '//span[text()="Login"]'
dashboard_page = '//h1[text()=\"Dashboard\"]'
person_button = '//*[text()="person"]'
logout_button = '//*[text()="Logout"]'

def Cau_01(startDate, closeDate, month_in):
    print('Cau_01')
    startDate = str(startDate)
    closeDate = str(closeDate)

    regex = r"(\d{4})(\d{2})(\d{2})"

    result_sd = re.search(regex, startDate)
    year_sd, month_sd, day_sd = (result_sd.groups())

    result_cd = re.search(regex, closeDate)
    year_cd, month_cd, day_cd = (result_cd.groups())

    startDate = datetime.datetime(int(year_sd), int(month_sd), int(day_sd))
    closeDate = datetime.datetime(int(year_cd), int(month_cd), int(day_cd))
    sumDays = str(closeDate - startDate).split(" ")
    print("Tong so ngay la:", sumDays[0], "days")

    closeDate = startDate + relativedelta(months=month_in)
    closeDate = str(closeDate).replace("-", "")

    print("Ngay ket thuc la:", closeDate[:9])

def Cau_02():
    print("Cau_02")
    driver.get(url)
    driver.maximize_window()
    try:
        driver.implicitly_wait(5)
        driver.find_element_by_xpath(login_page)
        print('Login Page Test Script 1')
    except:
        print('fail')
    driver.find_element_by_xpath(email_input).send_keys(email_true)
    driver.implicitly_wait(1)
    driver.find_element_by_xpath(password_input).send_keys(password_true)
    driver.implicitly_wait(1)
    driver.find_element_by_xpath(login_button).click()
    try:
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(dashboard_page)
        print('pass')
    except:
        print('fail')
    driver.find_element_by_xpath(person_button).click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath(logout_button).click()
    try:
        driver.implicitly_wait(5)
        driver.find_element_by_xpath(login_page).click()
        print('Login Page Test Script 2')
    except:
        print('fail')
    driver.implicitly_wait(1)
    email_placeholder = EC.invisibility_of_element_located(email_input+'/following-sibling::span')
    password_placeholder = EC.invisibility_of_element_located(password_input+'/following-sibling::span')
    print(email_placeholder)
    print(password_placeholder)
    try:
        driver.find_element_by_xpath(remember_pw_checked)
    except:
        driver.find_element_by_xpath(remember_pw).click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath(remember_pw_hover_checked)
        print('Click Remember Button Pass')
    print("Close Chrome ")
    driver.close()

Cau_01(20170220, 20211225, 24)
Cau_02()
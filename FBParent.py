from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import argparse
import sys
import itertools
from queue import Queue
import threading
import os

driver = webdriver.PhantomJS()
#userId = "srikar.0896@gmail.com"
start_time = time.time()
try:
    driver.get("https://www.facebook.com")
    emailFieldID = ".//*[@id='email']"
    passFieldID = ".//*[@id='pass']"
    loginButtonXPath = ".//input[@value='Log In']"
    flLogoXpath = "(//a[contains(@href, 'logo')])[1]"
    emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(emailFieldID))
    passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passFieldID))
    loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXPath))
    emailFieldElement.click()
    emailFieldElement.clear()
    emailFieldElement.send_keys("Mail Id")
    passFieldElement.click()
    passFieldElement.clear()
    passFieldElement.send_keys("Password")
    loginButtonElement.click()
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(flLogoXpath))
    driver.save_screenshot("LoginPage.png")
    print("\n    Time Executed - " + str(time.time() - start_time))
    print("Login Succesfully!!")
except Exception as e:
    driver.save_screenshot("erro.png")
    driver.quit()
    raise
# display.stop()

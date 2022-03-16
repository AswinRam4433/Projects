from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os
import time
from datetime import datetime


driver = webdriver.Chrome("C:/SeleniumDrivers/chromedriver.exe") 
driver.get('https://www.whatsapp.com/?lang=en')
waweb=driver.find_element_by_xpath('//*[@id="hide_till_load"]/div[1]/div[1]/header/div/div[2]/span[1]/a[1]')
waweb.click()
# now we will wait for 15 seconds for the user to scan the code
#before this time, the user should've scanned the QR code or else the code will throw an error
time.sleep(15)
name_of_person='vijay beer'
# replace the 'Data Science To Do' with the name of your contact or WA group
con=driver.find_element_by_css_selector(f"[title^='{name_of_person}']")
# con=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[13]/div/div/div[2]/div[1]/div[1]/span')
con.click()

count=40
# count stores the number of times we want to send the specific message

typearea=driver.find_element_by_css_selector("[title^='Type a message']")
# finding the text box to send the message

x= datetime.now()
# x will store the time at which the program begins to execute
print(x)
for i in range(0,count):
    typearea.send_keys("Hello",Keys.ENTER)


y=datetime.now()
# y will store the time at which the program has successfully sent out the given number of messages
print(y)
print(f'The time taken to print {count} messages is {(y-x).seconds} seconds' )
# using timedeltas to find the time taken to send out the messages
# printing out the time taken to send the messages


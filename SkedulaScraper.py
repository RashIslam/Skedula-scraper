"""
Rashadul Islam
SkedulaScraper.py
9/3/19

Throughout high school we often check our grades on this online grades website
called skedula. However, even when the grades are there, we have a hard time
gauging our academic standing and want to average our grades so that we can
accurately see where we are in school. Using selenium and webdrivers, this program
can cirvumvent the anti-robot measures in this site by physically opening up the
browser, inputting the user and password information, scraping the grades data, and
closing itself for future computation.
"""

import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time

def formfill(username, password):
    signInButton = brow.find_element_by_id("sign_in")
    signInButton.send_keys(Keys.ENTER)
    time.sleep(1)
    userEntry =  brow.find_element_by_name("user[username]")
    userEntry.send_keys(username)
    userEntry.send_keys(Keys.ENTER)
    time.sleep(1)
    passwordEntry = brow.find_element_by_name("user[password]")
    passwordEntry.send_keys(password)
    passwordEntry.send_keys(Keys.ENTER)
    
user = input("Enter your OSIS: ") #Unique student identifier
pswd = input("Enter your password") #will be hidden

brow = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver") #Path used for driver
brow.get("https://pupilpath.skedula.com/") #opens webpage in Chromium
time.sleep(3)
formfill(user, pswd)

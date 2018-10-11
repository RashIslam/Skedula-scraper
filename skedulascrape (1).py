#Rashadul Islam and Aren Moss
#skedulascrape.py
#6/6/16
#Computer Science Principles

import getpass
from selenium import webdriver #Selenium is used to emulate browsers.
from selenium.webdriver.common.keys import Keys
#from selenium
import selenium
import time

#Run in powershell using chromedriver.

def formfill(us, pa): #logs into skedula
    entry1 = brow.find_element_by_name("user[username]")
    entry1.send_keys(us) #Enters the username.
    entry2 = brow.find_element_by_name("user[password]")
    entry2.send_keys(pa) #Enters the password.
    
def cleaningtrash(): #This function gets rid of unneccesary information.
    for x in classlist:
        if 'REG' in x:
            del finallist[classlist.index(x)]
            classlist.remove(x)
        if 'LUNCH' in x:
            del finallist[classlist.index(x)]
            classlist.remove(x)
        if 'MAJOR' in x:
            del finallist[classlist.index(x)]
            classlist.remove(x)
        if 'FINANCE' in x:
            del finallist[classlist.index(x)]
            classlist.remove(x)
        if 'CLASS' in x:
            del finallist[classlist.index(x)]
            classlist.remove(x)
        if 'CITIZENS' in x:
            del finallist[classlist.index(x)]
            classlist.remove(x)
        if 'LOTE' in x:
            del finallist[classlist.index(x)]
            classlist.remove(x)
        if 'SAT' in x:
            del finallist[classlist.index(x)]
            classlist.remove(x)
    for x in finallist:
        if x == '':
            del classlist[finallist.index(x)]
            finallist.remove(x)

user = raw_input("Enter your OSIS: ") #Osis and password are used to login to skedula.
pswd = getpass.getpass("Enter your password: ") #Getpass is used to keep the password input hidden.

brow = webdriver.Chrome()
brow.get("https://pupilpath.skedula.com/") #This is the link to the skedula login page.

but1 = brow.find_element_by_id("sign_in")
but1.send_keys(Keys.ENTER)

time.sleep(3) #wait for page to load

formfill(user, pswd)

but1 = brow.find_element_by_id("sign_in")
but1.send_keys(Keys.ENTER) #Presses the enter button.

time.sleep(4) #wait for page to load

but2 = brow.find_element_by_id("loginSKD")
but2.send_keys(Keys.ENTER)

time.sleep(5) #wait for page to load

listrow = []
headers= brow.find_elements_by_tag_name('td')
file_header = [header.text.encode("utf8") for header in headers]
#This list includes all the data including marking period, class code, grade, teacher, and more.

brow.quit()

file_header.reverse() #to make sorting data easier
numlist = [] #list of grades
classlist = [] #list of classes

for x in range(5, (len(file_header)+5)): # removes unnecessary columns
    if (x%5 == 0):
        numlist.append(file_header[x-5])
        classlist.append(file_header[x-2])

numlist = filter(lambda x: 'MP2: ' or 'MP1: ' in x, numlist) #filtering for the phrase MP2 or MP1


finallist = []
for x in numlist:
    x = x[5: ]
    finallist.append(x)
#This list consists of just the grades.

cleaningtrash() 
    
floatlist = [] #making string to float
for x in finallist:
    floatlist.append(float(x))


weightlist = [] 
print " The weight for GYM is 0.5 . The weight for AP/Major course is 1.1 "
for x in classlist: #asking for the weight of each class
    y = float(raw_input("What is the weight of %s: " %x))
    weightlist.append(y)

weightsum = 0 
for x in floatlist: #adding all the weights together
    weightsum = weightsum + (x * weightlist[floatlist.index(x)])
              
sum = 0
for x in weightlist: #This for loop adds the grades together to calculate the total sum.
    sum += x
mean = weightsum/sum #This calculates the average of all the grades.
print "Your weighted average is: %f" % mean

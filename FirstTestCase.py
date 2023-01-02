import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\driver\chromedriver_win32.zip\chromedriver")


driver= webdriver.Chrome(service =serv_obj)
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("http://127.0.0.1:8000/")
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='header']/div/ul/li/a").click()
time.sleep(1)
driver.find_element(By.ID, "Newusn").send_keys("Wrong USN")
time.sleep(1)
driver.find_element(By.ID, "Password").send_keys("randompw")
time.sleep(1)
driver.find_element(By.ID, "Login").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='header']/div/ul/li/a").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='header']/div/ul/li/a").click()
time.sleep(1)

ele1 = driver.find_element(By.ID, "CollegeName")
drp = Select(ele1)
drp.select_by_visible_text("DSCE")
time.sleep(1)


#random words generator 1
N = 7
res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=N))

fn= str(res)


driver.find_element(By.ID,"FName").send_keys(fn)
time.sleep(1)


#random words generator 2
N = 5
res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=N))

ln= str(res)


driver.find_element(By.ID,"LName").send_keys(ln)
time.sleep(1)

mail=(fn+"@"+ln)
driver.find_element(By.ID,"email").send_keys(mail)
time.sleep(1)

usn= random.randint(0,5000)
driver.find_element(By.ID,"usn").send_keys(usn)
time.sleep(1)
pw=random.randint(0,15000)
driver.find_element(By.ID,"password").send_keys(pw)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(4)

#var= driver.find_element(By.XPATH, "//*[@id='SignUpBtn']")
#driver.execute_script("arguments[0].scrollIntoView();",var)

#driver.implicitly_wait(20)


driver.find_element(By.ID,"ConfiPass").send_keys(pw)
time.sleep(2)

driver.find_element(By.ID,"SignUpBtn").click()
time.sleep(2)
driver.find_element(By.ID, "Newusn").send_keys(usn)
time.sleep(1)
driver.find_element(By.ID, "Password").send_keys(pw)
time.sleep(1)
driver.find_element(By.ID, "Login").click()
time.sleep(100)






#time.sleep(100)
'''
Author : @rahul_agrawal_99
Project : Instagram Bomber
function : This script is used to send infinite message to the instagram account
purpose : learn about selenium , webdriver and automated test 
'''
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
import time

start_time = time.time()



print(" *****************       Welcome To IG Bomber   *********************************\n")

print("  This is fully safe to enter your credential here as testing is done on local machine and you can visually view the all parts\n")
print(" --- Warning: Use only for fun purpoes with known person only with their proper permission ---\n")
fb_mobile = input("Enter mobile/email :")
fb_pass = input("Enter Password :")
user = input("Enter User Id of instagram user :")
msg = input("Enter a messege to send: ")
loop = int(input("Enter number of times to send: "))
num = input("Press 0 to send with msg no also (if not press any button) : ")

try:
    driver =  webdriver.Chrome('./chromedriver.exe') 
except Exception as e:
    print(f"You Got an Error {e} \n check your current chrome version and path")






#  go to instagram
driver.get('https://www.instagram.com/')     
  

#  login using facebook
fbbtn=WebDriverWait(driver,50).until(lambda driver:driver.find_element_by_class_name('KPnG0'))
fbbtn.click()

email = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_id('email'))
passw = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_id('pass'))
email.send_keys(fb_mobile)
passw.send_keys(fb_pass)


login=WebDriverWait(driver,50).until(lambda driver:driver.find_element_by_name('login'))

login.click()

print("successfully login")

# x_path = //button[contains(text(),'Not Now')]

close_btn =WebDriverWait(driver,50).until(lambda driver:driver.find_element_by_xpath("//button[contains(text(),'Not Now')]"))

close_btn.click()

#  get to user that is choosen as target to bomb

driver.get(f'https://www.instagram.com/{user}/')   


msg_btn = WebDriverWait(driver,50).until(lambda driver:driver.find_element_by_xpath("//div[contains(text(),'Message')]"))
msg_btn.click()

print("successfully reached inbox")

click_msg = WebDriverWait(driver,50).until(lambda driver:driver.find_element_by_xpath("//body/div[@id='react-root']/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/textarea[1]"))




if num == 0 or num == "0":
    for i in range(loop):
        click_msg.send_keys(f"{msg} - msg no. {i+1}")
        click_msg.send_keys(keys.Keys.ENTER)
else:
    for i in range(loop):
        click_msg.send_keys(f"{msg}")
        click_msg.send_keys(keys.Keys.ENTER)
        

    
click_msg.send_keys(f"bomb on you requested by '{fb_mobile[:len(fb_mobile)-3]}***' with {loop} messages")
click_msg.send_keys(keys.Keys.ENTER)
click_msg.send_keys("IG-bomber made by @rahul_agrawal_99")
click_msg.send_keys(keys.Keys.ENTER)
click_msg.send_keys(keys.Keys.ENTER)
end_time = time.time()
print(f"sent all messages in {end_time-start_time}sec")

# //button[contains(text(),'Send')]




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time #imported to wait for the webpage to load
username = input("Enter username/email/phonenumber of your Instagram handle: ")
password = getpass.getpass(prompt='Enter password: ')#getpass enables user to enter password without revealing it on the terminal(only on terminal not in idle)
usersleep = 3 #keep the number of seconds based on your internet speed
driver = webdriver.Chrome() #make sure the chromedriver.exe is in the directory where your python file is there
driver.get('https://www.instagram.com/')
time.sleep(usersleep)#wait for the webpage to load
search = driver.find_element_by_name('username')
search.send_keys(username)
search = driver.find_element_by_name('password')
search.send_keys(password)
search.send_keys(Keys.RETURN)
time.sleep(usersleep)
driver.find_element_by_xpath('//button[text()="Not Now"]').click()
time.sleep(usersleep)
driver.find_element_by_xpath('//button[text()="Not Now"]').click()
time.sleep(usersleep)
driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(username)).click()
time.sleep(usersleep)

driver.find_element_by_xpath('//a[text()=" following"]').click()#opens following list
time.sleep(usersleep)
scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
prev_height, height = 0, 1
while prev_height != height:
    prev_height = height
    time.sleep(usersleep/2)
    height = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        return arguments[0].scrollHeight;
        """, scroll_box)
links = scroll_box.find_elements_by_tag_name('a')
following = [name.text for name in links if name.text != '']
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()#closes following list


driver.find_element_by_xpath('//a[text()=" followers"]').click()#opens followers list
time.sleep(usersleep)
scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
prev_height, height = 0, 1
while prev_height != height:
    prev_height = height
    time.sleep(usersleep/2)
    height = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        return arguments[0].scrollHeight;
        """, scroll_box)
links = scroll_box.find_elements_by_tag_name('a')
followers = [name.text for name in links if name.text != '']
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()#closes followers list
driver.quit()

print("Dont close program is running\n")
output = [user for user in following if user not in followers]
for user in output:
    print(user)
print("Program Ended")

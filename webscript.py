from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
import random

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

while(1):

	driver1 = webdriver.Chrome('C:/Users/Andrew/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/selenium/chromedriver', chrome_options=chrome_options) #10minutemail
	driver2 = webdriver.Chrome('C:/Users/Andrew/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/selenium/chromedriver', chrome_options=chrome_options) #thehabit     #edit the path according to where you have your own chromedriver downloaded



	driver1.get("https://10minutemail.net/")
	driver2.get("https://www.habitburger.com/signup/")
	
	time.sleep(10)

	copy_button = driver1.find_element_by_id('copy-button')
	copy_button.send_keys(Keys.RETURN)

	first_name = driver2.find_element_by_id('input_6_10')
	fname = id_generator()
	first_name.send_keys(fname)

	last_name = driver2.find_element_by_id('input_6_11')
	lname = id_generator()
	last_name.send_keys(lname)

	email = driver2.find_element_by_id('input_6_2')
	email.send_keys(Keys.CONTROL + 'v')

	zip_code = driver2.find_element_by_id('input_6_6')
	zip_code.send_keys('92887')

	time.sleep(5)

	location = driver2.find_element_by_id('input_6_3')
	location.send_keys(Keys.RETURN + Keys.DOWN + Keys.RETURN)

	month = driver2.find_element_by_id('input_6_4')
	month.send_keys(Keys.RETURN + Keys.DOWN + Keys.RETURN)

	day = driver2.find_element_by_id('input_6_5')
	day.send_keys(Keys.RETURN + Keys.DOWN + Keys.RETURN)

	join_now = driver2.find_element_by_id('gform_submit_button_6')
	join_now.send_keys(Keys.RETURN)

	time.sleep(50)

	burger_link = driver1.find_element_by_link_text('Enjoy Your Free Charburger On Us!')
	burger_link.send_keys(Keys.RETURN)

	time.sleep(1)

	i_d = id_generator()

	driver1.execute_script("window.scrollTo(0, 1400)") 
	driver1.save_screenshot("C:/Users/Andrew/Desktop/coupons/" + i_d  + ".png")   #edit the path according to where you would like to save the coupons

	driver1.close()
	driver2.close()
































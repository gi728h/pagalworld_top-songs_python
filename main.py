
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from time import sleep

####>DOWNLOAD MUSIC FILES<####
page = int(input('pages: '))
try:
	try:
		chrome_options = webdriver.ChromeOptions()

		#########>Change to your dir<#########
		prefs = {'download.default_directory' : '/home/padhiyar/Downloads/down'}
		chrome_options.add_experimental_option('prefs', prefs)
		driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')
	except:
		driver = webdriver.Chrome(executable_path='./chromedriver')
except:
	#####>for windows<#####
	driver = webdriver.Chrome()

for i in range(page):
    driver.get('https://www.pagalworld.tv/top-songs.html?page={}'.format(i+1))
    for i in range(25):
        listt = driver.find_elements(By.XPATH,"//div[@class='cat-list']")
        io = listt[i]
        io.click()
        music = driver.find_element(By.CLASS_NAME,'dbutton')
        music.click()
        sleep(1)
        driver.back()

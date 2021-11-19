### for selenium
from numpy import add, datetime_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
import pandas

import time
from datetime import datetime
import requests

def mySendKeys(str,keys):
    try:
        kys = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                 (By.XPATH, str))
        )
        kys.send_keys(keys)
    except:
        #browser.quit()
        print('aaaaaaaaaaaaaaaaaaaaaaa')

def myClick(str):
    try:
        clck = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, str))
        )
        hover = ActionChains(driver)
        print(clck.is_displayed())
        hover.move_to_element(clck)
        hover.click(clck)
        hover.perform()
    except:
        driver.quit()


driver = webdriver.Chrome('C:\\Users\\salim\\Desktop\\python\\driver\\chromedriver.exe')


driver.get('https://www.blockchain.com/?utm_campaign=expnav_logo')

mySendKeys('/html/body/div/div/header/div/div[2]/div[1]/input','geldik')

driver.find_element_by_xpath('/html/body/div/div/header/div/div[2]/div[1]/input').send_keys(Keys.ENTER)

complete = pandas.read_csv('Complete.csv')

addresses = complete['Address'].to_list()

start_time = datetime.now()
for j in range(600,1000):
    address = addresses[j]
    output = open('output.txt','a')
    mySendKeys(' //*[@id="__next"]/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/input',address)
    driver.find_element_by_xpath(' //*[@id="__next"]/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/input').send_keys(Keys.ENTER)

    for i in range(1,int(driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div/div[2]/div/div[1]/div[2]/div/div[3]/div[2]/span').text.replace(',',''))+1):
        try:
            transactionHash = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div[3]/div[{}]/div[1]/div[1]/div[2]/a'.format(i))
            response = requests.get(url="https://api.blockchain.info/v2/eth/data/transaction/{}".format(transactionHash.text))
            output.write(response.json()['blockNumber'])

        except:
            output.close()
            print(address)
            print(i)
            continue

    output.close()    

print(datetime.now()-start_time)

#//*[@id="__next"]/div[3]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/div[2]/a
#//*[@id="__next"]/div[3]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[1]/div[1]/div[2]/a
#//*[@id="__next"]/div[3]/div/div[2]/div/div[2]/div/div[3]/div[3]/div[1]/div[1]/div[2]/a
#//*[@id="__next"]/div[3]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/div[2]/a

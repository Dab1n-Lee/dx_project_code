import re
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
from bs4 import BeautifulSoup

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)

driver.maximize_window()
driver.get('https://www.instagram.com')
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('')
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(3)

'//*[@id="mount_0_0_AB"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button'


def MakeXpath(xpath):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    insta_id = soup.select('div')[1]['id']
    time.sleep(1)
    xpath_result = xpath[0:9] + insta_id + xpath[21:]

    return xpath_result


time.sleep(1)
xpath = '//*[@id="mount_0_0_4r"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button'
driver.find_element(By.XPATH, MakeXpath(xpath)).click()

time.sleep(2)
xpath = '//*[@id="mount_0_0_K8"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
driver.find_element(By.XPATH, MakeXpath(xpath)).click()

time.sleep(1)
driver.get('https://www.instagram.com/explore/tags/헛걸음')
time.sleep(5)
# mount_0_0_Vk > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m > section > main > article > div._aaq8 > div > div > div:nth-child(1) > div:nth-child(1) > a > div > div._aagw
a = driver.find_elements(By.CSS_SELECTOR, 'div._aagw')
for i in range(40):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.8)

a[0].click()
time.sleep(3)

post_count = 5
# img_list = []

result_dict = {}
content_list = []
for temp in range(100):

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    comment = soup.find_all('div', class_='_a9zs')
    print(f'{temp}번째--')
    for temp1 in comment:
        print(re.sub("[^0-9a-zA-Z가-힣# ]", '', temp1.text))
        content_list.append(re.sub("[^0-9a-zA-Z가-힣# ]", '', temp1.text))

    # img = soup.find('div', class_="_aagv").find('img')
    # img_list.append(img.get('src'))

    if temp == 0:
        driver.find_element(By.XPATH, MakeXpath(
            '//*[@id="mount_0_0_K8"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div['
            '1]/div/div/div/button')).click()
    else:
        driver.find_element(By.XPATH, MakeXpath(
            '//*[@id="mount_0_0_K8"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div['
            '2]/button')).click()

    time.sleep(1.6)

result_dict['내용'] = content_list
df = pd.DataFrame.from_dict(result_dict)
df.to_csv('인스타 게시글.csv')

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
import os
import sys

sys.path.insert(0, '/Users/CREEP/Downloads/python/lib')
#path to your project folder where this is in or to any lib folders to grab functions from

from findChapterNumber import *
from writeChToFile import *

lightNovelTitle = "The novel's extra"

option = Options()
option.add_extension(r'C:\Users\CREEP\Downloads\extension_5_0_5_0.crx')
#you need to download adblock in crx version
driver = uc.Chrome(use_subprocess=True, options = option)
driver.get("https://www.lightnovelpub.com")

driver.find_element(by=By.XPATH, value="/html/body/header/div/div[2]/nav/ul/li[1]/a").click()
element = driver.find_element(by=By.NAME, value="inputContent")
element.send_keys(lightNovelTitle)
element.send_keys(Keys.RETURN)
WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="novelListBase"]/div')))
searchResult = driver.find_element(by=By.XPATH, value='//*[@id="novelListBase"]/*').text
if searchResult == 'No novel could be found.':
    #break
    print("lmao")
else:
    resultTitle = driver.find_element(by=By.XPATH, value='//*[@id="novelListBase"]/ul/li/a/div[2]/h4').text
    print("Matching light novel found: " + resultTitle)
    LNpath = 'C:/Users/CREEP/Downloads/python/novelRip/'
    #this is where your novels will be stored
    novelName = resultTitle
    LNpath = os.path.join(LNpath, novelName)
    if not os.path.exists(LNpath):
        os.mkdir(LNpath)
    resultLink = driver.find_element(by=By.XPATH, value='//*[@id="novelListBase"]/ul/li/a').click()
    driver.find_element(by=By.XPATH, value='//*[@id="novel"]/div[1]/nav/a[1]').click()
    numPage = len(driver.find_elements(by=By.XPATH, value='//*[@id="chpagedlist"]/div/div/div/ul/*'))
    currentPage = 1
    addPage = False
    while currentPage <= numPage:
        if numPage > 1 and not addPage:
            currentPage += 1
            addPage = True
        numCh = len(driver.find_elements(by=By.XPATH, value='//*[@id="chpagedlist"]/ul/*'))
        print(numCh)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="chpagedlist"]/ul/li[1]/a'))).click()
        paragraphs = driver.find_elements(by=By.TAG_NAME, value="p")
        chNum = findChNum(driver.find_element(by=By.XPATH, value='//*[@id="chapter-article"]/section[1]/div[2]/h1/span[2]').text)
        print(driver.find_element(by=By.XPATH, value='//*[@id="chapter-article"]/section[1]/div[2]/h1/span[2]').text)
        chPath = os.path.join(LNpath, chNum + '.txt')
        writeChToFile(chPath=chPath, paragraphs=paragraphs)
        for n in range(1, numCh):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button.nextchap'))).click()
            paragraphs = driver.find_elements(by=By.TAG_NAME, value="p")
            chNum = findChNum(driver.find_element(by=By.XPATH, value='//*[@id="chapter-article"]/section[1]/div[2]/h1/span[2]').text)
            chPath = os.path.join(LNpath, chNum + '.txt')
            writeChToFile(chPath=chPath, paragraphs=paragraphs)     
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#chapter-article > section.page-in.content-wrap > div.chapternav.skiptranslate > a.button.chapindex'))).click()
        driver.find_element(by=By.XPATH, value='//*[@id="novel"]/div[1]/nav/a[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="chpagedlist"]/div/div/div/ul/li[' + str(currentPage) + ']').click()
        currentPage += 1
    print('done')


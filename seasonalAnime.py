from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import webbrowser

season = "summer"
animeYear = 2019

""" print("Seasonal Anime List Finder")
seasonList = ["winter", "summer", "spring", "fall"]
season = input("what season? ").lower()

while True:
    if season in seasonList:
        break
    print("Invalid input. The seasons are: ")
    print(seasonList)
    season = input("what season? ").lower()

animeYear = input("what year? ")
currentYear = date.today().year

def animeYearIssue():
    print("There is no anime for requested year.")
    animeYear = input("what year? ")
    return animeYear

while True:
    if animeYear.isnumeric() == False: 
        animeYear = animeYearIssue()
    if int(animeYear) > currentYear or int(animeYear) < 1917:
        animeYear = animeYearIssue()
    else:
        break
print("searching for anime in: " + season + " " + animeYear) """

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
driver.get("https://myanimelist.net/")
driver.find_element(by=By.CSS_SELECTOR, value="#nav > li:nth-child(1)").click()
driver.find_element(by=By.CSS_SELECTOR, value="#nav > li:nth-child(1) > ul > li:nth-child(3) > a").click()
driver.find_element(by=By.NAME, value="season").click()
select = Select(driver.find_element(by=By.NAME, value="season"))
WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.NAME, "season")))
select.select_by_value(season)
element = driver.find_element(by=By.NAME, value="year")
element.send_keys(animeYear)
driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[2]/div[1]/ul/li[9]/form/input[2]').click()

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("C:/Users/anahitha/Downloads/whitehat/chromedriver")
browser.get(starturl)
time.sleep(10)
def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planetdata = []
    for i in range(0, 170):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for ultag in soup.find_all("ul", attrs = {"class", "exoplanet"}):
            litags = ultag.find_all("li")
            temlist = []
            for index, litag in enumerate(litags):
                if index == 0:
                    temlist.append(litag.find_all("a")[0].contents[0])
                else:
                    try:
                        temlist.append(litag.contents[0])
                    except:
                        temlist.append("")
            planetdata.append(temlist)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("data.csv", "w") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetdata)
scrape()
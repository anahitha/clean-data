from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests 

starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("C:/Users/anahitha/Downloads/whitehat/chromedriver")
browser.get(starturl)
newplanetdata = []
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
planetdata = []
time.sleep(10)
def scrape():
    for i in range(0, 170):
        while True:
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            currentpg = int(soup.find_all("input",attrs= {"class", "page_num"})[0].get("value"))
            if currentpg<i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif currentpg>i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break
        
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
        print("page number ", i)

def scrapeMore(hyperlink):
    try:
        pg = requests.get(hyperlink)
        soup = BeautifulSoup(pg.content, "html.parser")
        templist = []
        for trtag in soup.find_all("tr", attrs={"class":"fact_row"}):
            trtags = trtag.find_all("td")
            for tdtag in trtags:
                try:
                    templist.append(tdtag.find_all("div", attrs={"class":"value"})[0].contents[0])
                except:
                    templist.append("")
        newplanetdata.append(templist)
    except:
        time.sleep(1)
        scrapeMore(hyperlink)
scrape()
for index, data in enumerate(planetdata):
    scrapeMore(data[5])
    print(index)
finalplanetdata = []
for index, data in enumerate(planetdata):
    newplanetelement = newplanetdata[index]
    newplanetelement = [elem.replace("\n", "") for elem in newplanetelement]
    newplanetelement = newplanetelement[:7]
    finalplanetdata.append(data+newplanetelement)
with open("data2.csv", "w") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(headers)
    csvwriter.writerows(finalplanetdata)
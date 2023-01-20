#assuming "https://sites.google.com/a/chromium.org/chromedriver/downloads" is downloaded, and chromedriver is added to path
#works with any browser

#google results logs top 5 links on result page to a text file

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# set up browser
driver = webdriver.Chrome()

# go to Google
driver.get("http://www.google.com")

# find the search box element and enter the search term
search_box = driver.find_element_by_name("q")
search_box.send_keys("example search term" + Keys.RETURN)

# list of links
links=[]

# get the first 5 links from the search results
for i in range(1,6):
    links.append(driver.find_element_by_css_selector("#rso > div:nth-child("+str(i)+") > div > div:nth-child(1) > div > div > div.r > a").get_attribute("href"))

# open a file to write links
with open("Links.txt", "w") as f:
    for link in links:
        f.write("%s\n" % link)

# close the browser
driver.quit()

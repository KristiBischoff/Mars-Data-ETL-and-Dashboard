#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time
import numpy as np
import pandas as pd

### NASA Mars News

#Scrape the NASA Mars News Site https://mars.nasa.gov/news/ and collect 
#the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

def init_browser():
    return Browser("chrome", headless=False)

def scrape_info():
    browser = init_browser()
    mars_info = {}
    browser = Browser("chrome", headless=False)
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find("div", class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text


    mars_info["NewsTitle"] = news_title
    mars_info["NewsDescription"] = news_p


    ### JPL Mars Space Images - Featured Image
    base_url = "https://www.jpl.nasa.gov"
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)

    browser.click_link_by_id('full_image')
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    featured_image_url1 = soup.find('img', class_="fancybox-image")
    featured_image_url = base_url + featured_image_url1['src']

    print(featured_image_url)

    mars_info["FeaturedImage"] = featured_image_url

    ### Mars Weather from Twitter

    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text.strip()



    mars_info["WeatherTweet"] = mars_weather

    ### Mars Facts

    #Visit the Mars Facts webpage http://space-facts.com/mars/ and use Pandas to scrape 
    #the table containing facts about the planet including Diameter, Mass, etc.

    #Use Pandas to convert the data to a HTML table string.
    url = "https://space-facts.com/mars/"  
    
    browser.visit(url)
    time.sleep(3)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    tables_df_list  = soup.find("table", id="tablepress-mars")


    for table in tables_df_list:

        html_table = table.to_html()
        html_table

        html_table.replace('\n', '')


        table.to_html('table.html')

    mars_info["MarsTable"] = table.to_html('table.html')
 

    # tables = pd.read_html(url)
    # tables

    # tables_df = tables[0]
    # tables_df

    # html_table = tables_df.to_html()
    # html_table

    # html_table.replace('\n', '')


    # tables_df.to_html('table.html')

    # mars_info["MarsTable"] = tables_df.to_html('table.html')


    ### Mars Hemispheres

    #Visit the USGS Astrogeology site https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    #to obtain high resolution images for each of Mar's hemispheres.

    #You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

    #Save both the image url string for the full resolution hemisphere image,
    #and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using 
    #the keys `img_url` and `title`.

    #Append the dictionary with the image url string and the hemisphere title to a list. 
    #This list will contain one dictionary for each hemisphere.


    ### JPL Mars Space Images - Featured Image
    base_url1 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(base_url1)
    time.sleep(1)
    #url_new = "https://astrogeology.usgs.gov/search/map/Mars/Viking/"

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    products = soup.find("div", id="product-section")
    link_lists = soup.find_all("div", class_="description")
    #link_lists = [x.find("a") for x in product_des]

    link_lists

    imagelist = []

    for link_list in link_lists:
        linktext = link_list.h3.text
        #browser.execute_script("arguments[0].scrollIntoView();", link_list)
        browser.click_link_by_partial_text(linktext)
        time.sleep(1)
        soup2 = BeautifulSoup(browser.html, "html.parser")
        image_url1 = soup2.find('a', target="_blank")
        img_url = image_url1['href']
        title = soup2.find('h2', class_= "title").get_text()
        imagelist.append({"title": title, "img_url": img_url})
        browser.back()
        time.sleep(1)

    mars_info["ImageTitle"] = title
    mars_info["ImageURL"] = img_url

    return(mars_info)

#scrape_info()


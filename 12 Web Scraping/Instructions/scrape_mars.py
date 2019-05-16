# import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd

# setup executable path
def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# define scrape function
def scrape():

    # initialize browser and dictionary
    browser = init_browser()
    mars_data = {}

    # visit mars nasa url
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # parse HTML object
    html = browser.html
    soup = bs(html, 'html.parser')

    # scrape elements from html
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # add scraped data to dictionary
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p

    # visit featured images url
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)

    # parse HTML object
    image_html = browser.html
    image_soup = bs(image_html, 'html.parser')

    # scrape elements from html
    featured_image = image_soup.find('img', class_='thumb')['src']
    featured_image_url = "https://www.jpl.nasa.gov" + featured_image

    # add scraped data to dictionary
    mars_data['image'] = featured_image_url

    # visit mars weather url
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)

    # parse HTML object
    weather_html = browser.html
    weather_soup = bs(weather_html, 'html.parser')

    # scrape elements from html
    weather = weather_soup.find_all('div', class_='js-tweet-text-container')
    for item in weather:
        mars_weather = item.find('p').text
        if 'low' and 'high' in mars_weather:
            print(mars_weather)
            break
    
    # add scraped data to dictionary
    mars_data['weather'] = mars_weather

    # visit mars facts url
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)

    # use pandas to parse table
    mars_facts = pd.read_html(facts_url)
    facts_df = mars_facts[0]
    facts_df.columns = ['Fact', 'Value']
    html_table = facts_df.to_html()
    
    # add scraped data to dictionary
    mars_data['table'] = html_table

    # visit usgs astrogeology url
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)

    # parse html object
    hemisphere_html = browser.html
    hemisphere_soup = bs(hemisphere_html, 'html.parser')

    # scrape elements from html
    hemisphere_image_url = 'https://astrogeology.usgs.gov'
    hemisphere_list = []

    hemisphere_items = hemisphere_soup.find_all('div', class_='item')

    # loop through all items to find title and image url
    for item in hemisphere_items:
        title = item.find('h3').text
        image_link = item.find('a')['href']
        browser.visit(hemisphere_image_url + image_link)
        image_link = browser.html
        soup = bs(image_link, 'html.parser')
        image_url = hemisphere_image_url + soup.find('img', class_='wide-image')['src']
        hemisphere_list.append({'title': title, 'img_url': image_url})

    # add scraped data to dictionary
    mars_data['hemispheres'] = hemisphere_list

    #return dictionary values
    return mars_data




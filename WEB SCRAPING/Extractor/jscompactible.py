import os
import requests
import sys
import re 
import time
import argparse
import selenium
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


'''
    A Script that extracts email and phone numbers from websites...
    And adds the result to a file...
    This script might not work with javascript generated website...
'''

# STEP 1: Use request among with header and cookies option to get the website data... DONE!
# 
# STEP 2: Use Beautiful Soup to parse data... DONE!
# 
# STEP 3: Use Regex to get the actual data...
# 
# STEP 4: Print output and also add them to a file...  

# NOTE: This script will crawl a javascript generated website...
# WE NEED TO MAKE THIS SCRIPT JAVASCRIPT COMPACTIBLE USING SELENIUM IN HEADLESS MODE... DONE!

# TEST DATA: https://www.nairaland.com/5705359/food-stuff-exportation-business
# TEST DATA: https://www.finelib.com/cities/asaba/business
# Seems the above along with facebook is restricting us... Consider using selenium in headless mode...

phone = r'(\+|\d)((\-|\d|\s)+){9,12}'

email = r'[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)'

results = './Results-js'


def getDataJs(link):
    chrome_option = Options()
    chrome_option.add_argument("--headless")
    driver = webdriver.Chrome('./chromedriver.exe', options=chrome_option)
    try:
        driver.get(link)
        time.sleep(3)
    except selenium.common.exceptions.InvalidArgumentException:
        print("The URL is Invalid... Please try prepend with 'https://' or 'http://' ")
        sys.exit()
    except selenium.common.exceptions.WebDriverException:
        print("Your internet connection is down or the URL is Bad!")
        sys.exit()
    else:
        pageSource = driver.page_source.encode('utf-8')
        driver.close()
        return BeautifulSoup(pageSource, 'html.parser')
    finally:
        driver.quit()

        
def extract(soup, reg):
    # Get all occurence of text that contains a match....
    raw_data =  soup.find_all(text=re.compile(reg))
    # Get a Nested list of every occurence within the text
    process_data = list(map(lambda x: [y.group() for y in re.finditer(reg, x)], raw_data))
    # Return a flat list of Unique data...
    return list(set([data for first_iter in process_data for data in first_iter]))

def processData(data, link, typ):

    if not os.path.isdir(results):
        os.makedirs(results)
    if data:
        now = datetime.now().strftime('%c')
        site_name = urlparse(link).netloc
        name = f'{results}/{site_name}-{typ}-{now}'.replace(':', '-')

        with open(f'{name}.txt', 'a') as f:
            f.write(f'{typ} Data for {site_name}: \n\n')
            for item in data:
                f.write(f'{item}\n')


def main():
    # options needed... link to website...
    # save result to text file...
    parser = argparse.ArgumentParser(description='...Email and Phone Number Extractor...')
    parser.add_argument('webLink', help='Input the website link you\'d like to crawl...', metavar='W')
    parsed_link = parser.parse_args().webLink
    data = getDataJs(parsed_link)
    phone_data = extract(data, phone)
    email_data = extract(data, email)
    processData(phone_data, parsed_link, 'Phone')
    processData(email_data, parsed_link, 'Email')
    # print(f'Phone Data: {phone_data}')
    # print(f'Email Data: {email_data}')
if __name__ == '__main__':
    main()
    print('*****======== Done Scraping! ========*****')
    print("\n Please Check 'Results-js folder' for output")
    
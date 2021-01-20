import os
import requests
import sys
import re 
import argparse
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from datetime import datetime


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

# NOTE: This script can't crawl a javascript generated website...
# WE NEED TO MAKE THIS SCRIPT JAVASCRIPT COMPACTIBLE USING SELENIUM IN HEADLESS MODE... 3/1/21

# TEST DATA: https://www.nairaland.com/5705359/food-stuff-exportation-business
# TEST DATA: https://www.finelib.com/cities/asaba/business
# Seems the above along with facebook is restricting us... Consider using selenium in headless mode...

phone = r'(\+|\d)((\-|\d|\s)+){9,12}'

email = r'[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)'

results = './Results'


def getData(link):
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    try:
        raw_data = session.get(link, headers=headers)
    except requests.exceptions.InvalidURL:
        print('The URL is Invalid... ')
        sys.exit()

    except requests.exceptions.ConnectionError:
        print('Your internet connection is down or the URL is Bad!')
        sys.exit()

    except requests.exceptions.MissingSchema:
        print("Please prepend with 'https://' or 'http://' ")
        sys.exit()
    else:
        return BeautifulSoup(raw_data.text, 'html.parser')

        
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
            f.write(f'{typ} Data\n')
            for item in data:
                f.write(f'{item}\n')


def main():
    # options needed... link to website...
    # save result to text file...
    parser = argparse.ArgumentParser(description='...Email and Phone Number Extractor...')
    parser.add_argument('webLink', help='Input the website link you\'d like to crawl...', metavar='W')
    parsed_link = parser.parse_args().webLink
    data = getData(parsed_link)
    phone_data = extract(data, phone)
    email_data = extract(data, email)
    processData(phone_data, parsed_link, 'Phone')
    processData(email_data, parsed_link, 'Email')
    # print(f'Phone Data: {phone_data}')
    # print(f'Email Data: {email_data}')
if __name__ == '__main__':
    main()
    print('*****======== Done Scraping! ========*****')
    print("\n Please Check 'Results folder' for output")
    
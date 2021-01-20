from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import requests
import re 
import time
import selenium
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
    GUI that extracts email and phone numbers from websites...
'''

# NOTE: Selinium source code was editted (common/service.py) to disable console creation from webdriver...

# NOTE: We changed it back after creating the executable version...

# TEST DATA: https://www.nairaland.com/5705359/food-stuff-exportation-business


phone = r'(\+|\d)((\-|\d|\s)+){9,12}'

email = r'[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)'

results = './Results-GUI'

def print_output(val):
    result_text.delete('1.0', END)
    result_text.insert(END, val)

def clear_output():
    result_text.delete('1.0', END)
    window.title('Data Crawler')

def open_file():
    file_name = askopenfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')],
        initialdir=results
    )
    if not file_name:
        return
    with open(file_name, 'r') as file_obj:
        result = file_obj.read()
        print_output(result)
    window.title(f'Data Crawler -- {file_name}')
    

def getDataJs(link):
    chrome_option = Options()
    chrome_option.add_argument("--headless")
    driver = webdriver.Chrome('./chromedriver.exe', options=chrome_option)
    try:
        driver.get(link)
        # To allow the javascript on the website load completely...
        time.sleep(3)
    except selenium.common.exceptions.InvalidArgumentException:
        print_output("The URL is Invalid... Please try prepend with 'https://' or 'http://' ")
    except selenium.common.exceptions.WebDriverException:
        print_output("Your internet connection is down or the URL is Bad!")
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
    website_link = ent_website.get()
    ent_website.delete(0, END)
    data = getDataJs(website_link)
    if data:
        phone_data = extract(data, phone)
        email_data = extract(data, email)
        processData(phone_data, website_link, 'Phone')
        processData(email_data, website_link, 'Email')
        print_output("*****======== Done Scraping! ========*****\n Click on View or Check  'Results-GUI folder' for output....")
    

window = Tk()

window.rowconfigure([0, 1, 2],  weight=1)
window.columnconfigure(0, weight=1)

window.title('Data Crawler')
window.iconbitmap('snake.ico')
frm_website = Frame(master=window)
lbl_website = Label(master=frm_website, text='Website: ', font=10)
ent_website = Entry(master=frm_website, width=80)

lbl_website.grid(row=0, column=0, sticky='e')
ent_website.grid(row=0, column=1, sticky='w', padx=20)

result_text = Text(master=window)

frm_btn = Frame(master=window)

btn_view = Button(master=frm_btn, text='View', command=open_file)
btn_clear = Button(master=frm_btn, text='Clear', command=clear_output)
btn_crawl = Button(master=frm_btn, text='CRAWL', fg='red', width=20, command=main)

btn_view.grid(row=0, column=0, sticky='e', padx=50)
btn_crawl.grid(row=0, column=1, padx=50)
btn_clear.grid(row=0, column=2, sticky='w', padx=50)



frm_website.grid(row=0, column=0, padx=20, pady=10, sticky='ew')
result_text.grid(row=1, column=0, padx=20, pady=10, sticky='nsew')
frm_btn.grid(row=2, column=0, padx=20, pady=10)


window.mainloop()
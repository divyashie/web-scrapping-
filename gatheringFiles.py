"""
LIBRARY & PACKAGES
""" 
import urllib3, re, requests 
from bs4 import BeautifulSoup 
from csv import DictReader, DictWriter
import warnings 
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
import pathlib
import pandas as pd 

def web_scrape_data(): 
    read_url= "https://web.stanford.edu/~jurafsky/people.html" 
    html = urllib3.PoolManager()
    response = html.request('GET', read_url)
    soup = BeautifulSoup(response.data)
    return soup
    
def scrape_students(soup):
    dict_students = {}
    text = []
    for tag in soup.find_all(re.compile("h3")): 
        header= str(tag.get_text()) 
        for ul in soup.select('ul'): 
            text.append(ul.text) 
        dict_students.__setitem__(header, text)
    return dict_students 

def output_file(dict_students): 
    with open ("output.txt", "w") as f: 
        for k, v in dict_students.items(): 
            f.write(k)
            f.writelines(v)
    f.close()
"""
MAIN FUNCTION 
"""

soup = web_scrape_data()
scraped = scrape_students(soup)
output_file(scraped)


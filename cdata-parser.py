import requests
from bs4 import BeautifulSoup
import csv
import os


LINK = 'http://www.nbg.ge/rss.php'

r = requests.get(LINK)
xml_str = r.text
xml_str = xml_str.replace('<![CDATA', '').split('[')[1].split(']')[0]

soup = BeautifulSoup(xml_str, 'html.parser')


dict_data = {x.find_all('td')[0].get_text().strip()\
             :float(x.find_all('td')[2].get_text().strip())\
             for x in soup.find_all('tr')}


FILE = 'currency_file01.csv'
if FILE in os.listdir():
    with open(FILE, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dict_data.keys())
        writer.writerow(dict_data)
else:
    with open(FILE, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dict_data.keys())
        writer.writeheader()
        writer.writerow(dict_data)    



































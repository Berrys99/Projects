""""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Tomáš Beránek
email: tomas.malehorky@seznam.cz
discord: Tomáš B. Berrys#6258
"""

from bs4 import BeautifulSoup as BS
import requests
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url', help= 'copy your chosen url')
parser.add_argument('file_name', help = 'file name')

args = parser.parse_args()

url = args.url
file_path = args.file_name

def arguments_check(first_agr, second_arg):
    """
    Checking if the arguments are right as well as their positinion.
    """
    if 'https://www.volby.cz/pls/ps2017nss/' not in first_agr:
        return 'Wrong url, please check your url.'
    if '.csv' not in second_arg:
        return 'You may have forgot to type ".csv" at the end of the name of the file'
    else:
        return None

def url_creator(links):
    """
    Creating urls from referal link to acces sub sites.
    """
    for link in links:
        urls.append('https://www.volby.cz/pls/ps2017nss/' + link)
    
def url_opener(url):
    """
    Openning urls to acces informations.
    """
    informations = requests.get(url).text
    return informations

def link_cleaner(html_soup):
    """
    Getting all the referal links from the main site.
    """
    for link_soup in html_soup.find_all(class_ = 'cislo'):
        for clean_link in link_soup:
            clean_links.append(str(clean_link.get('href')))

def puling_information(html_soup,information_row):
    """
    Getting informations about electorates.
    """
    sa2 = html_soup.find(['td'], headers = 'sa2')
    information_row.append(sa2.string)
    sa3 = html_soup.find(['td'], headers = 'sa3')
    information_row.append(sa3.string)
    sa6 = html_soup.find(['td'], headers = 'sa6')
    information_row.append(sa6.string)

def first_tabble_vote_counter(html_soup,information_row):
    """
    Getting information about votes for the parties, from the first table.
    """
    for a in html_soup.find_all(['td'], headers = 't1sb3'):
        information_row.append(a.string)
        
def second_tabble_vote_counter(html_soup,information_row):
    """
    Getting information about votes for the parties, from the second table.
    """
    for a in html_soup.find_all(['td'], headers = 't2sb3'):
        information_row.append(a.string)                   

error_in_attempt = arguments_check(args.url,args.file_name)

if error_in_attempt is not None:
    exit(error_in_attempt)

print('Downloading data from chosen url: ' + url)

result = requests.get(url).text
main_site_html = BS(result, 'html.parser')

clean_links = list()
urls = list()

first_row = ['code','location','registered','envelops','valid',]

link_cleaner(main_site_html)

url_creator(clean_links)

first_sub_site = BS(url_opener(urls[0]), 'html.parser')
political_parties = list(first_sub_site.find_all('td',class_ = 'overflow_name'))
codes = list(main_site_html.find_all('td',class_ = 'cislo'))
township_names = list(main_site_html.find_all('td',class_ = 'overflow_name'))

for partie_name in political_parties:
    first_row.append(partie_name.string)

with open(file_path, 'w') as file:
        writer = csv.writer(file, delimiter = ',')
        writer.writerow(first_row)

one_row = list()
index = 0

print('writing data to the file: ' + file_path)

for writing_informations in range(len(clean_links)):
    one_row.append(codes[index].string)
    one_row.append(township_names[index].string)

    sub_site = BS(url_opener(urls[index]), 'html.parser')
    puling_information(sub_site,one_row)
    first_tabble_vote_counter(sub_site,one_row)
    second_tabble_vote_counter(sub_site,one_row)

    with open(file_path, 'r+') as file:
        file.seek(0,2)
        writer = csv.writer(file, delimiter = '\t')
        writer.writerow(one_row)

    one_row.clear()
    index += 1

print('Proces completed')
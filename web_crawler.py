import requests
from pprint import pprint
from bs4 import BeautifulSoup


def site_map(link):
    """ Return dictionary of links from http site in following format:
        {
        'link1':
            {
            'title': '<title_of_link1>',
            'links':{'sub_link1','sub_link2'},
            },
        'link2':
            {
            'title': '<title_of_link2>',
            'links':{'sub_link1','sub_link2'},
            },
        }
    """
    
    r = requests.get(link)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    parsed_data = {link:{
            'title':soup.title.text,
             'links':set()}}


    for tag_a in soup.find_all('a'):
        sub_link = tag_a.get('href')

        if sub_link.startswith(link):
            parsed_data[link]['links'].add(sub_link)
        elif sub_link.startswith('/'):
            parsed_data[link]['links'].add(link + sub_link)
        elif sub_link.startswith('#'):
            continue
        else:
            parsed_data[link]['links'].add(sub_link)

    pprint(parsed_data)



if __name__ == '__main__':
    site_map('http://malovanka.pl')

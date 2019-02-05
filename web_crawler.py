import requests
from bs4 import BeautifulSoup


def site_map(link):
    """ Return dictionary of links from http site in following format:
        {'link1':{
            'title': '<title_of_link1>',
            'links':{'sub_link1','sub_link2'},
         'link2':{
            'title': '<title_of_link2>',
            'links':{'sub_link1','sub_link2'}}
    """
    r = requests.get(link)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')

if __name__ == '__main__':
    site_map('http://localhost:8000')

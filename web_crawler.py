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
    # Preparing variables for use
    parsed_data = {}
    queue = [link]
    history = set()

    # system of queueing
    while queue:
        current_link = queue[0]

        # Make sure if it has not been parsed
        if current_link in history:
            del queue[0]
            continue
        history.add(current_link)


        # html parsing
        r = requests.get(current_link)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')

        # add dict entry
        parsed_data[current_link] = {
                'title':soup.title.text,
                'links':set()}

        # parsing sublinks
        for tag_a in soup.find_all('a'):
            sub_link = tag_a.get('href')

            # Correct link1
            if sub_link.startswith(link):
                parsed_data[current_link]['links'].add(sub_link)
                if sub_link not in queue:
                    queue.append(sub_link)
            # Relative link
            elif sub_link.startswith('/'):
                parsed_data[current_link]['links'].add(link + sub_link)
                if sub_link not in queue:
                    queue.append(link + sub_link)
            # Anchored link
            elif sub_link.startswith('#'):
                continue
            # Alien link
            else:
                parsed_data[current_link]['links'].add(sub_link)
        del queue[0]


if __name__ == '__main__':
    site_map('http://malovanka.pl/')

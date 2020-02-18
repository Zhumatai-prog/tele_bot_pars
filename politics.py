import requests
import csv
from bs4 import BeautifulSoup

new_list = []
def get_html(url):
    r = requests.get(url)
    return r.text

def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', class_='list').find_all('div', class_='elem')
    links = []
    for a in divs:
        try:
            link = a.find('a').get('href')
            print(link)
            
        except:
            link = a.find('a', class_='title').get('href')
        links.append(link)
    return links

def write_csv(data):
    with open('politics.csv', 'w') as file:
        writer = csv.writer(file)
        for i in data:
            writer.writerow(i.split(','))

def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    ads = soup.find('div', class_='news_in')
    try:
        title = ads.find('h1').text
    except:
        title = ''

    return title

def main():
    url = 'https://kg.akipress.org/page:1/cat:1/'
    all_links = get_all_links(get_html(url))
    for i in range(21):
        html = get_html(all_links[i])
        data = get_page_data(html)
        new_list.append(data)
        new_list.append(all_links[i])

    write_csv(new_list)

if __name__ == '__main__':
    main()
from bs4 import BeautifulSoup
import argparse
import json
import logging
import os
import requests
import sys
import urllib.parse


def save_page(title):
    error = 1
    url = 'https://en.wikipedia.org/wiki/'+title
    r = requests.get(url)
    if r.status_code == 200:
        f = open("temp.html", 'w')
        f.write(r.text)
        f.close()
        logging.info(url)

    else:
        message = "Error opening page" + url
        logging.error(message)
        error = 0
    return error


def parse_page(link_count):
    wiki_links = []
    with open("temp.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    article = soup.find('div', id='mw-content-text')
    links = article.find_all('a')
    for link in links:
        if link.has_attr('href'):
            dec_link = urllib.parse.unquote(link['href'][6:].replace("_", " ")).split('#')[0]
            if (link['href'][:5] == '/wiki') and (link['href'].find(":") == -1) and (dec_link not in wiki_links):
                wiki_links += [dec_link]
        if len(wiki_links) >= max_link - link_count - 1:
            break
    if os.path.exists("temp.html"):
        os.remove("temp.html")
    return wiki_links


logging.basicConfig(level=logging.INFO)
max_link = 1000
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--page", type=str, required=True, help="First page title")
parser.add_argument("-d", "--deep", default=3, type=int, help="Parsing deep")
args = parser.parse_args()
deep = args.deep
query = urllib.parse.quote(args.page.replace(" ", "_"))
deep_link = []
graph = {}
if save_page(query):
    i = 0
    titles = parse_page(0)
    graph[args.page] = titles
    titles_count = len(titles)
    link_count = titles_count
    while (i < deep) and (link_count < max_link - 1):
        for title in titles:
            if save_page(title):
                parse_links = parse_page(link_count)
                deep_link += parse_links
                graph[title] = parse_links
            link_count = len(deep_link) + titles_count
            if link_count >= max_link - 1:
                break
        print("Link count ", link_count+1)
        titles = parse_links
        i += 1
    with open("graph.json", "w") as fo:
        json.dump(graph, fo, indent=4)
        os.environ['WIKI_FILE'] = 'graph.json'

else:
    message = "Error opening page"
    sys.exit(message)

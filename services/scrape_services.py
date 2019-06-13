import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
http = httplib2.Http()

def getXMLLinks(url):
    status, response = http.request(url, headers=headers)
    xml_list = []
    print(status['status'])
    if status['status'] == '200':
        for link in BeautifulSoup(response, 'html.parser', parseOnlyThese=SoupStrainer('a')):
            if link.has_attr('href') and '.xml' in link['href']:
                xml_list.append('https://www.bluetooth.com' + link['href'])
        return xml_list
    return []


def parseLinkName(link):
    name = link.split('service.')[1]
    if '.xml' not in name:
        return name
    return name.split('.xml')[0]

def downloadLinks(link):
    URL = link
    status, response = http.request(URL, headers=headers)
    if status['status'] == '200':
        name = parseLinkName(link)
        with open(name + '.xml', 'wb') as file:
            file.write(response)
    return


def main():
    links = getXMLLinks('https://www.bluetooth.com/specifications/gatt/services/')
    for link in links:
        downloadLinks(link)


if __name__ == "__main__":
    main()
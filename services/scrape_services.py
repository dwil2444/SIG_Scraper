from selenium import webdriver
import httplib2

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
http = httplib2.Http()
option = webdriver.ChromeOptions()
option.add_argument("--incognito")


def parseLinkName(link):
    name = link.split('service.')[1]
    if '.xml' not in name:
        return name
    return name.split('.xml')[0]


def downloadLinks(link):
    print(link)
    status, response = http.request(link, headers=headers)
    if status['status'] == '200':
        name = parseLinkName(link)
        with open(name + '.xml', 'wb') as file:
            file.write(response)
    return


def openBrowser():
    browser = webdriver.Chrome(executable_path='../chromedriver', chrome_options=option)
    browser.get("https://bluetooth.com/specifications/gatt/services/")
    try:
        list_links = browser.find_elements_by_tag_name('a')
        for link in list_links:
            val = link.get_attribute('href')
            if('xml' in val):
                downloadLinks(val)
        browser.quit()

    except:
        print('Error')


def main():
    openBrowser()


if __name__ == "__main__":
    main()
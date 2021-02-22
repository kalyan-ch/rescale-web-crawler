import requests

def getUrls(siteUrl):
    urls = []

    page = requests.get(siteUrl)
    print(page.content)
    return urls

if __name__ == '__main__':
    print(getUrls("https://www.rescale.com"))


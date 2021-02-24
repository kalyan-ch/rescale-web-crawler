import requests, sys
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool as Pool

def getUrls(siteUrl):


    page = requests.get(siteUrl)
    soup = BeautifulSoup(page.text, 'html.parser')

    urls = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if (url is not None) and ("http" in url):
            urls.append(url)


    urls = set(urls)

    print(siteUrl)
    for url in urls:
        print(" ", url)

    return urls

if __name__ == '__main__':
    siteUrl = sys.argv[1]
    urls = []
    
    pool_size = 5
    pool = Pool(pool_size)

    urls.append(siteUrl)

    i = 0
    while len(urls) != 0:
        newurls = pool.apple_async(getUrls, (urls[i], ))
        urls.extend(newurls)
        i += 1 

    pool.close()
    pool.join()


import time
import requests

def download_site(url, session):
    with session.get(url) as response:
        print(f'Downloaded {len(response.content)} from {url}')

def download_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            download_site(url, session)

if __name__ == '__main__':
    urls = ['https://www.cs.usfca.edu', 'https://git-scm.com', 'https://ru.wikipedia.org'] * 30
    start_time = time.time()
    download_all_sites(urls)
    download_time = time.time() - start_time
    print(f'Downloaded {len(urls)} pages for {download_time} seconds')

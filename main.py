import sys
import re
from urllib.parse import urlparse
from pprint import pprint
import asyncio
import aiohttp
import traceback

paths_reg = r"\"\/[^\/][^\"\>\<]+\""
file_links_reg = r"\"https?:\/\/[^\"\.]+\.[a-b]+\""
host_links_reg

async def get_host_link(url, session):
    async with session.get(url) as response:
        html = await response.text()
        return re.findall(host_links_reg, html)

async def crawl(url, session):
    async with session.get(url) as response:
        html = await response.text()
        # differents paths 
        host_links = re.findall(host_links_reg, html)
        # links to files
        file_links = re.findall(file_links_reg, html)
        # possibles paths of host
        paths = re.findall(paths_reg, html)

        tasks = []
        for file_link in file_links:
            tasks.append(get_host_link(file_link, session))
        host_links = host_links + [item for sublist in await asyncio.gather(*tasks, return_exceptions=True) for item in sublist]

        tasks = []
        for host_link in host_links:
            tasks.append(crawl(host_link, session))
        res = await asyncio.gather(*tasks, return_exceptions=True)
        [host_links, paths] = [set(host_links) | set([a for [a,_] in res]), set(paths) | set([b for [_,b] in res])]
        # possible path for same host, to be tested

        return [list(host_links), list(paths)]

async def get_paths(url):
    async with aiohttp.SessionClient() as session:
        await crawl(url, session)

def main():
    if len(sys.argv) == 1:
        print("supply of a website url is mandatory")
        sys.exit(1)
    url = sys.argv[1]

    global host_links_reg
    host_links_reg = rf"\"https?:\/\/{urlparse(url).netloc}[^\"]+\""
    event_loop = asyncio.get_event_loop()

    try:
        with aiohttp.ClientSession() as session:
            [links, possible_links] = event_loop.run_until_complete(crawl(url, session))
            pprint(links, possible_links)
    except Exception as e:
        print(f"crawler failed :")
        traceback.print_exc()
    finally:
        event_loop.close()

if __name__ == "__main__":
    main()
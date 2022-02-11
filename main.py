import sys
import json
import re
from urllib.parse import urlparse
import asyncio
import aiohttp
import traceback
from http import HTTPStatus 

paths_reg = r"\"\/[^\"\>\<\.]+(?:\.js|\.json)?\""
is_good_url = r"https?://[a-zA-Z0-9.-:]+/"
requested_url = set([])

def clean_arr_string(arr):
    return [string.replace("\"", "") for string in arr]

def already_visited(url):
    if url in requested_url:
        return True
    requested_url.add(url)
    return False

async def crawl(url, session):
    async with session.get(url, headers=headers) as response:
        if response.status != HTTPStatus.OK:
            return []
        html = await response.text()
        # differents paths 
        host_links = clean_arr_string(re.findall(host_links_reg, html))
        # possibles paths of host
        paths = clean_arr_string(re.findall(paths_reg, html))

        possibles_urls = host_links + [basic_url + path[1:] for path in paths]

        tasks = []
        for possible_url in possibles_urls:
            if not already_visited(possible_url):
                tasks.append(crawl(possible_url, session))

        gather_res = await asyncio.gather(*tasks, return_exceptions=True)
        res = [item for sublist in gather_res if type(sublist) == list for item in sublist]
        res.append(url)

        return res

async def main(url):
    if not re.match(is_good_url, url):
        raise Exception(f"bad format url, should be {is_good_url}")
    netloc = urlparse(url).netloc

    global basic_url, host_links_reg, headers
    host_links_reg, basic_url = rf"\"https?:\/\/{netloc}[^\"\.]+(?:\.json|\.js)?\"", url
    with open("custom_headers.py", "r") as file:
        headers = json.loads(file.readlines())

    async with aiohttp.ClientSession() as session:
        res = await crawl(url, session)
        with open(f"{netloc}.txt", "w") as file:
            file.write("\n".join(res))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("command should look like:")
        print("python3 main.py <url>")
        sys.exit(1)
    url = sys.argv[1]

    event_loop = asyncio.new_event_loop()
    try:
        event_loop.run_until_complete(main(url))
    except Exception:
        print(f"R2D2 failed :")
        traceback.print_exc()

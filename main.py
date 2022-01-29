import sys
import requests
import re
from urllib.parse import urlparse
from pprint import pprint


paths_reg = r"\"\/[^\/][^\"\>\<]+\""
links_reg = r"\"https?:\/\/[^\"]+\""

def get_host_links_reg(host):
    return rf"\"https?:\/\/{host}[^\"]+\""

def get_non_host_links_reg(host):
    return rf"\"https?:\/\/[^{host}][^\"]+\""

def main(url):
    response = requests.get(url)
    host = urlparse(url).netloc
    host_links_reg = get_host_links_reg(host)
    non_host_links_reg = get_non_host_links_reg(host)
    # differents links for same host
    host_links = re.findall(host_links_reg, response.text)
    # every other links
    non_host_links = re.findall(non_host_links_reg, response.text)
    # possible path for same host, to be tested
    paths = re.findall(paths_reg, response.text)
    
    # routes = crawl(links, reg)
    # with open(f"{parsed_url}.json", "w") as file:
    #     file.write
    # return

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("supply of a website url is mandatory")
        sys.exit(1)
    main(sys.argv[1])
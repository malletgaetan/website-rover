from http import HTTPStatus
import asyncio
import sys
import aiohttp

async def get_print(session, url, index):
    async with session.get(url) as response:
        return response.status

async def main(url, nb_requests):
    async with aiohttp.ClientSession() as session:
        task = []
        for i in range(nb_requests):
            task.append(get_print(session, url, i))
        status = await asyncio.gather(*task)
        for code in status:
            if code == HTTPStatus.TOO_MANY_REQUESTS:
                print("The requested website is rate limiting")
                return
            if code != HTTPStatus.OK:
                print(f"Received a non OK status {code}")
                return
        print("Website isn't rate limiting, don't bother use proxies :p")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("command should be used as:")
        print("python3 rate_limit_tester.py <url> <nb_request>")
        sys.exit(1)
    url = sys.argv[1]
    nb_requests = int(sys.argv[2])
    event_loop = asyncio.new_event_loop()
    event_loop.run_until_complete(main(url, nb_requests))

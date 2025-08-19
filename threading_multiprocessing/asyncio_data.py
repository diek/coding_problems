import asyncio
import time

import aiohttp

urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://httpbin.org/delay/2",  # Simulates a 2-second delay
]


async def fetch(session, url):
    print(f"Fetching {url}")
    async with session.get(url) as response:
        content = await response.text()
        print(f"Finished {url} (status: {response.status})")
        return content[:100]  # return first 100 chars


async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    duration = time.time() - start
    print(f"\nDownloaded {len(urls)} sites in {duration:.2f} seconds.")
    print("\nSample output:")
    for i, content in enumerate(results, 1):
        print(f"\nSite {i} preview:\n{content}\n")


asyncio.run(main())

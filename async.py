#!/usr/bin/env python3
from aiohttp import ClientSession
import asyncio
import time



async def download_site(session: ClientSession, url: str):
    async with session.get(url) as response:
        l = await response.text()
        print(f'Read {len(l)} from {url}')


async def download_all_sites(sites):
    async with ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(download_site(session, url))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    sites = ['https://www.cs.usfca.edu', 'https://git-scm.com', 'https://ru.wikipedia.org'] * 30
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
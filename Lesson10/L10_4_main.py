import aiohttp
import asyncio

async def get_text(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return text
        
async def tasks(urls):
    task = []
    for url in urls:
        task.append(asyncio.create_task(get_text(url)))
    text = await asyncio.gather(*task)
    return text

async def create_urls():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3',
        'https://jsonplaceholder.typicode.com/posts/4'
    ]
    text = await tasks(urls)
    length = 0
    for page in text:
        length += len(str(page))
    print(length)

asyncio.run(create_urls())

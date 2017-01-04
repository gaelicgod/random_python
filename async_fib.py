import asyncio

async def fib(nums):
    if nums < 2:
        return 1
    else:
        return await fib(nums-1) + await fib(nums-2)

async def main():
    for num in range(30):
        print(await fib(num))

def async():
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(main())

if __name__ == '__main__':
    async()

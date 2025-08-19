import asyncio


async def async_task(name):
    print(f"{name} started")
    await asyncio.sleep(2)  # Non-blocking wait
    print(f"{name} finished")


async def main():
    await asyncio.gather(async_task("Async-1"), async_task("Async-2"))
    print("AsyncIO example done.")


asyncio.run(main())

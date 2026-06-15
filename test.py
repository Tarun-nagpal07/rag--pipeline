from src.tools.retriver_tool import retrieve_from_doc

async def main():
    result = await retrieve_from_doc("Hello")
    print(result)



import asyncio

asyncio.run(main())
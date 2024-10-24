import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/fetch-data")
async def fetch_data():
    async with httpx.AsyncClient() as client:
        response1 = await client.get("https://api1.example.com/data")
        response2 = await client.get("https://api2.example.com/data")
        return await asyncio.gather(response1.json(), response2.json())
    
@app.get("/fetch-data")
async def fetch_data2():
    return await some_other_process()

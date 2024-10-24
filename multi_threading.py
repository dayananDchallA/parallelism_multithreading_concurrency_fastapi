import asyncio
from fastapi import FastAPI, uploadfile
import time

app = FastAPI()

def process_file(file):
    time.sleep(5)
    return file_data.upper()

async  def upload(file: uploadfile):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, process_file, await file.read())
    return {"processed content": result}
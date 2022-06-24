from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import redis
import httpx

from helpers_.dropbox import dropbox_upload_file, dropbox_download_file

app = FastAPI()

r = redis.Redis(host='redis_integration', port='6380', db=0, charset='utf-8', decode_responses=True)


@app.put('/upload_file/{key}')
async def upload_file(key: str, file: UploadFile = File(...)):
    local_path = f'temp_/{file.filename}'
    r.set(key, file.filename)
    dropbox_upload_file(await file.read(), file.filename)
    async with httpx.AsyncClient() as client:
        await client.get(url=f'http://0.0.0.0:8080/download_file/{key}')
    return FileResponse(local_path)


@app.get('/download_file/{key}')
async def download_file(key: str):
    file_name = r.get(key)
    if not file_name:
        return {'message': 'Have not file with that name'}
    local_path = dropbox_download_file(file_name)
    return FileResponse(local_path)

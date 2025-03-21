from fastapi import FastAPI
from pydantic import BaseModel
import requests,json,asyncio


app = FastAPI()

# class TrelloUpdateUrl(BaseModel):
@app.get("/url")
async def getUrl():
  id = "TrelloID"
  url = "https://trello.com/b/EyVgS1IC/api-prueba/boards/cards"

  query = {
  'key': 'APIKey',
  'token': 'APIToken'
  }

  headers = {
  "Accept": "application/json"
  } 

  response = requests.request(
   "get",
    url,
    headers=headers,
    params=query
  )
  await response

asyncio.run(getUrl())

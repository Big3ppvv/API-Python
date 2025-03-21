import requests,asyncio
from flask import Flask
def main():
  app = Flask(__name__)

  @app.route('/getURL')
  def getURL():
      id = "TrelloID"
      url = f"https://trello.com/b/EyVgS1IC/api-prueba/1/{id}/boards/cards"

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
      return "Hello World"

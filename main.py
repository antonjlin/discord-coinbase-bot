import time
from datetime import datetime
import requests
import json
delay = 60 #seconds
discordWebhook = 'MY_WEBHOOK'
def getPrice(currency):
    priceUrl = 'https://api.coinbase.com/v2/prices/{}-USD/spot'.format(currency)
    r = requests.get(priceUrl)
    r = json.loads(r.text)
    return r['data']['amount']
while True:
    btc = getPrice('BTC')
    eth = getPrice('ETH')
    ltc = getPrice('LTC')
    bch = getPrice('BCH')
    timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
    embeds = [{
        'type': 'rich',
        "title": "Crypto Prices",
        "url": "https://coinbase.com",
        "color": 2149376,
        "timestamp": timestamp,
        "fields": [
          {
            "name": "BTC:",
            "value": '$' + str(btc),
            "inline": True
          },
          {
            "name": "ETH:",
            "value": '$' + str(eth),
            "inline": True

          },
          {
            "name": "LTC:",
            "value": '$' + str(ltc),
            "inline": True
          },
            {
              "name": "BCH:",
              "value": '$' + str(bch),
              "inline": True
            }
          ]
        }]
    payload = {"embeds": embeds}
    r = requests.post(discordWebhook,json=payload)
    print(timestamp) #print to console to make sure program isnt frozen
    time.sleep(delay)

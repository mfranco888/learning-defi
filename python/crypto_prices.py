import requests
import pandas as pd
from datetime import datetime

coins = ["bitcoin", "sui", "chainlink"]

response = requests.get(
    "https://api.coingecko.com/api/v3/simple/price?ids="
    + ",".join(coins)
    + "&vs_currencies=usd"
)
data = response.json()

rows = []
for coin in coins:
    rows.append(
        {"coin": coin, "price_usd": data[coin]["usd"], "timestamp": datetime.now()}
    )
df = pd.DataFrame(rows)

df.to_csv("crypto_prices.csv", index=False)

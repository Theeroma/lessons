import schedule, requests, time
def hello_world():
    print("Hello World")

def get_btc_price():
    url = 'https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT'
    response = requests.get(url).json()
    price = round(float(response['price']))
    print("Текущая цена биткоина;",  price, "$")

# schedule.every(3).seconds.do(hello_world)
# # schedule.every().day.at("18:26").do(hello_world)
# # schedule.every().monday.at("18:30").do(hello_world)
# schedule.every().minute.at(':34').do(hello_world)
schedule.every(59).seconds.do(get_btc_price)

while True:
    schedule.run_pending()


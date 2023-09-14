import schedule
import time
import requests

def perform_request(url):
    try:
        response = requests.get(url).json()
        price = round(float(response['price']), 2)
        
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Текущая цена биткоина: {price} $\n")

    except requests.exceptions.RequestException as e:
        with open('log.txt', 'a') as log_file:
            log_file.write(f'Ошибка при выполнении запроса: {e}\n')
        
    except Exception as e:
        with open('log.txt', 'a') as log_file:
            log_file.write(f'Неожиданная ошибка: {e}\n')

def main():
    url = 'https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT'
    
    schedule.every(3).seconds.do(perform_request, url) 
    while True:
        schedule.run_pending()
        time.sleep(1)

main()

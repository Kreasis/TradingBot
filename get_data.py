import config, csv
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

client = Client(config.API_KEY, config.API_SECRET)

#prices = client.get_all_tickers()

#for price in prices:
    #print(price)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('daily.csv', "w",newline='')

candlestick_writer = csv.writer(csvfile, delimiter=',',)

#for candlestick in candles:
 #   print(candlestick)

  #  candlestick_writer.writerow(candlestick)

#print(len(candles))

candlesticks  = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "10 Jan, 2022", "30 Sep, 2022")

for candlestick in candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()
from __future__ import print_function
import json
import requests
import matplotlib.pyplot as plt

'''
Every cut contains:time, buy price, sell price, lowest price, highest price and trade volume
A k_line is a list of cut in sequence.
'''


class KLineCut:
    def __init__(self, raw_cut):
        self.time = raw_cut[0]
        self.buy = raw_cut[1]
        self.sell = raw_cut[2]
        self.low = raw_cut[3]
        self.high = raw_cut[4]
        self.vol = raw_cut[5]

    def __str__(self):
        string = ''
        string += 'Time at:' + str(self.time) + '\n'
        string += 'Buy Price:' + str(self.buy) + '\n'
        string += 'Sell Price:' + str(self.sell) + '\n'
        string += 'Low:' + str(self.low) + '\n'
        string += 'High:' + str(self.high) + '\n'
        string += 'Trade Volume:' + str(self.vol)
        return string

    def get_time(self):
        return self.time

    def get_buy_price(self):
        return self.buy

    def get_sell_price(self):
        return self.sell

    def get_low(self):
        return self.low

    def get_high(self):
        return self.high

    def get_trade_volume(self):
        return self.vol


# return the k line of the specific market.
# for available markets run markets.py
# @limit: Limit the number of returned data points, default to 1000.
# @period: Time period of K line, default to 1.
# You can choose between 1, 5, 15, 30, 60, 120, 240, 360, 720, 1440, 4320, 10080

def get_k_line(market, period=360, limit=1000, log=False):
    url = 'https://yunbi.com//api/v2/k.json?market=' + market \
          + '&limit=' + str(limit) \
          + '&period=' + str(period)
    if log:
        print('API url:' + url)
    html = requests.get(url)
    raw_json = html.text
    json_object = json.loads(raw_json)
    k_line = []
    for i in json_object:
        k_line.append(KLineCut(i))
    return k_line


def plot_k_line(k_line):
    time = []
    sell = []
    for i in k_line:
        time.append(i.get_time())
        sell.append(i.get_sell_price())
    plt.plot(time, sell)
    plt.show()


if __name__ == '__main__':
    print(get_k_line('btccny')[0])

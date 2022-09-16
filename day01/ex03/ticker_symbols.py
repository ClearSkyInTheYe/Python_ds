import sys

def data(str):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }
    if str not in STOCKS.keys():
        print("Unknown ticker")
        return
    inv_COMPANIES = {value: key for key, value in COMPANIES.items()}
    print(inv_COMPANIES[str], STOCKS[str])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        data(sys.argv[1].upper())

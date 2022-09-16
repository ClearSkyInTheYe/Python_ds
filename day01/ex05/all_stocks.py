import sys

def search_by_value_or_by_key(argv):
    list_of_companies = argv.split(",")
    for n in range(len(list_of_companies)):
        list_of_companies[n] = list_of_companies[n].strip()
    original_list = argv.split(",")
    for n in range(len(original_list)):
        original_list[n] = original_list[n].strip()
    for n in range(len(original_list)):
        if len(original_list[n]) == 0:
            return
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
    for n in range(len(list_of_companies)):
        flag = 0
        list_of_companies[n] = list_of_companies[n].lower()
        list_of_companies[n] = list_of_companies[n].title()
        original = list_of_companies[n]
        if list_of_companies[n] in COMPANIES:
            print(list_of_companies[n], "stock price is", STOCKS[COMPANIES[list_of_companies[n]]])
            flag = 1
        list_of_companies[n] = list_of_companies[n].upper()

        if list_of_companies[n] in STOCKS:
            inv_COMPANIES = {value: key for key, value in COMPANIES.items()}
            print(list_of_companies[n], " is a ticker symbol for ", inv_COMPANIES[list_of_companies[n]])
            flag = 1
        if flag == 0:
            print(original_list[n], "is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        search_by_value_or_by_key(sys.argv[1])


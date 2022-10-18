import sys

def ticker_symbols():
    companies = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }
    stocks = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    arg = sys.argv[1].lower()

    def in_dict(company, stock, arg):
        for key, value in company.items():
            if value.lower() == arg.lower():
                print(key, stock[value])
                return True

    if not in_dict(companies, stocks, arg):
            print("Unknown ticker")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        ticker_symbols()

import sys

def data():
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
    return COMPANIES, STOCKS

def all_stocks(arg):
    COMPANIES, STOCKS = data()
    # arg = sys.argv[1]
    line = arg.split(',')
    tmp = []
    for i in line:
        tmp.append(i.strip())
        if "" in tmp:
            return
    for i in tmp:
        if i.capitalize() in COMPANIES:
            v = COMPANIES[i.capitalize()]
            print(f"{i.capitalize()} stock price is {STOCKS[v]}")
        elif i.upper() in STOCKS:
            for key, value in COMPANIES.items():
                if value == i.upper():
                    print(f"{value} is a ticker symbol for {key}")
        else:
             print(f"{i} is an unknown company or an unknown ticker symbol")


def main():
	if len(sys.argv) == 2:
		all_stocks(sys.argv[1])

if __name__ == "__main__":
	main()



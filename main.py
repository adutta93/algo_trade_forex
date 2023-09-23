from api.oanda_api import OandaApi


def main():
    print("Fetching data...!!!")
    api = OandaApi()
    data = api.get_account_summary()
    # [print(x['name']) for x in data]
    print(data)


if __name__ == '__main__':
    main()

from api.oanda_api import OandaApi
from infra.instrument_collection import intruments_collection


def main():
    print("Fetching data...!!!")
    api = OandaApi()

    intruments_collection.create_instruments_file(
        api.get_instruments(), './data')
    intruments_collection.load_instruments("./data")
    intruments_collection.print_instruments()


if __name__ == '__main__':
    main()

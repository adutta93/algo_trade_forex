import pandas as pd
from api.oanda_api import OandaApi
from infra.instrument_collection import intruments_collection
from exploration.plotter import CandlePlot


def main():
    print("Fetching data...!!!")
    api = OandaApi()

    # intruments_collection.create_instruments_file(
    #     api.get_instruments(), './data')
    # intruments_collection.load_instruments("./data")
    # intruments_collection.print_instruments()

    # read data
    pair = "EUR_USD"
    granularity = "H4"
    df = pd.read_pickle(f"./data/{pair}_{granularity}.pkl")

    # getting 100 data for plot
    df_plot = df[:100]

    # CandlePlot

    cp = CandlePlot(df_plot)

    cp.show_plot()


if __name__ == '__main__':
    main()

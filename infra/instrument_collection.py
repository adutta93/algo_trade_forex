import json
from models.instrument import Instrument


class InstrumentCollection:
    file_name = "instruments.json"
    test_file_name = "test.json"  # testing purpose
    inst_keys = ['name', 'type', 'displayName', 'pipLocation',
                 'displayPrecision', 'tradeUnitsPrecision', 'marginRate']

    def __init__(self):
        self.instrument_dict = {}

# * Function to create the ./data/instruments.json file
    def create_instruments_file(self, data, path):
        if data is None:
            print("Failed creating instrument file")
            return

        instrument_dict = {}
        for item in data:
            key = item["name"]
            instrument_dict[key] = {k: item[k] for k in self.inst_keys}
        # !TODO: We can cached this data somewhere e.g Redis, Memecached etc
        file_name = f"{path}/{self.file_name}"  # testing purpose
        with open(file_name, "w") as f:
            f.write(json.dumps(instrument_dict, indent=2))

# * Function to load instruments from the ./data/instruments.json file
    def load_instruments(self, path):

        # !TODO: We can cached this data somewhere e.g Redis, Memecached etc
        self.instrument_dict = {}
        file_name = f"{path}/{self.file_name}"  # testing purpose
        # file_name = f"{path}/{self.file_name}"

        with open(file_name, "r") as f:
            data = json.loads(f.read())
            for key, val in data.items():
                self.instrument_dict[key] = Instrument.FromApiObject(val)

# * Function to print instruments
    def print_instruments(self):
        print("Printing instruments....!!")
        # [print(key, val) for key, val in self.instrument_dict.items()]
        print(len(self.instrument_dict.keys()), "instruments")


intruments_collection = InstrumentCollection()

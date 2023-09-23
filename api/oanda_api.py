import requests
import constant.defs as defs


class OandaApi:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {defs.api_key}",
            "Content-Type": "application/json"
        })

    def make_request(self, url, verb='get', code=200, params=None, data=None, headers=None):
        full_url = f"{defs.oanda_url_practice}/{url}"
        try:
            response = None
            if verb == 'get':
                response = self.session.get(
                    full_url, params=params, data=data, headers=headers)

            if response == None:
                return False, {'error': 'verb not found'}

            if response.status_code == code:
                return True, response.json()
            else:
                return False, response.json()

        except Exception as error:
            return False, {'Exception': error}

    def get_account_data(self, end_point, data_key_type):
        url = f"accounts/{defs.account_id}/{end_point}"
        ok, data = self.make_request(url)

        if ok == True and data_key_type in data:
            return data[data_key_type]
        else:
            print("ERROR: get_account_data()", data)
            return None

    def get_account_summary(self):
        return self.get_account_data("summary", "account")

    def get_instruments(self):
        return self.get_account_data("instruments", "instruments")

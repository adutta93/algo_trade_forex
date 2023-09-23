import requests
import constant.defs as defs


class OandaApi:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {defs.api_key}",
            "Content-Type": "application/json"
        })

    def make_request(self, url, verb='get', params=None, data=None, headers=None):
        full_url = f"{defs.oanda_url_practice}/{url}"
        try:
            return
        except:
            return

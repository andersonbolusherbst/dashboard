class IEXStock:
    def __init__(self, token, symbol):
        self.BASE_URL ='https://cloud.iexapis.com/stable'
        self.token = token
        self.symbol = symbol

    def get_logo(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/logo?token={self.token}"
        p = requests.get(url)
        
        return p.json()

    def get_company_info(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/company?token={self.token}"
        p = requests.get(url)
        
        return p.json()
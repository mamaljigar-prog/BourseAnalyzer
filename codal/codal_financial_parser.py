class CodalFinancial:

    def __init__(
        self,
        assets,
        equity
    ):
        self.assets = assets
        self.equity = equity


    def get_assets(self):
        return self.assets


    def get_equity(self):
        return self.equity


    def report(self):

        return {

            "assets": self.assets,

            "equity": self.equity

        }
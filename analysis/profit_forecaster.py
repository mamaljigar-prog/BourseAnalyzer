# analysis/profit_forecaster.py

from analysis.normalized_profit import NormalizedProfitCalculator


class ProfitForecaster:

    def __init__(self):

        self.normalizer = NormalizedProfitCalculator()


    def calculate_growth(self, current, previous):

        if previous is None or previous == 0:
            return 0

        return (current - previous) / previous



    def calculate_margin(self, profit, sales):

        if sales == 0:
            return 0

        return profit / sales



    def forecast_sales(self, current_sales, growth):

        return current_sales * (1 + growth)



    def forecast_profit(self, forecast_sales, margin):

        return forecast_sales * margin



    def analyze(self, income_statement):


        sales = income_statement["sales"]

        operating_profit = (
            income_statement["operating_profit"]
        )


        current_sales = sales["current"]

        previous_sales = sales["previous"]



        normalized = self.normalizer.calculate(

            operating_profit=operating_profit["current"],

            recurring_non_operating=0

        )



        normalized_profit = normalized["normalized_profit"]



        growth = self.calculate_growth(

            current_sales,

            previous_sales

        )



        margin = self.calculate_margin(

            normalized_profit,

            current_sales

        )



        forecast_sales = self.forecast_sales(

            current_sales,

            growth

        )



        forecast_profit = self.forecast_profit(

            forecast_sales,

            margin

        )



        return {

            "sales_growth": growth,

            "normalized_profit_margin": margin,

            "forecast_sales": forecast_sales,

            "forecast_normalized_profit": forecast_profit,

            "base_period": sales["current_date"]

        }



if __name__ == "__main__":


    sample = {

        "sales": {

            "current": 143134988,

            "previous": 70072719,

            "current_date": "1404/12/29"

        },


        "operating_profit": {

            "current": 75110367

        }

    }



    engine = ProfitForecaster()


    print(engine.analyze(sample))
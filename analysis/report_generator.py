class ReportGenerator:


    def generate(
        self,
        company,
        forecast_sales,
        forecast_profit,
        profit_quality,
        valuation,
        liabilities,
        balance_status
    ):


        sales_growth = (
            (
                forecast_sales - company.sales
            )
            /
            company.sales
            *
            100
            if company.sales
            else 0
        )


        profit_growth = (
            (
                forecast_profit - company.net_profit
            )
            /
            company.net_profit
            *
            100
            if company.net_profit
            else 0
        )


        debt_equity = (
            liabilities / company.equity
            if company.equity
            else 0
        )


        return f"""
==============================
FINAL ANALYSIS REPORT
==============================

Company:
{company.name}

Symbol:
{company.symbol}


PERFORMANCE
------------------------------
Current Sales:
{company.sales}

Forecast Sales:
{round(forecast_sales)}

Sales Growth:
{round(sales_growth,2)} %


PROFITABILITY
------------------------------
Current Profit:
{company.net_profit}

Forecast Profit:
{round(forecast_profit)}

Profit Growth:
{round(profit_growth,2)} %

Net Margin:
{round((company.net_profit/company.sales)*100,2) if company.sales else 0} %


PROFIT QUALITY
------------------------------
Operating Profit Coverage:
{profit_quality["operating_profit_ratio"]} %

Non Operating Income Ratio:
{profit_quality["non_operating_ratio"]} %

Quality Status:
{profit_quality["status"]}


BALANCE SHEET
------------------------------
Assets:
{company.assets}

Equity:
{company.equity}

Liabilities:
{liabilities}

Balance Status:
{balance_status}

Debt / Equity:
{round(debt_equity,2)}


VALUATION
------------------------------
Market Cap:
{company.market_cap}

P/E Forward:
{valuation["PE"]}

P/S Forward:
{valuation["PS"]}

P/B:
{valuation["PB"]}

P/A:
{valuation["PA"]}

P/D Forward:
{valuation["PD"]}


ANALYST SUMMARY
------------------------------
Profit Quality:
{profit_quality["status"]}

Valuation:
Forward P/E = {valuation["PE"]}

==============================
"""
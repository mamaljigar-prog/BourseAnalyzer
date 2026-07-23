class ReportGenerator:


    def generate(
        self,
        company,
        forecast_sales,
        forecast_profit,
        profit_quality,
        valuation,
        liabilities,
        balance_status,
        company_structure=None,
        analysis_strategy=None,
        report_period=None,
        industry_rank=None
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



        structure_section = ""


        if company_structure:

            structure_section = f"""

COMPANY STRUCTURE
------------------------------
Type:
{company_structure.get("type")}

Confidence:
{company_structure.get("confidence")}

Reason:
{company_structure.get("reason")}

"""



        strategy_section = ""


        if analysis_strategy:

            strategy_section = f"""

ANALYSIS STRATEGY
------------------------------
Type:
{analysis_strategy.get("type")}

Forecast Method:
{analysis_strategy.get("forecast")}

Valuation Methods:
{analysis_strategy.get("valuation")}

Metrics:
{analysis_strategy.get("metrics")}

"""



        industry_section = ""


        if industry_rank:

            industry_section = f"""

INDUSTRY POSITION
------------------------------
Industry:
{company.industry}

Market Cap Rank:
{industry_rank}

"""



        period_section = ""


        if report_period:

            period_section = f"""

REPORT INFORMATION
------------------------------
Report Period:
{report_period.get("period")}

Forecast Method:
{report_period.get("forecast_method")}

"""



        return f"""
==============================
FINAL ANALYSIS REPORT
==============================

Company:
{company.name}

Symbol:
{company.symbol}


{structure_section}

{strategy_section}

{industry_section}

{period_section}


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
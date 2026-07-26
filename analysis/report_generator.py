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
        report_period=None,
        industry_rank=None
    ):

        # =========================
        # Financial Period
        # =========================

        period_type = None

        duration_months = None

        annualization_factor = None

        report_period_end = None

        fiscal_year_end = None

        forecast_method = None

        growth_method = (
            "Comparable-period growth "
            "not available yet"
        )

        if report_period:

            period_type = (
                report_period.get(
                    "period_type"
                )
            )

            duration_months = (
                report_period.get(
                    "duration_months"
                )
            )

            annualization_factor = (
                report_period.get(
                    "annualization_factor"
                )
            )

            report_period_end = (
                report_period.get(
                    "period"
                )
            )

            fiscal_year_end = (
                report_period.get(
                    "fiscal_year_end"
                )
            )

            forecast_method = (
                report_period.get(
                    "forecast_method"
                )
            )

            growth_method = (
                report_period.get(
                    "growth_method",
                    growth_method
                )
            )

        # =========================
        # Comparable Growth
        # =========================

        # Forecast سالانه‌شده با دوره جاری
        # قابل مقایسه نیست.
        #
        # مثال:
        #
        # 3M Current Sales:
        # 3,814,414
        #
        # Annual Forecast:
        # 15,257,656
        #
        # این اختلاف 300 درصد رشد نیست.
        #
        # رشد واقعی باید بعداً با مقایسه
        # دوره مشابه سال قبل محاسبه شود.

        sales_growth = None

        profit_growth = None

        # =========================
        # Debt / Equity
        # =========================

        debt_equity = (

            liabilities /

            company.equity

            if company.equity

            else 0

        )

        # =========================
        # Industry
        # =========================

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

        # =========================
        # Report Information
        # =========================

        period_section = ""

        if report_period:

            period_section = f"""

REPORT INFORMATION
------------------------------
Report Period End:
{report_period_end}

Fiscal Year End:
{fiscal_year_end}

Period Type:
{period_type}

Duration:
{duration_months} months

Annualization Factor:
{annualization_factor}

Forecast Method:
{forecast_method}

Growth Method:
{growth_method}

"""

        # =========================
        # Growth Display
        # =========================

        sales_growth_display = (

            f"{round(sales_growth, 2)} %"

            if sales_growth is not None

            else

            "N/A"

        )

        profit_growth_display = (

            f"{round(profit_growth, 2)} %"

            if profit_growth is not None

            else

            "N/A"

        )

        # =========================
        # Final Report
        # =========================

        return f"""
==============================
FINAL ANALYSIS REPORT
==============================

Company:
{company.name}

Symbol:
{company.symbol}


{industry_section}

{period_section}

PERFORMANCE
------------------------------
Current Period Sales:
{company.sales}

Annual Forecast Sales:
{round(forecast_sales)}

Comparable Sales Growth:
{sales_growth_display}

Growth Status:
Comparable-period data not available


PROFITABILITY
------------------------------
Current Period Profit:
{company.net_profit}

Annual Forecast Profit:
{round(forecast_profit)}

Comparable Profit Growth:
{profit_growth_display}

Growth Status:
Comparable-period data not available

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

Growth Analysis:
Comparable-period growth requires
the same financial period from the
previous fiscal year.

==============================
"""
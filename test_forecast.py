from forecast.profit_forecast import ProfitForecast


forecast = ProfitForecast(

    sales=143134988,
    net_profit=65862967,

    # مثلا گزارش 9 ماهه
    months_passed=9
)


forecast.report()
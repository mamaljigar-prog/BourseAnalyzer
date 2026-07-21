\# Active Files - Bourse Analyzer





\## اجرای اصلی پروژه



main.py





\## TSETMC



فعال:



tsetmc/

&nbsp;   tsetmc\_adapter.py

&nbsp;   tsetmc\_market.py

&nbsp;   tsetmc\_data.py





\## CODAL



فعال:



codal/

&nbsp;   codal\_parser.py

&nbsp;   codal\_financial\_parser.py

&nbsp;   codal\_profit\_loss\_parser.py

&nbsp;   codal\_monthly.py





\## Forecast



فعال:



forecast/

&nbsp;   sales\_forecast.py

&nbsp;   profit\_forecast.py





\## Valuation



فعال:



valuation/

&nbsp;   valuation\_model.py





\## Models



فعال:



models/

&nbsp;   company.py

&nbsp;   sales.py







\# فایل‌های قدیمی یا آزمایشی



نیاز به بررسی:



codal.py

financial.py

financial\_model.py

forecast\_old.py

main\_analysis.py

integrated\_analysis.py

integrated\_report.py

integrated\_engine.py

company.py

company\_data.py





\# تست‌ها



فعلاً نگهداری شود:



tests/

test\_\*.py





\# هدف مرحله بعد



1\. اتصال CODAL واقعی به مدل FinancialReport

2\. حذف داده‌های دستی از main.py

3\. ساخت pipeline:



TSETMC

&nbsp;   |

CODAL

&nbsp;   |

Financial Model

&nbsp;   |

Forecast

&nbsp;   |

Valuation

&nbsp;   |

Report


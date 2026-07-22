# BourseAnalyzer Project State

## Current Stage

Date: 1405/04/31

---

## Completed

### Environment
- Python environment آماده است.
- پروژه در Windows + VS Code اجرا می‌شود.
- اجرای ماژول‌ها با:
  python -m module.path

---

## Codal Layer

Status: Working

Completed:

✅ CodalAdapter
- دریافت گزارش‌ها از کدال

✅ ReportSelector
- انتخاب جدیدترین گزارش مالی

✅ CodalProfitLossParser
- استخراج شیت‌ها و سلول‌های مالی

---

## Financial Mapping

Status: Initial Stable Version

Completed:

✅ FinancialConceptMapper

تشخیص:

- sales
- gross_profit
- operating_profit
- net_profit
- non_operating_income


تست شده روی:

1. خراسان
- موفق

2. شپنا
- موفق

3. فزر
- موفق


مشکل قبلی:
- net_profit اشتباه برابر gross_profit تشخیص داده می‌شد.

حل شد با:
- scoring matching
- exclude words
- انتخاب تطبیقی ردیف‌ها

---

## FinancialStatement Layer

Status: Created

مسیر:

financial/
 ├── __init__.py
 └── financial_statement.py


هدف:

جدا کردن داده خام کدال از موتور تحلیل.


فعلاً شامل:

- revenue
- gross_profit
- operating_profit
- net_profit
- non_operating_income


آماده توسعه:

- assets
- liabilities
- equity
- operating_cash_flow


---

## Current Data Flow

Codal
 ↓
Parser
 ↓
FinancialMapper
 ↓
FinancialStatement
 ↓
(Next)
Valuation Engine


---

## Next Tasks

Priority 1:

ساخت Balance Sheet Mapper

هدف:

استخراج:

- Total Assets
- Total Liabilities
- Equity


اتصال به:

FinancialStatement


برای آماده شدن:

- P/B
- P/A
- تحلیل ساختار مالی


---

## Coding Rules

Rule #1:

در پروژه فقط فایل کامل جایگزین ارائه شود.

ممنوع:

- تکه کد
- patch
- تغییر دستی چند خطی


هر تغییر:
- مسیر فایل مشخص
- کل فایل ارائه شود


---

## Financial Analysis Rules

- استفاده از P/E خود TSETMC ممنوع.
- محاسبه نسبت‌ها از داده مالی استخراج‌شده انجام می‌شود.
- سودهای غیرتکرارشونده باید جدا شوند.
- تمرکز تحلیل اصلی روی یک دوره مالی.
- روند ۵ ساله بعداً برای کیفیت و رشد استفاده می‌شود.

هدف نهایی:

محاسبه:

- Forward P/E
- Forward P/S
- Forward P/D
- P/B
- P/A

و رتبه‌بندی شرکت‌ها بر اساس رشد و ارزش.
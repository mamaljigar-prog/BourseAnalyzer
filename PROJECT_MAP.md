# BourseAnalyzer Project State

## Current Stage

Date: 1405/04/31

Checkpoint:
Stable after:

* Forecast logic restoration
* Report selection testing
* Balance sheet extraction validation

---

# Environment

Status: Ready

Completed:

✅ Python environment آماده است.
✅ پروژه روی Windows + VS Code اجرا می‌شود.
✅ اجرای ماژول‌ها:

```text
python -m module.path
```

---

# Codal Layer

Status: Working

Completed:

## CodalAdapter

وظیفه:

* دریافت گزارش‌های مالی از کدال
* استخراج گزارش‌های موجود
* دریافت URL گزارش

## ReportSelector

Status:
Initial stable version

Completed:

* تفکیک گزارش سالانه و میان‌دوره‌ای
* انتخاب گزارش سالانه حسابرسی‌شده
* انتخاب گزارش میان‌دوره‌ای جدید

Important rule:

گزارش جدید همیشه جایگزین گزارش سالانه نمی‌شود.

منطق:

```text
Annual Report
      |
      ↓
Primary Analysis Base

Interim Report
      |
      ↓
Performance Update
```

---

# Financial Mapping Layer

Status: Stable Initial Version

Completed:

## FinancialConceptMapper

تشخیص:

* sales
* gross_profit
* operating_profit
* net_profit
* non_operating_income

Tested:

### خراسان

✅ موفق

### شپنا

✅ موفق

### فزر

✅ موفق

مشکل قبلی:

* net_profit اشتباه برابر gross_profit تشخیص داده می‌شد.

حل شده با:

* scoring matching
* exclude words
* adaptive row selection

---

# FinancialStatement Layer

Status: Created

Path:

```text
financial/
 ├── __init__.py
 └── financial_statement.py
```

هدف:

جدا کردن داده خام کدال از موتور تحلیل.

Current fields:

* revenue
* gross_profit
* operating_profit
* net_profit
* non_operating_income

Ready for expansion:

* assets
* liabilities
* equity
* operating_cash_flow

---

# Balance Sheet Layer

Status: Working Initial Version

Completed:

## BalanceSheetParser

استخراج:

* Total Assets
* Equity
* Liabilities
* Balance validation

تست شده روی:

* خراسان
* پترول
* درهآور
* فسبزوار
* غشاذر
* پکویر
* فولاد
* فارس
* شپنا
* کگل
* کچاد
* رمپنا
* تاپیکو

Current limitation:

برخی شرکت‌ها نیازمند تشخیص ساختار هستند:

* هلدینگ‌ها
* شرکت‌های دارای زیرمجموعه مهم
* بانک‌ها
* بیمه‌ها

---

# Current Data Flow

```text
Codal
  ↓
Parser
  ↓
FinancialConceptMapper
  ↓
FinancialStatement
  ↓
Balance Sheet Data
  ↓
Forecast Engine
  ↓
Valuation Engine
```

---

# Company Structure Classification Layer

Status:
Next Major Task

هدف:

تشخیص نوع شرکت قبل از تحلیل.

Categories:

## Production Company

Examples:

* خراسان
* فولاد
* کگل
* کچاد

Model:

* Sales
* Profit
* Margin
* Forward Multiples

---

## Group / Subsidiary Based Company

Examples:

* فزر
* پترول

نیاز:

بررسی همزمان:

* صورت مالی اصلی
* صورت مالی تلفیقی

---

## Holding Company

Examples:

* فارس
* تاپیکو

Future:

NAV Model

---

## Bank

Example:

* وبملت

Future:

Banking Model

---

## Insurance

Future:

Insurance Model

---

# Forecast Engine

Status:
Working

Completed:

Annual forecasting based on financial period.

Outputs:

* Forecast Sales
* Forecast Profit
* Net Margin

Example خراسان:

* Sales Growth: 33.33%
* Profit Growth: 33.33%
* Forward P/E: ~5.7

---

# Valuation Engine

Status:
Working

Supported:

* Forward P/E
* Forward P/S
* Forward P/D
* P/B
* P/A

Rules:

❌ استفاده از P/E تاسیسات TSETMC ممنوع

✅ محاسبه نسبت‌ها از داده مالی استخراج‌شده

---

# Profit Quality Analysis

Status:
Working

Checks:

* Operating Profit
* Non Operating Income

هدف:

تشخیص سودهای غیرتکرارشونده.

---

# Coding Rules

## Rule #1

در پروژه فقط فایل کامل جایگزین ارائه شود.

ممنوع:

* تکه کد
* patch
* تغییر دستی چند خطی

هر تغییر:

* مسیر فایل مشخص
* کل فایل ارائه شود

---

# Financial Analysis Rules

* P/E از TSETMC استفاده نمی‌شود.
* نسبت‌ها از داده مالی محاسبه می‌شوند.
* سودهای غیرتکرارشونده جدا می‌شوند.
* تمرکز تحلیل اصلی روی یک دوره مالی است.
* روند ۵ ساله فعلاً خارج از محدوده اصلی است و بعداً برای کیفیت و رشد استفاده می‌شود.

---

# Final Goal

ساخت موتور تحلیل که بتواند:

* Forward P/E
* Forward P/S
* Forward P/D
* P/B
* P/A

را محاسبه کند.

و شرکت‌ها را بر اساس:

* رشد
* کیفیت سود
* ارزش‌گذاری
* ساختار مالی

رتبه‌بندی کند.

---

# Next Priority

## Priority 1

Company Structure Classification

بعد از آن:

## Priority 2

Dynamic Balance Sheet Mapping

## Priority 3

Advanced Models:

* NAV
* Bank Analysis
* Insurance Analysis

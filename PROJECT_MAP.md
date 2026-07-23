# BourseAnalyzer Project State

## Current Stage

Date: 1405/04/31

Checkpoint:

Stable after:

* Forecast logic restoration
* Codal report selection testing
* Financial mapping validation
* Balance sheet extraction validation
* Git local checkpoint + GitHub sync

---

# Repository Status

## Git

Status:

✅ Local repository saved
✅ Commit created
✅ GitHub main branch synchronized

Latest checkpoint:

```
Initial BourseAnalyzer checkpoint
```

Purpose:

بازگشت امن در صورت ایجاد خطا در مراحل بعدی توسعه.

---

# Environment

Status: Ready

Completed:

✅ Python environment آماده است.
✅ Windows + VS Code setup فعال است.
✅ اجرای ماژول‌ها با:

```text
python -m module.path
```

---

# Codal Layer

Status: Working

Completed:

## CodalReportService

وظیفه:

* دریافت گزارش مالی شرکت
* انتخاب گزارش مناسب
* دریافت URL گزارش

---

## SheetLoader

Completed:

* دریافت شیت‌های گزارش
* تشخیص جدول‌های مالی

---

## SheetSelector

Status:

Initial stable version

وظیفه:

تفکیک:

* صورت سود و زیان
* صورت وضعیت مالی

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

حل مشکلات:

* تشخیص اشتباه net_profit
* انتخاب اشتباه ردیف‌های مالی

روش فعلی:

* scoring matching
* exclude words
* adaptive row selection

تست شده:

✅ خراسان
✅ شپنا
✅ فزر

---

# FinancialStatement Layer

Status: Created

Path:

```text
financial/

├── __init__.py
├── financial_statement.py
├── financial_service.py
├── financial_statement_assembler.py
└── balance_sheet_mapper.py
```

هدف:

جدا کردن:

Codal Raw Data

از

Analysis Engine

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

Status:

Working Initial Version

Completed:

## BalanceSheetParser

استخراج:

* Total Assets
* Equity
* Liabilities
* Balance validation

---

## BalanceSheetMapper

Status:

Initial stable

وظیفه:

تطبیق ساختارهای مختلف صورت وضعیت مالی.

پشتیبانی:

* گزارش مستقل
* گزارش تلفیقی
* تغییر شماره ردیف‌ها

Validation:

فرمول کنترل:

```text
Assets =
Equity
+
Non Controlling Interest
+
Liabilities
```

تست موفق:

✅ شپنا
✅ خراسان

---

# Current Data Flow

```text
Codal Report
      ↓
Sheet Loader
      ↓
Sheet Selector
      ↓
Financial Parser
      ↓
Financial Concept Mapper
      ↓
Financial Statement
      ↓
Balance Sheet Mapper
      ↓
Forecast Engine
      ↓
Valuation Engine
      ↓
Final Analyzer
      ↓
Report Generator
```

---

# Forecast Engine

Status:

Working

Current model:

Annualized forecast based on latest financial period.

Outputs:

* Forecast Sales
* Forecast Profit
* Net Margin

Example:

خراسان:

```
Sales Growth:
33.33%

Profit Growth:
33.33%

Forward P/E:
≈5.7
```

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

❌ استفاده از P/E سایت TSETMC ممنوع

✅ محاسبه نسبت‌ها فقط از داده مالی استخراج‌شده

Formula:

```text
Forward P/E =
Market Cap /
Forecast Profit
```

---

# Profit Quality Analysis

Status:

Working

Checks:

* Operating Profit
* Non Operating Income

هدف:

تشخیص:

* سود عملیاتی واقعی
* سود غیرتکرارشونده

---

# Company Structure Classification Layer

Status:

Next Major Task

هدف:

تشخیص نوع شرکت قبل از تحلیل.

---

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

## Holding Company

Examples:

* فارس
* تاپیکو

Future Model:

NAV Analysis

---

## Group / Subsidiary Based Company

Examples:

* پترول
* فزر

نیاز:

بررسی:

* صورت مالی اصلی
* صورت مالی تلفیقی
* شرکت‌های مهم زیرمجموعه

---

## Bank

Future:

Banking Model

---

## Insurance

Future:

Insurance Model

---

# Financial Analysis Rules

قوانین ثابت پروژه:

1. گزارش مالی جدید، پایه اصلی تحلیل است.

2. گزارش‌های قدیمی فقط برای:

* مقایسه
* رشد
* کیفیت داده

استفاده می‌شوند.

3. روند ۵ ساله فعلاً خارج از محدوده اصلی است.

4. سود فروش دارایی و درآمد غیرعملیاتی غیرتکرارشونده نباید سود اصلی تلقی شود.

5. برای هلدینگ‌ها تحلیل باید بر اساس NAV توسعه پیدا کند.

---

# Coding Rules

## Rule #1

هر تغییر کد:

فقط با فایل کامل جایگزین انجام می‌شود.

ممنوع:

* patch
* تغییر چند خطی دستی
* تکه کد ناقص

فرمت تغییر:

```
File Path:

Complete Replacement Code
```

---

# Next Development Priority

## Priority 1

Company Structure Classification

هدف:

قبل از valuation مشخص شود شرکت:

* تولیدی است
* هلدینگ است
* بانک است
* بیمه است

---

## Priority 2

Dynamic Balance Sheet Mapping

هدف:

پشتیبانی کامل از:

* گزارش‌های مستقل
* تلفیقی
* هلدینگ‌ها

---

## Priority 3

Advanced Models

شامل:

* NAV Engine
* Holding Analyzer
* Bank Analyzer
* Insurance Analyzer

---

# Final Goal

ساخت موتور تحلیل بورس که بتواند:

* داده مالی را از کدال استخراج کند
* ساختار شرکت را تشخیص دهد
* سود واقعی را ارزیابی کند
* ارزش‌گذاری انجام دهد
* شرکت‌ها را رتبه‌بندی کند

بر اساس:

* رشد
* کیفیت سود
* ارزش‌گذاری
* ساختار مالی
* ریسک بنیادی

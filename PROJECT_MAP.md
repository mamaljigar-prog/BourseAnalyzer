# BourseAnalyzer Project State

## Current Stage

Date: 1405/04/31

Current checkpoint:

Stable after:

* Codal automatic report selection
* Financial mapping validation
* Balance sheet extraction
* Forecast engine integration
* Valuation engine integration
* Company structure classification
* Analysis strategy integration

---

# Repository Status

## Git

Latest completed commits:

```
Upgrade company structure classifier
Connect company classifier and analysis strategy to engine
Add strategy based forecast engine
```

Current state:

✅ Local checkpoint saved
✅ Main branch working
✅ Core analysis pipeline executes successfully

---

# Current Execution Result

Test company:

```
پتروشیمی خراسان
```

Successful pipeline:

```
Codal
 ↓
Financial Extraction
 ↓
Balance Sheet Mapping
 ↓
Company Classification
 ↓
Analysis Strategy
 ↓
Forecast Engine
 ↓
Valuation
 ↓
Final Analyzer
 ↓
Report Generator
```

Output validation:

```
Company Structure:
production

Strategy:
sales_margin

Forward P/E:
≈ 5.7
```

---

# Project Architecture

```
BourseAnalyzer

├── core
│   ├── analyzer_engine.py
│   └── analyzer_request.py
│
├── codal
│   ├── codal_report_service.py
│   ├── sheet_loader.py
│   ├── sheet_selector.py
│   ├── financial_adapter.py
│   └── balance_sheet_parser.py
│
├── financial
│   ├── financial_statement.py
│   ├── financial_service.py
│   ├── financial_statement_assembler.py
│   └── balance_sheet_mapper.py
│
├── analysis
│   ├── company_classifier.py
│   ├── analysis_strategy.py
│   ├── profit_quality.py
│   ├── final_analyzer.py
│   └── report_generator.py
│
├── forecast
│   └── forecast_engine.py
│
├── valuation
│   ├── valuation_model.py
│   └── valuation_engine.py
│
├── models
│   └── company.py
│
└── tsetmc
    ├── tsetmc_adapter.py
    ├── tsetmc_market.py
    └── symbol_resolver.py
```

---

# Data Pipeline

## Input

```
Symbol
```

↓

## Market Layer

دریافت:

* Price
* Market Cap
* Instrument Information

↓

## Codal Layer

وظیفه:

* پیدا کردن آخرین گزارش مالی معتبر
* دریافت URL گزارش
* انتخاب شیت مالی

↓

## Financial Layer

استخراج:

* Sales
* Gross Profit
* Operating Profit
* Net Profit
* Non Operating Income

↓

## Balance Sheet Layer

استخراج:

* Assets
* Equity
* Liabilities

Validation:

```
Assets =
Equity
+
Liabilities
+
Non Controlling Interest
```

---

# Company Classification

Status:

Working Initial Version

هدف:

تشخیص مدل تحلیل قبل از Forecast و Valuation.

Supported:

## Production

مثال:

* خراسان
* فولاد
* کگل

تحلیل:

* Sales
* Profit
* Margin
* Forward Multiples

## Holding

آماده توسعه:

* NAV
* ارزش پرتفوی
* شرکت‌های زیرمجموعه

## Bank

آینده:

* Loan Quality
* Capital Adequacy
* PB Model

## Insurance

آینده:

* Premium Growth
* Combined Ratio
* PB / PE

## Subsidiary Based

آینده:

* Consolidated Analysis
* Major Subsidiary Impact

---

# Analysis Strategy

Status:

Integrated

وظیفه:

تعیین روش تحلیل بر اساس نوع شرکت.

Current:

Production:

```
Forecast:
sales_margin

Valuation:
PE
PS
PB
PA
PD

Metrics:
sales_growth
profit_growth
net_margin
```

---

# Forecast Engine

Status:

Working

Current method:

```
Annualized Forecast
```

Formula:

```
Forecast Sales =
Current Sales / Months Passed × 12
```

Profit:

```
Forecast Profit =
Forecast Sales × Current Net Margin
```

Output:

* Forecast Sales
* Forecast Profit
* Forecast Method

---

# Valuation Engine

Status:

Working

Rules:

❌ P/E سایت TSETMC استفاده نمی‌شود.

محاسبه:

```
Forward P/E =
Market Cap /
Forecast Profit
```

Supported:

* Forward P/E
* Forward P/S
* Forward P/D
* P/B
* P/A

Target:

```
Target Market Cap =
Forecast Profit × Base PE
```

Base PE:

```
7
```

---

# Profit Quality

Status:

Working

بررسی:

* Operating Profit
* Net Profit
* Non Operating Income

هدف:

تشخیص:

* سود عملیاتی واقعی
* سود ناشی از درآمد غیرتکرارشونده

---

# Financial Rules

قوانین ثابت:

1. آخرین گزارش مالی معتبر، مبنای اصلی تحلیل است.

2. گزارش‌های قدیمی فقط برای:

* مقایسه
* رشد
* کنترل کیفیت

استفاده می‌شوند.

3. روند ۵ ساله فعلاً خارج از محدوده است.

4. فروش دارایی و درآمد غیرعملیاتی غیرتکرارشونده نباید سود اصلی محسوب شود.

5. هلدینگ‌ها باید با NAV تحلیل شوند.

6. P/E فقط از سود پیش‌بینی‌شده داخلی محاسبه می‌شود.

---

# Current Known Issue

در زمان اتصال AnalysisStrategy:

اشکال:

```
AttributeError:
'Company' object has no attribute 'get'
```

علت:

AnalysisStrategy انتظار dictionary دارد ولی Company object ارسال شده است.

راه اصلاح:

قبل از ارسال:

```
company_structure
```

یا تبدیل Company به dictionary انجام شود.

---

# Next Development Priority

## Priority 1

اصلاح اتصال:

```
Company
 ↓
CompanyClassifier
 ↓
AnalysisStrategy
```

---

## Priority 2

اتصال کامل:

```
ForecastEngine
 ↓
ValuationEngine
```

به جای فراخوانی مستقیم:

```
calculate_valuation()
```

در core engine.

---

## Priority 3

توسعه مدل‌ها:

* NAV Engine
* Holding Analyzer
* Bank Analyzer
* Insurance Analyzer

---

# Coding Rules

## Rule #1

هر تغییر کد:

فقط فایل کامل جایگزین شود.

ممنوع:

* Patch
* تکه کد ناقص
* تغییر چند خطی

فرمت:

```
File Path:

Complete Replacement Code
```

## Rule #2

دستور بعدی توسعه باید در همان پیام ارسال شود و کار به پیام بعدی موکول نشود.

---

# Final Goal

ساخت موتور تحلیل بنیادی خودکار که:

* گزارش کدال را استخراج کند
* ساختار شرکت را تشخیص دهد
* سود واقعی را ارزیابی کند
* Forecast انجام دهد
* Valuation انجام دهد
* ریسک بنیادی را تشخیص دهد
* شرکت‌ها را رتبه‌بندی کند

بر اساس:

* رشد
* کیفیت سود
* ارزش‌گذاری
* ساختار مالی
* ریسک

# BourseAnalyzer — PROJECT MAP
Version: 0.1
Last Updated: 2026-07-21

---

# 1. هدف اصلی پروژه

ساخت یک سیستم تحلیل بنیادی و ارزش‌گذاری سهام بورس ایران که:

1. اطلاعات بازار را از TSETMC دریافت کند.
2. گزارش‌های مالی شرکت‌ها را از Codal استخراج کند.
3. داده‌های مالی را مستقیماً از صورت‌های مالی استخراج و استانداردسازی کند.
4. عملکرد مالی شرکت را بر اساس آخرین دوره مالی تحلیل کند.
5. روند 5 ساله را در مرحله بعد برای تحلیل روند استفاده کند.
6. فروش و سود سالانه را تا پایان سال مالی پیش‌بینی کند.
7. نسبت‌های ارزندگی را خودش محاسبه کند.
8. از P/E ارائه‌شده توسط TSETMC استفاده نکند.
9. خروجی نهایی قابل استفاده برای تحلیل بنیادی ارائه دهد.

---

# 2. اصل معماری پروژه

مسیر اصلی داده:

TSETMC
    ↓
Market Data
    ↓
Codal
    ↓
Financial Reports
    ↓
Financial Adapter
    ↓
Normalized Financial Data
    ↓
Forecast Engine
    ↓
Valuation Engine
    ↓
Fundamental Analysis
    ↓
Final Report

---

# 3. منابع داده

## 3.1 TSETMC

منبع اطلاعات بازار:

- نماد
- نام شرکت
- قیمت
- قیمت پایانی
- ارزش بازار
- تعداد سهام
- اطلاعات معاملاتی مورد نیاز

### قانون مهم

P/E موجود در TSETMC نباید به عنوان منبع اصلی استفاده شود.

P/E باید توسط خود سیستم و بر اساس سود پیش‌بینی‌شده محاسبه شود.

فرمول:

P/E Forward =
Market Cap / Forecasted Net Profit

---

## 3.2 Codal

منبع اطلاعات مالی و گزارش‌های رسمی شرکت.

اطلاعات مورد استفاده:

- صورت سود و زیان
- صورت وضعیت مالی
- صورت جریان‌های نقدی
- گزارش‌های مالی دوره‌ای
- گزارش‌های سالانه
- اطلاعات مقایسه‌ای دوره‌های قبل

---

# 4. وضعیت فعلی Codal Parser

## 4.1 تشخیص گزارش مالی

Status: COMPLETED

سیستم توانسته گزارش مالی شرکت را شناسایی کند.

نمونه تست:

شرکت:
پتروشیمی خراسان

نماد:
خراسان

گزارش:
صورت‌های مالی 12 ماهه منتهی به 1404/12/29

وضعیت:
حسابرسی شده

---

## 4.2 تشخیص Sheetها

Status: COMPLETED

Codal Report دارای Sheetهای مختلف است.

نمونه:

- Sheet 19 — نظر حسابرس
- Sheet 1 — صورت سود و زیان
- Sheet 1058 — صورت سود و زیان جامع
- Sheet 0 — صورت وضعیت مالی
- Sheet 1060 — صورت تغییرات در حقوق مالکانه
- Sheet 9 — صورت جریان‌های نقدی
- Sheet 20 تا 25 — خلاصه اطلاعات گزارش تفسیری
- Sheet 30 — اعضای هیئت مدیره

### نکته

Sheetها باید به صورت Dynamic شناسایی شوند.

نباید فرض شود که همیشه فقط یک ساختار ثابت وجود دارد.

---

# 5. معماری استخراج اطلاعات Codal

## تصمیم نهایی

روش استخراج داده:

HTML Table Scraping ❌

JSON Datasource Parsing ✅

---

## دلیل

HTML صفحه Codal لزوماً داده‌های مالی را به صورت Table استاندارد ارائه نمی‌کند.

در بررسی انجام‌شده:

BeautifulSoup / HTML Table Parsing

نتیجه:

TABLE COUNT = 0

بنابراین استخراج مستقیم Table از HTML روش قابل اتکایی نیست.

---

## روش صحیح

اطلاعات مالی در JavaScript صفحه و متغیر:

datasource

وجود دارد.

ساختار کلی:

datasource
    ↓
sheets
    ↓
sheet
    ↓
tables
    ↓
cells

---

# 6. Codal Datasource

Status: COMPLETED

ساختار datasource شناسایی شده است.

کلیدهای اصلی:

- title_Fa
- title_En
- subject
- dsc
- type
- period
- periodEndToDate
- yearEndToDate
- periodExtraDay
- isConsolidated
- tracingNo
- kind
- isAudited
- auditState
- registerDateTime
- sentDateTime
- publishDateTime
- state
- isForAuditing
- sheets

---

# 7. Sheet Structure

هر Sheet دارای ساختاری مشابه زیر است:

- code
- title_Fa
- title_En
- sequence
- isDynamic
- tables
- aliasName
- versionNo
- sheetComponents

---

# 8. Table Structure

هر Table شامل:

- metaTableId
- title_En
- title_Fa
- sequence
- sheetCode
- code
- description
- aliasName
- versionNo
- cells

---

# 9. Cell Structure

هر Cell شامل اطلاعاتی مانند:

- address
- formula
- financialConcept
- cellGroupName
- rowCode
- rowSequence
- colSpan
- columnCode
- columnSequence
- value
- valueTypeName
- dataTypeName
- periodEndToDate
- yearEndToDate
- isAudited

---

# 10. Balance Sheet Extraction

## صورت وضعیت مالی

Sheet:

code = 0

Status: RAW EXTRACTION COMPLETED

---

## داده‌های استخراج‌شده

نمونه شرکت پتروشیمی خراسان:

دوره جاری:

1404/12/29

دوره مقایسه‌ای:

1403/12/30

دوره قدیمی‌تر:

1403/01/01

---

## اقلام مهم استخراج‌شده

### دارایی‌ها

- دارایی‌های غیرجاری
- دارایی‌های ثابت مشهود
- سرمایه‌گذاری در املاک
- دارایی‌های نامشهود
- سرمایه‌گذاری‌های بلندمدت
- دریافتنی‌های بلندمدت
- دارایی مالیات انتقالی
- سایر دارایی‌ها
- جمع دارایی‌های غیرجاری

### دارایی‌های جاری

- سفارشات و پیش‌پرداخت‌ها
- موجودی مواد و کالا
- دریافتنی‌های تجاری و سایر دریافتنی‌ها
- سرمایه‌گذاری‌های کوتاه‌مدت
- موجودی نقد
- دارایی‌های نگهداری شده برای فروش
- جمع دارایی‌های جاری

### جمع دارایی‌ها

ردیف:

جمع دارایی‌ها

---

### حقوق مالکانه

- سرمایه
- افزایش سرمایه در جریان
- صرف سهام
- صرف سهام خزانه
- اندوخته قانونی
- سایر اندوخته‌ها
- مازاد تجدید ارزیابی دارایی‌ها
- تفاوت تسعیر ارز عملیات خارجی
- سود و زیان انباشته
- سهام خزانه
- جمع حقوق مالکانه

---

### بدهی‌ها

- بدهی‌های غیر
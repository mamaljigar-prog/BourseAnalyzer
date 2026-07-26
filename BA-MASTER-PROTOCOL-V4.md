# BOURSEANALYZER MASTER PROTOCOL V4

## Project Governance, Architecture, Continuity, Coding, Testing and Control Standard

**Project:** BourseAnalyzer  
**Protocol ID:** BA-MASTER-PROTOCOL-V4  
**Protocol Version:** V4  
**Status:** FINAL  
**Authority:** Project Master Governance Document  
**Repository:** BourseAnalyzer  
**Primary Branch:** Must always be determined from actual Git state  
**Last Updated:** 2026-07-26  

---

# 0. PURPOSE OF THIS PROTOCOL

این سند، اساسنامه و پروتکل مادر پروژه BourseAnalyzer است.

هدف این پروتکل جلوگیری از موارد زیر است:

- گم شدن مسیر پروژه
- شروع مجدد غیرضروری پروژه
- تکرار Audit بدون دلیل
- فراموش شدن تصمیم‌های معماری
- ایجاد کدهای موازی و تکراری
- ایجاد ماژول‌های هم‌وظیفه
- باقی ماندن Hard-Codeهای غیرضروری
- پخش شدن Logic در چند فایل
- افزایش بی‌دلیل پیچیدگی
- تغییر معماری بدون بررسی Dependency Flow
- خروج پروژه از Scope
- اضافه شدن قابلیت‌های جدید قبل از تثبیت معماری
- از بین رفتن ارتباط بین Checkpointها
- وابستگی بیش از حد به حافظه مکالمه
- نیاز کاربر به توضیح دوباره وضعیت پروژه
- ادامه دادن یک Task از نقطه اشتباه
- تصور موفقیت تست بدون دریافت نتیجه واقعی
- حذف یا تغییر Legacy بدون تصمیم آگاهانه
- ایجاد Technical Debt جدید هنگام رفع Technical Debt قدیمی

این سند باید به‌عنوان مرجع اصلی کنترل پروژه مورد استفاده قرار گیرد.

---

# 1. GOLDEN RULE

قانون طلایی پروژه:

> هیچ کاری در BourseAnalyzer نباید صرفاً به دلیل اینکه «ممکن است مفید باشد» انجام شود.

هر تغییر باید:

1. با Scope فعلی سازگار باشد.
2. با معماری Active سازگار باشد.
3. در Roadmap جای مشخص داشته باشد.
4. دلیل فنی یا محصولی مشخص داشته باشد.
5. از ایجاد پیچیدگی غیرضروری جلوگیری کند.
6. قابل تست باشد.
7. وضعیت آن در Checkpoint ثبت شود.

اگر کاری خارج از Scope فعلی است:

- انجام نشود.
- وارد معماری نشود.
- به‌عنوان قابلیت جدید معرفی نشود.
- فقط در صورت نیاز به‌عنوان Future Scope ثبت شود.

---

# 2. PRIMARY CONTINUATION COMMAND

دستور استاندارد ادامه پروژه:

> ادامه BourseAnalyzer از آخرین Checkpoint

این دستور به معنی ادامه دادن پروژه از آخرین وضعیت معتبر است.

در پاسخ به این دستور، دستیار نباید پروژه را از ابتدا شروع کند.

فرآیند ادامه:

1. آخرین Checkpoint معتبر را پیدا کند.
2. وضعیت واقعی Repository را بررسی کند.
3. Branch فعلی را بررسی کند.
4. آخرین Commit را بررسی کند.
5. وضعیت Git را بررسی کند.
6. فایل‌های Project Control را بررسی کند.
7. Active Architecture را بررسی کند.
8. Legacy / Archive را بررسی کند.
9. آخرین Task تکمیل‌شده را مشخص کند.
10. Task در حال اجرا را مشخص کند.
11. Task بعدی ثبت‌شده را بررسی کند.
12. اگر Task قبلی هنوز کامل نشده، همان Task ادامه پیدا کند.
13. اگر Task کامل شده، نتیجه آن Verify شود.
14. سپس فقط یک Next Step قطعی انتخاب شود.

---

# 3. NO-RESTART RULE

پروژه نباید بدون دلیل از ابتدا شروع شود.

موارد زیر به‌تنهایی دلیل کافی برای شروع دوباره نیستند:

- باز شدن چت جدید
- طولانی شدن چت قبلی
- فراموش شدن بخشی از Context
- تغییر مدل
- تغییر Session
- عدم دسترسی فوری به حافظه مکالمه
- وجود کد Legacy
- وجود چند فایل مشابه
- وجود Technical Debt

در این شرایط ابتدا باید:

1. GitHub بررسی شود.
2. Project Control بررسی شود.
3. Checkpoint بررسی شود.
4. Architecture Map بررسی شود.
5. Roadmap بررسی شود.
6. Git History بررسی شود.

فقط در صورت عدم امکان بازیابی وضعیت واقعی، Recovery Procedure اجرا شود.

---

# 4. RECOVERY RULE

اگر آخرین Checkpoint در Context مکالمه موجود نباشد:

نباید حدس زده شود.

باید وضعیت واقعی پروژه از منابع قابل اعتماد بازیابی شود.

ترتیب بازیابی:

1. GitHub Repository
2. Current Branch
3. Latest Commit
4. Git History
5. Project Control Documents
6. Roadmap
7. Architecture Documentation
8. Repository Structure
9. Active Entry Point
10. Active Dependency Flow
11. Tests
12. Latest Runtime Evidence

اگر وضعیت دقیق قابل تشخیص نباشد:

یک Recovery Checkpoint ساخته شود.

عنوان:

> RECOVERY CHECKPOINT

و در آن موارد نامشخص صریحاً نوشته شود.

هرگز وضعیت نامعلوم به‌صورت قطعی گزارش نشود.

---

# 5. GITHUB FIRST PRINCIPLE

GitHub منبع اصلی بررسی وضعیت واقعی Repository است، زمانی که دسترسی به Repository وجود دارد.

قبل از هر تصمیم مهم، باید وضعیت واقعی Repository بررسی شود.

موارد ضروری:

- Repository URL
- Current Branch
- Latest Commit
- Commit Date
- Working Tree State در صورت دسترسی
- Recent Commits
- Open Pull Requests
- Open Issues در صورت مرتبط بودن
- GitHub Actions / Checks
- Project Control Documents
- Architecture Documents
- Roadmap
- Current Source Tree

اگر GitHub در دسترس است:

نباید از کاربر خواسته شود کل پروژه را دوباره Copy/Paste کند، مگر اینکه:

- فایل موردنظر در Repository موجود نباشد.
- Branch محلی با GitHub متفاوت باشد.
- تغییرات Local هنوز Push نشده باشند.
- فایل موردنظر در وضعیت Git ثبت نشده باشد.
- Permission یا دسترسی Repository مانع بررسی باشد.

---

# 6. GITHUB CONTINUITY PRINCIPLE

هر تغییر مهم پروژه باید تا حد امکان در Git ثبت شود.

هدف:

GitHub باید بتواند وضعیت پروژه را حتی در صورت از دست رفتن Context مکالمه بازسازی کند.

برای این منظور Repository باید شامل Control Documents باشد.

حداقل اسناد پیشنهادی:

```text
BA-MASTER-PROTOCOL-V4.md
PROJECT-CONTROL.md
PROJECT-ROADMAP.md
ARCHITECTURE.md
ACTIVE-ARCHITECTURE.md
LEGACY-MAP.md
DECISIONS.md
CHECKPOINTS.md
CURRENT-STATE.md

نام فایل‌ها می‌تواند در صورت وجود ساختار متفاوت تغییر کند، اما نقش آن‌ها باید حفظ شود.

7. SINGLE SOURCE OF TRUTH

برای هر نوع اطلاعات فقط یک منبع اصلی وجود داشته باشد.

نمونه:

Project Governance
→ BA-MASTER-PROTOCOL-V4.md

Current State
→ CURRENT-STATE.md

Roadmap
→ PROJECT-ROADMAP.md

Architecture
→ ARCHITECTURE.md

Active Architecture
→ ACTIVE-ARCHITECTURE.md

Legacy
→ LEGACY-MAP.md

Architectural Decisions
→ DECISIONS.md

Checkpoint History
→ CHECKPOINTS.md

نباید یک تصمیم مهم در چند فایل با نسخه‌های متفاوت ثبت شود.

اگر تعارض وجود داشت:

Git state واقعی
Current State
Latest Checkpoint
Architecture
Roadmap
سایر اسناد

بررسی شوند.

در صورت تعارض، وضعیت واقعی Repository بر متن قدیمی ترجیح دارد.

8. MASTER PROTOCOL AUTHORITY

این سند قوانین سطح بالای پروژه را تعریف می‌کند.

اما این سند نباید جایگزین وضعیت واقعی پروژه شود.

یعنی:

Master Protocol
→ قوانین و اصول

Project Control
→ وضعیت و کنترل

Roadmap
→ مسیر

Architecture
→ ساختار

Checkpoint
→ نقطه زمانی پروژه

GitHub
→ وضعیت واقعی کد

هیچ‌کدام نباید نقش دیگری را بدون دلیل بر عهده بگیرند.

9. PROJECT SCOPE CONTROL

Scope فعلی پروژه باید صریحاً مشخص باشد.

هر قابلیت جدید باید قبل از توسعه بررسی شود.

اگر قابلیت خارج از Scope فعلی است:

STATUS: OUT OF SCOPE

ثبت شود.

نباید به‌صورت خودکار وارد توسعه شود.

برای اضافه کردن قابلیت جدید:

نیازمندی مشخص شود.
تأثیر معماری بررسی شود.
تأثیر Data Model بررسی شود.
تأثیر Testing بررسی شود.
تأثیر Performance بررسی شود.
تأثیر Maintainability بررسی شود.
جای آن در Roadmap مشخص شود.
سپس اجازه توسعه داده شود.
10. NO FEATURE CREEP RULE

در هنگام رفع مشکل معماری یا کدنویسی:

نباید قابلیت جدید اضافه شود.

مثال:

اگر Task:

Refactor Financial Mapping

است، نباید همزمان:

UI جدید
تحلیل تکنیکال
Machine Learning
Portfolio Optimization
Web API
Database Layer

اضافه شود.

مگر اینکه صراحتاً در Scope همان Task تعریف شده باشد.

11. PROJECT PHASES

پروژه باید به مراحل منطقی تقسیم شود.

مراحل پیشنهادی:

PHASE 0
Project Governance

PHASE 1
Repository Audit

PHASE 2
Architecture Discovery

PHASE 3
Active / Legacy Separation

PHASE 4
Canonical Data Layer

PHASE 5
Domain Model Stabilization

PHASE 6
Forecast Engine Stabilization

PHASE 7
Analysis Engine

PHASE 8
Valuation Engine

PHASE 9
Risk Analysis

PHASE 10
Reporting Pipeline

PHASE 11
Testing and Validation

PHASE 12
Production Hardening

هیچ Phase نباید صرفاً به دلیل زمان یا فشار کاری رد شود.

12. CURRENT PHASE IDENTIFICATION

در هر لحظه باید دقیقاً مشخص باشد:

CURRENT PHASE
CURRENT TASK
LAST COMPLETED TASK
NEXT TASK
BLOCKER

اگر این اطلاعات مشخص نیست:

نباید حدس زده شود.

ابتدا وضعیت بررسی شود.

13. TASK CONTINUITY

هر Task باید دارای:

Task ID
عنوان
هدف
Scope
فایل‌های مرتبط
پیش‌نیازها
معیار تکمیل
تست
وضعیت

باشد.

وضعیت:

PLANNED
IN PROGRESS
BLOCKED
WAITING FOR USER
TESTING
COMPLETED
ABANDONED
14. RUNNING APP REQUEST RULE

اگر کاربر اعلام کند:

Running app request

ابتدا باید بررسی شود که این عبارت مربوط به کدام Task فعال است.

اگر مربوط به Task فعال باشد:

همان Task ادامه پیدا کند.

Audit دوباره شروع نشود.

اگر Task قابل تشخیص نباشد:

ابتدا وضعیت گزارش شود.

حدس ممنوع است.

15. AUDIT RULE

Audit فقط زمانی دوباره اجرا شود که:

Scope Audit جدید تعریف شده باشد.
Repository تغییر اساسی کرده باشد.
Branch تغییر کرده باشد.
معماری تغییر کرده باشد.
Checkpoint معتبر وجود نداشته باشد.
وضعیت واقعی قابل بازیابی نباشد.

در غیر این صورت:

Audit تکراری ممنوع است.

16. REPOSITORY AUDIT SCOPE

Audit کامل باید موارد زیر را بررسی کند:

Repository Structure
Entry Points
Imports
Dependency Graph
Active Flow
Dead Code
Duplicate Code
Duplicate Responsibilities
Hard-Coded Values
Configuration
Environment Variables
Error Handling
Logging
Data Models
External Adapters
Parsers
Financial Mapping
Forecasting
Analysis
Valuation
Reporting
Tests
Legacy Files
Unused Files
Circular Dependencies
Tight Coupling
Hidden Side Effects
Global State
Technical Debt
17. DUPLICATE CODE RULE

یکی از اولویت‌های اصلی Audit:

شناسایی کدهای تکراری است.

تکرار ممکن است در:

چند فایل
چند کلاس
چند تابع
چند ماژول
چند Parser
چند Adapter
چند Engine

وجود داشته باشد.

اگر دو قطعه کد وظیفه یکسان دارند:

ابتدا مشخص شود:

Which one is Active?
Which one is Legacy?
Which one is Canonical?

سپس:

Active حفظ شود.
Legacy علامت‌گذاری شود.
پیاده‌سازی موازی جدید ایجاد نشود.
18. DUPLICATE RESPONSIBILITY RULE

تکرار فقط کد مشابه نیست.

اگر چند ماژول مسئولیت یکسان دارند، حتی اگر کد آن‌ها متفاوت باشد، Duplicate Responsibility محسوب می‌شود.

مثال:

financial_mapper.py
financial_concept_mapper.py
financial_mapping_engine.py

اگر هر سه بخشی از Mapping یکسان را انجام دهند، باید مسئولیت آن‌ها تفکیک شود.

اصل:

هر مسئولیت اصلی باید یک Owner مشخص داشته باشد.

19. SINGLE RESPONSIBILITY

هر ماژول باید مسئولیت مشخص داشته باشد.

مثال:

Adapter
→ دریافت و تبدیل داده خارجی

Parser
→ استخراج داده از ساختار خام

Mapper
→ تبدیل مفهوم داده به Canonical Concept

Domain Model
→ نمایش داده استاندارد

Forecast
→ پیش‌بینی

Analysis
→ تحلیل

Valuation
→ ارزش‌گذاری

Report
→ نمایش نتیجه

یک فایل نباید همزمان:

Scraping
Parsing
Mapping
Forecasting
Valuation
Printing

را انجام دهد.

20. HARD-CODE AUDIT

Hard-Codeهای باقی‌مانده باید شناسایی شوند.

موارد مشکوک:

Symbolهای ثابت
URLهای ثابت
Thresholdهای مالی
PE ثابت
نام شرکت
مسیر فایل
تاریخ
مقادیر مالی
Mappingهای ثابت
Credentials
API Keys
Configuration

اما همه Hard-Codeها بد نیستند.

موارد ثابت واقعی می‌توانند Hard-Code باقی بمانند.

مثال:

Mathematical constants
Protocol constants
Enum values
Immutable business rules

اصل:

Hard-Code فقط زمانی حذف شود که واقعاً Configuration یا Domain Rule است.

21. CONFIGURATION RULE

Configuration نباید در سراسر کد پخش شود.

موارد قابل تنظیم باید در یک محل مشخص باشند.

مثال:

Base PE
Forecast Horizon
Risk Threshold
Margin Threshold
API Endpoint
Timeout
Retry Count

اما Business Ruleهای اصلی نباید بدون دلیل به Configuration تبدیل شوند.

22. SECRET MANAGEMENT

هیچ Secret نباید داخل Repository ثبت شود.

ممنوع:

API Key
Password
Token
Credential
Private Key

باید از:

Environment Variables
.env
Secret Manager

استفاده شود.

فایل .env نباید Commit شود.

23. ACTIVE VS LEGACY

پروژه همیشه باید دو بخش داشته باشد:

ACTIVE
LEGACY / ARCHIVE

Active:

کدی که در مسیر اصلی اجرای پروژه استفاده می‌شود.

Legacy:

کد قدیمی
نسخه قبلی
آزمایشی
Deprecated
Unused

Legacy نباید بدون دلیل حذف شود.

24. LEGACY RULE

Legacy نباید وارد Dependency Flow اصلی شود.

اگر Active به Legacy وابسته است:

این وضعیت باید به‌عنوان Technical Debt ثبت شود.

هدف:

کاهش تدریجی وابستگی Active به Legacy.

25. LEGACY DELETE RULE

حذف Legacy فقط زمانی انجام شود که:

استفاده نشدن آن اثبات شود.
Dependency آن بررسی شود.
جایگزین Active مشخص باشد.
Rollback ممکن باشد.
تصمیم در DECISIONS.md ثبت شود.
26. ARCHITECTURE TARGET

معماری هدف:

Raw External Data
        ↓
Adapters / Parsers
        ↓
Canonical Domain Models
        ↓
Forecast / Normalization
        ↓
Analysis
        ↓
Valuation
        ↓
Risk Analysis
        ↓
Final Report
27. DATA FLOW

جریان داده باید قابل ردیابی باشد.

از:

External Source

تا:

Final Report

نباید داده به‌صورت مخفی یا غیرقابل پیش‌بینی عبور کند.

28. TSETMC DATA FLOW
Raw TSETMC
    ↓
TSETMC Adapter
    ↓
CompanyIdentity
    ↓
MarketSnapshot
    ↓
Company Domain
29. CODAL DATA FLOW
Raw Codal
    ↓
Codal Adapter
    ↓
Codal Parser
    ↓
Financial Mapping
    ↓
Canonical Financial Data
    ↓
Financial Domain Model
30. CANONICAL DATA PRINCIPLE

داده خام External نباید مستقیماً در کل سیستم پخش شود.

هر External Adapter باید داده را به مدل استاندارد تبدیل کند.

31. CANONICAL MODEL

Canonical Model باید:

مستقل از منبع خارجی باشد.
پایدار باشد.
قابل تست باشد.
قابل استفاده توسط چند Consumer باشد.

Consumer نباید مجبور باشد ساختار خام Codal یا TSETMC را بشناسد.

32. ENTRY POINT

Entry Point اصلی پروژه باید مشخص باشد.

هدف نهایی:

main.py

یا Entry Point معادل:

Input Symbol
    ↓
Market Data
    ↓
Financial Data
    ↓
Canonical Domain
    ↓
Forecast
    ↓
Analysis
    ↓
Valuation
    ↓
Risk
    ↓
Report
33. MAIN.PY RULE

main.py باید تا حد امکان Thin باشد.

نباید محل اصلی:

Business Logic
Financial Mapping
Forecast Logic
Valuation Formula
Parsing

باشد.

وظیفه اصلی:

Orchestration.

34. CORE ENGINE RULE

تا زمانی که Dependency Flow کامل بررسی نشده:

core/analyzer_engine.py

نباید بازنویسی گسترده شود.

ابتدا:

Import Graph
Call Graph
Data Flow
Consumer Map

بررسی شود.

35. FINANCIAL ANALYSIS BASIS

مبنای اصلی تحلیل:

آخرین گزارش معتبر و جدید Codal.

گزارش‌های قدیمی برای:

Trend
Growth
Comparison
Quality Check

استفاده می‌شوند.

36. FIVE-YEAR TREND RULE

روند پنج‌ساله فعلاً خارج از Scope است.

نباید خودسرانه وارد پروژه شود.

اگر در آینده لازم شد:

باید به‌عنوان Feature یا Scope Change ثبت شود.

37. PRIMARY ANALYSIS PERIOD

تمرکز اصلی:

دوره مالی یک‌ساله.

داده‌های کوتاه‌تر می‌توانند برای:

Trend
Seasonality
Risk
Momentum

استفاده شوند.

اما مبنای اصلی تحلیل باید با آخرین گزارش معتبر سازگار باشد.

38. TSETMC P/E RULE

P/E آماده TSETMC استفاده نشود.

محاسبه:

Forward P/E =
Market Value / Forecasted Net Profit
39. TSETMC DATA

TSETMC برای:

Symbol
Company Name
Instrument Code
Last Price
Closing Price
Shares
Market Value

استفاده شود.

40. MARKET VALUE

Market Value باید از داده بازار یا محاسبه معتبر به دست آید.

در صورت نیاز:

Market Value =
Price × Shares

واحدها باید مشخص و یکسان باشند.

41. FORECAST PRINCIPLE

Forecast باید تا حد امکان بر اساس داده واقعی باشد.

نباید صرفاً با یک ضریب ثابت و بدون بررسی کیفیت سود انجام شود.

42. NON-RECURRING INCOME

باید شناسایی شود:

فروش دارایی
سود غیرعادی
درآمد یک‌باره
سود تسعیر غیرتکرارشونده
سایر درآمدهای غیرتکراری

این موارد نباید بدون بررسی وارد سود پایدار Forecast شوند.

43. NON-OPERATING INCOME

موارد:

سود بانکی
سود سهام
درآمد سرمایه‌گذاری
فروش دارایی

باید بررسی شوند.

فقط در صورت وجود شواهد تکرارشوندگی، در Forecast پایدار لحاظ شوند.

44. MARGIN RISK

کاهش ناگهانی و معنادار Margin باید بررسی شود.

علل احتمالی:

کاهش قیمت فروش
افزایش هزینه
کاهش حجم فروش
تغییر Product Mix
هزینه غیرعادی

نباید صرفاً با یک Threshold ساده تصمیم‌گیری شود.

45. SALES DECLINE RULE

اگر فروش سه ماه متوالی کاهش داشته باشد:

Fundamental Stop-Loss Warning

ممکن است فعال شود.

این Warning باید بر اساس داده معتبر دوره‌ای محاسبه شود.

46. PROFIT MARGIN RISK

کاهش ناگهانی و معنادار Margin:

Fundamental Risk Warning

ایجاد می‌کند.

47. HOLDING / INVESTMENT COMPANY RULE

برای شرکت‌های سرمایه‌گذاری و هلدینگ‌ها:

ریسک باید با توجه به شرکت‌های تابعه مهم بررسی شود.

اگر چند شرکت تابعه مهم وارد وضعیت Stop-Loss شوند:

ریسک شرکت مادر باید افزایش یابد.

48. VALUATION METRICS

شاخص‌های اصلی:

Forward P/E
Forward P/S
Forward P/D
P/A
P/B
49. VALUATION FORMULAS
P/E =
Market Value / Forecasted Net Profit
P/S =
Market Value / Forecasted Sales
P/A =
Market Value / Total Assets
P/B =
Market Value / Equity

P/D باید بر اساس تعریف دقیق Dividend مورد استفاده پروژه محاسبه شود.

50. P/A AND P/B WARNING

اگر P/A یا P/B بالا باشد:

احتمال عدم تجدید ارزیابی دارایی‌ها باید بررسی شود.

این یک Warning تحلیلی است، نه نتیجه قطعی.

51. BASE PE

برای Base Case:

PE = 7

قابل استفاده است.

اما اگر Architecture جدید منطق دیگری تعریف کرده باشد:

Architecture جدید اولویت دارد.

52. ANALYSIS VS VALUATION

Analysis و Valuation نباید یکی باشند.

Analysis:

کیفیت سود
رشد
ریسک
عملکرد

Valuation:

P/E
P/S
P/B
P/A
P/D
53. RISK ENGINE

Risk باید خروجی ساختاریافته داشته باشد.

مثال:

RiskLevel
RiskType
Severity
Reason
Evidence
54. WARNING VS ERROR

Warning:

سیستم می‌تواند ادامه دهد.

Error:

سیستم نمی‌تواند نتیجه معتبر تولید کند.

این دو نباید مخلوط شوند.

55. ERROR HANDLING

خطاها باید:

قابل تشخیص
قابل ثبت
قابل Debug
قابل تست

باشند.

ممنوع:

except:
    pass

مگر با دلیل بسیار مشخص.

56. LOGGING

Logging باید:

قابل کنترل
سطح‌بندی شده
معنی‌دار

باشد.

سطوح:

DEBUG
INFO
WARNING
ERROR
CRITICAL
57. DEBUG OUTPUT

Debug Output نباید با Final Report مخلوط شود.

برای Debug:

DEBUG

برای User:

REPORT
58. OUTPUT CONTRACT

Final Report باید ساختار مشخص داشته باشد.

مثلاً:

Company Identity
Market Data
Financial Summary
Forecast
Analysis
Risk
Valuation
Conclusion
59. NO HIDDEN LOGIC

Business Logic نباید در:

print
formatting
UI
CLI

پنهان شود.

60. TYPE SAFETY

در صورت امکان:

Type Hints
Dataclasses
Explicit Models

استفاده شود.

61. DATA VALIDATION

داده ورودی باید Validate شود.

موارد:

Missing Values
Negative Values
Unit Mismatch
Currency Mismatch
Period Mismatch
Duplicate Records
62. UNIT CONSISTENCY

واحدهای:

ریال
تومان
میلیون
میلیارد

باید صریح باشند.

تبدیل واحد باید در یک لایه مشخص انجام شود.

63. DATE CONSISTENCY

تاریخ‌ها باید استاندارد شوند.

گزارش‌ها باید دارای:

Fiscal Period
Report Date
Publication Date

باشند.

64. PERIOD COMPARISON

مقایسه دوره‌ها باید:

هم‌دوره
هم‌واحد
هم‌تعریف

باشد.

65. FINANCIAL MAPPING

Financial Mapping یکی از حساس‌ترین بخش‌های پروژه است.

Mapping باید:

قابل تست
قابل Trace
قابل Debug

باشد.

66. MAPPING TRACEABILITY

هر مقدار مالی باید قابل ردیابی باشد:

Source Row
→ Source Label
→ Canonical Concept
→ Domain Field
67. MAPPING FALLBACK

Fallback Mapping باید کنترل‌شده باشد.

نباید با حدس نامطمئن داده اشتباه به Concept اشتباه متصل شود.

68. MAPPING CONFIDENCE

در صورت امکان Mapping باید Confidence داشته باشد:

HIGH
MEDIUM
LOW

Mapping کم‌اطمینان باید قابل مشاهده باشد.

69. PARSER RESPONSIBILITY

Parser فقط باید داده را استخراج کند.

Parser نباید Forecast یا Valuation انجام دهد.

70. ADAPTER RESPONSIBILITY

Adapter:

اتصال
دریافت
تبدیل اولیه

را انجام می‌دهد.

Business Logic نباید در Adapter قرار گیرد.

71. FORECAST RESPONSIBILITY

Forecast Engine:

داده تاریخی
کیفیت داده
Trend
Recurrence

را بررسی می‌کند.

72. ANALYSIS RESPONSIBILITY

Analysis Engine:

رشد
سودآوری
ریسک
کیفیت عملکرد

را تحلیل می‌کند.

73. VALUATION RESPONSIBILITY

Valuation Engine:

محاسبه شاخص‌های ارزش‌گذاری.

74. REPORT RESPONSIBILITY

Report Layer:

نتیجه نهایی را نمایش می‌دهد.

75. NO PARALLEL IMPLEMENTATION

قبل از ایجاد ماژول جدید:

بررسی شود آیا مسئولیت مشابه قبلاً وجود دارد.

اگر وجود دارد:

ماژول جدید ایجاد نشود.

76. REFACTOR RULE

Refactor باید:

کوچک
مرحله‌ای
قابل تست

باشد.

Refactor بزرگ بدون Checkpoint ممنوع.

77. BIG BANG REWRITE RULE

بازنویسی کامل فقط زمانی مجاز است که:

Architecture فعلی بررسی شده باشد.
Dependency Flow مشخص باشد.
Active / Legacy مشخص باشد.
Data Contract مشخص باشد.
Rollback ممکن باشد.
Test Baseline موجود باشد.
78. REWRITE STRATEGY

در صورت نیاز به بازنویسی:

ترجیح:

Strangler Pattern

یعنی:

Old Component
    ↓
New Component
    ↓
Validation
    ↓
Switch Active Path
79. TESTING PYRAMID

ترتیب:

Unit
Component
Integration
End-to-End
80. TEST RULE

هر تغییر مهم باید تست شود.

اگر تست انجام نشده:

نباید وضعیت:

COMPLETED

ثبت شود.

می‌تواند:

IMPLEMENTED
WAITING FOR TEST

باشد.

81. POWERSHELL WAITING

اگر کاربر باید دستور PowerShell اجرا کند:

تا نتیجه دریافت نشده:

موفقیت فرض نشود.
شکست فرض نشود.
همان کار تکرار نشود.
Checkpoint جدید ساخته نشود.
82. USER ACTION

اگر اقدام کاربر لازم است:

دستور دقیق ارائه شود.

مثال:

python main.py درهآور
83. TEST EVIDENCE

نتیجه تست باید ثبت شود:

Command
Input
Output
Expected
Actual
Status
84. REGRESSION TEST

هر اصلاح مهم باید بررسی کند:

آیا قابلیت قبلی شکسته است؟

85. RUNTIME EVIDENCE

خروجی واقعی برنامه معتبرتر از فرضیات است.

اما Runtime Output باید با Code و Test مقایسه شود.

86. NO ASSUMPTION RULE

هرگز نگوییم:

احتمالاً درست است

و آن را به‌عنوان:

Verified

ثبت نکنیم.

87. PROGRESS PERCENTAGE

درصد پیشرفت فقط تخمینی است.

نباید ساختگی باشد.

درصد باید بر اساس:

Scope
Completed Tasks
Remaining Tasks
Architecture Maturity
Test Coverage

تخمین زده شود.

88. CHECKPOINT SYSTEM

Checkpoint قلب سیستم Continuity است.

هر تغییر مهم باید Checkpoint داشته باشد.

89. CHECKPOINT ID

فرمت:

BOURSE-XXXX

یا:

BOURSE-YYYYMMDD-XXX
90. CHECKPOINT CONTENT

هر Checkpoint باید شامل:

ID
DATE
PHASE
CURRENT STATE
LAST COMPLETED
CURRENT TASK
ACTIVE ARCHITECTURE
LEGACY
CHANGED FILES
TEST STATUS
KNOWN ISSUES
ARCHITECTURAL DECISIONS
NEXT STEP
PRIORITY
USER ACTION
91. NEXT STEP RULE

هر Checkpoint فقط یک Next Step اصلی داشته باشد.

نه چند مسیر موازی.

92. PRIORITY

اولویت‌ها:

P0 = Blocker / Critical
P1 = High
P2 = Normal
P3 = Low
93. TASK BLOCKER

اگر Task Blocked است:

دلیل دقیق ثبت شود.

94. DECISION LOG

تصمیم‌های معماری مهم باید ثبت شوند.

مثال:

Decision ID
Date
Problem
Options
Decision
Reason
Consequences
95. ARCHITECTURAL DECISION RULE

تصمیم معماری نباید فقط در چت باقی بماند.

باید وارد Repository شود.

96. ROADMAP RULE

Roadmap باید:

مرحله‌ای
اولویت‌بندی شده
قابل اندازه‌گیری

باشد.

97. ROADMAP UPDATE

پس از تکمیل هر Phase:

Roadmap به‌روزرسانی شود.

98. CURRENT STATE

Current State باید وضعیت واقعی فعلی را نشان دهد.

نه هدف آینده را.

99. ARCHITECTURE DOCUMENT

Architecture باید:

Componentها
Data Flow
Dependency Flow
Active Modules

را نشان دهد.

100. ACTIVE ARCHITECTURE MAP

باید مشخص کند:

ENTRY POINT
↓
ORCHESTRATOR
↓
ADAPTERS
↓
PARSERS
↓
MAPPERS
↓
DOMAIN
↓
FORECAST
↓
ANALYSIS
↓
VALUATION
↓
RISK
↓
REPORT
101. DEPENDENCY FLOW

Dependency باید تا حد امکان یک‌طرفه باشد.

لایه بالاتر نباید به جزئیات داخلی لایه پایین وابستگی غیرضروری داشته باشد.

102. CIRCULAR DEPENDENCY

Circular Dependency باید شناسایی و حذف یا مستندسازی شود.

103. GLOBAL STATE

Global Mutable State باید تا حد امکان حذف شود.

104. SIDE EFFECTS

Side Effect باید مشخص باشد.

مثلاً:

Network
File I/O
Database
Cache
105. PURE LOGIC

Business Logic ترجیحاً Pure باشد.

106. CACHING

Cache نباید باعث شود داده قدیمی به‌عنوان داده جدید استفاده شود.

Cache باید:

TTL
Source
Timestamp

داشته باشد.

107. NETWORK RESILIENCE

External Request باید:

Timeout
Retry
Error Handling

داشته باشد.

108. EXTERNAL SOURCE FAILURE

اگر Codal یا TSETMC در دسترس نیست:

خطای مشخص ایجاد شود.

سیستم نباید داده جعلی تولید کند.

109. DATA QUALITY

اگر داده ناقص است:

سیستم باید مشخص کند:

Data Quality: LOW
110. NO SILENT CORRECTION

داده نباید بدون ثبت یا اطلاع، اصلاح شود.

111. FINANCIAL INTEGRITY

اعداد مالی باید:

قابل ردیابی
قابل تکرار
قابل بررسی

باشند.

112. REPRODUCIBILITY

یک Input مشخص باید تا حد امکان خروجی قابل تکرار ایجاد کند.

113. VERSIONING

تغییرات مهم باید در Git ثبت شوند.

114. COMMIT RULE

Commit باید:

کوچک
معنی‌دار
Atomic

باشد.

115. COMMIT MESSAGE

پیام Commit باید مشخص کند:

چه چیزی تغییر کرده است.

مثال:

fix: stabilize financial mapping
refactor: separate forecast from valuation
test: add Codal parser coverage
docs: update architecture map
116. BRANCH RULE

Branch باید مشخص باشد.

قبل از کار:

Current Branch

بررسی شود.

117. BRANCH SAFETY

تغییر مستقیم روی Branch اصلی فقط با آگاهی از وضعیت Repository انجام شود.

118. PULL REQUEST

تغییرات بزرگ ترجیحاً از طریق PR بررسی شوند.

119. CI

اگر CI وجود دارد:

باید بررسی شود.

120. FAILED CHECKS

اگر Check شکست خورده:

ابتدا Root Cause مشخص شود.

نباید صرفاً با تغییرات تصادفی Fix شود.

121. ROOT CAUSE RULE

برای هر Bug:

Symptom
Root Cause
Fix
Regression Test

ثبت شود.

122. NO PATCH LOOP

چرخه:

Error
→ Random Fix
→ New Error
→ Another Fix

ممنوع است.

ابتدا Root Cause.

123. DEBUGGING ORDER

ترتیب:

Reproduce
Observe
Trace
Isolate
Understand
Fix
Test
Regression Test
124. USER CODE REQUEST

وقتی کاربر درخواست تغییر کد می‌کند:

فایل کامل و یکپارچه قابل جایگزینی ارائه شود.

125. NO PARTIAL CODE

ارائه:

Snippet ناقص
Patch ناقص
کد تکه‌ای

برای جایگزینی مستقیم ممنوع است.

126. CODE FILE OUTPUT

اگر فایل کامل درخواست شد:

کل فایل ارائه شود.

نه فقط بخش تغییرکرده.

127. FILE OWNERSHIP

هر فایل باید نقش مشخص داشته باشد.

128. NAMING

نام‌ها باید:

معنی‌دار
یکنواخت
قابل جست‌وجو

باشند.

129. DEAD CODE

Dead Code باید شناسایی شود.

اما حذف آن نیازمند بررسی Dependency است.

130. UNUSED IMPORTS

Importهای بدون استفاده حذف شوند.

131. TODO RULE

TODOهای مهم باید به Task تبدیل شوند.

TODOهای بی‌صاحب نباید انباشته شوند.

132. TECHNICAL DEBT

Technical Debt باید ثبت شود.

مثال:

TD-001
Description
Impact
Priority
Plan
133. TECHNICAL DEBT PRIORITY

اولویت:

Critical
High
Medium
Low
134. DEBT PREVENTION

رفع یک مشکل نباید Technical Debt جدید بزرگ ایجاد کند.

135. COMPLEXITY RULE

اگر دو راه‌حل از نظر فنی مشابه هستند:

راه‌حل ساده‌تر ترجیح دارد.

136. YAGNI

چیزی که فعلاً نیاز نیست:

نباید ساخته شود.

137. DRY

کد تکراری باید کاهش یابد.

اما DRY نباید باعث Abstraction مصنوعی شود.

138. KISS

راه‌حل ساده و قابل نگهداری ترجیح دارد.

139. EXPLICIT OVER MAGIC

رفتارهای مهم باید Explicit باشند.

140. NO MAGIC FALLBACK

Fallbackهای مخفی ممنوع.

141. DOCUMENTATION

Documentation باید:

کوتاه
دقیق
به‌روز

باشد.

142. DOCUMENTATION DRIFT

اگر کد تغییر کرد و Documentation دیگر درست نیست:

Documentation باید به‌روزرسانی شود.

143. CODE AND DOC CONSISTENCY

کد و مستندات نباید متناقض باشند.

144. CURRENT PROJECT PRINCIPLE

هدف نهایی:

TSETMC
→ Market Canonical Layer

Codal
→ Financial Canonical Layer

Canonical Models
→ Company Domain

Company Domain
→ Forecast

Forecast
→ Analysis

Analysis
→ Valuation

Valuation + Risk Analysis
→ Final Report

و:

main.py
→ Clean Entry Point
→ Pipeline Execution
→ Final Report
145. PROJECT CONTROL LOOP

چرخه استاندارد:

CHECK CURRENT STATE
        ↓
VERIFY GITHUB
        ↓
VERIFY CHECKPOINT
        ↓
IDENTIFY ACTIVE TASK
        ↓
IMPLEMENT ONE STEP
        ↓
TEST
        ↓
VERIFY
        ↓
UPDATE CONTROL DOCS
        ↓
CREATE CHECKPOINT
        ↓
SELECT ONE NEXT STEP
146. CONTINUATION ALGORITHM

هنگام دریافت:

ادامه BourseAnalyzer از آخرین Checkpoint

الگوریتم:

1. Locate latest checkpoint
2. Verify repository
3. Verify branch
4. Verify latest commit
5. Verify active architecture
6. Verify current task
7. Verify latest completed task
8. Check whether current task is already completed
9. If incomplete, continue
10. If complete, verify result
11. Run required test
12. Update state
13. Create checkpoint
14. Select one next step
147. IF GITHUB AVAILABLE

اگر GitHub قابل دسترسی است:

دستیار باید خودش وضعیت Repository را بررسی کند.

کاربر نباید مجبور شود:

کل فایل‌ها را Copy کند.
ساختار پروژه را دوباره توضیح دهد.
آخرین Commit را دستی اعلام کند.

مگر در موارد استثنا.

148. IF GITHUB UNAVAILABLE

اگر GitHub در دسترس نیست:

ابتدا مشخص شود چه چیزی قابل دسترسی است.

اگر Context کافی وجود دارد:

از آن استفاده شود.

اگر کافی نیست:

Recovery Mode.

149. IF TASK UNKNOWN

اگر Task فعلی مشخص نیست:

نباید Audit کامل را خودکار شروع کرد.

ابتدا گزارش:

CURRENT TASK: UNKNOWN
EVIDENCE: ...

سپس فقط اقدام لازم برای بازیابی وضعیت.

150. IF RUNNING TASK EXISTS

اگر Task فعال وجود دارد:

همان Task ادامه پیدا کند.

151. IF USER SAYS "CONTINUE"

اگر فقط گفته شود:

ادامه بده

در صورت وجود Checkpoint معتبر:

از آن ادامه داده شود.

152. IF USER OPENS NEW CHAT

چت جدید نباید به معنی شروع پروژه جدید باشد.

اول:

GitHub
Project Control
Checkpoint

بررسی شود.

153. MEMORY LIMIT MITIGATION

به دلیل محدودیت حافظه بلندمدت مکالمه:

اطلاعات مهم نباید فقط در Chat باقی بمانند.

اطلاعات مهم باید در Repository ثبت شوند.

154. CHAT AS TEMPORARY CONTEXT

Chat:

Context موقت.

GitHub:

Project Memory.

155. PROJECT MEMORY

Project Memory باید شامل:

Protocol
Roadmap
Architecture
Current State
Decisions
Checkpoints

باشد.

156. CHECKPOINT AS SNAPSHOT

Checkpoint باید Snapshot قابل بازیابی باشد.

157. RECOVERY QUALITY

Checkpoint باید آن‌قدر دقیق باشد که یک Developer جدید بتواند پروژه را ادامه دهد.

158. NO ORPHAN TASK

هیچ Task نباید بدون Status باقی بماند.

159. NO ORPHAN DECISION

تصمیم معماری مهم نباید بدون ثبت باقی بماند.

160. NO ORPHAN MODULE

هر Module باید مشخص باشد:

Active
Legacy
Experimental
Deprecated
161. NO ORPHAN FILE

فایل بدون Owner یا Purpose باید بررسی شود.

162. PROJECT CLEANLINESS

Repository باید به‌مرور تمیز شود.

اما:

Cleanup نباید با Feature Development قاطی شود.

163. CLEANUP TASK

Cleanup باید Task مستقل باشد.

164. REFACTOR VS FEATURE

Refactor:

رفتار را حفظ می‌کند.

Feature:

رفتار جدید اضافه می‌کند.

این دو نباید مخلوط شوند.

165. BUGFIX VS REFACTOR

Bugfix:

رفع رفتار اشتباه.

Refactor:

تغییر ساختار بدون تغییر رفتار.

166. TEST BASELINE

قبل از Refactor بزرگ:

Baseline تست باید ثبت شود.

167. BACKWARD COMPATIBILITY

در صورت امکان رفتارهای معتبر قبلی حفظ شوند.

168. BREAKING CHANGE

Breaking Change باید صریحاً ثبت شود.

169. DATA CONTRACT

تغییر Domain Model باید با Consumerها بررسی شود.

170. API CONTRACT

اگر API وجود دارد:

Contract باید مشخص باشد.

171. MODEL CONTRACT

Canonical Model باید پایدار باشد.

172. MODEL EVOLUTION

تغییر Model باید:

Impact Analysis
Tests
Migration

داشته باشد.

173. FINANCIAL MODEL SAFETY

هیچ اصلاح مالی نباید بدون بررسی واحدها و دوره‌ها انجام شود.

174. PROFIT QUALITY

Forecast باید Quality of Earnings را در نظر بگیرد.

175. GROWTH ANALYSIS

Growth باید بر اساس داده قابل مقایسه باشد.

176. REVENUE ANALYSIS

Sales باید:

Current
Historical
Forecast

تفکیک شود.

177. PROFIT ANALYSIS

Profit باید:

Reported
Normalized
Forecast

تفکیک شود.

178. NORMALIZED PROFIT

سود Normalized نباید با سود Reported اشتباه شود.

179. NON-RECURRING ADJUSTMENT

Adjustmentها باید قابل توضیح باشند.

180. FORECAST TRANSPARENCY

Forecast باید نشان دهد:

Input
Assumption
Formula
Output
181. VALUATION TRANSPARENCY

Valuation باید قابل محاسبه مجدد باشد.

182. REPORT TRANSPARENCY

Final Report باید قابل Trace باشد.

183. NO FALSE PRECISION

اگر داده تقریبی است:

نباید با Precision کاذب نمایش داده شود.

184. UNKNOWN VALUES

اگر مقدار ناشناخته است:

N/A
Unknown
Unavailable

استفاده شود.

صفر نباید جای Unknown قرار گیرد.

185. ZERO VS MISSING

این دو متفاوت‌اند:

0

و:

Missing
186. NULL HANDLING

Null باید صریح مدیریت شود.

187. VALIDATION FAILURE

اگر داده Validation را رد کرد:

باید Error یا Warning مناسب ایجاد شود.

188. REPORT QUALITY

Report باید:

واضح
قابل اعتماد
قابل ردیابی

باشد.

189. FINAL OUTPUT PRINCIPLE

کاربر باید بتواند بفهمد:

What happened?
Why?
Based on what data?
What is forecast?
What is risk?
What is valuation?
190. NO BLACK BOX

تا حد امکان Logic اصلی نباید Black Box باشد.

191. PROJECT MATURITY

مراحل بلوغ:

Code Exists
↓
Code Runs
↓
Architecture Stable
↓
Data Reliable
↓
Tests Reliable
↓
Output Trustworthy
↓
Production Ready
192. DEFINITION OF DONE

Task زمانی Done است که:

Code complete
Architecture aligned
Tests passed
Regression checked
Documentation updated if needed
Checkpoint updated

باشد.

193. PHASE DONE

Phase زمانی Done است که:

تمام Taskهای ضروری آن Phase تکمیل شده باشند.

194. PROJECT DONE

Project زمانی Done است که:

Scope تعریف‌شده تکمیل شده باشد.

نه اینکه تمام قابلیت‌های ممکن جهان اضافه شده باشند.

195. CHANGE CONTROL

هر تغییر مهم باید:

Why?
What?
Where?
Impact?
Test?

مشخص داشته باشد.

196. ONE STEP POLICY

در هر لحظه:

یک قدم اصلی.

197. NO PARALLEL WORKSTREAMS

مگر با دلیل مشخص.

198. PRIORITY ORDER

ترتیب پیش‌فرض:

P0 Blockers
↓
Architecture Integrity
↓
Data Integrity
↓
Core Correctness
↓
Testing
↓
Technical Debt
↓
Performance
↓
Features
199. ARCHITECTURE BEFORE FEATURES

تا زمانی که Architecture Active تثبیت نشده:

Feature جدید توسعه داده نشود.

200. DATA BEFORE ANALYSIS

داده نادرست:

تحلیل نادرست.

بنابراین:

Data Integrity اولویت دارد.

201. TEST BEFORE CLAIM

بدون تست:

ادعای موفقیت قطعی ممنوع.

202. EVIDENCE BEFORE DECISION

تصمیم باید بر اساس Evidence باشد.

203. NO GUESSING

در صورت نبود Evidence:

Unknown

اعلام شود.

204. PROJECT STATUS REPORT

Status Report باید:

Current Phase
Progress
Last Completed
Current Task
Blocker
Next Step

را نشان دهد.

205. CHECKPOINT TEMPLATE
CHECKPOINT
ID: BOURSE-XXXX

DATE:
YYYY-MM-DD

PHASE:
...

CURRENT STATE:
...

LAST COMPLETED:
...

CURRENT TASK:
...

CHANGED FILES:
...

ACTIVE ARCHITECTURE:
...

LEGACY / ARCHIVE:
...

TEST STATUS:
...

KNOWN ISSUES:
...

ARCHITECTURAL DECISIONS:
...

NEXT STEP:
...

NEXT STEP PRIORITY:
P0 / P1 / P2 / P3

USER ACTION:
PowerShell command / None

CONTINUATION COMMAND:
«ادامه BourseAnalyzer از آخرین Checkpoint»
206. RECOVERY CHECKPOINT TEMPLATE
RECOVERY CHECKPOINT

REPOSITORY:
...

BRANCH:
...

LATEST COMMIT:
...

PROJECT CONTROL FOUND:
YES / NO

ROADMAP FOUND:
YES / NO

ARCHITECTURE FOUND:
YES / NO

CURRENT TASK:
KNOWN / UNKNOWN

LAST COMPLETED:
...

ACTIVE ARCHITECTURE:
...

LEGACY:
...

KNOWN ISSUES:
...

EVIDENCE:
...

UNCERTAINTIES:
...

NEXT STEP:
...

PRIORITY:
...
207. PROJECT CONTROL FILES

حداقل ساختار پیشنهادی:

/docs
    BA-MASTER-PROTOCOL-V4.md
    PROJECT-CONTROL.md
    PROJECT-ROADMAP.md
    ARCHITECTURE.md
    ACTIVE-ARCHITECTURE.md
    LEGACY-MAP.md
    DECISIONS.md
    CHECKPOINTS.md
    CURRENT-STATE.md

ساختار واقعی Repository اولویت دارد.

208. DOCUMENT UPDATE ORDER

بعد از تغییر مهم:

Code
↓
Tests
↓
Current State
↓
Architecture
↓
Roadmap
↓
Checkpoint

فقط فایل‌هایی که واقعاً تغییر کرده‌اند.

209. CONTROL DOCUMENT CONSISTENCY

اگر اسناد با هم تضاد دارند:

ابتدا وضعیت واقعی Code بررسی شود.

210. GIT AS FINAL EVIDENCE

برای وضعیت Code:

Git مرجع نهایی است.

211. CHAT AS DECISION SOURCE

Chat می‌تواند Decision را ایجاد کند.

اما Decision مهم باید به Repository منتقل شود.

212. NO LOST DECISIONS

هیچ تصمیم مهمی نباید فقط در Chat باقی بماند.

213. PROJECT HANDOFF

اگر پروژه به Developer دیگری منتقل شد:

با مطالعه:

BA-MASTER-PROTOCOL-V4.md
PROJECT-CONTROL.md
CURRENT-STATE.md
ARCHITECTURE.md
PROJECT-ROADMAP.md
CHECKPOINTS.md

باید امکان ادامه وجود داشته باشد.

214. AI CONTINUITY

AI باید از Repository برای بازیابی Context استفاده کند.

215. AI MUST NOT PRETEND

اگر اطلاعات در دسترس نیست:

نباید وانمود کند که می‌داند.

216. AI MUST VERIFY

در صورت دسترسی به GitHub:

اطلاعات مهم باید Verify شوند.

217. AI MUST NOT REPEAT AUDIT

اگر Audit قبلاً انجام شده و Repository تغییر اساسی نکرده:

Audit تکرار نشود.

218. AI MUST FOLLOW CURRENT TASK

Task فعلی اولویت دارد.

219. AI MUST NOT EXPAND SCOPE

Scope نباید بدون اجازه تغییر کند.

220. AI MUST PRESERVE ARCHITECTURE

معماری بدون دلیل تغییر نکند.

221. AI MUST TRACK ACTIVE / LEGACY

قبل از تغییر:

Active و Legacy مشخص شوند.

222. AI MUST DETECT DUPLICATION

کدهای تکراری و مسئولیت‌های تکراری باید در Audit بررسی شوند.

223. AI MUST DETECT HARD-CODE

Hard-Codeهای غیرضروری باید شناسایی شوند.

224. AI MUST DETECT ARCHITECTURAL DRIFT

اگر Implementation از Architecture فاصله گرفته:

ثبت شود.

225. AI MUST DETECT DOCUMENTATION DRIFT

اگر Documentation با Code متفاوت است:

ثبت و اصلاح شود.

226. AI MUST DETECT SCOPE DRIFT

اگر پروژه در حال خروج از Scope است:

هشدار داده شود.

227. AI MUST DETECT COMPLEXITY GROWTH

اگر راه‌حل بیش از حد پیچیده شده:

صریحاً اعلام شود.

228. HONEST ENGINEERING RULE

اگر ایده یا راه‌حل ضعیف است:

باید صریحاً گفته شود.

هدف:

ساخت سیستم قابل اعتماد.

نه صرفاً ادامه دادن کدنویسی.

229. CHALLENGE RULE

هر تصمیم مهم باید در صورت نیاز به چالش کشیده شود.

سؤال:

Do we really need this?
230. NO COSMETIC ARCHITECTURE

صرفاً تغییر نام فایل‌ها Architecture Refactor محسوب نمی‌شود.

231. NO FAKE PROGRESS

تعداد فایل‌های تغییرکرده معیار پیشرفت نیست.

232. REAL PROGRESS

پیشرفت واقعی یعنی:

Correctness
Reliability
Maintainability
Testability
Architectural Integrity
233. PROJECT PERCENTAGE

درصد پیشرفت باید بر اساس Scope واقعی باشد.

مثلاً:

Architecture 70%
Data Layer 80%
Forecast 60%
Valuation 70%
Testing 30%

اما درصدها باید Evidence داشته باشند.

234. NO ARBITRARY PERCENTAGE

درصد ساختگی ممنوع.

235. RELEASE READINESS

قبل از Release:

Tests
Data Validation
Error Handling
Documentation
Regression

بررسی شوند.

236. PRODUCTION HARDENING

Production Hardening شامل:

Logging
Error Handling
Retry
Timeout
Validation
Reproducibility

است.

237. SECURITY

Security باید در تمام مراحل رعایت شود.

238. PERFORMANCE

Performance بعد از Correctness و Architecture اولویت دارد.

239. PREMATURE OPTIMIZATION

Optimization زودهنگام ممنوع.

240. FINAL ARCHITECTURE PRINCIPLE

معماری مطلوب:

External Sources
        ↓
Adapters
        ↓
Parsers
        ↓
Canonicalization
        ↓
Domain Models
        ↓
Forecast / Normalization
        ↓
Analysis
        ↓
Valuation
        ↓
Risk
        ↓
Report
241. FINAL CONTINUATION PRINCIPLE

هر زمان کاربر گفت:

ادامه BourseAnalyzer از آخرین Checkpoint

دستیار باید:

STOP RESTARTING
STOP GUESSING
STOP RE-AUDITING
CHECK GITHUB
CHECK CONTROL DOCS
CHECK CHECKPOINT
IDENTIFY CURRENT TASK
CONTINUE EXACTLY FROM THERE
242. FINAL PROJECT COMMAND

دستور استاندارد:

ادامه BourseAnalyzer از آخرین Checkpoint

243. FINAL PROJECT RULE

اگر فقط یک قانون از این پروتکل باقی بماند:

پروژه را از روی حدس ادامه نده؛ وضعیت واقعی را از GitHub، Control Documents و آخرین Checkpoint بازیابی کن و دقیقاً از همان نقطه ادامه بده.

244. FINAL ARCHITECTURAL RULE

تا زمانی که Architecture Active تثبیت نشده:

No unnecessary rewrite
No parallel implementation
No new feature
No scope expansion
No legacy deletion
245. FINAL ENGINEERING RULE

هر تغییر باید:

Understand
→ Plan
→ Implement
→ Test
→ Verify
→ Document
→ Checkpoint
246. FINAL CONTINUITY RULE

Chat می‌تواند طولانی شود.

Memory می‌تواند محدود باشد.

Context می‌تواند از بین برود.

اما اگر این پروتکل، Project Control، Architecture، Roadmap و Checkpointها در GitHub به‌روز باشند:

پروژه نباید گم شود.

247. FINAL AUTHORITY

این سند:

BA-MASTER-PROTOCOL-V4.md

مرجع اصلی Governance پروژه BourseAnalyzer است.

هر پروتکل قدیمی‌تر:

V1
V2
V3

در صورت تعارض با V4 فاقد اولویت است.

248. VERSION CONTROL

Current:

BA-MASTER-PROTOCOL-V4

Previous:

V1
V2
V3

Status:

SUPERSEDED
249. END STATE

هدف نهایی BourseAnalyzer:

یک سیستم تحلیلی مالی تمیز، قابل اعتماد، قابل تست، قابل توسعه و قابل نگهداری که:

داده بازار را از TSETMC دریافت کند.
داده مالی را از Codal دریافت کند.
داده‌ها را Canonicalize کند.
Domain Model استاندارد داشته باشد.
Forecast قابل توضیح تولید کند.
سودهای غیرتکرارشونده را تشخیص دهد.
تحلیل بنیادی انجام دهد.
ریسک بنیادی را شناسایی کند.
Stop-Loss بنیادی را بررسی کند.
Valuation استاندارد تولید کند.
P/E را مستقل از P/E آماده TSETMC محاسبه کند.
خروجی قابل ردیابی ارائه دهد.
و در تمام مسیر دارای Architecture و Control پایدار باشد.
250. FINAL MASTER FLOW
USER INPUT
    ↓
MAIN ENTRY POINT
    ↓
MARKET DATA ADAPTER
    ↓
TSETMC CANONICAL MARKET DATA
    ↓
CODAL ADAPTER
    ↓
CODAL PARSER
    ↓
FINANCIAL MAPPING
    ↓
CANONICAL FINANCIAL DATA
    ↓
COMPANY DOMAIN
    ↓
NORMALIZATION
    ↓
FORECAST
    ↓
FUNDAMENTAL ANALYSIS
    ↓
RISK ANALYSIS
    ↓
VALUATION
    ↓
FINAL REPORT
    ↓
CHECKPOINT
    ↓
NEXT SINGLE PRIORITY TASK
251. FINAL CHECKPOINT STANDARD

در پایان هر مرحله‌ای که وضعیت پروژه تغییر می‌کند:

CHECKPOINT
ID: BOURSE-XXXX

CURRENT STATE:
[واقعیت فعلی پروژه]

ACTIVE ARCHITECTURE:
[مسیر فعال]

LEGACY / ARCHIVE:
[کدهای قدیمی]

COMPLETED:
[آخرین کار تکمیل‌شده]

CURRENT TASK:
[Task فعال]

TEST STATUS:
[وضعیت واقعی تست]

KNOWN ISSUES:
[مشکلات]

ARCHITECTURAL DECISIONS:
[تصمیم‌ها]

NEXT STEP:
[فقط یک قدم]

NEXT STEP PRIORITY:
[P0 / P1 / P2 / P3]

USER ACTION:
[دستور PowerShell یا None]

CONTINUATION COMMAND:
«ادامه BourseAnalyzer از آخرین Checkpoint»
252. FINAL INSTRUCTION TO AI

هنگام کار روی پروژه BourseAnalyzer:

1. وضعیت واقعی را بررسی کن.
2. حدس نزن.
3. GitHub را در صورت دسترسی بررسی کن.
4. آخرین Checkpoint را پیدا کن.
5. Active و Legacy را جدا کن.
6. Duplicate Code را بررسی کن.
7. Duplicate Responsibility را بررسی کن.
8. Hard-Codeهای غیرضروری را بررسی کن.
9. Scope را حفظ کن.
10. Architecture را بدون دلیل تغییر نده.
11. Task فعلی را ادامه بده.
12. Audit تکراری انجام نده.
13. Feature جدید اضافه نکن مگر در Scope.
14. Root Cause را پیدا کن.
15. تغییرات را تست کن.
16. نتیجه تست را بدون Evidence موفق اعلام نکن.
17. وضعیت پروژه را ثبت کن.
18. فقط یک Next Step انتخاب کن.
19. Checkpoint را به‌روز کن.
20. پروژه را از مسیر اصلی خارج نکن.
253. MASTER COMMAND

برای ادامه پروژه:

ادامه BourseAnalyzer از آخرین Checkpoint

END OF BA-MASTER-PROTOCOL-V4

Protocol Status: FINAL

Project: BourseAnalyzer

Version: V4

END
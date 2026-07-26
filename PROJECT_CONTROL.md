# BourseAnalyzer — PROJECT CONTROL

**Project:** BourseAnalyzer  
**Control Document Version:** 1.0  
**Document Role:** Operational Project Control / Continuity / Task Lock  
**Repository:** `mamaljigar-prog/BourseAnalyzer`  
**Default Branch:** `master`

---

# 1. PURPOSE

This document is the operational control center for the BourseAnalyzer project.

Its purpose is to prevent:

- Loss of project continuity
- Repeating completed audits
- Repeating completed tasks
- Uncontrolled architecture changes
- Scope creep
- Creation of duplicate implementations
- Hard-coded business logic spread across the project
- Confusion between Active and Legacy code
- Losing the current task after a long conversation
- Starting a new task before the current task is complete
- Requiring the user to repeatedly explain the project state

This document works together with:

- `BA-MASTER-PROTOCOL-V4.md`
- `BA-ROADMAP.md`
- `BA-ARCHITECTURE.md`
- `BA-CHECKPOINT.md`

The GitHub repository is the source of truth for actual code.

This document is the source of truth for the current operational project state.

When documentation and actual code disagree:

1. Inspect the actual repository.
2. Determine the real state.
3. Do not guess.
4. Update the control documents after verification.

---

# 2. PRIMARY CONTINUATION COMMAND

The standard command for continuing the project is:

>«ادامه BourseAnalyzer از آخرین Checkpoint — Protocol V4 و PROJECT_CONTROL را مبنا قرار بده و وضعیت Task فعلی را از GitHub و آخرین Commit تطبیق بده.»

When this command is received, the assistant must:

1. Read `PROJECT_CONTROL.md`.
2. Read `BA-MASTER-PROTOCOL-V4.md` if present.
3. Read `BA-CHECKPOINT.md` if present.
4. Inspect the current GitHub branch.
5. Inspect the latest commit.
6. Inspect the actual active code path.
7. Compare documentation against the actual repository.
8. Identify the current Task Lock.
9. Continue the current Task if it is still `IN PROGRESS`.
10. Do not restart a completed audit.
11. Do not start a new task unless the current task is completed, cancelled, blocked, or explicitly changed by the user.
12. Do not change the project scope without explicit user approval.

The assistant must not rely only on conversational memory when repository access is available.

---

# 3. SOURCE OF TRUTH HIERARCHY

When resolving conflicting information, use this priority:

1. Actual GitHub repository code
2. Latest verified Git commit
3. `PROJECT_CONTROL.md`
4. `BA-CHECKPOINT.md`
5. `BA-ARCHITECTURE.md`
6. `BA-ROADMAP.md`
7. `BA-MASTER-PROTOCOL-V4.md`
8. Previous conversation memory

Important:

The Master Protocol defines permanent rules.

The Project Control defines the current operational state.

The Checkpoint defines the latest precise continuation point.

The actual repository defines what code really exists.

---

# 4. CURRENT PROJECT STATE

## Current Phase

**Codal Report Selection / Period Detection / Pipeline Stabilization**

## Current Task Status

**IN PROGRESS**

## Current Task

**Stabilize and consolidate the active Codal Report Selection Pipeline.**

## Task Objective

The current task is to ensure that the active Codal report-selection pipeline is:

- Deterministic
- Consistent
- Maintainable
- Free from unnecessary duplicate responsibilities
- Free from unnecessary duplicate data retrieval
- Correctly separating Annual and Interim reports
- Compatible with the active architecture
- Testable end-to-end

No new product features are to be added during this task.

The current scope must not be expanded.

---

# 5. TASK LOCK RULE

A Task Lock is active whenever:

```text
CURRENT TASK STATUS = IN PROGRESS

When a Task Lock is active:

The current task has priority over all unrelated work.
A new task must not be started automatically.
A new audit must not be started automatically.
Previously completed work must not be repeated without evidence of regression.
The architecture must not be redesigned unnecessarily.
New features must not be added.
Scope must not be expanded.
The project must not jump to another module merely because it is easier or more convenient.

The current task remains locked until one of the following occurs:

Task is completed.
Task is explicitly cancelled by the user.
Task is explicitly replaced by the user.
Task is technically blocked and the blocker is documented.
A higher-priority critical defect requires temporary interruption.

If interrupted, the current task must remain recorded as:

PAUSED

and must not be forgotten.

6. TASK CONTINUITY LOCK

If the latest Checkpoint or Project Control state says:

CURRENT TASK:
X

STATUS:
IN PROGRESS

then the next project session must continue Task X.

The assistant must not:

Start a new Audit
Restart architecture review
Rebuild the project from zero
Rewrite unrelated modules
Introduce new features
Change the roadmap

unless the current task is first completed or explicitly replaced.

The assistant must always answer:

What was the last completed action?
What is the current unfinished task?
What is the next single priority step?

before modifying code.

7. CURRENT TASK COMPLETION CRITERIA

The current Codal Report Selection task is complete only when all of the following are verified:

Active report-selection dependency flow is understood.
Actual callers of report-selection modules are identified.
Active versus Legacy report-selection code is identified.
Annual and Interim classification responsibility is clearly defined.
Duplicate normalization responsibility is identified.
Duplicate Codal retrieval is identified.
Unnecessary duplicate logic is removed or centralized safely.
Existing valid behavior is preserved.
At least one real symbol is tested.
The active application path reaches the correct report-selection logic.
The result is verified through the actual application pipeline.
Test output is recorded.
The Checkpoint is updated.
The next single priority task is defined.

Until these criteria are met:

TASK STATUS = IN PROGRESS
8. LATEST VERIFIED REPOSITORY STATE

The repository currently identified for this project is:

mamaljigar-prog/BourseAnalyzer

Default branch:

master

Latest verified commit at the time this control document was created:

1493eda2e5464cbca99863383abe802244795aeb

Commit message:

improve_report_selection_logic_checkpoint

This information must be re-verified whenever the project is resumed.

Never assume the commit remains the latest commit.

9. LAST COMPLETED WORK

The latest verified work was related to:

Improvement of Codal Report Selection Logic

The project reached a checkpoint around:

Report selection
Annual / Interim distinction
Financial report selection
Codal report retrieval

The task is not considered fully complete.

The next work must continue from this stage.

Do not restart the entire project audit.

10. KNOWN CURRENT ISSUES

The following issues are currently suspected or identified and must be verified against the actual repository before modification:

10.1 Annual / Interim Classification

Report classification remains dependent on report metadata and/or title interpretation.

This must be verified and stabilized.

The classification logic must not be duplicated in multiple unrelated modules.

10.2 Duplicate Codal Retrieval

The current Codal retrieval architecture may retrieve overlapping report sets through separate searches.

Before changing this:

Trace actual callers.
Determine whether the same raw data can be reused.
Confirm that changing retrieval behavior does not break report selection.

Do not optimize blindly.

10.3 Duplicate Normalization Logic

Normalization behavior may exist in more than one location.

Before changing:

Find all implementations.
Identify actual callers.
Determine Active implementation.
Determine Legacy implementation.
Centralize only when behavior can be preserved safely.
10.4 Active / Legacy Ambiguity

Some modules may have overlapping responsibilities.

The assistant must determine:

ACTIVE

versus:

LEGACY / ARCHIVE

before modifying them.

Legacy code must not be deleted without explicit user approval.

11. ACTIVE ARCHITECTURE PRINCIPLE

The target architecture is:

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

For market data:

Raw TSETMC
        ↓
TSETMC Adapter
        ↓
Canonical CompanyIdentity
        ↓
Canonical MarketSnapshot

For Codal data:

Raw Codal
        ↓
Codal Adapter
        ↓
Report Selection
        ↓
Period Classification
        ↓
Financial Parser
        ↓
Canonical Financial Data
        ↓
Company / Financial Models

The final application flow should approach:

main.py
    ↓
Pipeline Entry Point
    ↓
Market Data
    ↓
Financial Data
    ↓
Canonical Models
    ↓
Forecast
    ↓
Analysis
    ↓
Valuation
    ↓
Risk Analysis
    ↓
Final Report
12. ACTIVE VS LEGACY

The project must always distinguish between:

ACTIVE

Code that is part of the actual current execution path.

Active code may be developed and improved.

LEGACY / ARCHIVE

Code that is:

Old
Experimental
Replaced
No longer imported
Historical
Superseded

Legacy code must not be expanded unless there is a documented reason.

Legacy code must not be deleted without explicit user approval.

If two files appear to perform the same responsibility:

Search repository references.
Inspect imports.
Inspect runtime call flow.
Identify Active implementation.
Identify Legacy implementation.
Document the decision.
Modify only the Active implementation unless migration is required.
13. CODE DUPLICATION CONTROL

Before creating a new function, class, module, or service:

The assistant must search the repository for existing implementations of the same or similar responsibility.

The assistant must check:

Function names
Class names
Similar logic
Similar formulas
Similar parsers
Similar normalization
Similar validation
Similar API calls
Similar business rules

If a responsibility already exists:

Reuse it if appropriate.
Extend it if appropriate.
Refactor it if necessary.
Mark competing implementation as Legacy if justified.

Creating a second implementation of the same responsibility is prohibited unless there is a documented architectural reason.

14. HARD-CODE CONTROL

Avoid hard-coded:

Business rules
Financial assumptions
Repeated constants
External identifiers
API behavior
Report classification rules
Thresholds
Magic numbers
Duplicate strings

Before adding a hard-coded value:

Search for existing definitions.
Determine whether the value belongs in a canonical model.
Determine whether it belongs in configuration.
Determine whether it is a true domain constant.
Avoid duplicating the value in multiple modules.

Existing hard-coded values must not be blindly refactored during unrelated tasks.

Refactor only when:

They are directly relevant to the current task.
They create a real bug.
They create architectural duplication.
They prevent correct testing.
They create a significant maintenance risk.
15. ARCHITECTURE CHANGE CONTROL

Before any significant architectural change:

Identify Entry Point.
Identify Dependency Flow.
Identify Active Data Flow.
Identify raw data sources.
Identify Canonical Models.
Identify Forecast layer.
Identify Analysis layer.
Identify Valuation layer.
Identify Risk layer.
Identify Final Report generation.

No architecture rewrite should be performed based only on assumptions.

Do not rewrite:

core/analyzer_engine.py

without first verifying its full dependency flow.

16. SCOPE CONTROL

Current project scope must remain unchanged.

Do not introduce unrelated features during the current task.

Do not reintroduce five-year trend analysis unless explicitly requested.

Do not redesign the entire project while fixing one module.

Do not replace working architecture without technical evidence.

Do not add modules merely because a new module appears cleaner.

Before adding a new module:

Search existing modules.
Check existing responsibilities.
Confirm no Active implementation already exists.
Confirm the new module is architecturally necessary.
17. FINANCIAL ANALYSIS RULES

Primary financial basis:

Latest Valid New Codal Report

Older reports are primarily used for:

Comparison
Trend
Growth
Quality Checks

Five-year trend analysis is currently outside project scope.

Primary analysis focuses on a one-year financial period.

18. TSETMC RULES

TSETMC P/E must not be used as the project's calculated valuation P/E.

The system calculates:

Forward P/E =
Market Value / Forecasted Net Profit

TSETMC may provide:

Symbol
Company Name
Instrument Code
Last Price
Closing Price
Shares
Market Value

External market data must be converted into canonical internal models.

19. FORECAST RULES

Forecast must be based as much as possible on actual financial data.

The system must consider:

Non-recurring profit
Asset sales
Non-operating income
Bank interest
Dividend income
Sudden margin changes
Performance decline

Non-operating income must not be treated as sustainable unless evidence of recurrence exists.

20. VALUATION RULES

Primary metrics:

Forward P/E
Forward P/S
Forward P/D
P/A
P/B

Formulas:

P/E = Market Value / Forecasted Net Profit

P/S = Market Value / Forecasted Sales

P/A = Market Value / Total Assets

P/B = Market Value / Equity

High P/A or P/B may require consideration of unrecognized asset revaluation.

Base-case valuation may use:

PE = 7

unless the active valuation architecture explicitly defines another rule.

21. ANALYTICAL RISK RULES

If sales decline for three consecutive months:

Fundamental Stop-Loss Warning

may be activated.

If profit margin suddenly and materially declines:

Fundamental Risk Warning

should be activated.

For investment companies and holdings:

Major subsidiaries must be considered.

If multiple significant subsidiaries trigger stop-loss conditions:

The parent company's fundamental risk status may increase.

22. TESTING CONTROL

Preferred order:

1. Unit Test
2. Component Test
3. Integration Test
4. End-to-End Test

Every significant code change must be tested as far as practical.

Never claim a test passed without actual evidence.

Never assume PowerShell output.

If the user is asked to execute a command:

Wait for the output.
Do not repeat the same task.
Do not create a new checkpoint while only waiting.
Do not assume success or failure.
23. POWERSHELL WAITING RULE

When waiting for user-provided PowerShell output:

STATUS = WAITING_FOR_USER_TEST_RESULT

During this state:

Do not repeat the operation.
Do not start a new task.
Do not change the current task.
Do not create a new project checkpoint unless project state actually changes.

When output is received:

Analyze it.
Determine pass/fail.
Modify code if necessary.
Test again if required.
Update checkpoint.
24. CHECKPOINT CONTROL

A Checkpoint must record:

Checkpoint ID
Date
Current Phase
Current Task
Task Status
Last Completed Work
Changed Files
Active Architecture
Legacy / Archive
Tests Performed
Test Results
Known Issues
Architectural Decisions
Start Checkpoint
Completion Criteria
Exactly one Next Step
Next Step Priority
User Action
PowerShell command if required
25. CHECKPOINT UPDATE RULE

When project state changes:

Update the Checkpoint.

When only waiting for PowerShell output:

Do not create a new Checkpoint.

The Checkpoint must always describe the actual state.

Never mark a task completed merely because code was written.

A task is complete only after its completion criteria are verified.

26. ONE NEXT STEP RULE

Every active Checkpoint must define exactly one:

NEXT STEP

The next step must be:

Concrete
Prioritized
Technically justified
Testable

It must specify:

What changes
Which file/module
Why
How it will be tested

Do not list multiple competing next steps.

If several tasks exist:

Choose the highest-priority task.

27. PROGRESS CONTROL

Project progress may be expressed as a percentage only when it is based on actual project scope.

Do not invent progress percentages.

Do not use progress percentage as a substitute for a real Checkpoint.

The project state is more important than the percentage.

28. RECOVERY PROCEDURE

If project continuity is lost:

Read PROJECT_CONTROL.md.
Read BA-CHECKPOINT.md.
Read BA-MASTER-PROTOCOL-V4.md.
Inspect current Git branch.
Inspect latest commit.
Inspect recent commits.
Inspect actual active code.
Identify current task.
Compare repository state with documentation.
Do not guess.

If the exact state cannot be established:

Create:

RECOVERY CHECKPOINT

The recovery checkpoint must document:

What is known
What is unknown
What was verified
What cannot be verified
What must be investigated next

Do not restart the entire project unless explicitly required.

29. CHAT CONTINUITY RULE

The project must remain recoverable even if:

The conversation becomes very long.
A new chat is started.
The previous chat is unavailable.
Context is incomplete.
The assistant's conversational memory is incomplete.

The assistant must use repository documents and actual code to reconstruct state.

The user should not be required to manually explain the entire project again.

30. NO-GUESS RULE

If the state cannot be established:

Do not guess.

Do not fabricate:

Last task
Last commit
Last test
Architecture
Completion status
Current branch
Project progress

Instead:

Inspect GitHub.
Inspect project files.
Report uncertainty.
Create Recovery Checkpoint if necessary.
31. CURRENT CHECKPOINT
CHECKPOINT ID
BOURSE-REPORT-SELECTION-01
DATE
2026-07-25
CURRENT PHASE
Codal Report Selection / Period Detection
CURRENT TASK
Stabilize and consolidate the active Codal Report Selection Pipeline
STATUS
IN PROGRESS
LAST COMPLETED WORK
Improved Codal report-selection logic.
CURRENT OBJECTIVE
Verify and stabilize report selection,
Annual / Interim classification,
normalization responsibility,
and Codal retrieval flow.
KNOWN ISSUES
1. Annual / Interim classification requires verification.
2. Codal retrieval may perform overlapping searches.
3. Normalization responsibility may be duplicated.
4. Active / Legacy boundaries require verification.
5. End-to-End validation is still required.
START CHECKPOINT
Latest verified report-selection checkpoint
associated with commit:
1493eda2e5464cbca99863383abe802244795aeb
COMPLETION CRITERIA
1. Active dependency flow verified.
2. Active report-selection implementation identified.
3. Annual / Interim classification responsibility identified.
4. Duplicate normalization identified.
5. Duplicate retrieval identified.
6. Safe consolidation completed where justified.
7. Existing behavior preserved.
8. Real-symbol test completed.
9. End-to-End path verified.
10. Checkpoint updated.
NEXT STEP
Trace the active Codal report-selection dependency flow
and identify the canonical responsibility for:
- report retrieval
- report normalization
- Annual / Interim classification
NEXT STEP PRIORITY
P0
USER ACTION
None
32. PROJECT CONTROL UPDATE POLICY

This file must be updated when:

Current task changes.
Task status changes.
Task is completed.
Task is paused.
Task is blocked.
Architecture changes.
Active / Legacy classification changes.
Important files change.
Major testing results are received.
Next priority changes.
Scope changes by explicit user decision.

Do not update the file merely because a conversation message was exchanged.

Update it when the project state changes.

33. FINAL OPERATIONAL RULE

The project must always answer these five questions:

1. Where are we?
2. What did we just complete?
3. What are we currently doing?
4. Why are we doing it?
5. What is the one next step?

If these five questions cannot be answered from the repository and control documents:

STOP
VERIFY
DO NOT GUESS
34. STANDARD RESUME COMMAND

Use:

ادامه BourseAnalyzer از آخرین Checkpoint

Recommended full continuation instruction:

ادامه BourseAnalyzer از آخرین Checkpoint. ابتدا PROJECT_CONTROL.md و BA-MASTER-PROTOCOL-V4.md را از GitHub بخوان، وضعیت واقعی Repository، Branch و آخرین Commit را بررسی کن، سپس وضعیت Active و Legacy را تطبیق بده. اگر Task فعلی IN PROGRESS است، فقط همان Task را ادامه بده و Audit مجدد انجام نده. قابلیت جدید اضافه نکن و Scope پروژه را تغییر نده. اگر وضعیت Task قابل تشخیص نیست، حدس نزن و ابتدا وضعیت واقعی پروژه را گزارش کن.

END OF PROJECT CONTROL
BourseAnalyzer
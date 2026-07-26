# BourseAnalyzer — PROJECT CONTROL

**Project:** BourseAnalyzer  
**Control Document Version:** 2.0  
**Document Role:** Operational Project Control / Continuity / Task Lock  
**Repository:** `mamaljigar-prog/BourseAnalyzer`  
**Active Branch:** `refactor/canonical-architecture`  
**Default Branch:** `master`

---

# 1. PURPOSE

This document is the operational control center for the BourseAnalyzer project.

Its purpose is to preserve project continuity while keeping project continuation fast and focused.

It prevents:

- Losing the current task
- Repeating completed work
- Restarting audits unnecessarily
- Uncontrolled architecture changes
- Scope creep
- Duplicate implementations
- Confusion between Active and Legacy code
- Forgetting the current Checkpoint
- Starting unrelated work before the current task is complete
- Requiring the user to repeatedly explain the project state

This document works together with:

- `BA-MASTER-PROTOCOL-V4.md`
- `BA-CHECKPOINT.md`
- `BA-ARCHITECTURE.md`
- `BA-ROADMAP.md`

The actual repository code is the source of truth for what exists.

`PROJECT_CONTROL.md` is the source of truth for the current operational task state.

`BA-CHECKPOINT.md` is the source of truth for the precise continuation point.

---

# 2. CORE OPERATING PRINCIPLE

The default behavior is:

```text
CONTINUE

Not:

AUDIT EVERYTHING AGAIN

The project must continue from the latest valid Checkpoint whenever the current Task is still IN PROGRESS.

A deep repository review is performed only when a defined Deep Review Trigger exists.

Therefore:

DEFAULT = CONTINUE FROM CHECKPOINT

DEEP REVIEW = ONLY WHEN TRIGGERED

This rule exists to prevent long conversations from becoming slow because the entire project is repeatedly re-audited.

3. SIMPLE CONTINUATION COMMAND

The standard continuation command is:

ادامه بده

When the user says:

ادامه بده

the assistant must:

Read the current PROJECT_CONTROL.md.
Read the latest BA-CHECKPOINT.md if present.
Identify the current Task.
Identify the Task Status.
Identify the latest completed action.
Identify the single NEXT STEP.
Continue that NEXT STEP.

The assistant must NOT automatically:

Re-audit the entire repository
Re-read the entire architecture
Re-check every GitHub commit
Restart the project audit
Rebuild the dependency map
Review unrelated modules
Start a new task
Add new features
Change project scope

unless a Deep Review Trigger is active.

The assistant must continue directly from the latest valid Checkpoint.

4. CONTINUATION DECISION LOGIC

Use the following decision process:

USER SAYS "ادامه بده"
        ↓
READ PROJECT_CONTROL
        ↓
READ BA-CHECKPOINT
        ↓
IS CURRENT TASK IN PROGRESS?
        ↓
YES
        ↓
IS CHECKPOINT VALID AND SPECIFIC?
        ↓
YES
        ↓
IS THERE A DEEP REVIEW TRIGGER?
        ↓
NO
        ↓
CONTINUE NEXT STEP DIRECTLY

If a Deep Review Trigger exists:

DEEP REVIEW
        ↓
VERIFY ONLY THE RELEVANT AREA
        ↓
UPDATE CHECKPOINT
        ↓
CONTINUE TASK

The project must never perform a full repository audit merely because a new chat started.

5. SOURCE OF TRUTH

Use the following hierarchy only when information conflicts:

Actual repository code
Latest verified commit relevant to the current task
PROJECT_CONTROL.md
BA-CHECKPOINT.md
BA-ARCHITECTURE.md
BA-ROADMAP.md
BA-MASTER-PROTOCOL-V4.md
Previous conversation memory

Important distinction:

Repository = what code actually exists
Project Control = what task is currently active
Checkpoint = where execution should continue
Master Protocol = permanent project rules

When no conflict exists, do not repeatedly re-verify higher-level sources.

6. TASK LOCK

A Task Lock is active when:

CURRENT TASK STATUS = IN PROGRESS

When a Task Lock is active:

The current task has priority.
Unrelated tasks must not start automatically.
New features must not be added.
Scope must not expand.
Completed work must not be repeated without evidence of regression.
Architecture must not be redesigned unnecessarily.
Work must continue from the latest valid Checkpoint.

The current Task Lock remains active until:

Task is completed
Task is explicitly cancelled
Task is explicitly replaced
Task is technically blocked
A critical higher-priority defect temporarily interrupts it

If interrupted:

TASK STATUS = PAUSED

The original task must remain recorded and recoverable.

7. CURRENT TASK
Current Phase

Codal Report Selection / Period Detection / Pipeline Stabilization

Current Task Status

IN PROGRESS

Current Task

Stabilize and consolidate the active Codal Report Selection Pipeline.

Current Objective

Ensure that the active Codal report-selection pipeline is:

Deterministic
Consistent
Maintainable
Correctly separating Annual and Interim reports
Free from unnecessary duplicate retrieval
Free from unnecessary duplicate normalization
Compatible with the active architecture
Testable through the real application path

No new product features are allowed during this task.

The current scope must remain unchanged.

8. CURRENT TASK COMPLETION CRITERIA

The current task is complete only when the following are verified:

Active report-selection dependency flow is understood.
Actual callers are identified.
Active versus Legacy implementation is identified.
Annual / Interim classification responsibility is defined.
Duplicate normalization responsibility is identified.
Duplicate Codal retrieval is identified.
Safe consolidation is completed where technically justified.
Existing valid behavior is preserved.
At least one real symbol is tested.
The real application path reaches the correct report-selection logic.
Test results are recorded.
Checkpoint is updated.
Exactly one next task is defined.

Until all required criteria are verified:

TASK STATUS = IN PROGRESS
9. SINGLE NEXT STEP RULE

Every active Checkpoint must contain exactly one:

NEXT STEP

The Next Step must be:

Concrete
Prioritized
Technically justified
Testable

It must identify:

What is being done
Which file/module is involved
Why it is needed
How it will be tested

Do not provide multiple competing next steps.

If several possible actions exist:

Choose the highest-priority action.
10. DEEP REVIEW TRIGGERS

A Deep Review is NOT performed by default.

Deep Review is required only when one or more of the following conditions exists.

TRIGGER A — Checkpoint Conflict

The current Checkpoint contradicts the actual repository state.

Examples:

File referenced by Checkpoint no longer exists
Commit referenced by Checkpoint cannot be found
Branch changed unexpectedly
Task marked complete but required work is missing

Action:

VERIFY RELEVANT REPOSITORY STATE

Do not audit the entire project.

TRIGGER B — New Code Changes Affect Current Task

A new commit contains changes that directly affect the current Task.

Action:

INSPECT ONLY THE RELEVANT DIFF AND DEPENDENCIES

Do not re-audit unrelated modules.

TRIGGER C — Test Failure

A test related to the current Task fails.

Action:

TRACE THE FAILURE FROM THE ACTUAL EXECUTION PATH

Inspect only the relevant dependency chain.

TRIGGER D — Active / Legacy Conflict

It becomes unclear which implementation is actually active.

Action:

TRACE IMPORTS
TRACE CALLERS
TRACE RUNTIME PATH

Determine Active versus Legacy.

Do not modify code before this is clear.

TRIGGER E — Architectural Contradiction

The current Task cannot be completed using the documented Active Architecture.

Action:

PERFORM TARGETED ARCHITECTURE REVIEW

Review only the affected dependency flow.

Do not redesign the entire architecture automatically.

TRIGGER F — Missing or Invalid Checkpoint

BA-CHECKPOINT.md is missing, corrupted, or too vague to determine:

Current Task
Task Status
Last completed action
Next Step

Action:

RECOVERY REVIEW

Reconstruct only the minimum required state.

TRIGGER G — User Explicitly Requests Audit

If the user explicitly asks for:

Full Audit
Deep Audit
Reconciliation
Architecture Review
GitHub verification
Dependency analysis

then perform the requested review.

Otherwise, continue normally.

11. DEEP REVIEW SCOPE CONTROL

When a Deep Review Trigger occurs:

Do NOT automatically inspect the entire project.

Use this order:

1. Identify the trigger.
2. Identify the affected module.
3. Identify the affected dependency path.
4. Inspect only the required repository area.
5. Verify the relevant facts.
6. Update Checkpoint.
7. Return to normal CONTINUE mode.

The purpose of Deep Review is to resolve uncertainty, not to restart the project.

12. ACTIVE VS LEGACY

The project must distinguish between:

ACTIVE

Code that is part of the actual current execution path.

Active code may be developed and improved.

LEGACY / ARCHIVE

Code that is:

Old
Experimental
Replaced
Superseded
No longer imported
Historical

Legacy code:

Must not be expanded unnecessarily.
Must not be deleted without explicit user approval.
Must not be modified unless required by the current task.

If two implementations appear to perform the same responsibility:

Search references.
Inspect imports.
Inspect actual callers.
Determine runtime path.
Identify Active implementation.
Identify Legacy implementation.
Document the decision.
Modify only the Active implementation unless migration is required.
13. CODE DUPLICATION CONTROL

Before creating a new:

Function
Class
Module
Service
Parser
Adapter

search the repository for an existing implementation.

Check:

Similar functions
Similar classes
Similar parsers
Similar normalization
Similar validation
Similar API calls
Similar formulas
Similar business rules

If an implementation already exists:

Reuse it where appropriate.
Extend it where appropriate.
Refactor it where necessary.
Do not create a parallel implementation without architectural justification.

Duplicate responsibility is prohibited unless there is a documented reason.

14. HARD-CODE CONTROL

Avoid unnecessary hard-coded:

Business rules
Financial assumptions
Repeated constants
External identifiers
Report classification rules
Thresholds
Magic numbers
Duplicate strings

Before adding a hard-coded value:

Search for an existing definition.
Determine whether it is a domain constant.
Determine whether it belongs in configuration.
Avoid duplicating it.

Do not refactor unrelated hard-coded values during the current Task.

Only refactor them if they:

Directly affect the current Task
Cause a real bug
Create architectural duplication
Prevent correct testing
Create significant maintenance risk
15. ARCHITECTURE CONTROL

Target architecture:

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

Codal flow:

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

Application flow:

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

Do not rewrite:

core/analyzer_engine.py

without first verifying its dependency flow.

Architecture changes require technical evidence.

16. SCOPE CONTROL

The current project scope must remain unchanged.

Do not:

Add unrelated features
Reintroduce five-year trend analysis
Redesign the entire project while fixing one module
Replace working architecture without evidence
Add modules merely because they appear cleaner

Before adding a new module:

Search existing modules.
Check existing responsibilities.
Confirm no Active implementation already exists.
Confirm the module is architecturally necessary.
17. FINANCIAL ANALYSIS RULES

Primary financial basis:

Latest Valid New Codal Report

Older reports are used primarily for:

Comparison
Trend
Growth
Quality Checks

Five-year trend analysis is outside current scope.

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

Forecast must rely as much as possible on actual financial data.

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

unless the Active valuation architecture explicitly defines another rule.

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

Unit Test
Component Test
Integration Test
End-to-End Test

Never claim a test passed without evidence.

Never assume PowerShell output.

When the user is asked to execute a command:

Wait for the result.
Do not repeat the operation.
Do not start another task.
Do not assume success or failure.
23. POWERSHELL WAITING STATE

When waiting for user-provided PowerShell output:

STATUS = WAITING_FOR_USER_TEST_RESULT

During this state:

Do not repeat the operation.
Do not start a new task.
Do not change the current Task.
Do not create a new Checkpoint unless project state actually changes.

When output arrives:

Analyze it.
Determine pass/fail.
Modify code if required.
Test again if required.
Update Checkpoint.
24. CHECKPOINT CONTROL

BA-CHECKPOINT.md must contain:

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
Completion Criteria
Exactly one Next Step
Next Step Priority
User Action
PowerShell command if required

The Checkpoint must represent the actual project state.

25. CHECKPOINT UPDATE RULE

Update the Checkpoint when project state changes.

Examples:

Code changed
Test result received
Task progressed
Task completed
Task blocked
Architecture decision changed
Active / Legacy classification changed
Next Step changed

Do NOT update the Checkpoint merely because another chat message was exchanged.

Do NOT create a new Checkpoint while simply waiting for PowerShell output.

Never mark a Task completed merely because code was written.

Completion requires verification against the Task completion criteria.

26. RECOVERY RULE

If the current state can be determined from:

PROJECT_CONTROL.md
+
BA-CHECKPOINT.md

continue directly.

Do not perform a full GitHub audit.

If the state cannot be determined:

RECOVERY MODE

Activate a targeted repository review.

Inspect:

Current branch
Latest relevant commits
Relevant files
Relevant execution path

Do not inspect unrelated parts of the project.

If exact state still cannot be established:

Create:

RECOVERY CHECKPOINT

Document:

What is known
What is unknown
What was verified
What cannot be verified
What must be investigated next

Do not guess.

27. NO-GUESS RULE

Never fabricate:

Last task
Last commit
Last test
Architecture
Completion status
Current branch
Project progress

If information is missing:

STOP
VERIFY
DO NOT GUESS

Verification must be proportional to the uncertainty.

28. CHAT CONTINUITY

The project must remain recoverable if:

The conversation becomes very long
A new chat is started
Previous chat context is unavailable
Assistant conversational memory is incomplete

The primary recovery mechanism is:

PROJECT_CONTROL.md
+
BA-CHECKPOINT.md
+
ACTUAL REPOSITORY WHEN REQUIRED

The user should not need to explain the entire project again.

A new chat does NOT automatically trigger a full audit.

29. CURRENT CHECKPOINT
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

Verify and stabilize:

Report selection
Annual / Interim classification
Normalization responsibility
Codal retrieval flow
KNOWN ISSUES
Annual / Interim classification requires verification.
Codal retrieval may perform overlapping searches.
Normalization responsibility may be duplicated.
Active / Legacy boundaries require verification.
End-to-End validation is still required.
COMPLETION CRITERIA
Active dependency flow verified.
Active report-selection implementation identified.
Annual / Interim classification responsibility identified.
Duplicate normalization identified.
Duplicate retrieval identified.
Safe consolidation completed where justified.
Existing behavior preserved.
Real-symbol test completed.
End-to-End path verified.
Checkpoint updated.
NEXT STEP

Trace the active Codal report-selection dependency flow and identify the canonical responsibility for:

Report retrieval
Report normalization
Annual / Interim classification
NEXT STEP PRIORITY

P0

USER ACTION

None

30. PROJECT CONTROL UPDATE POLICY

Update this file only when operational project state changes significantly.

Update when:

Current Task changes
Task Status changes
Task is completed
Task is paused
Task is blocked
Architecture changes
Active / Legacy classification changes materially
Scope changes by explicit user decision
A major project-control rule changes

Do NOT update this file for every small code change.

Small execution-level changes belong in:

BA-CHECKPOINT.md

This separation is intentional.

PROJECT_CONTROL.md
= Stable operational rules and current high-level Task Lock

BA-CHECKPOINT.md
= Fast-changing execution state and precise continuation point
31. FINAL OPERATING RULE

At any point, the project must be able to answer:

Where are we?
What did we just complete?
What are we currently doing?
Why are we doing it?
What is the one next step?

The answer should normally come from:

PROJECT_CONTROL.md
+
BA-CHECKPOINT.md

If the answer is clear:

CONTINUE

If the answer is unclear:

VERIFY

If the repository contradicts the documents:

TARGETED RECONCILIATION

If the current Task is clear and no Deep Review Trigger exists:

DO NOT AUDIT AGAIN
DO NOT RESTART
CONTINUE THE NEXT STEP
32. STANDARD CONTINUATION COMMAND

The normal user command is simply:

ادامه بده

No additional explanation is required.

The assistant must interpret this as:

Continue BourseAnalyzer from the latest valid Checkpoint.

Read PROJECT_CONTROL.md and BA-CHECKPOINT.md.

Identify the current Task and Task Status.

If the Task is IN PROGRESS and the Checkpoint is valid:
continue the single NEXT STEP directly.

Do not perform a full repository audit.

Do not restart completed work.

Do not add new features.

Do not change scope.

Do not redesign architecture unnecessarily.

Only perform targeted repository verification if a Deep Review Trigger exists.

If the Checkpoint is invalid or insufficient:
enter targeted Recovery Mode.

Never guess.
33. OPERATIONAL MODE SUMMARY

The project operates in one of four modes:

MODE 1 — CONTINUE

Default mode.

Condition:

Checkpoint valid
Task IN PROGRESS
No Deep Review Trigger

Action:

Continue NEXT STEP
MODE 2 — TARGETED VERIFY

Condition:

Relevant uncertainty exists

Action:

Verify only the affected area
MODE 3 — DEEP REVIEW

Condition:

Explicit user request
OR
Major architectural contradiction
OR
Active/Legacy conflict
OR
Critical test failure
OR
Checkpoint conflict

Action:

Perform targeted deep review
MODE 4 — RECOVERY

Condition:

Current Task or continuation point cannot be established

Action:

Reconstruct minimum required state
Create Recovery Checkpoint if necessary
34. PROJECT CONTINUITY GUARANTEE

The following rules are mandatory:

A long conversation must not cause project drift.

A new chat must not cause automatic full re-audit.

A valid Checkpoint must be respected.

An IN PROGRESS Task must remain locked.

The NEXT STEP must be followed.

Completed work must not be repeated without evidence.

The repository must be checked only when verification is necessary.

Deep Review must be triggered by evidence, not habit.

The assistant must never guess project state.

The user must be able to say only:

"ادامه بده"

and the project must continue from the correct point.
END OF PROJECT CONTROL
BourseAnalyzer
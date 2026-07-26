# BourseAnalyzer — Master Protocol V4

**Project:** BourseAnalyzer  
**Protocol:** BA-MASTER-PROTOCOL-V4  
**Protocol Status:** FINAL / OPERATIONAL  
**Document Type:** Master Project Governance, Architecture, Continuity and Coding Protocol  
**Repository:** `mamaljigar-prog/BourseAnalyzer`

---

# 0. PURPOSE

This document defines the permanent operating rules for the BourseAnalyzer project.

The purpose of this protocol is to ensure that the project:

- Does not lose direction during long conversations.
- Does not restart completed work unnecessarily.
- Does not repeat audits without evidence.
- Does not introduce uncontrolled architecture changes.
- Does not accumulate unnecessary duplicate code.
- Does not create parallel implementations for the same responsibility.
- Does not spread hard-coded business rules throughout the codebase.
- Does not allow Legacy code to be confused with Active code.
- Does not expand scope without explicit authorization.
- Can be resumed reliably after a long conversation.
- Can be resumed from a new chat.
- Can be recovered even if conversational memory is incomplete.
- Maintains a clear distinction between project rules, project state, architecture and code.
- Uses the actual GitHub repository as the source of truth for the actual implementation.

This protocol must be used together with:

```text
PROJECT_CONTROL.md
BA-CHECKPOINT.md
BA-ROADMAP.md
BA-ARCHITECTURE.md

These documents have different responsibilities.

1. DOCUMENT AUTHORITY MODEL

The project uses the following authority hierarchy.

1.1 Actual Repository Code

The actual repository is the source of truth for:

What code exists.
What files exist.
What imports exist.
What code is executable.
What branch contains the code.
What commit contains the code.
What implementation is actually active.

Documentation must never be assumed to be more accurate than verified code.

1.2 PROJECT_CONTROL.md

PROJECT_CONTROL.md is the source of truth for the current operational state.

It controls:

Current Task.
Task Status.
Task Lock.
Scope Lock.
Current Priority.
Current operational phase.
Current blockers.
Current completion criteria.
Current next step.
1.3 BA-CHECKPOINT.md

BA-CHECKPOINT.md is the source of truth for the latest verified continuation point.

It records:

What was completed.
What changed.
What was tested.
What failed.
What remains.
Where the project must continue.
1.4 BA-ROADMAP.md

BA-ROADMAP.md defines the long-term project sequence.

It must not be changed merely because a new idea appears during implementation.

1.5 BA-ARCHITECTURE.md

BA-ARCHITECTURE.md defines the intended and verified architecture.

It must distinguish:

CURRENT ACTIVE ARCHITECTURE

from:

LEGACY / ARCHIVE
1.6 BA-MASTER-PROTOCOL-V4.md

This document defines permanent rules.

It defines:

How the project must be handled.
How tasks must be continued.
How architecture changes are controlled.
How code changes are made.
How testing is handled.
How continuity is preserved.

This document does not replace the current project state.

2. PRIMARY CONTINUATION COMMAND

The standard project continuation command is:

«ادامه BourseAnalyzer از آخرین Checkpoint — Protocol V4 و PROJECT_CONTROL را مبنا قرار بده و وضعیت Task فعلی را از GitHub و آخرین Commit تطبیق بده.»

When this command is received, the assistant must not immediately start coding.

The assistant must first:

Read PROJECT_CONTROL.md.
Read BA-CHECKPOINT.md.
Read BA-MASTER-PROTOCOL-V4.md.
If necessary, read BA-ARCHITECTURE.md.
If necessary, read BA-ROADMAP.md.
Verify the current Git branch.
Verify the latest commit.
Inspect the latest relevant repository changes.
Compare documentation with the actual repository.
Identify the current Task.
Identify the Task Status.
Determine whether a Task Lock is active.
Determine the last completed action.
Determine the exact unfinished action.
Determine the single next priority step.

Only after this verification may the assistant continue the project.

3. NO-RESTART RULE

The assistant must not restart the project from the beginning merely because:

The conversation became long.
The chat changed.
Some previous context is unavailable.
The project has many files.
The assistant does not immediately remember every detail.

The assistant must first attempt recovery from:

GitHub Repository
        ↓
Current Branch
        ↓
Latest Commit
        ↓
PROJECT_CONTROL.md
        ↓
BA-CHECKPOINT.md
        ↓
BA-ARCHITECTURE.md
        ↓
BA-ROADMAP.md

Only if the state cannot be reconstructed should a Recovery Checkpoint be created.

4. NO-GUESS RULE

The assistant must never guess the project state.

The assistant must not fabricate:

Current branch.
Latest commit.
Current task.
Task completion.
Test results.
Architecture.
File existence.
Active implementation.
Legacy implementation.
GitHub synchronization status.

If the state is unclear:

STOP
VERIFY
REPORT

Then continue only after the state is established.

5. TASK LOCK

Every active project task must have:

TASK ID
TASK NAME
TASK STATUS
TASK OBJECTIVE
TASK SCOPE
COMPLETION CRITERIA
START CHECKPOINT
NEXT STEP
PRIORITY

Allowed Task Status values:

PLANNED
IN PROGRESS
WAITING_FOR_USER
BLOCKED
PAUSED
COMPLETED
CANCELLED

If:

TASK STATUS = IN PROGRESS

a Task Lock is active.

While Task Lock is active:

Do not start unrelated tasks.
Do not restart completed audits.
Do not introduce new features.
Do not change architecture unnecessarily.
Do not expand Scope.
Do not switch to another module without technical justification.
Do not abandon the current Task silently.
6. TASK CONTINUITY LOCK

If the project state says:

CURRENT TASK = X
STATUS = IN PROGRESS

then the assistant must continue Task X.

The assistant must not interpret a long conversation as permission to change the Task.

The assistant must not:

Restart Audit.
Start a new Refactor.
Start a new Feature.
Rebuild architecture.
Reanalyze the entire repository from zero.

unless:

The current Task is completed.
The current Task is blocked.
The user explicitly changes the Task.
A critical technical defect requires interruption.

If the current Task is interrupted:

STATUS = PAUSED

must be recorded.

The Task must remain recoverable.

7. TASK COMPLETION RULE

A Task is not completed merely because:

Code was written.
A file was changed.
The application started.
A single command succeeded.

A Task is completed only when its defined Completion Criteria have been verified.

Every Task must define measurable Completion Criteria.

8. ONE NEXT STEP RULE

Every active Checkpoint must define exactly one:

NEXT STEP

The assistant must not provide multiple competing directions as the primary continuation path.

If multiple possible tasks exist:

Evaluate priority.
Select the most important one.
Execute or assign only that one as the Next Step.

The Next Step must specify:

What changes.
Which file/module is involved.
Why it must change.
How it will be tested.
9. SCOPE LOCK

The project Scope must remain stable unless the user explicitly changes it.

The assistant must not introduce:

New features.
New analytical dimensions.
New data sources.
New architecture layers.
New reports.
New valuation models.

merely because they appear useful.

Useful does not mean authorized.

Any proposed Scope change must be clearly identified as:

OUT OF CURRENT SCOPE

and must not be implemented without explicit authorization.

10. NO-SCOPE-CREEP RULE

The following behavior is prohibited:

Fix one issue
    ↓
Add unrelated feature
    ↓
Refactor another module
    ↓
Change architecture
    ↓
Modify valuation
    ↓
Change output

during a single unrelated task.

The assistant must maintain task boundaries.

If an unrelated issue is discovered:

Record as Known Issue

and continue the current Task unless the issue blocks the current Task.

11. ACTIVE VS LEGACY

Every implementation must be classified as one of:

ACTIVE
LEGACY
ARCHIVE
EXPERIMENTAL
UNKNOWN

The project must never maintain ambiguity indefinitely.

If two modules appear to perform the same responsibility:

Search all references.
Search all imports.
Search runtime call paths.
Identify which implementation is actually executed.
Identify which implementation is historical.
Record the classification.
Modify only the Active implementation.

Legacy code must not be deleted without explicit user approval.

12. DUPLICATE CODE CONTROL

Before creating:

A new function.
A new class.
A new parser.
A new adapter.
A new service.
A new normalization layer.
A new calculation.
A new business-rule implementation.

the assistant must search the repository for an existing implementation.

The assistant must inspect:

Similar function names.
Similar classes.
Similar formulas.
Similar parsing.
Similar API calls.
Similar normalization.
Similar validation.
Similar business rules.
Similar output generation.

If the responsibility already exists:

Reuse
OR
Extend
OR
Refactor

before creating a new implementation.

Creating multiple implementations of one responsibility is prohibited unless there is a documented architectural reason.

13. SINGLE RESPONSIBILITY CONTROL

Each responsibility should have one canonical owner.

Examples:

Codal Retrieval
Codal Report Selection
Period Classification
Financial Parsing
Financial Normalization
Forecasting
Valuation
Risk Analysis
Report Generation

Each must have a clearly identified owner.

The same business rule must not be independently implemented in several modules.

14. HARD-CODE CONTROL

The assistant must identify and control:

Magic numbers.
Repeated strings.
Repeated thresholds.
Repeated business rules.
Repeated external identifiers.
Repeated report classification rules.
Repeated valuation assumptions.
Repeated financial constants.

Before adding a hard-coded value:

Search the repository.
Determine whether it already exists.
Determine whether it is a configuration value.
Determine whether it is a domain constant.
Determine whether it belongs in a model.
Determine whether it belongs in a dedicated configuration layer.

Existing hard-coded values must not be refactored blindly during unrelated tasks.

15. MAGIC NUMBER RULE

A numeric value must not be considered a magic number automatically.

Determine whether it is:

Domain Constant
Configuration
Business Rule
Threshold
Temporary Debug Value
Accidental Hard-Code

Examples requiring architectural review:

PE = 7

or:

Three consecutive declining months

or:

Financial thresholds

These values must have an explicit business meaning.

16. ARCHITECTURE-FIRST RULE

Before major architectural changes, determine:

Entry Point.
Dependency Flow.
Data Flow.
External Data Sources.
Adapter Layer.
Parser Layer.
Canonical Domain Models.
Forecast Layer.
Analysis Layer.
Valuation Layer.
Risk Layer.
Report Layer.

No major architecture rewrite may be performed based only on assumptions.

17. TARGET ARCHITECTURE

The target architecture is:

Raw External Data
        ↓
Adapters / Parsers
        ↓
Canonical Domain Models
        ↓
Normalization
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

The architecture should remain modular.

18. MARKET DATA CANONICALIZATION

Market data flow:

Raw TSETMC
        ↓
TSETMC Adapter
        ↓
CompanyIdentity
        ↓
MarketSnapshot

TSETMC data may include:

Symbol.
Company Name.
Instrument Code.
Last Price.
Closing Price.
Shares.
Market Value.

Raw TSETMC data must not be spread throughout the application.

19. FINANCIAL DATA CANONICALIZATION

Codal flow:

Raw Codal
        ↓
Codal Adapter
        ↓
Report Retrieval
        ↓
Report Selection
        ↓
Period Classification
        ↓
Financial Parser
        ↓
Canonical Financial Data
        ↓
Company / Financial Domain

Each stage must have a defined responsibility.

Raw Codal structures must not be directly consumed by unrelated layers.

20. EXTERNAL ADAPTER RULE

Every external Adapter is responsible for converting external raw data into a stable internal representation.

An Adapter should not:

Perform unrelated valuation.
Perform unrelated forecasting.
Generate final reports.
Contain duplicated business logic.

Adapters should isolate external data formats from the domain layer.

21. CODAL REPORT SELECTION RULE

The Codal report-selection system must distinguish:

Annual Reports.
Interim Reports.
Quarterly Reports.
Other relevant financial reports.

The selection mechanism must be deterministic.

Report selection must not depend on fragile assumptions when reliable metadata is available.

Report classification must have one canonical responsibility.

22. FINANCIAL ANALYSIS PERIOD RULE

Primary financial analysis is based on:

Latest Valid New Codal Report

Older reports are used for:

Comparison.
Trend.
Growth.
Quality Checks.

Five-year trend analysis is currently outside Scope.

The primary financial analysis focuses on a one-year financial period unless the active architecture explicitly requires another period.

23. FORECAST RULE

Forecasting must use real financial data whenever possible.

The Forecast layer must consider:

Non-recurring profit.
Asset sales.
Non-operating income.
Bank interest.
Dividend income.
Sudden margin changes.
Performance decline.

Non-operating income must not automatically be treated as sustainable.

It may be included in sustainable Forecast only when there is evidence of recurrence.

24. VALUATION RULE

Primary valuation metrics:

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

The system must not blindly use TSETMC's P/E as the project's calculated Forward P/E.

25. TSETMC P/E RULE

TSETMC P/E is not the canonical valuation P/E.

The system calculates:

Forward P/E =
Market Value / Forecasted Net Profit

TSETMC may provide market information.

The project's own valuation logic must use the canonical financial and forecast data.

26. BASE CASE VALUATION RULE

A base-case PE of:

PE = 7

may be used as a Base Case unless the active architecture defines a different validated assumption.

This is a valuation assumption.

It must not be duplicated throughout the codebase.

27. ASSET VALUATION RULE

High P/A or P/B may be affected by:

Unrecognized asset revaluation.
Historical book values.
Accounting valuation differences.

The system should identify this as an analytical consideration.

28. FUNDAMENTAL RISK RULES

If sales decline for three consecutive months:

Fundamental Stop-Loss Warning

may be activated.

If profit margin suddenly and materially declines:

Fundamental Risk Warning

must be considered.

These warnings are analytical signals.

They must not automatically be treated as trading commands without additional context.

29. HOLDING COMPANY RULE

For investment companies and holdings:

Fundamental risk analysis should consider major subsidiaries.

If multiple significant subsidiaries trigger fundamental Stop-Loss conditions:

The parent company's risk status may increase.

This logic must be implemented in the appropriate Analysis/Risk layer.

It must not be duplicated in individual parsers.

30. TESTING HIERARCHY

Preferred test order:

1. Unit Test
2. Component Test
3. Integration Test
4. End-to-End Test

Not every change requires all four levels.

The required test level depends on the change.

Major pipeline changes should reach Integration or End-to-End testing.

31. TEST EVIDENCE RULE

A test is considered successful only when there is evidence.

Evidence may include:

Test output.
Assertion result.
Application output.
PowerShell output.
CI result.

The assistant must not claim:

TEST PASSED

without evidence.

32. POWERSHELL WAITING RULE

When the assistant asks the user to execute a PowerShell command:

STATUS = WAITING_FOR_USER

The assistant must:

Wait for the result.
Not repeat the same operation.
Not assume success.
Not assume failure.
Not start an unrelated task.
Not create a new Checkpoint merely because the conversation continued.

When the result arrives:

Analyze.
Determine outcome.
Continue.
Update Checkpoint if state changed.
33. USER ACTION RULE

Every user action request must contain:

Exact command.
Expected output.
Reason for execution.

The user must not be asked to perform vague operations.

34. CODE DELIVERY RULE

When the user requests a code change:

The assistant must provide:

COMPLETE
INTEGRATED
REPLACEMENT-READY
FILE

Do not provide:

Partial snippets.
Fragmented patches.
Incomplete sections.

Unless the user explicitly asks for a patch or diff.

35. CODE COMPATIBILITY RULE

Any replacement file must be compatible with:

Active architecture.
Existing imports.
Existing models.
Existing call sites.
Existing data structures.

Before replacing a file:

Inspect callers.
Inspect imports.
Inspect dependencies.
Inspect expected interfaces.
Preserve compatible behavior unless intentionally changing it.
36. FILE REPLACEMENT SAFETY

Before replacing a major file:

Identify its callers.
Identify its imports.
Identify its outputs.
Identify its dependencies.
Identify its tests.

Do not replace a major file merely because it appears poorly structured.

37. ARCHITECTURE REWRITE RULE

Do not rewrite the entire architecture because:

One module has bugs.
One parser is incomplete.
One calculation is wrong.
One integration fails.

A rewrite is justified only when:

Existing architecture is fundamentally unsalvageable.
Dependency structure prevents reliable maintenance.
Duplication is systemic.
Data flow is fundamentally broken.
A documented architectural decision approves the rewrite.
38. CORE ANALYZER ENGINE RULE

Until Active Architecture is fully verified:

core/analyzer_engine.py

must not be rewritten blindly.

Before changing it:

Map imports.
Map callers.
Map data flow.
Map dependencies.
Identify Active responsibilities.
Identify Legacy responsibilities.
Determine whether refactoring is necessary.
39. REPOSITORY AUDIT RULE

A Repository Audit must be performed only when:

Starting a new major phase.
Recovering from unknown state.
Investigating architecture.
Investigating duplication.
Investigating a systemic defect.

A completed Audit must not be restarted automatically.

If an Audit was already completed:

Continue from the Audit's resulting Task.

Do not return to Audit unless new evidence requires it.

40. RUNNING APP REQUEST RULE

If the previous Task was:

Running app request

and it is still recorded as:

IN PROGRESS

the assistant must continue that Task.

It must not automatically:

Start another Audit.
Rebuild architecture.
Start a new feature.
Return to the beginning.

If the status cannot be verified:

Check PROJECT_CONTROL.md.
Check BA-CHECKPOINT.md.
Check GitHub.
Check latest commits.
Report actual status.
Do not guess.
41. GITHUB VERIFICATION RULE

When GitHub access is available, the assistant should verify:

Repository.
Branch.
Latest commit.
Recent relevant commits.
Current file structure.
Relevant active files.
Relevant documentation.

The assistant must not rely only on copied code from the user when the repository itself is accessible.

42. BRANCH RULE

The current branch must always be known before significant work.

Never assume:

master
main
develop

or any other branch.

The assistant must verify the actual branch.

43. COMMIT RULE

Important project milestones should be committed.

Commit messages should be:

Clear.
Specific.
Related to the actual change.

Do not create meaningless commits.

44. PUSH VERIFICATION RULE

A successful local Commit does not mean GitHub was updated.

After pushing:

Verify:

Branch
Remote
Commit

A command such as:

git push

must be interpreted according to its actual output.

45. DOCUMENTATION CONSISTENCY RULE

Control documents must remain consistent with actual repository state.

If a document says:

Task = IN PROGRESS

but the code and tests prove the Task is complete:

The document must be updated.

If a document says:

Task = COMPLETED

but the code is not actually complete:

The Task must not be treated as completed.

Actual verification takes priority.

46. CHECKPOINT PROTOCOL

At meaningful project-state changes, create or update a Checkpoint.

Checkpoint must include:

CHECKPOINT ID
DATE
PROJECT PHASE
CURRENT TASK
TASK STATUS
LAST COMPLETED WORK
CHANGED FILES
ACTIVE ARCHITECTURE
LEGACY / ARCHIVE
TESTS PERFORMED
TEST RESULTS
KNOWN ISSUES
ARCHITECTURAL DECISIONS
START CHECKPOINT
COMPLETION CRITERIA
NEXT STEP
NEXT STEP PRIORITY
USER ACTION
CONTINUATION COMMAND
47. CHECKPOINT UPDATE EXCEPTION

If the assistant is only waiting for PowerShell output:

Do not create a new Checkpoint.

The previous Checkpoint remains valid.

When the result arrives:

Analyze it.
Continue.
Update Checkpoint if state changes.
48. RECOVERY PROTOCOL

If project continuity cannot be recovered from conversation:

Perform:

Repository Verification
        ↓
Branch Verification
        ↓
Latest Commit Verification
        ↓
Control Document Verification
        ↓
Checkpoint Verification
        ↓
Active Architecture Verification
        ↓
Task Identification

If the exact Task remains unknown:

Create:

RECOVERY CHECKPOINT

The Recovery Checkpoint must state:

What is verified.
What is uncertain.
What evidence exists.
What cannot be established.
What must be checked next.

Never guess.

49. CHAT CHANGE PROTOCOL

When a new chat is started:

The user should only need to provide:

ادامه BourseAnalyzer از آخرین Checkpoint

The assistant should then recover state from the repository and control documents.

If repository access is unavailable:

The assistant should use the latest available control documents.

If neither is available:

The assistant must explicitly state that project state cannot be verified.

50. MEMORY LIMITATION COMPENSATION

Conversational memory is not considered the primary continuity mechanism.

The project must compensate for memory limitations through persistent artifacts:

GitHub
    +
PROJECT_CONTROL.md
    +
BA-CHECKPOINT.md
    +
BA-ROADMAP.md
    +
BA-ARCHITECTURE.md

These documents are the project's external memory system.

The project must remain understandable without relying on one long conversation.

51. PROJECT STATE QUESTIONS

Before continuing work, the assistant must be able to answer:

1. Where are we?
2. What did we just complete?
3. What is currently in progress?
4. Why is it in progress?
5. What is the next single action?

If any answer is unknown:

VERIFY BEFORE CODING
52. PROGRESS RULE

Progress percentages must not be fabricated.

Progress should be estimated based on:

Defined Scope.
Completed Roadmap phases.
Remaining major work.
Actual implementation status.

Percentage is informational only.

The real state is represented by:

Task Status
Checkpoint
Roadmap Phase
Completion Criteria
53. PROJECT ROADMAP PRINCIPLE

The project roadmap must proceed in controlled phases.

General target sequence:

Phase 1
Repository and Architecture Stabilization

        ↓

Phase 2
External Data Adapters

        ↓

Phase 3
Canonical Data Models

        ↓

Phase 4
Financial Data Normalization

        ↓

Phase 5
Forecast Engine

        ↓

Phase 6
Analysis Engine

        ↓

Phase 7
Valuation Engine

        ↓

Phase 8
Risk Analysis

        ↓

Phase 9
Final Reporting

        ↓

Phase 10
Testing and Production Hardening

The actual active phase must be defined in PROJECT_CONTROL.md.

54. CURRENT PROJECT PRINCIPLE

The final intended pipeline is:

TSETMC
    ↓
Market Canonical Layer

Codal
    ↓
Financial Canonical Layer

Canonical Models
    ↓
Company Domain

Company Domain
    ↓
Forecast

Forecast
    ↓
Analysis

Analysis
    ↓
Valuation

Valuation
    +
Risk Analysis
    ↓
Final Report

The final entry point should approach:

main.py
    ↓
Clean Entry Point
    ↓
Main Pipeline
    ↓
Final Report
55. PROJECT QUALITY PRINCIPLE

The goal is not merely:

The application runs.

The goal is:

The application is correct,
maintainable,
testable,
traceable,
recoverable,
and architecturally coherent.
56. ANTI-CHAOS PRINCIPLE

When the project becomes complex:

Do not add more complexity to hide existing complexity.

Instead:

Identify responsibility.
Identify ownership.
Identify dependency.
Identify duplication.
Identify Active path.
Identify Legacy path.
Simplify where safe.
Test.
Document.
57. ANTI-BRANCHING PRINCIPLE

Do not allow multiple competing implementations to remain Active.

For every major responsibility:

One Canonical Active Implementation

is preferred.

Legacy implementations may remain for historical safety.

58. ANTI-REGRESSION PRINCIPLE

Before changing working behavior:

Record current behavior.
Record current output.
Record current test result.

After changing:

Re-run the same validation.
Compare results.

Do not improve one area by silently breaking another.

59. DEBUGGING PRINCIPLE

Debugging must proceed from evidence.

Preferred sequence:

Observed Error
    ↓
Reproduce
    ↓
Locate Source
    ↓
Trace Dependency
    ↓
Identify Root Cause
    ↓
Apply Minimal Correct Fix
    ↓
Test
    ↓
Verify No Regression

Do not blindly rewrite code to eliminate an error.

60. ROOT-CAUSE RULE

Fix the root cause whenever possible.

Do not mask errors with:

Random defaults.
Silent exceptions.
Broad try/except.
Hard-coded fallbacks.
Duplicate logic.

unless the behavior is explicitly intentional and documented.

61. ERROR HANDLING RULE

Errors must not be silently ignored.

If an error is intentionally handled:

The reason must be clear.
The fallback must be valid.
The behavior must be testable.
62. DATA INTEGRITY RULE

Financial data must preserve:

Source.
Period.
Unit.
Currency.
Sign.
Date.
Report type.
Classification.

Transformations must not silently change financial meaning.

63. FINANCIAL DATA TRACEABILITY

Every important financial output should be traceable to:

Source Report
    ↓
Parsed Value
    ↓
Canonical Value
    ↓
Forecast Input
    ↓
Forecast Output
    ↓
Valuation

The system should avoid unexplained calculations.

64. REPORT SELECTION TRACEABILITY

The selected Codal report should be explainable.

The system should be able to determine:

Why the report was selected.
What period it represents.
Whether it is Annual or Interim.
Whether it is the latest valid report.
Whether an older report was rejected and why.
65. FORECAST TRACEABILITY

Forecast outputs should be traceable to:

Actual financial values.
Forecast assumptions.
Adjustments.
Non-recurring items.
Recurring/non-recurring classification.
66. VALUATION TRACEABILITY

Valuation outputs should be traceable to:

Market Value.
Forecast Sales.
Forecast Net Profit.
Assets.
Equity.
Valuation assumptions.
67. NO-HIDDEN-BUSINESS-LOGIC RULE

Important business logic must not be hidden inside:

Parsers.
API adapters.
UI code.
Print statements.
Utility functions.

Business rules belong in appropriate domain/analysis layers.

68. PRINT-BASED LOGIC RULE

Console output must not be the source of truth for application logic.

Printing is for:

Debugging.
Reporting.
Diagnostics.

Not for data storage or business decisions.

69. CONFIGURATION RULE

Configuration should be centralized where appropriate.

Avoid repeating:

URLs.
Timeouts.
Thresholds.
Valuation assumptions.
Paths.
External identifiers.

throughout multiple modules.

70. DEPENDENCY RULE

Dependencies must flow in a controlled direction.

Preferred:

External Layer
    ↓
Adapter
    ↓
Canonical Model
    ↓
Domain
    ↓
Analysis
    ↓
Valuation
    ↓
Reporting

Higher-level business logic should not depend directly on raw external structures.

71. CIRCULAR DEPENDENCY RULE

Circular dependencies must be avoided.

If detected:

Map the cycle.
Identify the architectural cause.
Refactor the dependency direction.
Test.

Do not solve circular dependencies with random imports or runtime hacks unless explicitly justified.

72. NEW MODULE RULE

Before adding a module:

Ask:

Does this responsibility already exist?

If yes:

Why is a new module necessary?

If no valid reason exists:

Do not create it.

73. REFACTORING RULE

Refactoring must have a defined objective.

Valid objectives include:

Remove duplication.
Clarify ownership.
Reduce coupling.
Improve testability.
Fix architectural violation.
Improve maintainability.

Do not refactor simply because code could look cleaner.

74. BIG-BANG REWRITE RULE

A complete rewrite is allowed only when:

The current system is demonstrably unsalvageable.
The migration path is defined.
The new architecture is documented.
The active path is identified.
Regression risk is controlled.

Otherwise prefer incremental refactoring.

75. LEGACY MIGRATION RULE

When migrating Legacy code:

Legacy
    ↓
Verify
    ↓
Extract
    ↓
Test
    ↓
Migrate
    ↓
Mark Legacy

Do not delete Legacy code prematurely.

76. USER CONFIRMATION RULE

User confirmation is required before:

Deleting Legacy files.
Changing project Scope.
Replacing the entire architecture.
Removing major modules.
Changing major business rules.
Replacing the primary valuation methodology.
77. AUTOMATIC DECISION RULE

The assistant may make independent technical decisions when:

They are within current Scope.
They preserve architecture.
They reduce duplication.
They fix a clear bug.
They improve maintainability.
They do not alter agreed business rules.

The assistant must not independently make decisions that change the project's strategic direction.

78. PROJECT CONTROL UPDATE RULE

Update PROJECT_CONTROL.md when:

Current Task changes.
Task Status changes.
Task is completed.
Task is blocked.
Task is paused.
Scope changes.
Architecture changes.
Active/Legacy classification changes.
Major milestone completes.

Do not update it for every conversation message.

79. CHECKPOINT UPDATE RULE

Update BA-CHECKPOINT.md when:

A meaningful Task step completes.
A significant code change is verified.
A test result changes project state.
A Task is completed.
A Task is blocked.
A new Next Step is established.

Do not create a new Checkpoint merely because the assistant sent another message.

80. RECOVERY CHECKPOINT

If continuity is lost:

Create:

RECOVERY CHECKPOINT

It must contain:

WHAT IS VERIFIED
WHAT IS UNKNOWN
WHAT WAS LAST COMPLETED
CURRENT REPOSITORY STATE
CURRENT BRANCH
LATEST COMMIT
CURRENT TASK
TASK STATUS
KNOWN ISSUES
NEXT VERIFICATION STEP

Do not guess missing information.

81. MASTER RECOVERY SEQUENCE

The recovery sequence is:

1. Repository
2. Branch
3. Latest Commit
4. Recent Commits
5. PROJECT_CONTROL.md
6. BA-CHECKPOINT.md
7. BA-ARCHITECTURE.md
8. BA-ROADMAP.md
9. Active Code Path
10. Current Task
11. Task Status
12. Next Step
82. PROJECT CONTINUITY COMMAND

The canonical command is:

ادامه BourseAnalyzer از آخرین Checkpoint

The assistant must interpret this command as:

Resume Existing Work

not:

Start New Audit

not:

Restart Project

not:

Redesign Architecture
83. FINAL PROJECT GOVERNANCE RULE

When uncertain:

VERIFY

When duplicate:

CONSOLIDATE

When Legacy:

DO NOT DELETE WITHOUT APPROVAL

When Task is IN PROGRESS:

CONTINUE

When Task is complete:

CHECKPOINT

When blocked:

DOCUMENT BLOCKER

When Scope changes:

REQUIRE EXPLICIT APPROVAL

When code is changed:

TEST

When chat becomes long:

USE PROJECT CONTROL

When starting a new chat:

RECOVER FROM REPOSITORY + CONTROL DOCUMENTS
84. FINAL CONTINUITY CONTRACT

The BourseAnalyzer project must always remain recoverable.

At any point, the following must be determinable:

WHERE ARE WE?
WHAT WAS COMPLETED?
WHAT IS IN PROGRESS?
WHY ARE WE DOING IT?
WHAT IS THE NEXT STEP?

The answer must be recoverable from:

GitHub
PROJECT_CONTROL.md
BA-CHECKPOINT.md
BA-ROADMAP.md
BA-ARCHITECTURE.md

The project must not depend on the memory of a single conversation.

The project must not depend on the memory of a single assistant instance.

The project must not depend on the user repeatedly reconstructing the project state.

The repository and its control documents must preserve continuity.

85. END OF MASTER PROTOCOL V4

BourseAnalyzer

CONTROLLED
TRACEABLE
TESTABLE
RECOVERABLE
MAINTAINABLE

END
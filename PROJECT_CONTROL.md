# BourseAnalyzer — PROJECT CONTROL

**Project:** BourseAnalyzer  
**Control Document Version:** 2.0  
**Document Role:** Operational Project Control / Continuity / Task Lock  
**Repository:** `mamaljigar-prog/BourseAnalyzer`  
**Default Branch:** `master`  
**Primary Development Branch:** Verify from actual Git state  
**Protocol:** `BA-MASTER-PROTOCOL-V4.md`

---

# 1. PURPOSE

This document is the operational control center for the BourseAnalyzer project.

Its purpose is to preserve project continuity across:

- Long conversations
- New chats
- Lost conversational context
- Interrupted development sessions
- Branch changes
- New commits
- Architecture refactoring
- Multiple development stages

This document exists to prevent:

- Loss of project continuity
- Repeating completed audits
- Repeating completed tasks
- Uncontrolled architecture changes
- Scope creep
- Creation of duplicate implementations
- Confusion between Active and Legacy code
- Losing the current task after a long conversation
- Starting a new task before the current task is complete
- Rebuilding the project from zero without technical justification
- Making decisions based only on conversational memory
- Forgetting the exact unfinished task
- Forgetting the last verified project state
- Replacing working code without evidence
- Changing architecture merely because a different design appears cleaner
- Requiring the user to repeatedly explain the project state

This document works together with:

- `BA-MASTER-PROTOCOL-V4.md`
- `BA-CHECKPOINT.md`
- `BA-ROADMAP.md`
- `BA-ARCHITECTURE.md`

The GitHub repository is the source of truth for actual code.

This document is the source of truth for the current operational project state.

The Master Protocol is the source of truth for permanent project rules.

The Checkpoint is the source of truth for the latest precise continuation point.

When these sources disagree, the assistant must verify the actual repository before making a decision.

---

# 2. DOCUMENT ROLES

The project control system has four distinct roles.

## 2.1 BA-MASTER-PROTOCOL-V4.md

Defines:

- Permanent project rules
- Coding rules
- Architectural principles
- Financial rules
- Valuation rules
- Testing principles
- Active vs Legacy rules
- Continuity principles

It should change rarely.

It is not a daily task tracker.

---

## 2.2 PROJECT_CONTROL.md

Defines:

- Current operational state
- Current Task Lock
- Current task
- Current phase
- Current blockers
- Current Active / Legacy boundaries
- Current completion criteria
- Current next step
- Current operational rules

It is the project's operational control center.

It should be updated only when project state actually changes.

---

## 2.3 BA-CHECKPOINT.md

Defines:

- Latest verified continuation point
- Last completed action
- Current unfinished task
- Current test status
- Current known issues
- Exact next step

It is the primary continuation record.

It must remain concise and factual.

---

## 2.4 BA-ROADMAP.md

Defines:

- Long-term project stages
- Future tasks
- Development sequence
- Strategic project direction

The Roadmap does not override the active Task Lock.

A future task must not automatically become the current task while another Task Lock is active.

---

# 3. PRIMARY CONTINUATION COMMAND

The standard continuation command is intentionally short:

> ادامه BourseAnalyzer از آخرین Checkpoint

This command is the official trigger for project continuation.

It is intentionally short so that:

- It is easy to remember
- It is fast to use
- It does not repeat the entire protocol
- It does not force unnecessary re-reading of all project documents
- It does not imply that a full repository audit must be repeated every time

The assistant must interpret this command as:

> Resume the project from the latest verified project state.

The assistant must not interpret this command as:

> Re-audit the entire project from zero.

---

# 4. CONTINUATION PROTOCOL

When the user sends:

> ادامه BourseAnalyzer از آخرین Checkpoint

the assistant must follow this sequence.

## STEP 1 — IDENTIFY THE CURRENT TASK

Read the latest available project state from:

1. `BA-CHECKPOINT.md`, if present
2. `PROJECT_CONTROL.md`
3. Current conversation context
4. Repository state, when needed

Determine:

- Current Task
- Task Status
- Current Phase
- Last Completed Work
- Current Unfinished Work
- Next Step

---

## STEP 2 — CHECK WHETHER THE TASK IS STILL ACTIVE

If:

```text
TASK STATUS = IN PROGRESS

continue the same task.

Do not automatically start another task.

Do not automatically perform a full project audit.

Do not restart previously completed work.

STEP 3 — VERIFY ONLY WHAT IS NECESSARY

Repository verification should be proportional to the task.

The assistant should not perform a full repository audit on every continuation.

Verify GitHub / repository state when:

The latest commit is unknown
The branch is unknown
The checkpoint may be stale
The user explicitly requests synchronization
The task depends on code that may have changed
There is evidence of a mismatch between documentation and code
The previous session may have changed the project state
The current next step requires inspecting actual code

If the current state is already verified and no relevant code change occurred, do not repeat the same full verification.

STEP 4 — CHECK THE LATEST RELEVANT CHANGE

The assistant should determine whether relevant code changed after the last verified checkpoint.

The relevant change may be:

A commit
A merged PR
A local code change
A modified file
A test result

The assistant should focus on changes relevant to the current Task Lock.

Unrelated commits do not automatically invalidate the current checkpoint.

STEP 5 — RESUME FROM THE EXACT UNFINISHED POINT

The assistant must answer internally:

Where are we?
What did we just complete?
What task is still unfinished?
What is the one next step?

Then continue from that point.

5. FULL RECONCILIATION COMMAND

A full repository reconciliation is a separate operation.

It is not automatically required by:

ادامه BourseAnalyzer از آخرین Checkpoint

When the user explicitly requests a full synchronization, use a command equivalent to:

وضعیت پروژه را با GitHub و آخرین Commit تطبیق بده.

During a full reconciliation, the assistant must:

Inspect current branch.
Inspect latest commit.
Inspect recent relevant commits.
Read PROJECT_CONTROL.md.
Read BA-CHECKPOINT.md if present.
Read BA-MASTER-PROTOCOL-V4.md if necessary.
Compare documentation with actual repository state.
Verify the current Task Lock.
Verify the active execution path relevant to the current task.
Report only material discrepancies.
Update the checkpoint if the actual project state changed.

A full reconciliation should not be repeated unnecessarily.

6. SOURCE OF TRUTH HIERARCHY

When resolving conflicts, use the following hierarchy.

For actual code existence and implementation:
Actual repository code
Latest verified Git state
Relevant commit history
For operational project state:
Latest verified BA-CHECKPOINT.md
PROJECT_CONTROL.md
Current conversation context
For permanent project rules:
BA-MASTER-PROTOCOL-V4.md
For future planning:
BA-ROADMAP.md
For architecture reference:
BA-ARCHITECTURE.md
Actual repository dependency flow
Lowest priority:

Previous conversational memory.

Important:

Conversational memory must never override verified repository state.

Documentation must never be treated as proof that code exists.

A commit message must never be treated as proof that a feature works.

7. DOCUMENTATION VS CODE CONFLICT

When documentation and code disagree:

Do not guess.
Inspect the actual repository.
Identify the discrepancy.
Determine the real state.
Continue from the real state.
Update the relevant control document.

Do not automatically rewrite all documentation because of a minor discrepancy.

Only update documents that are actually affected.

8. CURRENT PROJECT STATE
Current Phase

Codal Report Selection / Period Detection / Pipeline Stabilization

Current Task Status

IN PROGRESS

Current Task

Stabilize and consolidate the active Codal Report Selection Pipeline.

Task Objective

The current task is to ensure that the active Codal report-selection pipeline is:

Deterministic
Consistent
Maintainable
Correctly separating Annual and Interim reports
Free from unnecessary duplicate responsibilities
Free from unnecessary duplicate data retrieval
Compatible with the active architecture
Testable through the real application path
Stable enough to serve as the foundation for downstream financial analysis

No unrelated product features are to be added during this task.

The current scope must not be expanded.

9. TASK LOCK

A Task Lock is active whenever:

CURRENT TASK STATUS = IN PROGRESS

When a Task Lock is active:

The current task has priority.
Unrelated tasks must not be started automatically.
New features must not be added.
Scope must not be expanded.
Completed audits must not be repeated without evidence.
The architecture must not be redesigned unnecessarily.
The project must not jump to another module merely because it is easier.
A downstream task must not replace the current task prematurely.

The Task Lock remains active until:

The task is completed
The task is explicitly cancelled
The task is explicitly replaced
The task is technically blocked
A critical defect requires temporary interruption

If interrupted:

TASK STATUS = PAUSED

The paused task must remain recorded.

It must be resumed unless explicitly cancelled or replaced.

10. TASK CONTINUITY RULE

If the latest verified state says:

CURRENT TASK:
X

STATUS:
IN PROGRESS

the next project session must continue Task X.

The assistant must not:

Start a new audit
Restart the architecture review
Rebuild the project from zero
Rewrite unrelated modules
Introduce unrelated features
Change the roadmap
Replace the current task with a downstream task

unless the current task is completed, cancelled, blocked, paused, or explicitly replaced.

Before modifying code, the assistant must identify:

LAST COMPLETED ACTION
CURRENT UNFINISHED TASK
ONE NEXT PRIORITY STEP
11. CURRENT TASK COMPLETION CRITERIA

The current Codal Report Selection task is complete only when all of the following are verified:

Active report-selection dependency flow is understood.
Actual callers of report-selection modules are identified.
Active versus Legacy report-selection code is identified.
Annual and Interim classification responsibility is clearly defined.
Duplicate normalization responsibility is identified.
Duplicate Codal retrieval is identified.
Unnecessary duplicate logic is removed or safely centralized where justified.
Existing valid behavior is preserved.
At least one real symbol is tested.
The active application path reaches the intended report-selection logic.
The selected report is correct for the tested symbol.
Test output is recorded.
End-to-End behavior is verified.
The Checkpoint is updated.
Exactly one next priority task is defined.

Until all applicable criteria are verified:

TASK STATUS = IN PROGRESS
12. LATEST VERIFIED REPOSITORY STATE

The repository is:

mamaljigar-prog/BourseAnalyzer

Default branch:

master

The primary development branch must always be verified from actual Git state.

The repository state must not be assumed.

The last known project-control-related commits include:

19a0e27
Add BourseAnalyzer Master Protocol V4

and:

9108c85
Add project control and task continuity rules

These commits are historical references only.

They must not automatically be treated as the current latest commit.

The current latest commit must be verified from the actual repository when synchronization is required.

The current Task Lock must not be inferred from commit messages alone.

13. LAST VERIFIED WORK

The latest known work related to the current Task Lock concerns:

Codal Report Selection
Annual / Interim distinction
Financial report selection
Codal report retrieval

A previous relevant report-selection checkpoint was associated with:

1493eda2e5464cbca99863383abe802244795aeb

Commit message:

improve_report_selection_logic_checkpoint

This is a historical reference point.

It is not necessarily the current repository HEAD.

The report-selection task is not considered complete until the completion criteria in Section 11 are verified.

Do not restart the entire project audit.

Do not automatically revert to the old commit.

Continue from the current repository state while preserving the valid work already completed.

14. KNOWN CURRENT ISSUES

The following issues are currently suspected or identified.

They must be verified against actual code before modification.

14.1 Annual / Interim Classification

Report classification may depend on:

Report metadata
Period metadata
Report title
Report type
Existing selection rules

The actual classification path must be verified.

Classification responsibility must not be duplicated across unrelated modules.

14.2 Duplicate Codal Retrieval

The Codal retrieval architecture may retrieve overlapping report sets through separate searches.

Before changing retrieval:

Trace actual callers.
Identify all retrieval entry points.
Determine whether the same raw data can be reused.
Determine whether duplicate retrieval is intentional.
Confirm that changes do not break report selection.

Do not optimize blindly.

14.3 Duplicate Normalization

Normalization behavior may exist in more than one location.

Before changing:

Find all implementations.
Identify actual callers.
Determine the Active implementation.
Determine Legacy implementations.
Compare behavior.
Consolidate only when behavior can be preserved safely.
14.4 Active / Legacy Ambiguity

Some modules may have overlapping responsibilities.

The assistant must determine:

ACTIVE

versus:

LEGACY / ARCHIVE

before modifying overlapping implementations.

Legacy code must not be deleted without explicit user approval.

15. ACTIVE ARCHITECTURE PRINCIPLE

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
Codal Adapter / Retrieval
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

This is a target architecture.

It must not be assumed to represent the exact current implementation until verified.

16. ACTIVE VS LEGACY

The project must distinguish between:

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

Legacy code:

Must not be expanded without reason.
Must not be deleted without explicit user approval.
Must not be assumed to be inactive solely because its filename looks old.

If two files appear to perform the same responsibility:

Search repository references.
Inspect imports.
Inspect runtime call flow.
Identify actual Active implementation.
Identify Legacy implementation.
Document the decision.
Modify only Active implementation unless migration is required.
17. CODE DUPLICATION CONTROL

Before creating a new:

Function
Class
Module
Service
Parser
Adapter

the assistant must search the repository for existing implementations with the same or similar responsibility.

Check:

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

18. HARD-CODE CONTROL

Avoid unnecessary hard-coded:

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
Avoid duplicating the value.

Existing hard-coded values must not be blindly refactored during unrelated tasks.

Refactor only when:

Directly relevant to the current task
Causing a real bug
Creating architectural duplication
Preventing correct testing
Creating significant maintenance risk
19. ARCHITECTURE CHANGE CONTROL

Before any significant architectural change:

Identify:

Entry Point
Dependency Flow
Active Data Flow
Raw data sources
Canonical Models
Forecast layer
Analysis layer
Valuation layer
Risk layer
Final Report generation

No architecture rewrite should be performed based only on assumptions.

Do not rewrite:

core/analyzer_engine.py

without first verifying its full dependency flow.

A cleaner-looking architecture is not sufficient justification for replacing working code.

20. SCOPE CONTROL

The current project scope must remain unchanged unless explicitly changed by the user.

Do not:

Introduce unrelated features
Reintroduce five-year trend analysis
Redesign the entire project while fixing one module
Replace working architecture without evidence
Add modules merely because a new module appears cleaner

Before adding a new module:

Search existing modules.
Check existing responsibilities.
Confirm no Active implementation already exists.
Confirm the new module is architecturally necessary.
21. FINANCIAL ANALYSIS RULES

Primary financial basis:

Latest Valid New Codal Report

Older reports are primarily used for:

Comparison
Trend
Growth
Quality Checks

Five-year trend analysis is currently outside project scope.

Primary analysis focuses on a one-year financial period.

22. TSETMC RULES

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

23. FORECAST RULES

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

24. VALUATION RULES

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

25. ANALYTICAL RISK RULES

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

26. TESTING CONTROL

Preferred testing order:

Unit Test
Component Test
Integration Test
End-to-End Test

Every significant code change must be tested as far as practical.

Never claim a test passed without actual evidence.

Never assume PowerShell output.

If the user is asked to execute a command:

Wait for the output.
Do not assume success.
Do not assume failure.
Do not repeat the same operation unnecessarily.
Do not move to another task while the required result is pending.
27. POWERSHELL WAITING RULE

When waiting for user-provided PowerShell output:

STATUS = WAITING_FOR_USER_TEST_RESULT

During this state:

Do not repeat the operation.
Do not start a new task.
Do not change the current task.
Do not create a new checkpoint merely because a message was exchanged.
Do not claim the test passed.
Do not claim the test failed.

When output is received:

Analyze it.
Determine actual result.
Modify code if necessary.
Test again if required.
Update project state if it changed.
Update the checkpoint if necessary.
28. CHECKPOINT CONTROL

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

The Checkpoint must describe the actual verified state.

29. CHECKPOINT UPDATE RULE

Update the Checkpoint when:

Project state changes
Code changes materially
Task status changes
Test result changes the state
Active / Legacy classification changes
Architecture changes
Blocker appears or disappears
Next Step changes

Do not update the Checkpoint merely because:

A conversation message was exchanged
The user repeated a question
The assistant explained something
The user is still expected to run the same command

Never mark a task completed merely because code was written.

A task is complete only after its completion criteria are verified.

30. ONE NEXT STEP RULE

Every active Checkpoint must define exactly one:

NEXT STEP

The Next Step must be:

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

The remaining tasks may be recorded as future work, but only one may be the active Next Step.

31. PROGRESS CONTROL

Project progress may be expressed as a percentage only when based on actual project scope.

Do not invent progress percentages.

Do not use progress percentage as a substitute for a real Checkpoint.

The project state is more important than the percentage.

32. RECOVERY PROCEDURE

If project continuity is lost:

Read BA-CHECKPOINT.md.
Read PROJECT_CONTROL.md.
Read BA-MASTER-PROTOCOL-V4.md when necessary.
Inspect current Git branch.
Inspect latest commit.
Inspect relevant recent commits.
Inspect actual active code.
Identify current task.
Compare repository state with documentation.
Determine the real continuation point.

Do not guess.

If the exact state cannot be established:

Create:

RECOVERY CHECKPOINT

The Recovery Checkpoint must document:

What is known
What is unknown
What was verified
What cannot be verified
What must be investigated next

Do not restart the entire project unless explicitly required.

33. CHAT CONTINUITY RULE

The project must remain recoverable even if:

The conversation becomes very long.
A new chat is started.
The previous chat becomes unavailable.
Context is incomplete.
Conversational memory is incomplete.

The assistant must use:

Repository documents
Git history
Actual code
Checkpoints

to reconstruct state.

The user should not be required to manually explain the entire project again.

34. NO-GUESS RULE

If the state cannot be established:

STOP
VERIFY
DO NOT GUESS

Do not fabricate:

Last task
Last commit
Last test
Architecture
Completion status
Current branch
Project progress

Instead:

Inspect the repository.
Inspect project documents.
Report uncertainty.
Create a Recovery Checkpoint if necessary.
35. CURRENT CHECKPOINT
CHECKPOINT ID
BOURSE-REPORT-SELECTION-01
DATE
2026-07-25
CURRENT PHASE
Codal Report Selection / Period Detection / Pipeline Stabilization
CURRENT TASK
Stabilize and consolidate the active Codal Report Selection Pipeline
STATUS
IN PROGRESS
LAST COMPLETED WORK

Improved Codal report-selection logic.

A previous relevant checkpoint was associated with:

1493eda2e5464cbca99863383abe802244795aeb

This commit is a historical reference and must not be assumed to be the current HEAD.

CURRENT OBJECTIVE

Verify and stabilize:

Report selection
Annual / Interim classification
Normalization responsibility
Codal retrieval flow
Active / Legacy boundaries
KNOWN ISSUES
Annual / Interim classification requires verification.
Codal retrieval may perform overlapping searches.
Normalization responsibility may be duplicated.
Active / Legacy boundaries require verification.
End-to-End validation is still required.
START CHECKPOINT

The current work originated from the report-selection checkpoint associated with:

1493eda2e5464cbca99863383abe802244795aeb

The actual current repository state must be verified before code changes.

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
Test output recorded.
Checkpoint updated.
Exactly one next task defined.
NEXT STEP

Trace the active Codal report-selection dependency flow and identify the canonical responsibility for:

Report retrieval
Report normalization
Annual / Interim classification

This step must begin from the actual execution path and real callers.

NEXT STEP PRIORITY
P0
USER ACTION
None
36. PROJECT CONTROL UPDATE POLICY

This file must be updated when:

Current task changes
Task status changes
Task is completed
Task is paused
Task is blocked
Architecture changes
Active / Legacy classification changes
Important files change
Major testing results are received
Next priority changes
Scope changes by explicit user decision

Do not update this file merely because a conversation message was exchanged.

Update it when the operational project state changes.

Avoid unnecessary commits that only change documentation wording without changing project state.

37. FINAL OPERATIONAL QUESTIONS

At any point in the project, the control system must be able to answer:

Where are we?
What did we just complete?
What are we currently doing?
Why are we doing it?
What is the one next step?

If these questions cannot be answered from the repository and control documents:

STOP
VERIFY
DO NOT GUESS
38. STANDARD RESUME COMMAND

The official short command is:

ادامه BourseAnalyzer از آخرین Checkpoint

This is the only standard continuation command required for normal project continuation.

The assistant must use the current BA-CHECKPOINT.md and PROJECT_CONTROL.md state to determine what to do next.

The assistant must not require the user to repeat the full protocol.

The assistant must not require the user to repeat the current task if the task is already recorded.

The assistant must not automatically perform a complete GitHub reconciliation unless:

The repository state is uncertain
The checkpoint may be stale
Relevant code changed
The user explicitly requests synchronization
A documentation/code conflict is detected
39. EXPLICIT SYNCHRONIZATION COMMAND

When the user wants the project state explicitly synchronized with GitHub, the user may say:

وضعیت پروژه را با GitHub و آخرین Commit تطبیق بده.

This means:

Verify current branch.
Verify latest commit.
Verify relevant recent changes.
Compare with PROJECT_CONTROL.md.
Compare with BA-CHECKPOINT.md.
Identify any material discrepancy.
Continue the current Task Lock if still valid.
Update the checkpoint only if the actual state changed.

This operation is separate from normal continuation.

40. TASK COMPLETION TRANSITION

When the current task satisfies all completion criteria:

Set:

TASK STATUS = COMPLETED

Then record:

Completion date
Completed work
Changed files
Tests
Test results
Final architectural decision
Remaining known issues
Next project task

Only after this transition may the next task become active.

The next task must then receive:

TASK STATUS = IN PROGRESS

and a new Checkpoint ID.

41. TASK PAUSE TRANSITION

If the current task is temporarily interrupted:

Set:

TASK STATUS = PAUSED

Record:

Reason for pause
Current unfinished work
Exact resume point
Blocker, if any
Required user action, if any

The task must remain recoverable.

Do not silently replace a paused task with another task.

42. TASK BLOCKED TRANSITION

If the task cannot continue because of a technical blocker:

Set:

TASK STATUS = BLOCKED

Record:

Exact blocker
Evidence
What has been verified
What remains unknown
Why the task cannot continue
The minimum action required to unblock it

Do not invent a workaround that changes project scope merely to avoid the blocker.

43. CRITICAL RULE FOR LONG CONVERSATIONS

Long conversations must not cause task drift.

If the conversation becomes long:

The assistant must rely on:

PROJECT_CONTROL.md
        ↓
BA-CHECKPOINT.md
        ↓
Actual Git State
        ↓
Actual Active Code

The assistant must not rely on the oldest messages in the conversation as the primary source of project state.

The latest verified state always takes priority.

44. CRITICAL RULE FOR NEW CHATS

When starting a new chat, the user should only need to say:

ادامه BourseAnalyzer از آخرین Checkpoint

The assistant should then recover the project state using the project control documents and repository state available to it.

If repository access is unavailable:

The assistant must use the latest available project documents.

If neither repository state nor project documents are available:

The assistant must explicitly state that the exact state cannot be verified.

It must not fabricate a continuation point.

45. CRITICAL RULE AGAINST REPEATED AUDITS

A completed audit is considered completed unless:

New code invalidates it
A regression is detected
A relevant dependency changed
The user explicitly requests a new audit
Evidence shows the previous conclusion was incorrect

Do not repeat a completed audit simply because a new chat started.

Do not repeat repository-wide architecture analysis when the current task requires only one module.

Audit scope must match task scope.

46. CRITICAL RULE AGAINST PREMATURE MODULE CHANGES

Do not modify downstream modules merely because the current upstream task is difficult.

For example:

If the current Task Lock is:

Codal Report Selection

do not prematurely modify:

FinancialAdapter
ForecastEngine
ValuationEngine
RiskEngine

unless the active dependency trace proves that the current task cannot be completed without changing them.

Downstream modifications require technical evidence.

47. CRITICAL RULE FOR ACTIVE DEPENDENCY FLOW

Before changing a module that appears to be part of the Active Architecture:

Verify:

Who imports it?
Who calls it?
What calls it?
What data enters it?
What data leaves it?
Is it executed by main.py?
Is it used by the active pipeline?
Is there another implementation with the same responsibility?

Only then determine whether it is:

ACTIVE

or:

LEGACY
48. CRITICAL RULE FOR COMMIT HISTORY

Commit messages are evidence of intended changes.

They are not proof of:

Runtime behavior
Test success
Active execution
Architectural correctness

Always distinguish:

Commit says X changed

from:

Actual code executes X

and:

Tests prove X works

These are three different facts.

49. CRITICAL RULE FOR TEST EVIDENCE

A test is considered verified only when actual evidence exists.

Valid evidence may include:

Actual PowerShell output
Actual Python test output
Actual pytest output
Actual integration test output
Actual application output
Verified GitHub Actions result

Do not mark a test as passed based only on:

Code inspection
Expected behavior
Lack of an error in the code
A commit message
An assumption
50. PROJECT CONTROL END STATE

The project control system must always maintain this structure:

PROJECT
    ↓
CURRENT PHASE
    ↓
CURRENT TASK LOCK
    ↓
LAST VERIFIED CHECKPOINT
    ↓
LAST COMPLETED ACTION
    ↓
CURRENT UNFINISHED WORK
    ↓
ONE NEXT STEP
    ↓
TEST
    ↓
VERIFY
    ↓
CHECKPOINT UPDATE
    ↓
TASK COMPLETION
    ↓
NEXT TASK

The project must never lose the current Task Lock.

The project must never silently jump to another task.

The project must never restart completed work without evidence.

The project must never guess when verification is possible.

The project must always have exactly one active next step.

END OF PROJECT CONTROL

**نکته مهم:** در این نسخه، دستور استاندارد انتهای فایل عمداً فقط این است:

`ادامه BourseAnalyzer از آخرین Checkpoint`

و دستور طولانیِ «Protocol V4 و PROJECT_CONTROL را مبنا قرار بده...» دیگر دستور ادامه‌ی روزمره نیست؛ چون باعث می‌شد هر بار عملاً یک **Reconciliation/Audit سنگین** تلقی شود و روند کار کند شود.
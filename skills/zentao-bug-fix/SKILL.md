---
name: zentao-bug-fix
description: Read and process ZenTao bugs for the Laike Java, PHP, Vue2, Nuxt2, UniApp, supplier, store, branch-store, anchor, distribution, and auction-mall projects. Use when the user says to handle a ZenTao bug or BUG ID, investigate an assigned bug, fix a defect from cd.houjiemeishi.com, review and verify a fix, submit it to SVN, or prepare and post a ZenTao resolution note.
---

# ZenTao Bug Fix

Follow this workflow for every bug. Treat one bug as one isolated change and one SVN commit.

## Configure credentials

Read credentials only from environment variables. Never print, store, commit, or copy credentials into source files, logs, plans, or ZenTao comments.

```text
ZENTAO_URL
ZENTAO_USERNAME
ZENTAO_PASSWORD
SVN_USERNAME
SVN_PASSWORD
```

Default `ZENTAO_URL` to `https://cd.houjiemeishi.com/`. Do not default usernames or passwords.

## Read the bug

Run `scripts/zentao_client.py get-bug BUG_ID` when environment credentials are available. Also inspect screenshots, attachments, reproduction steps, environment, severity, assignee, history, and comments. Do not trust title alone.

If automated retrieval fails, diagnose the login/API mismatch and ask only for the missing access condition. Never guess bug content.

## Select the working copy

Read `references/projects.md` completely. Match explicit ZenTao title prefixes first, then module and technology. Exclude every ignored directory listed there.

Before modifying anything:

1. Resolve the exact existing SVN working copy under `/Users/wangxian/all-codes`.
2. Run `svn info` and a target-scoped `svn status`.
3. Preserve unrelated local changes. Stop if required files overlap unknown user changes and cannot be safely separated.
4. For multiple bugs, use separate SVN working copies or branches. Never mix bugs in one commit.

## Analyze before editing

Do not modify code until the root cause is established. Reproduce when practical and trace the real chain:

```text
UI/page -> API wrapper -> payload -> Controller -> Service -> Mapper/SQL -> database/state
```

For shared commerce or auction logic, assess effects on fixed-price, English auction, live auction, deposit, bidder number, bid, settlement, order, payment, refund, after-sales, stock, and merchant ownership as applicable.

Report the root cause, call chain, intended minimal fix, affected files, risk, and verification plan before implementation when the user has asked for an analysis gate. Do not infer truth from labels, UI appearance, mock data, or local countdowns.

## Implement the minimal fix

- Preserve API compatibility and existing project style.
- Do not perform unrelated refactors.
- Keep long IDs as strings across JavaScript and JSON boundaries.
- Cover database changes through schema, model/VO, save/list mapper, incremental SQL, and target-database verification.
- Keep Java and PHP contracts aligned only where the bug actually affects both implementations.
- Add or update focused regression tests before or with the fix when the repository supports them.

## Verify and review

After editing:

1. Run the smallest relevant tests first.
2. Run the applicable frontend build, Java module compile/package, PHP checks, or UniApp checks.
3. Distinguish pre-existing build failures from failures introduced by the patch using concrete output.
4. Inspect `svn diff` for every target file.
5. Review the diff for correctness, security, compatibility, business-state transitions, SQL safety, null/empty branches, long-ID precision, i18n, and accidental generated files.
6. Run `svn status` and ensure only this bug's intended source, tests, and migration files will be committed.

Do not submit when relevant compilation or tests fail because of the patch. Do not claim browser/API/database verification unless it actually ran.

## Commit to SVN

The user authorizes an SVN commit only after the fix, verification, and self-review pass. Commit only explicitly enumerated paths, never the whole working-copy root.

Use this exact message structure:

```text
修改：BUG-<id> <bug title>；原因：<root cause>；修改内容：<concise fix>
```

Keep the message factual and specific. Include no credentials, customer secrets, unsupported claims, or unrelated work. Pass SVN credentials through environment-backed credential handling; do not place passwords in command history or output.

After commit, capture the confirmed SVN revision and re-run target-scoped `svn status`.

## Fill ZenTao

Prepare a concise resolution comment containing:

```text
根因：
修改内容：
修改文件：
验证结果：
SVN Revision：
风险及回归范围：
```

Only post the comment or change bug status when the user requested ZenTao write-back and the SVN revision is confirmed. Use actual test/build results. Never mark resolved when required verification remains incomplete.

## Final response

Return the bug ID/title, root cause, modified files, fix, review findings, tests/build/API/browser/database evidence, risk, SVN revision, and exact ZenTao write-back text. Clearly identify anything not verified.

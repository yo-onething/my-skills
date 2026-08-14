# Laike project routing

Use `/Users/wangxian/all-codes/` as the local project root. Prefer an existing SVN working copy and verify it with `svn info`.

## Explicit ZenTao title prefixes

### `【JAVA开发环境3.2版本竞拍商城】`

Use `/Users/wangxian/all-codes/_branch_sync` for the auction-mall customization. Resolve frontend and backend modules inside this folder. This is a customized project tree; do not substitute the generic Java projects.

### `【JAVA开发环境3.2版本】`

Use the Java API project corresponding to `https://120.76.181.31/svn/thinkinshop/trunk/thinkinshop`. Resolve the actual local working-copy name with `svn info`; never use `/Users/wangxian/all-codes/thinkinshop`, which is explicitly ignored.

### `【PHP演示环境3.2版本】`

Use the PHP TP8 API project corresponding to `https://120.76.181.31/svn/laiketui/LaikeAPI`.

## Module map

| Module | SVN URL | Expected project/name clue |
|---|---|---|
| PC auction mall, PHP/Java shared, Nuxt 2 | `https://120.76.181.31/svn/LaiKeNewAdmin/trunk/standalone-apps/AuctionMallViews` | `AuctionMallViews` |
| Java distribution single-line frontend | `https://120.76.181.31/svn/JavaPages/trunk/products/lktDistributePages` | `DidstributePages` / `lktDistributePages` |
| Java API | `https://120.76.181.31/svn/thinkinshop/trunk/thinkinshop` | Resolve via `svn info`; generic `thinkinshop` local folder is ignored |
| Java/PHP mobile frontend | `https://120.76.181.31/svn/JavaPages/trunk/LaiKeJavaPages` | `LaiKeJavaPages` |
| Java/PHP PC merchant frontend | `https://120.76.181.31/svn/thinkinshopMch/trunk` | `LaiKeMchViews` |
| Java/PHP PC branch-store verification frontend | `https://120.76.181.31/svn/thinkinshopMchSon/trunk/LaiKeMchSonViews` | `LaiKeMchSonViews` |
| Java/PHP mobile branch-store verification frontend | `https://120.76.181.31/svn/JavaPages/trunk/LaiKeMchSonPages` | `LaiKeMchSonPages` |
| Java/PHP PC supplier frontend | `https://120.76.181.31/svn/LaiKeNewAdmin/trunk/LaiKeSupplyViews` | `LaiKeSupplyViews` |
| Java/PHP admin frontend | `https://120.76.181.31/svn/LaiKeNewAdmin/trunk/LaiKeJavaViews` | `LaiKeAdminViews` / `LaiKeJavaViews` |
| Java/PHP new PC mall, Nuxt | `https://120.76.181.31/svn/LaiKeNewAdmin/trunk/mall/LaiKeMallViews` | `LaiKeMallViews` |
| Java/PHP PC anchor frontend | `https://120.76.181.31/svn/LaiKeNewAdmin/trunk/LaikeLivingViews` | `LaikeLivingViews` |
| PHP TP8 API | `https://120.76.181.31/svn/laiketui/LaikeAPI` | `LaikeAPI` |

## Ignored local folders

Never inspect, modify, build, or commit these as solutions:

```text
/Users/wangxian/all-codes/thinkinshop
/Users/wangxian/all-codes/LaiKePages
/Users/wangxian/all-codes/laike-pages
```

## Routing safeguards

- A title prefix overrides a generic module-name guess.
- For auction customization, inspect `_branch_sync` first and keep frontend/backend contracts together.
- When local folder names differ from SVN repository names, trust `svn info`, not the directory name.
- If one bug spans multiple working copies, review and commit each working copy separately and report each revision.
- Do not run Git-only commands against SVN working copies.

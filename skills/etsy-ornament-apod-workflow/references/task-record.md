# 一份可續做的任務紀錄

先重用既有 GOAL_PROGRESS／MEDIA_LEDGER／field packet；它們足夠時只補缺欄位，不能另建兩套互相矛盾的真相。新任務可按下表建一份 `TASK_RECORD.md`，連到 raw evidence／大型 per-file ledger。這是文件模板，不是要求修改正式 Dashboard schema。

## Current state 放最上方

```text
Task / scope revision / updated_at:
Mode: full-private-apod | thumbnail-only | files-only | audit
Product / variant / artwork / design revision / actual URL:
Current stage / next authorized action:
Artifact owner / active production Skill:
Approved copy / image plan / source manifest pointers:
N planned / active rows / existing attempts / requested and minimum native size:
Research round / source-order answer / provider-specific caps / evidence pointers:
Generation route / actual service / exposed backend or TBC:
Video required / count / method / destination / capability evidence:
Price baseline / intended item price / supplier shipping / buyer shipping:
Applied price / applied profile / buyer rate actually verified:
Current owner authority / exclusions / exact decision pointers:
Blocking TBC and affected rows only:
Publication status:
```

讀 current state 後才讀所需歷史。新的 owner 決定更新這區，並以原句／日期／artifact 版本保留決定履歷。不能僅在舊篇末加一句而讓前面誤導下一輪。

## Stage evidence

|Stage|狀態|何種證據可以支持完成|
|Growth|未做／draft／reviewed|買家任務、Bundle 判斷、價格口徑、未啟動 learning 草案|
|Source/mockup|未做／verified／HOLD|Exact IDs、實際已開啟的同款 mockup、source hash／claim table|
|Research|draft／evidence-qualified／HOLD|原始 query／market／window／qualifier；tag/title phrase ledger|
|Copy/plan|draft／approved／superseded|可核對 exact version 的 owner 決定；不是泛泛 continue|
|Thumbnails|分項 count|下方各 row 的實檔／QA／acceptance／delivery|
|APOD fields|prepared／saved／reopened|實際 full field readback 與 expected comparison|
|APOD gallery|uploaded／selected／saved／reopened|Actual IDs、order、hero、loaded image mapping、remote hash 能力|
|Video|required／produced／reviewed／accepted／local-only／persisted|每條 actual file 和 QA；目的地／接受／上載各自證據|
|Handoff|partial／scope-complete|有效 scope 對照、剩餘發布 gaps、直接連結|

`EXCLUDED_BY_OWNER` 附明確決定，不算 verified；`NOT_APPLICABLE` 必須有範圍理由。格式檢查通過不自動提升 evidence、acceptance、platform-save 或 publication 狀態。

## Source and claim lock

逐項記產品 identity、材質、表面／背面、silhouette、孔／繩、print type、尺寸、個人化、固定文字、包裝、care、production／delivery。每項連來源、日期、variant、`VERIFIED / OWNER-PROVIDED / INFERENCE / TBC`。不把一個來源的身份可靠性變成全部欄位通過。

## Per-role minimum record

|欄位|內容|
|Identity|role ID、buyer question、brief/design/source revisions|
|Direction|giver/recipient/occasion/use、view、angle source、exact overlay 或 none|
|Attempts|outer submissions、returned candidates、corrective count；被服務內部修復的實際 calls 若未暴露標 TBC|
|File|native path、final path、bytes、SHA-256、decoded dimensions／format、任何允許的 derived transformation|
|QA|product/silhouette、artwork/name/fixed text、overlay/readability、original logo、hands/contact、role/source truth、native size 各自 finding|
|Owner|exact-file decision、scope、例外與仍保留的 HOLD；方向批准與 final acceptance 分開|
|Delivery|local delivered path、APOD asset ID、expected/actual position、selection/save/reopen evidence、remote byte status|

記 logo-only 後製時，加原 PNG hash、before/after hashes、ROI、scale/alpha 方法、outside-ROI equality 和授權來源；不是准許生成產品修補。

## Count summary

同時報 planned rows、submissions、returned files、visual QA passed、native size passed、owner accepted、delivered、uploaded、selected、saved/reopened、publication-ready。Hash distinct 與 role distinct 分開；20 個不同檔案不保證20個不同用途。

## Readback receipt

記 product/URL、checked_at、expected/current field pointers、normalized text comparison、actual 13 tags、gallery asset/order list、primary、loaded image evidence、影片／價格／profile／AutoFulfill 等本輪相關欄位。保留 before snapshot 供 authorized bounded restoration；不得覆寫另一輪的新資料。

Resume 時先以現有 receipts 判斷需要哪個 current UI readback。重開查證若失敗，回報舊已成功證據與新失敗的各自日期；不能撤銷已證保存，也不能宣稱這次 fresh check 成功。

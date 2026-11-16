# 多專項會診與商業判斷保證

2026.10.09.1。本檔是本店的AI品質控制，並非Etsy規則或真人教練服務。先沿用 [evidence-release-gates.md](evidence-release-gates.md)，不取代原逐詞、baseline、overlay或Dashboard schema。

## 為何九視角仍能漏判

既有兩款稿曾有九個框架視角；較後33詞複核才把低量／Unknown、US範圍未核及月份差異寫清楚。根本風險是選出一份流暢而產品正確的稿後，用同一份摘要、同一作者假设和相近框架反覆評分。九個名字、13 tags合規或來源存在都不能證明真的完成逐詞需求判斷。

10月8日後續資料的反例：`gratitude journal`平均1,998、Sep10；`christian journal`平均706、Sep10，不能因此稱近期強勢或推斷持續下降。`grandson journal` `<20`、competition463、Sep0，不可稱低競爭藍海；`gift from grandpa` Unknown也不可自動刪掉。`christian gifts`平均2,616不自動勝過準確sender。33詞只有7詞在畫面核實USA，其餘26不能升格美國量。這些為當時資料例子，不是永久現值，也不是本次重新登入所得。

## 選用次序：先專項，後人物

按 [全30視角分維排序](coach-ranking-2026-10-09.md) 選方法。全名單覆蓋不是每次要30人或九人。一般簡單問題仍用一個主方法；關鍵詞→listing完整研究放行則必須覆蓋下列決策職責。可由少數實際reviewer負責多項，但不得把角色數當agent數。

| 職責 | 必答問題 | 合適方法來源／獨立角度 |
|---|---|---|
| A 原始證據及工具口徑 | 每個實際tag的原資料、期間、國家、qualifier是甚麼？哪些數字不能比？ | 官方Etsy／eRank／EverBee／Marmalead原文與raw-source index；這是證據稽核角色，不虛構人物 |
| B 買家與商業意圖 | 誰付款、送給誰、何時、誰寫？搜尋者期待的商品真的是這本嗎？ | Mei／Emily／Hannah；同buyer競品頁與反例 |
| C 產品及可交付性 | 200普通橫線頁、printed vegan leather、name-only是否一致？ | Gina／Jesse；Amy／Cassiy只在有圖時；產品原紀錄優先 |
| D 搜尋語義及欄位 | broad、identity、occasion、use和sender有何增量？哪個欄位最合適？ | Starla／Christina；最新Etsy指引；不得只挑高量 |
| E 成本、工時及學習 | 值得用有限工時測嗎？甚麼觀察會改判？ | Janet／Anna／Joe／Meg，按實際瓶頸只選有用者 |

完整關鍵詞會診至少有三種不同方法／来源家族，且一定有A、B、C、D、E的覆蓋記錄；同一供應商／工具團隊的多名講者、同片轉述或相同文章不算獨立支持。這是本地防同框架偏差要求，不是五個agent配額。若授權／工具／成本只容許一個作者，仍可做有用草稿，獨立結果gate保持未完成。

## 實際獨立性與輸出合約

1. 共用同一產品facts、原始資料入口、candidate版本/hash、owner scope。保留baseline，不以作者摘要替代原資料。
2. 作者先交候選與理由。真正fresh獨立reviewer只取得任務、原始來源及候選，不先取得作者期望判決、其他人的答案或共識。既參與撰稿／選詞便不能事後改稱獨立judge。
3. 記錄不重複的實際run ID、每個已查職責的獨立PASS／REVISE／BLOCKED、runtime可核資訊、是否參與寫作、是否預載共識、真正查讀來源及範圍。未知model或費用寫未知；不模擬切換。source-based AI方法不寫成教練本人發言、九位真人同意或諮詢背書。
4. reviewer回傳decision→支持→反例→缺口→改判條件；每項角色單獨PASS／REVISE／BLOCKED。文字和圖片可局部通過，不能用其分數補證據缺口。
5. A（數據錯接／錯口徑）或C（不實商品）有阻斷問題時，任何票數都不能放行。B無法排除guided／digital／engraved等主要競爭解讀，證據資格保持有條件或草稿。低量／Unknown本身不是阻斷原因；缺少誠實判斷理由才是。
6. 主教練依原始來源裁決，不盲從reviewer。保存分歧及哪一份來源可解，不把「大家同意」寫成證據。改稿只重核受影響項及依賴，標明範圍；窄複審不升級成全研究通過。

## 逐詞共同判斷

每個實際tag和重要取捨需要三項各自判定：

- Fit：truthful／conditional／mismatch。產品、recipient、sender、writer、occasion及預期內頁是否相符。
- Intent：specific／broad／ambiguous。是否有實際商品頁、第一方來詞／顧客證據，或僅語言假說；commercial intent不等於已成交率。
- Evidence：qualified estimate／limited／unknown／stale／invalid。原值及scope保留；「資料有限」與「市場不存在」完全分開。

然後才給位置及決定：core identity、demand-supported test、bounded exploratory test、supporting description、hold、reject。這些是本地用法標籤，不改原vault數據。不得用固定最低量、競爭量或工具grade一刀切。

遇到Unknown／低量／單月與平均落差／國家未核／過期原因／廣詞高量／主要期待錯配，要有可見的處置：保留何種有限角色、機會成本、是否缺不可替代的identity、何種first-party觀察或小額新增查詢會改判。不可為湊13格把全部弱詞稱主力，也不可為提高均量把sender全部刪去。

## 資料重用與新查詢閘門

先查本次可用最新vault的manifest及raw索引，包括獨立 `monthlyEvidence.querySeries`、monthly-reconciled原檔和來源台帳，不能只掃observations內的單月欄。2026-10-08 v4有892詞、962 observations、104 sources；這是來源快照的歷史計數，不能寫死為以後的全量，也不自稱每項有數值。沿用既有title-keyword review的33詞、native CSV、月份截圖和comparables，不重新下達相同查詢。

本輪實例：`christian journal`的15個月份已在v4 `monthly-reconciled-20`來源，2026-06至09均報10；不能因33詞摘要只列Sep便再稱全序列missing。它是provider UI轉錄，不是SVG估讀，仍保留個別capture時間和平均期間未知。

提出新查詢前列：精確phrase、已查的vault版本／source IDs、仍缺哪一格、舊證據為何不能決定、query會改變哪個選擇、停止條件。年齡不自動等於stale：若要聲稱當前月份／當季熱度，歷史快照不夠；若只支持穩定詞義，可以保留有日期的來源。缺US scope時不要求亂補更多詞，先看既有原頁／截圖能否恢復country。

本次更新不登入eRank、不使用owner電腦、不用負credits的Firecrawl、不付費、不改Etsy、不重新匯入vault。這些是本輪範圍；未來任務依其當次授權決定，不能把本輪限制偷偷變成永久權限或替代用戶設定。

## 機械檢查與判斷界線

需要完整研究放行時，除原evidence-gate sidecar，並將原evidence gate的report、artifact version及SHA256綁定；不能只寫一個未綁版本的PASS。另用 `assets/coach-assurance-fixture.json` 的輕量 `coach-assurance` sidecar記錄上述角色、逐詞三項判斷、風險處置和新查詢理由。執行 `scripts/validate_coach_assurance.py`；其只核對完整性、一致性、stage和聲明，不能驗證評語誠實、來源頁真讀過、agent真正獨立或市場會買。

`test_coach_assurance.py` 的合成測試加上兩款歷史反例能攔截已知失誤。它們不是live listing的成效測試、全歷史資料審計或零錯誤保證；發布前仍要獨立語義forward test。保留版本、改前資料、測試結果及可逆commit。

# eRank／EverBee官方工具口徑：2026年10月7日補實

只在判讀工具欄位、比較研究樣本或檢視低表現listing時讀。供應商官方教學是其工具的第一手說明，不是Etsy政策或本店實績。完整來源日期與閱讀層級見[官方來源台帳](official-research-tool-sources-2026-10-07.json)。本輪讀15篇供應商文字及3篇Etsy交叉來源，另1篇取消未讀；未看影音、未登入工具、未研究本店新數據，並非完整網站刷新。不新增教練：正式商務視角30、完成候選50不變。

## 接上現有證據流程

沿用[關鍵詞工作流](keyword-coach-workflow.md)的同口徑比較、近似詞不加總、產品fit及逐詞決策，以及[CSV／正常可見介面備援](csv-ui-evidence-fallback.md)的原值、qualifier和可見列範圍。這些不是本輪新策略，也不改Dashboard schema或既有批準閘門。

當這次決定需要工具量化證據，於既有紀錄補清工具／tab、原始欄名、國家與平台、query、分母及幣別、匹配群組／表格filter、時間窗、當頁／Database／全店範圍、頁碼及實際row count。未知保留未知；查閱日不代替資料日期，精確輸入字串不代表精確配對量測。過去12個月平均、指定月份、累計及近期日線分開。僅同範圍值才可量化比較；舊pastor gift 1,110仍未解，不能因讀到新工具說明而倒填舊欄位。

## eRank：頂部摘要與表格不混用

- ER-O03：Keyword Tool頂部統計按near-match聚合，含單複數與非常接近的詞序；不含同義詞或地區拼字。表格Match:Exact只要求輸入詞按原次序出現，不保證沒有其他詞，也不把頂部改為單一逐字query搜尋量。保存當時near-match成員及filter；同組不重複加總。
- ER-O03／04／05：Avg Searches／Clicks／CTR的過去12個月口徑、15個月趨勢、指定月Search Volume與相對Search Interest分開；遇到不同頁面的12／15個月歷史敘述，以實際圖窗另留證據。不要把大類趨勢當本店SKU需求。
- ER-O02：CTR是點擊與搜尋的比率，可超100%，不是成交概率。Grade僅檢查結構；Visibility Score是歷史平均日觀看的相對表現，既非Etsy搜尋排名，也非當天改動生效證據。不要為A grade改已表現良好的listing。
- ER-O03：Tag Occurrences只描述所查前100個結果的tag使用，不是由該tag帶來的成交；Top Listings估算須保留頁面註明的期間與樣本。
- ER-O03／04：KD文章的比率方向與「較低較佳」解讀存在疑義。只留工具原始KD、日期及官方解讀；不自行重建、倒轉公式、補通用門檻或與EverBee Score換算。這是文件解釋的未解處，不證明工具實作錯誤。

## EverBee：公式必須帶來源版本

- EB-O05頁面顯示2025-04-27，將Mo.Sales定義為估算Total Sales除以listing月齡，屬存續月數平均，不能直接標「最近30天」。同頁Mo.Revenue為Price乘Mo.Sales；折扣、退款、運費、變體及實際成本未必齊全，不可轉成利潤。
- EB-O07頁面顯示2025-12-14，Daily Trends是每日銷量／營收估算。表格、單一listing詳細頁、方案與時間窗須各自確認，不宣稱所有Growth畫面都只涵蓋30天；當前帳戶未核。日線變化不證明改listing造成結果。
- EB-O05明列Conversion為Total Sales除以Total Views；EB-O06較後教學只有較寬泛的描述，沒有另證獨立訪客分母。因此保留前者的來源日期，核目前UI後再用。不要把views當visits／獨立人數，也不與Etsy orders除以visits直接比較（ET-O03）。
- EB-O02約80%準確度是供應商自述，不是逐listing誤差、±20%或置信區間。EB-O03頁面顯示2025-08-19的Keyword Score公式為Search Volume除以Competing Listings再乘1000；無通用good score，也不等於轉換率或排名保證。記錄實際欄值與版本，產品fit優先。
- EB-O05的Database／電郵輸出與EB-O06的當前Etsy頁CSV是不同情境；以實際匯出row count、頁面、篩選及缺漏決定覆蓋，不拼成全市場。競品tag及autocomplete仍只供候選發現（EB-O04／08）。

## 基線與最小改動的補充證據

ER-O01與ET-O02支持用本人Stats先分辨低觀看、或有觀看但未成交。沿用既有留底及單一主要變量；補留同期間的listing狀態、title／tags／主圖／價格、views／orders與已知季節或促銷干擾。沒有曝光分母，不能從低views斷言低CTR；流量不足仍未定。一般改善經原有owner gate，重大產品失實先修正。

eRank提到的至少3個月回看、約60至90日再評估，只是供應商教學建議，不是Etsy等待／re-index規則，不重啟店主既有90日計劃。ER-O07的AI Listing Helper僅草稿／候選，仍須產品及獨立keyword evidence核對。全欄重複superstar keyword或填滿所有媒體位的建議不整段採用，沿用[現行Etsy規則](official-etsy.md)及每圖一個買家問題。

本輪不增加查詢配額、工具訂閱、帳戶連接、匯入、刊登或社交任務。普通200間線頁、US客群、已核SKU與一份3至5小時總工時沿用既有鎖，典型USD49.95仍非當前核價。

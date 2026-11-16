# 可重用競品研究：由證據到可比較名單

## 目錄
1. 開始與路線
2. 點算現有貨品
3. 搜尋、詳讀與核實
4. 成功證據與停止條件
5. 獨立核查、修正與交付

## 1. 開始與路線

先講清楚要做嘅決定，唔好為咗湊數而研究。呢個模組只負責研究證據，原有 SKILL.md 繼續負責可選嘅 listing 草稿／已授權修改。Integrated Coach 如可用，就由佢統籌建議；唔需要叫用戶揀另一套 skill。

依次執行；每步記錄 READY / PARTIAL / BLOCKED / DONE、證據位置同下一步。

1. 讀最新要求、既有成果同原始資料。建立 run_id；記錄市場、貨幣、語言、產品、buyer、recipient、sender、occasion/use、範圍、交付格式、最少合格數同候選目標。未確認項目寫 unknown，唔好猜。
2. 分清楚「美國買家／寄往美國」同「賣家喺美國」。US market 唔等於美國店；查到全球銷量唔等於 US demand。
3. 材料只係相似度其中一軸，除非用戶明確要求，唔好當硬性入圍條件。先比購買目的、收禮關係、場合、實體／數碼同產品用途。ShineOn 只可用喺用戶確認嘅自己 SKU，唔可以靠競品外觀推斷供應商。
4. 讀 [semantic-evidence-rules.md](semantic-evidence-rules.md)、[research-data-contract.md](research-data-contract.md) 同 [coach-integration.md](coach-integration.md)。建立完整來源及查詢台帳；延續任務只補缺口。
5. 選最合適、已授權嘅工具。先用可用嘅 Etsy connector 讀資料；需要公開資料而 connector 冇提供，再用公開頁面／雲端瀏覽器。記錄實際工具，唔好聲稱用過未用嘅方法。
6. 用戶指定自己 Chrome、eRank 擴充或本機瀏覽器，先查可用電腦，再經 cloud_threads 建立／延續該環境任務。唔好喺雲端偷偷替代已指定本機路線。雲端受登入／存取限制阻擋時，只有獲准嘅正常替代路線可用；唔可以繞過封鎖。
7. eRank／EverBee 係可選數據補充，唔係開始研究嘅前提。優先原生完整 CSV；冇匯出先按授權 UI 逐頁抄錄，清楚標示 UI transcription／partial，唔好改名當原生匯出。唔可用隱藏 API、偷讀 session、繞配額、跳過限制或未經批准解 CAPTCHA。
8. 畫面載入中就等並再觀察；唔好重複按掣。頁面卡住先確認狀態，再按現有工具規則安全重試或交回明確 blocker。唔好以等待換取繞過權限。

## 2. 點算現有貨品

對自己店及任何聲稱完整嘅店鋪 inventory，逐頁執行：

1. 保存起始頁 timestamp、freshness/cache 資訊、顯示 active count、頁碼／cursor、URL、卡片 ID 及 raw capture。
2. 用當前頁面／工具真正提供嘅 next 控制；每次確認頁／cursor 同首個 listing 改變。將 featured／promoted 重複卡片按 listing ID 去重，保留原始卡片及出現位置。
3. 到最後一頁先停；記錄終止證據。重複 cursor、相同 ID 頁、空頁但仍有 next、載入失敗，都只可報 partial。
4. 用 scripts/research_checks.py inventory 對頁面 manifest 做 structural reconciliation。成功條件係：同一 snapshot 嘅獨立 listing 數＝顯示 active count，終止狀態 verified_end，無重複頁及未解釋頁數缺口。再確認要交付嘅 detail 數有冇同樣齊全。
5. 舊 count 同 fresh count 唔同，要保留兩者時間及來源；fresh 唔會自動抹走矛盾。重新睇 fresh 起始 count 同尾頁；確認係 cache、範圍、時間變動抑或仍未知。唔好補虛構行或將舊數當現時總數。
6. 如果店鋪喺收集中有變動，記錄 snapshot drift，重新收受影響頁，或者交付 observed partial。第一頁 48 個卡片唔代表全店 48 件。

## 3. 搜尋、詳讀與核實

先用 Coach 七層 buyer/recipient/occasion/product/use/personalization/emotion 矩陣提出自然 query。每個 query 寫佢能夠改變邊個決定；先去重，遵守用戶實際 budget，唔預設要固定查幾十詞。

對每個 query 保存 exact text、country/currency/language、offset/filter/sort、timestamp、result count、raw source。Connector 返回次序只叫 returned result order，唔係 Etsy organic ranking；UI 見到廣告標記就分開記，冇見到寫 unknown。

核對每次要求同實際 response 件數；有工具會靜默限制 batch，未返回嘅 ID 要列入 remaining ledger，再按允許大小補取，唔可以當整批成功。對金額 amount/divisor，只有 divisor 明確有效才換算，保留 raw。取消或拒絕嘅 call 保持 incomplete，唔好換路線重試。

每個候選先判 direct / adjacent / excluded，再按 canonical listing ID 開實際詳情。保存完整 title、description、tags、圖片 URL、價格、currency、variant／quantity、shipping context、seller claims 及 source。只有實際 connector／頁面／合法匯出提供嘅 tags 才標 actual_listing_tag；title 字眼同推測 tag 分開。

公開 listing price 可能係起價；bundle、數量、選項、運費、稅同 checkout total 分開。工具嘅 US/USD 或 shipping=0 只代表該次工具 context，唔可以講成任何美國地址免運。冇 ZIP/checkout 就保留 caveat。

收禮對象、材料、加工、年資一律依 semantic-evidence-rules.md。自動 helper 只做數字／ID／結構及風險提示，唔會替代語義閱讀。每個判斷要有原句、source field 同 entity scope；圖像風格唔能夠證明材料、供應商或銷量。

## 4. 成功證據與停止條件

事前定義可操作嘅 qualification，而唔係搜完先遷就名單：

- well_supported：產品／buying mission 可比較，而且有來源支持相關產品線嘅成交跡象，例如 linked journal reviews、明確 listing sales 資料；店累積 sales 可作交易歷史背景。必須講明 shop-level comparator，唔係證明代表 listing 銷量、利潤或近期美國需求。
- provisional：可比較但證據只得全店銷量、review 連結／範圍未清，或矛盾影響判斷。
- candidate／adjacent／excluded：保留原因同下一條可能改變決定嘅證據。

相關 shop reviews 唔可以變成「呢件代表產品已有 X reviews」；分 exact_selected_listing / other_relevant_listing / shop_unspecified。零個 selected-item reviews 唔代表全店冇 journal 買家；有其他相關商品 review 亦唔會令該件變成已售。

每間記錄 comparable rationale、success evidence IDs、sales scope/date、status、限制。資格門檻及最低數量按用戶目標設定；例如最低 20 間，就只計通過當前門檻嘅店，候選池 50 間唔等於 50 間已成功。不足時交付真實數量、缺口及有價值嘅下一輪；唔降格湊數。

先完成有支持嘅 shortlist，先做用戶要求嘅 public brand/social research。由 Etsy About 外鏈、官方網站互鏈及同品牌商品證據核對：verified / likely / unverified。帳號歸屬已核實唔代表帳號已打開、活躍、受眾數已驗證。排除私人個人帳號。記錄每平台 bounded_search / blocked / not_checked / not_found_in_bounded_search；搵唔到唔等於不存在。

## 5. 獨立核查、修正與交付

1. 保存 immutable raw + source manifest；每個文件有 SHA-256、實際 bytes、capture time、來源 URL／tool，canonical key 唔改。HTML entity 解碼等允許轉換要記錄，原文仍保存。
2. 先做 deterministic checks：schema、IDs/joins、missing≠0、counts、metric scopes、date、age parse、quote exactness、caption/links、output openability。
3. 再由另一個獨立 reviewer 讀原始資料做分層語義樣本：納入 high/low confidence、每種 metric scope、fractional age、每種材料加工及其 negation/options、每種 recipient/sender/deceased grief 角色、selected-item versus shop review。冇獨立 reviewer 就明示 semantic QA blocked／未獨立驗證，唔好用同一 regex 自證。
4. 任一樣本有分類錯誤，擴至受影響類別全部記錄，修正並重新檢查 qualification／排名／建議／所有輸出；唔係只改抽中嗰一行。記 correction_id、entity/key、field、before/after、exact evidence、reason、reviewer、time、affected outputs。
5. 執行 `python3 scripts/research_checks.py validate research_bundle.json` 及 `python3 -m unittest discover -s tests -v`。PASS 只表示程式覆蓋嘅檢查，唔等於競品事實已全部核實。語義審核要有獨立紀錄同類別數量。
6. 按要求輸出 XLSX、HTML、CSV、JSON。CSV 保留 canonical IDs、raw qualifiers、來源欄及空白；JSON 用 null 表未知。XLSX 用 hyperlink 而唔用由不可信文字組成嘅公式；CSV 對 = + - @ 開頭嘅文字做安全輸出，raw 保持不變。HTML escape 全部外部文字，只 link 已驗證 http(s) URL。唔將私人本機路徑／metadata 放入用戶頁面。
7. 保存目的地係設定，唔硬編碼舊 Windows 或雲端路徑。Native export 原檔同 assistant-derived table 分開。檢查實際 bytes、zip test、row counts、IDs 及重新開啟；另做 workbook rendering／HTML 視覺 QA。只跑 OOXML check 就要如實寫未喺 Excel 打開。
8. 更新已存在 Library 文件要保留同一 library_file_id、先讀 current version，做 guarded replace。遇 conflict 先重新讀及 reconcile，唔去掉 guard／唔建立重複副本掩蓋失敗。使用當前 Library skill 上傳／writeback 方法；每個 item 都要確定 succeeded。Local fallback 只有真實文件經驗證先報 saved；Library 未成功唔講「已交付」。
9. 將修正帶入全部派生版本；回覆實際完成範圍、合格數／候選數、未知資料、下一個可行決定。現有檔案若缺 raw sources，保留來源指標並說明無法做獨立源級核查，唔好重建虛構 raw。

### 用戶可直接講
「用競品研究 skill，針對美國 Christian family/friends gifts，比較實體個人化 journal。先核實自己店 live inventory，再搵至少 20 間有來源支持嘅 comparable shops。材料係次要，唔好推斷競品供應商。保留原始資料、逐欄核查、合格名單同 CSV 可續接資料；暫時只做研究。」

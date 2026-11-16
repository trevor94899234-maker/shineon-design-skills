# Growth → 私人 APOD：掛飾完整工序

共用跨環境執行、減少重問、APOD 操作與完成核對，使用 [etsy-apod-product-workflow](../../etsy-apod-product-workflow/SKILL.md)；只維持一個 coordinator／current record。以下保留 ornament/full-build 的具體要求。已由新入口調用本配方時，只補 category-specific 要求，不再次啟動 Growth 或另一份計劃。

用於已要求的完整 ornament build／跨階段續做。單張 pilot、純 prompts 或 thumbnail-only 不自動繼承整套範圍。這份 runbook 串接既有方法，不取代它們的 source、permission、QA 或 owner gates。

## 0. 恢復 scope，先安排 media 與目的地

讀當前 brief、最近 owner 決定、[task record](task-record.md) 或等價既有 ledger。記 exact product／variant／artwork revision、當前 approved copy、角色計劃、source files/hashes、已保存 APOD 狀態和重試記錄。先讀 current-state，再用歷史 receipt 解釋來源；不要被舊 pending 段落重開已取消的工作。

明記交付邊界：full private APOD、images-only、files/manual handoff 或 audit。完整 MyGiftStyle build 沿用 [Coach APOD-ready contract](../../etsy-coach-integrated/references/apod-ready-listing-build.md) 的 20 圖、實際影片 capability/count 和保存要求。開始就記 `video_required`、方法、數量及目的地，不等做完圖才發現漏片。若未查 capability，標 `TBC`，不是 optional；只做 read-only capability 準備，未過 thumbnail gate 不做片。

Owner 後來縮窄成 local-only video／不改運費時，將受影響步驟列 `EXCLUDED_BY_OWNER` 並附原句；保留未知事實，不用登入或設定來「補完」被取消工作。接受檔案、批准上載、批准發布分開記；沿用仍有效的本輪授權。

## 1. Growth 決定：買家、送禮任務、offer

讀 [brand-marketing-growth](../../brand-marketing-growth/SKILL.md) 相關部分，沿用當前策略，不重讀整個案例庫。只有已選掛飾 carrier／SKU 才進本流程；尚未選產品的 open-market discovery 留在 Growth，不提前選 final keywords／寫 listing。

輸出短 direction brief：

- 精確產品、買家、送禮人、收禮人／使用者、場合、用途、個人化和情感假設。
- 與已知事實相容的差異；案例啟發、keyword signal 和本店結果分開。
- Bundle 固定檢查結論：值得驗證／先補資料／暫不適合＋理由。缺第二 SKU、同購理由、成本或履約，就不製作可售套裝或假定合箱省運。
- 價格草案及運費方向：分開 item price、supplier shipping、buyer shipping、fees、buyer total 和部分／完整 contribution。採用 Growth 的價格方法；保留幣別、來源日、首件／加件及市場。
- 最小 learning 草案：指標、分母、基線、期間與混雜因素。未 live 時 start_at 保持未定；不是已啟動實驗、排程或監控。

「差價套入賣價」先明列計算基準及目標總額，從同輪指示判斷是維持買家總額、吸收供應商運費差額，還是改價格水平。若關鍵基準真的不明，完成情境比較後只問該決定；不要默默用舊價再加一次運費。profile 名稱不證明地區費率；buyer shipping 未套用時不能寫成實際 checkout。APOD 顯示的 item-minus-cost 不叫淨利。

## 2. 同款來源與 actual mockup gate

由 [Integrated Etsy Coach](../../etsy-coach-integrated/SKILL.md) 接手商品及 listing 階段，按 APOD-ready contract 執行；Growth 傳已有 brief，不觸發往返循環。

核對 product／variant／supplier catalog／artwork／個人化欄位，保存現有文字、gallery selection/order、影片、價格／profile、AutoFulfill、LivePreview 與警告的 before snapshot。保留原檔，任何既有新變更先 reconcile。

從正常可用來源取得同款 actual APOD mockup，匯出、打開實檔、記 hash，確認與指定 artwork／variant 相符。已有同版本已驗 mockup 直接重用；Ready badge、模板預覽、供應商規格文字或另一款圖片不替代實檔。來源衝突按 claim 分項 HOLD；不以新日期自動選一邊。

在 full build 中，mockup gate 過之前只做盤點／準備，不做實質 keyword selection、copy 或出圖。印刷安全姓名長度、實際尺寸／厚度、背面、包裝、雙面與 material 按同 SKU 證據；欄位 maxlength 不是可印長度。未證 production readiness 不阻止已明確授權的 preview 範圍，但不得稱 print-ready。

## 3. Research → 可追溯文案

遵循 Growth 的 [研究來源次序規則](../../brand-marketing-growth/references/keyword-research-source-policy-2026-10-24.md) 和 Coach 的 [keyword workflow](../../etsy-coach-integrated/references/keyword-coach-workflow.md)。每個新研究 round 先恢復是否已回答 Vault-first／Online-first；同輪答案不用再問。只有新 round 沒答案才按既有 owner 要求確認一次；歷史 628811 的答案和配額不變成新 round 授權。

不論來源次序，查重已讀 raw records，沿用有來源的 exact phrase；只補能改變選詞／定位的真缺口。Provider 配額分開記錄，bulk request 數與詞數分開，失敗重試不假定免費；不購買額度。

保存 exact query、provider/feature、market、觀察日期、資料月份／window、raw response pointer 和 qualifier。`Unknown`、`<20`、missing、null、0 不合併；相關詞不能借 volume。Keyword evidence 不是 competitor 成交／需求勝出證據；沒有資料不叫 Golden。需要競品研究才調用既有專項方法，不為填數量擴樣本。

形成同一版 listing packet：

- Title：產品清楚、可讀，保留已正確且有理由的文案；不為顯示工作而全改。
- Full description：產品／個人化／收到甚麼／用途／care／重要限制；supplier production average、shop processing、transit、arrival 分開。寫得準確比加齊未知段落重要。
- 13 個相關、不同且符合當前欄位限制的 tags；每個 actual tag 連 exact evidence 或明示 bounded test 理由。
- 個人化指示、類別／attributes 等按可見欄位和證據填；未暴露的 Etsy 欄位保留 handoff gap，不能假裝 APOD 已填。
- 文字、價格／運費變更、image 角色／exact copy 對照表；研究判斷與格式 QA 分開，保留 Coach 要求的獨立 outcome check，重用本輪仍有效結果。

## 4. Ornament 圖片：計劃 → pilot → 全套 QA

讀 [Studio](../../etsy-listing-image-studio/SKILL.md) 及 [ornament profile](../../etsy-listing-image-studio/references/ornament-thumbnail-profile.md)。Production handoff 包含同款檔案／hash、exact printed text、logo、approved listing／positioning、每張角色與 exact added copy、active rows、attempt history、尺寸／route 和 owner 決定。

新方向先短計劃及 owner direction confirmation；有匹配批准就沿用。先一張實檔 pilot＋QA，再做已授權 rows；不逐圖重新問已批准方向。每次仍依 Studio 驗 exact file，失敗保留，不計入完成數。原生尺寸、one-pass／whole-image、retry ceiling、logo 與 source fidelity 沿用 Studio，profile 只補掛飾專項。

每張 answer one buyer question；N 跟 brief，full MyGiftStyle build 的 N=20。Contact sheet 和 ZIP 支援 review，不能代替逐檔 QA 或擅自放寬未通過的 real-photo／delivery proof。Owner 接受指定私人 mockup 的範圍，與 Etsy publication readiness 分開。

## 5. 私人 APOD 文案保存

平台操作前核對當前 URL／產品 identity、latest authority、before snapshot 和待寫的 exact packet。優先現有適用 connector；不足才用已授權 documented Browser Use。讀當前工具文件、確認實際頁面，不硬編舊 tab ID／CSS 路徑，不讀私有 API／憑證。明確 safety stop 不換 controller 繞過；普通 timeout 則按工具規則判斷是否已執行。

只寫批准欄位，Save 後 reload／離開重開，讀回**完整** title、description、tags、personalization 及任何本輪改動的價格／profile。將 approved text 與實際 readback 正規化換行後比較，保留必要段落／tag order／missing 差異。Toast 或填好未儲存表單不算完成。未改欄位不隨手重設；AutoFulfill、LivePreview 保持既定安全值，異常依原授權處理而非擅改。

## 6. Thumbnail 上載、選取、排序、保存、重開

依 [APOD media handoff](../../etsy-coach-integrated/references/apod-media-handoff.md)，先固定 role → exact final file/hash → intended position。新 upload 路徑先做一個已授權 asset 的 upload/save/readback pilot；同一路徑已有本輪成功證據就重用，不額外造一張。

1. 讀實際 gallery inventory／已選 asset IDs／order。先等正常 hydration／圖片載入，初到頁面的 0 selected 不是已清空證據。主頁只有 primary 也不是只存一張。
2. 用當前支援的 file chooser 上載缺少的確切檔案。檔案 input 若只支援 image，不拿來上傳 MP4。未出現 chooser／工具拒絕就停該步，不連按或繞權限。
3. 每張上載後記 actual asset ID 和 role；到期望選取數後核對每個 ID／順序，hero 在首位。Selection cap 依當前 UI／destination 觀察，不假定永久20；不足就回報能力限制，不私自刪減 brief。
4. 舊 supplier/source assets 保留。只有在批准的 selection 範圍內可 recoverably deselect，記原 order；不刪原圖、不影響其他 variant。
5. Save Selection，重開同 SKU selector，核對 count、選取、順序、hero 與實際載入圖片。Timeout 先讀狀態，避免二次 upload/save。若勾選導致 layout 移動，逐項讀回 selection，不依舊座標盲按。
6. 正常工具可取得 remote bytes 時，下載對應 asset 並 hash 比對。若平台轉檔，記 local/remote hashes 和可見映射，不能說 byte-equal；拿不到 remote bytes就明示 hash unavailable，用 asset/order/full-image 證據。不得為湊 hash 開隱藏 endpoint。

不要重傳已驗證相同版本。Snapshot 要在圖片已載入後保存，提供一張清晰證據及可點的產品／gallery 連結，不只說「已上載」。

## 7. 影片：必做與去向分開

完整 build 沿用 [video routing](../../etsy-coach-integrated/references/listing-video-workflow.md) 及 APOD-ready native video contract。兩條／至少一條依當前 APOD 支援證據和既有 owner fallback，不臆測支援或費用。Thumbnail set 未通過所需 exact-file acceptance/delivery gate 前，不能開始影片 scripting、storyboard、生成、剪接或 render。

Owner 指定 alternative/local MP4 時，才按當前已安裝可用影片 Skill 執行該 scope。只用同款已接受 assets；清楚說 photo-motion、native render 或生成情節的實際方法。相片縮放／crossfade 不是實物動作證據。驗 actual MP4 的 duration、dimensions、fps、codec、audio、檔案 hash、decode 和首／中／轉場／尾影格；視覺 QA 與 owner creative acceptance 分開，未完整觀看不說已完整播放驗收。

`只保留本地影片`：交實檔、可播放預覽及必要 source package，APOD video upload 列 owner-excluded；不能把此選擇當成品質接受。若要求上載現有 MP4，先核實 genuine import control；Generate Video 不是 import。未授權新費用就停依賴步驟，保留已完成圖文。

## 8. Whole-record readback 與 handoff

比較同 SKU 的完整文字／tags、個人化、批准改價、profile scope、gallery IDs/order/hero、影片實際去向及安全設定。讀回有差異先處理；不得靠一張局部 screenshot 宣稱全部完成。

分開交代：已製作／已 QA／owner 已接受／APOD uploaded／saved／reopened；owner-excluded、blocked／TBC；Etsy published 狀態。只有本次有效 scope 的必要步驟都有證據，才叫該 scope complete。真實完成品照片、印刷適配、生產伙伴／政策、履約／Etsy欄位等 publication gaps 不因私人 APOD 完成而關閉。

交付 exact files／contact sheet／ZIP、APOD 產品和 gallery 連結、可見 proof、current task record。Etsy push 留 owner 操作；若另有明確發布任務才核當時平台規則及該次批准。學習草案保持未啟動，直到實際 live 與測量範圍明確；不自動安排提醒或花廣告費。

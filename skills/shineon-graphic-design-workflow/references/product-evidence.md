# 產品與證據檢查

只在 APOD、產品圖像、縮圖或 print 相關階段載入；按該階段實際範圍檢查，不把未要求的階段變成額外執行授權。

## Brief、實物與來源鎖定

鎖定 SKU／variant、buyer／recipient／occasion、想傳達的故事、固定與可變文字、可核實產品幾何／材料及適用模板的來源、日期與 revision。對照同批相關作品，說明構圖及故事有何實質差異。準確引用受來源及權利限制的經文或其他原文；缺來源、版本衝突、教義或重要產品事實未知時，只停依賴主張，不自行補全。生活情境、示意圖及模擬回應如屬 AI／假設，照實標示。

原創背景須按當前適用的生成 route、真實模板及印區準備；姓名留在獨立欄位，不以內嵌示例冒充變數。可見 safe area、bleed、實體尺寸及 variant 規格分別證實；資料缺失保留 TBC。不得從另一款或歷史 template 移植未知值。

## 可變欄位與保存讀回

在獲明確覆蓋的私人 APOD 操作範圍內：

1. 對每個計劃的變數記錄字段 label、固定／可變內容、位置、實際字體、required／optional 及其可支持的限制與證據；不假設 auto-fit、字元上限、符號驗證或 optional 空值行為。不能建立／確認 customer field 時，標未實作或未驗，保留 seller-editable 與 customer-editable 的差異。
2. 在正確 product／variant／artwork revision 的正常欄位中，至少使用兩組不同長度的 synthetic 名稱值，讓可變長度的姓名欄得到短／長覆蓋；其他欄位亦在兩組中各自觀察，固定格式欄位（如只接受四位數的年份）使用已核可的不同有效值，不強造不合法長度。對每組各自記錄：輸入值和欄位 → 正常預覽中對應變化 → 保存 → 重開 → 同欄與預覽讀回；附時間、產品身分、版本、結果和證據。逐組核對固定文案正確、短／長姓名可讀及無裁切或重疊，保存重開後亦核對；不可讀或證據不足時分別記未通過／未驗。多欄時記各欄的觀察，不用只改其中一欄冒充所有欄已測。可按當前已核限制選擇示例；已測兩組不代表任意長名或所有字元通過。
3. 以正常 UI 顯示的 field 配置及可用的 customer-facing 證據區分 customer-editable 與 seller-only；證據不足標 TBC，不能由 PSD 層或示例文字推定。Etsy 端客戶輸入／欄位 mapping 需要其獨立、獲授權的觀察；APOD 預覽、私存和只寫 listing 不能證明它。

如果只能做 source／art／預覽，列明哪一步未執行；不為補齊驗證而擅自保存或上載。失敗、衝突或安全 stop 要保留原紀錄，不把重試當作第一次。

## 同款、同版 mockup 與縮圖

先確認該 SKU 與 artwork／personalization revision 綁定的實際 personalized mockup。完整 listing build 沿用既有 APOD coordinator 的實際 mockup-first 合約；單一圖像階段不因此啟動其他階段。每張縮圖與該同款同 revision mockup、產品外形、實際裝飾及已授權文案比對；確認名字位置／主次、可讀性、必要角度、裁切及差異角色。示例姓名須能讓人明白是示例，不假裝每位買家收到固定名字。

記錄原生輸出、實際尺寸、版本、hash、來源、檢查者、缺陷及驗證證據。舊版／generic mockup 即使外觀相似也不能充作新 revision 已完成；如無正確同版證據，保留現有圖、該項標 HOLD／未驗，不自動生成或上載。logo、特殊合成及圖片次數只接受當前具體授權，保留來源與衍生版本，不把舊批次例外通用化。

## Print 與完成邊界

將以下證據各自記錄，不互相推論：

- 螢幕可視 QA：實檔／預覽的文字、構圖、對比、裁切與產品一致性。
- 私人 APOD：正確產品的實際欄位、兩組 synthetic 測試與保存重開。
- Etsy：獲授權後的實際 buyer-field mapping／發布狀態。
- 印刷：針對本 SKU／variant 的官方 template、物理印區／bleed／safe area、輸出及供應商適用要求；如有不同來源或日期，記來源與分歧。
- 實物及 production release：實際打樣／供應商驗證與具體批准，各自記證據；不可由數碼預覽代替。

依已知資料分別記像素尺寸、檔案 density metadata、已驗 physical mapping 及計算假設。沒有可信物理尺寸／mapping 時，實際 PPI 為 TBC；單改 metadata、放大像素、缺 metadata 或 viewer fallback 都不能證明可印或不可印。透明度、白墨、透光與固定 raster 細節的實際結果，沒有供應商或實物證據時保持 TBC。對未驗印刷只給有界的 screen／private 狀態，不寫 production PASS；不可推論所有產品都失敗。

遇到官方模板已足以支持有界數位 preflight、卻因未取得工廠內部資料而新增阻塞的爭議，可讀 [2026-11 觀察案例](observed-cases-2026-11.md)；只採用方法，不移植案例的 SKU 數值或放行結論。

版本歷史、原檔、必要 hash／readback 及有關的失敗保留，避免重置或覆蓋 WIP。適用條件真正通過後才標該階段完成；有未滿足的必要條件就保留 blocked／HOLD 或 TBC，並指出誰可處理下一步。

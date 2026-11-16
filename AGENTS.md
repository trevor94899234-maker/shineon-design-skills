# ShineOn Graphic Design — Project 規則

Owner 決定日期：2026-11-06。適用本 project 所有產品設計；繼承當次 Global／owner 的權限底線。本檔不授權 Etsy 發布、同步、訂單、付款、店舖／安全設定或生產放行；設計稿、私人保存及 QA 均不等於上述批准。

## 新 task 的預設 Skill 入口與分工

Owner 決定日期：2026-11-16。適用本 project 新 task 及續辦；使用者毋須每次指定 Skill 名稱。

- 先讀本檔及當次 owner 要求，再載入當前已安裝的 `shineon-graphic-design-workflow`，用它確認本次範圍、產品／revision、現有紀錄及階段分工。本機位置：`C:/Users/ctcc0/.codex/skills/shineon-graphic-design-workflow/SKILL.md`；其他環境按實際可用 Skill 名稱定位，不假設 GitHub 副本已自動安裝或同步。
- ShineOn 主流程是本專案的預設協調入口；按實際任務選下表的階段 primary production Skill，只讀需要的 references，不一次載入全部 Skills。每階段保留一名 artifact owner、一個 primary production Skill 及同一份 task record；不因載入 Skill 而另開 agent、重啟 intake 或重做有效成果。

| 本次工作 | 選用的 Skill 與責任 |
|---|---|
| 買家／送禮定位、原創個人化概念、designer brief／成品覆核、研究判斷、SEO／listing 文案 | `etsy-coach-integrated`：負責本階段的商業／設計判斷與建議；未選產品的新系列探索按其路由接 `brand-marketing-growth`。 |
| 品牌故事、系列方向、bundle、內容及自然增長策略 | `brand-marketing-growth`：在本次範圍內交策略與定位成果。 |
| 競品、店舖盤點與 keyword 原始證據；既有 keyword CSV 清理 | 分別用 `etsy-competitor-listing-optimization`、`etsy-keyword-pool-cleaning`；研究證據交回 Coach 作建議，不另建第二套推薦流程。 |
| 同款縮圖／mockup 製作與視覺 QA | `etsy-listing-image-studio`；需要 prompt 規劃時用 `etsy-pod-image-prompts` 支援，單做 prompt 亦保留該較窄範圍。 |
| 已選實體產品的完整私人 APOD listing 製作或跨階段續辦 | `etsy-apod-product-workflow` 作該款唯一跨階段 coordinator；ShineOn 主線只管跨產品資源及總狀態，接收結果，不重複指揮工序。 |
| 掛飾／杯款的完整 APOD 流程 | 按款式讀 `etsy-ornament-apod-workflow`／`etsy-mug-apod-workflow` 的專用要求，再接同一個 APOD coordinator，不另外啟動平行流程。 |
| 明確在範圍內的 Canva 可編輯美術 | `canva-personalizable-product-art`；原本採網頁 art-only＋APOD native text 的工作，不因路由而新增必經 Canva 步驟。 |
| 買家角度的模擬審視 | 有適用要求或實際需要時用 `superpersona`；深度、次數、委派及成本按當次規則，不能當真買家研究。 |

- 若 owner 明確指定 Skill，保留指定方法及本次 endpoint，與上述專案協調分工銜接，不要求 owner 再選一次。單純解釋、只讀查詢、局部修改或概念工作，先用主流程確認範圍即可；不自動變成完整 listing、20 張圖、影片、APOD 寫入或完整 LoopForge。
- 選用前確認 Skill 存在並讀取其目前版本。缺少時列明能力缺口，只暫停依賴它的部分；本入口不擴大原有授權、費用、human gate 或發布權限。

## 每款必須個人化及差異化

- 每款最終成果必須同時有**真正 personalization**及**實質設計差異**；fixed 款不能當最終完成。固定背景／illustration 可以保留，但須為本款適合的可變姓名等內容安排清楚主次及留位。
- 先說清買家、受贈者、occasion、情感、原創構圖，以及姓名如何融入故事。差異不只改色、換名或貼通用經文；保留批次比較，分清 source/reference 與本次原創決定，不照抄來源，不虛稱需求、銷售或印刷工藝。

## 真正可編輯的 personalization

- 按實際 SKU 支持及送禮關係選 recipient／child／household／sender name 等欄位；在 APOD 正常 editable text layer／customer field 實作。不能把示例名字或 placeholder 烤死在 PNG 冒稱可編輯，也不能只在 listing 寫 personalized。
- 記錄字段 label、實際字體、位置、已核可用限制及示例；未知為 `TBC`，不自行宣稱字元上限、字元驗證、auto-fit 或任意長名字適用。
- 至少用兩組不同長度的 **synthetic 輸入**驗證：改值 → 預覽變化 → 保存 → 重開讀回，並分清 customer-editable 與僅 seller-editable 的證據。
- APOD 配置與 Etsy 端客戶輸入 mapping 分開驗證；未推送不得宣稱 Etsy mapping 完成。

## 圖像、模板及版本

- 本批原創圖像用 **ChatGPT 網頁版圖片生成，任何版本可**；背景／圖像與 APOD editable text layer 分開準備，名字不得烤死在圖中。
- 按當款真實 ShineOn template／印區製作；thumbnails 必須使用同款、同 revision 的 personalized mockup。generic v1／舊 mockup 不能作新版已完成證據。
- 保存 v1／歷史來源、hash、狀態及必要備份；不 reset、刪除或覆寫他款 WIP。

## 逐款完成檢查

- 檢查 personalization 確實可改、差異化清楚、固定文案及長短名字可讀、無裁切，source／revision／實際保存重開證據一致。
- 關鍵能力或來源有缺口，只停依賴步驟並列出影響；未知不猜 `PASS`。私人預覽通過不等於 owner 接受或正式生產／發布批准。
- 今次批次用 Superpersona 輔助買家角度檢視：主線記錄第一輪 v1 歷史評估已完成 3 passes，第二輪針對 v2 個人化／縮圖。它不代替真買家研究、技術 QA 或 owner 決定；不將本批次數變成所有未來工作必須 3×2 或完整 LoopForge 的規則。
## 視窗／分頁清理及 browser lease 交還

- 每階段完成或交還 browser lease 前，先保存及核對必要成果，再關閉本任務自己建立、已用完且沒有未保存內容的視窗／分頁；保留仍必要的未保存工作、登入 handoff 等，不為清理而丟失成果。
- 只關閉已用當前工具核對歸屬於自己的項目；不得關閉 user 原有或其他 agent 仍在使用的視窗／分頁，不沿用舊 tab ID 推定歸屬或狀態。
- 暫時仍需保留的項目，記錄保留原因、owner 及下一步；未實際關閉不能當作已清理。
- 結束時以當前工具可見結果確認 cleanup 並記錄；不能只口頭聲稱已關，或以歷史 tab ID／舊紀錄代替當次確認。

---
name: etsy-ornament-apod-workflow
description: 為 Etsy ornament／聖誕掛飾／個人化吊飾整理 Growth 定位、keyword research、listing 文案、thumbnail 製作與私人 Anywhere POD（APOD）上載保存驗證。適用於「ornament thumbnail skills」、「由 growth 做到 APOD」、完整掛飾 listing、續做或流程補漏；亦可只做已批准縮圖。重用既有 Image Studio，不取代原創產品設計或授權 Etsy 發佈。
---

# Ornament：Growth → Thumbnail → 私人 APOD

完整 build／跨階段續做的共用執行，交 [etsy-apod-product-workflow](../etsy-apod-product-workflow/SKILL.md) 作唯一 coordinator；本入口保留 ornament 的來源、幾何、角色及既有 full-build 規則。沿用同一 task record，回傳本階段結果，不相互重啟入口。純 thumbnail 仍直接用 Studio，不擴大成平台工作。

把同一款掛飾由買家／送禮故事接到可核對的私人 APOD 成果。這是產品類別的流程入口；實際 thumbnail 生產仍由 `etsy-listing-image-studio` 執行。當前 agent 維持一份 task record，每個階段只用一個 primary production Skill，不因引用而另開 agent 或第二套計劃。

## 選擇最窄的已授權模式

|使用者要做甚麼|執行範圍|
|完整 ornament listing、由 Growth 做到／post 去 APOD|讀 [完整工序](references/growth-to-apod.md)，接上既有 Coach 的 APOD-ready contract；終點是指定私人 draft 的保存及重開驗證。|
|Ornament thumbnail、掛飾出圖、pilot、改指定幾張|讀既有 [Studio](../etsy-listing-image-studio/SKILL.md) 及其 [ornament 配方](../etsy-listing-image-studio/references/ornament-thumbnail-profile.md)。沿用已批准 source／copy／active rows；不自動啟動 SEO、影片或 APOD 寫入。|
|Keep going、檢查漏咗、全部傳咗未、繼續指定 SKU|先恢復 [任務紀錄](references/task-record.md) 或等價既有 ledger，只補最早未完成且仍獲授權的步驟。已保存的圖先核對，不重新生成或重傳。|
|只要 prompts／流程建議|交付相應本地文字；不發動生成或平台操作。|

不要求 owner 選 Skill。從當前要求推斷模式；無法確定會影響平台寫入的產品／目的地時，只暫停該步，繼續可獨立準備的工作。

## 接力原則

1. **先恢復決定。** 精確 APOD product／variant／design revision、source hashes、目前 copy／image 版本、生成入口、active rows、重試歷史、價格／運費與影片目的地，都從同輪紀錄恢復。有答案不重問。
2. **分清策略和製作。** Growth 負責定位、Bundle 判斷和 learning 草案；Integrated Etsy Coach 負責商品／研究／文案／APOD contract；Studio 負責圖片；影片按 Coach 的當前 video routing。交接現有 evidence，不重新開始另一套流程。
3. **沿用 mockup-first。** 完整實物 build 必須先取得同款實際 APOD mockup、匯出並檢查，才開始實質 keyword／copy／thumbnail。獨立 fidelity pilot 依 Studio 的最小 brief，不把 full-build 全部條件強加到單張圖。
4. **數量跟 scope。** MyGiftStyle 完整 APOD build 沿用既有 20 圖及影片要求；thumbnail-only 的 N 跟 owner brief。20 是本店 full-build 約定，不是 Etsy 通用最低要求。沒有批准的減量不能叫完成。
5. **owner 例外逐項記錄。** `只保留本地影片`、`不用改運費`、指定檔案接受或 logo-only 後製，控制本次指定範圍。它們不變成其他款的授權，也不把未驗證項目改成 PASS。
6. **保存與發佈分開。** 私人 APOD upload/save/reopen 不是 Etsy push/publish。先確認本輪對指定 draft 的寫入授權；完整 build 指令的解讀依 Coach contract，重用有效授權，不逐張再問。未授權的 Etsy 發佈、設定、付款或登入仍不執行。

## 如何開始

明確啟動可用：

> 用 $etsy-ornament-apod-workflow，為這款 ornament 由 Growth 定位做到私人 APOD 保存驗證；先恢復現有資料及批准，重用已完成步驟。

只做圖可用：

> 用 $etsy-ornament-apod-workflow，只做這款 ornament 已批准的 thumbnail，沿用 Image Studio；不要擴大成完整 listing 工作。

開始實際工作時，用一句話報告模式、SKU、當前階段和實際生產 Skill。自然語言描述有助發現；精確 `$etsy-ornament-apod-workflow` 是較可靠入口，不能保證每句描述必定自動啟動。

## 按需讀取

- [完整工序](references/growth-to-apod.md)：full build 或跨階段補漏。
- [任務紀錄與完成證據](references/task-record.md)：新 run 的簡短記錄模板，或續做時核對等價既有 ledger；不要另開平行台帳。
- [Ornament thumbnail 配方](../etsy-listing-image-studio/references/ornament-thumbnail-profile.md)：只有出圖／image plan／QA 時讀；20 個角色是可按 SKU 設定的素材，不是已批准文案。
- [628811 實例與適用界線](references/case-628811.md)：需要理解本流程來源、排錯或避免照抄歷史例外時讀。它不是新 SKU 的規格或現況證明。

若必要的本機 Skill／reference 不存在，指出缺的是甚麼，繼續不依賴它的準備；不假裝已調用、不靜默換 generator。已安裝路徑以當前 catalog 為準，不沿用舊 browser/tab IDs。

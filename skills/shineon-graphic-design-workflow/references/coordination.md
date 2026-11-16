# 主線統籌與交接

多款、跨階段、涉及共用 browser 或需要從中斷處續辦時使用。簡單、單人及單階段工作可把相關資料縮成一段紀錄；不要為填表新增工作。

## 建立可執行的 task 邊界

1. 主線從最新 owner 授權、適用規則和 authoritative current record 建立一份總覽；不同來源衝突要指出時間及權威層級，不能單按檔名或舊摘要決定。不同批次及每款 product ID 各自維持狀態。
2. 每款指定一名具名 product owner，在其範圍內協調階段；每份產物同一時間只有一名 artifact owner。主線可兼任，但唯有真正接手且無衝突才可改值。技術 reviewer 只核查，除非被指派且已交接，否則不改產物。每款分開交付路徑／版本及最小 handoff。
3. 當前可委派且確有幫助時，按已獲授權數量／模型／reasoning／成本啟動有界工作；否則主線順序執行，不創造虛構 worker。派工前交付身份、scope、可寫位置、排除項、版本、依賴及需回傳的證據，並記錄活動／完成／失敗。不得接管其他產品或覆寫其他任務 WIP。
4. 建立依賴圖或簡短順序：互不相依的本地準備可在授權內並行；相同產品／artifact 的可變狀態、同一 browser session／tab 或前後有依賴的步驟須序列化。主線檢查交接完整及實際成果，再放行下一個已授權依賴；未核實的聲稱保持未驗。

每個產品紀錄至少有以下適用資料，可沿用已有欄位而非複製另一份：

| 欄位 | 應記錄的內容 |
|---|---|
| 身分及 owner | task／product ID、SKU／variant、product owner、各階段 artifact owner、可寫路徑 |
| charter | 本次交付與階段、授權／human gate 的來源及精確界線、排除項、次數和成本上限 |
| 來源與 revision | brief／真實產品及模板來源、source／輸出檔案、版本、hash、已核事實與 TBC |
| 依賴與狀態 | 每階段所需先決條件、當前狀態及該階段最新有效成果／驗證連結；舊證據保留為歷史，HOLD／paused 原因不被其他階段覆蓋 |
| 交付 | 改了甚麼、未改甚麼、已測條件／結果、精確檔案或遠端身分、已知缺口、下一步與其 owner |

可用 NOT_STARTED、IN_PROGRESS、BLOCKED、HOLD／PAUSED、COMPLETE_FOR_SCOPE 等狀態，並以文字界定完成的階段及證據，不把 COMPLETE_FOR_SCOPE 解讀為產品／production 全部通過。全批總覽按產品分列，不能只以百分比或舊整批狀態代替。對客戶欄位、Etsy mapping、print、owner acceptance 等維持獨立狀態。

交接時，接收者先對照 producer 指定的檔案／SHA-256、source revision 及 QA receipt，再打開 receiver 實際要評的檔案；將兩邊身分核對結果留在同一份既有紀錄。兩者不一致時先修正對應、再覆核交付檔，不用另一個 pilot 的特徵宣告 worker QA 錯誤。相似外觀、編號較大或修改時間較新，都不能單獨代替本次交付收據。若確有 QA 錯誤，另加有日期、綁定實檔的更正，保留原記錄。

需要時可把現有交接濃縮為：`product／revision | producer 檔案＋hash | receiver 實看檔案＋hash | source／QA receipt | 核對者與時間 | 一致／不一致／未驗及處理`。這是可選記法，不新增資料庫、schema 或第二份狀態表；遠端成果使用可核實的正常 UI readback 身分，不能虛構 byte hash。沒有證據或接收者未能核實的部分標 TBC／未驗，不因收到訊息當完成。只在有權限時讀回 UI，不因驗證而擅自修改商品或新增外部操作。

診斷錯版交接或混用批次完成數時，可讀 [有日期的觀察案例](observed-cases-2026-11.md)；案例不恢復舊任務或改變當前驗收。

## 共享 browser lease

主線在任何瀏覽器操作前記錄唯一 lease holder、任務／產品、授權目的、工具及工作階段；根據當前工具 inventory 確認目標網址、tab 所屬及 lease 狀態。不能沿用歷史 tab ID 或推定已 release。其他任務即使產品不同也不得同時操作同一共享 session／tab；可繼續獨立本地工作。衝突時排隊，等待持有人完成安全交還，主線只在確認後重新分配；不得強行接手或刷新別人的 tab。

完成階段或交還前，先保存並核對必要成果。只關閉本任務自己建立、已用完、無未保存內容且以當前工具核實歸屬的頁面；保留 user／其他 agent 的頁面及仍需手動交接的工作。用當前工具確認關閉／inventory，逐項記實際關閉、仍保留的原因、owner 和下一步。工具不可用或 ownership 不明時標清理未驗或未完成，不宣稱成功；lease 狀態亦不可猜。

遇安全／政策 stop、ownership guard 或工具明確拒絕時，停止相關 UI 動作，不換 controller、browser、runtime 或改權限繞過；保留已知成果與未確定副作用。按適用的正式恢復依據處理，必要時交 owner；只繼續無依賴的獲授權本地工作。一般連線故障與明確安全 stop 分開記錄，不把任何一個推成整個瀏覽器永久失效。

## 結束與恢復

主線查實每款實際 handoff，記錄總覽更新時間、來源及 unresolved risks，交還任何可安全交還的 lease。歷史 attempt／失敗／成本保留，不重置配額。HOLD 或 paused 的工作不能因相關 task 前進而自動恢復；收到涵蓋該工作的新明確恢復指示後，先讀 checkpoint、確認當前授權與 UI／檔案狀態，再從第一個未滿足依賴續做。

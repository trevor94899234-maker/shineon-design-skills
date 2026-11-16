# ShineOn：有日期的觀察案例

整理日期：2026-11-16；事件日期見各節。只在相似交接、階段計數或 preflight 爭議時讀取。以下是歷史證據與可重用方法，不是目前 APOD／Etsy 狀態、批次授權或新驗收門檻。

來源標籤均相對於 **ShineOn Graphic Design project root**，不是此 Skill／Git repository 的相對連結；來源檔、產品圖及聊天全文不隨 Skill 複製。

## 1. Pilot-04／pilot-05：先核收件，再更正 QA

2026-11-08 的 662779 worker 最後交付 pilot-05，主管卻檢視 pilot-04，並據此質疑 logo／樹形描述。2026-11-16 專案覆核重新開檔及計算 hash，確認是不同輸出：

| 交接檔案 | SHA-256 | 覆核可見差異 |
|---|---|---|
| `pilot-04-background-edit.png` | `5341135580336EEDE393B8BB71AA71ABCDC7B865219554EB55F5C0D34B852AC4` | 無外部 logo；右側雪樹被圓邊裁切 |
| `pilot-05-native.png` | `DF013541F9DA8588A006E57697D4F4FED622EA85B259D373E8B8A6A128344102` | 有外部標誌與 headline；完整樹冠／樹幹可見 |

這支持「覆核檔與交付檔不一致」，不支持任何一檔合格。原 QA 的 REVISE／logo HOLD 保留；標誌看得見也不證明含原裝 logo pixels。接收者應先把 producer receipt 與實看檔案對上，再判斷 QA 有沒有錯。

pilot-04 的記錄明言只在「描述修改內容」輸入背景編輯要求，沒有實際畫選區／遮罩。故其結果不能用來證明已測真正選區；即使使用選區，亦須檢查輸出，不能承諾區外像素不變。

來源標籤：

- `output/thumbnail-20-20261108-new-supervisor/662779/PILOT-04-BACKGROUND-EDIT.md`
- `output/thumbnail-20-20261108-new-supervisor/662779/PILOT-05-RESULT.md`
- `output/2026-11-16-project-skill-review/PROPOSAL.md` §4.1；主管 chat `01a1b998-2e6a-7ac2-8a19-2d7db11946c6`／turn `01a1ba20-17d7-7b62-8a8a-6b11524f0b1a`，worker turn `01a1ba20-4868-7ce0-9fd6-143fd00597e3`。

## 2. 私人保存、來源結構與新縮圖各有完成範圍

2026-11-07 原四款私人更新收據記錄 13 張既有同版選圖及 5 個姓名欄的保存讀回；沒有新生成這 13 張。2026-11-08 另開的每款 20 張縮圖工作，至 2026-11-16 所查歷史仍各為 0/20 確認合格，沒有該批新圖上載。兩批不能互相抵銷，也不能因一批前進而恢復 paused 工作。私人 APOD 保存與 Etsy 實際欄位／政策配對仍分開。

另六款的 2026-11-06 來源報告取得 6 份 PSD、96 個 layer records、36 個文字 descriptor；包含固定與替代文字，並非 36 個 customer fields。來源結構或 art-content 階段通過，均不替代實際改值、保存重開及同版 mockup。

來源標籤：

- `output/2026-11-05-shineon-batch/production-ready-20261106/resume-goal-20261106/private-review-owner-20261107/FOR-OWNER-REVIEW.md`
- `output/2026-11-16-project-skill-review/PROPOSAL.md` §2
- `output/2026-11-06-designer-coach-review/source-layer-batch/STATUS.md`

## 3. 官方模板可支持有界數位 preflight

2026-11-06 的 Children Prayer 662866 技術澄清，依實際官方 PSD、來源 pixels、放置與輸出分別記錄：1410×2220 畫布、模板文件尺度、背景約 212.98 有效 PPI，以及 export 約 72 DPI metadata；原生姓名另行評估。這些值不互相替代，也不能由模板文件尺度聲稱量得實物印區。

該版記錄支持有界數位可讀／fit 結論，並保留低於 300 最佳建議及實物結果未驗的限制；當時來源沒有要求工廠內部 RIP 或先買 sample 才能完成該數位檢查。可重用的方法是按本 SKU 的真實要求與具體缺陷判斷阻塞，不新增無來源門檻。不可把此案例變成所有 SKU 免驗、任意低 PPI 合格、供應商逐檔認證或 production release；新硬規格、模板修訂或實物缺陷應重開受影響檢查。

來源標籤：`output/2026-11-05-shineon-batch/01-children-prayer/v2-personalized/production-ready-20261106/official-template-recovery/resume-technical-clarification/TECHNICAL-DISPOSITION.md`。

# eRank、EverBee、Marmalead：工具教學增量與判斷邊界

研究完成時間：2026-10-09 01:12 UTC。閱讀公開第一方文字，使用 web.run；沒有登入、付費、連接工具、查詢店主帳戶或修改正式 skill。這是 2026-10-07 既有工具口徑的增量，不是重做整站審核。逐頁 URL、原始日期、閱讀層級和限制見[同目錄來源台帳](official-tool-sources-2026-10-09.json)。

## 最值得加入的五項

1. **EverBee 的更新教學支持「需求＋競爭＋產品適配」，明確反對搜尋量單獨決策。** 2026-09-13 文章說較低量長尾在意圖清楚、切入可行時可能較好；要看實際搜尋結果、個人化、價格、照片、既有競爭者、利潤與製作能力。這補強既有逐詞判斷，不能解讀成所有候選都須先通過一個量值門檻。[EB-D03](https://blog.everbee.io/how-to-use-real-search-volume-data-to-pick-etsy-products)
2. **三工具的「月搜尋」不是同一個量。** eRank 是過去 12 個月的月平均；EverBee Keyword Research 2026-02-25 指過去 30 天；Marmalead 現行首頁指未來 30 天預測。不要合併、平均、投票或同欄排序。[ER-D05](https://hc.erank.com/en/articles/11178612-understand-erank-metrics-in-5-minutes)、[EB-D01](https://help.everbee.io/en/article/4-keyword-research-suite)、[MM-D01](https://marmalead.com/)
3. **Unknown 明確不等於零；<20 也不是零。** eRank 2023 法文官方教學說資料未掌握時會顯示 Unknown，極相關詞仍可能值得用。<20 的公開解釋來自 2020 舊文章；它說當年低於 20 無法準確捕捉，圖表可能不顯數字。保留原值和日期，不能延伸為各工具／各現行畫面的共同計量規則。[ER-D02](https://help.erank.com/fr/blog/guide-de-demarrage-sur-erank/)、[ER-D03](https://help.erank.com/blog/what-if-my-keyword-has-no-etsy-searches/)
4. **Marmalead A 級標準不是選詞門檻。** 2024 教學建議主詞 engagement 至少 300，並將較多長尾納入評級；那是供應商的評級建議，不是 Etsy 規則，更不是本店低量高適配词的否決線。[MM-D03](https://intercom.help/marmalead/en/articles/2347564-how-to-achieve-an-a-grade-in-marmalead)
5. **供應商聲称「tag 帶來流量」仍須核欄位／方法。** EverBee 2026-09-23 MCP 教學作此宣稱，卻沒有在該頁給出逐 tag 歸因分母、方法或實際第一方報表。不能用競品可見 tag、一般關鍵詞量或 AI 回答代替競品實際引流證據。[EB-D05](https://help.everbee.io/en/article/211-everbee-research-mcp-ask-claude-for-etsy-market-research)

## 口徑補丁：保留原始量，不自創共同分數

| 欄位／情境 | 可採用的定義 | 必須保留的限制 |
|---|---|---|
| eRank Avg Searches／Clicks／CTR | 所選平台、國家，過去 12 月月平均／比率；CTR 可超過 100% | 是工具量，不是本店轉換率；不把比率當購買機率。ER-D01／05 |
| eRank 頂部 vs Exact filter | 頂部含 near-match；Exact filter 指輸入詞原序出現在結果內 | 不保證完全逐字匹配；既有規則不變。ER-D04 |
| eRank Search Trends | 15 個月趨勢 | 本次 Keyword Tool 頁同時出現點選「specific day」敘述；不要推定每個點一律日／月。按實際 tooltip 保存日期和粒度；沒有 UI 證據就標未核。ER-D04／05 |
| EverBee Keyword Research Search Volume | 該 2026-02-25 版說明為過去 30 天 | 2025 Product Analytics 的 Tag Analytics Volume 另寫 average monthly，未給平均窗口；不能把前者定義自動搬到後者。EB-D01／04 |
| EverBee Mo. Sales | 既有 2025-04-27 公式仍為估算總銷量÷listing 月齡 | 存續平均與近期趨勢不同；本輪無帳戶 UI 驗證。EB-D04 |
| Marmalead Searches／Engagement | 現行首頁：未來 30 日預期搜尋／unique visits；歷史＋3 個月 forecast | 是預測，不是已發生月數；原值外另存預測生成日、目標窗口和檢視窗口。MM-D01 |
| Marmalead Competition／Top Tags | 舊教學說為競爭 listing 數／該詞結果的常見 tag | 小競爭數不是自動機會；Top Tags 不提供每 tag 實際流量。MM-D02 |

### 缺值與低量的落地規則（本報告的整合建議）

- 保存 raw_value 原文，例如 Unknown、<20、0、空白、未提供；另分別記 missing、threshold、reported_zero，不能統一為 0。
- <20 不填 10、19 或 0；若需要结构化界限，可保存 upper_bound=20、exclusive=true、numeric_value=null，且明說未得確數。
- UI 顯示 0 可以記「供應商報 0」，不可跳成「現實市場完全無需求」。Unknown 表示資訊不足，既不證實也不反證需求。
- 低量／缺量＋強適配可保留為小規模試驗或輔助覆蓋，需寫出支持的買家任務、其他證據、擬用欄位和剩餘疑問；不自動入選，也不自動淘汰。
- 高量＋錯誤材質／製程／內頁／個人化承諾，直接因商品不符而拒絕。量值不能抵銷產品錯誤。
- 搜尋量屬候選市場訊號；實際本店 search terms／orders／相關買家回饋是不同類證據。查閱教學不是完成新的 keyword lookup。

## 供應商內部／彼此的差異如何處理

### 1. 高搜尋量 vs 長尾適配

EverBee 2025 教學的清單稱好詞應為 high/medium volume，但同頁亦建議較不熱門、能描述真實產品的長尾；其 2026-09-13 教學更直接說低量詞可能較好。採用「fit、意圖、競爭、證據一起判斷」，不搬用硬性 minimum。[EB-D02](https://help.everbee.io/en/article/10-boost-your-keyword-research)、[EB-D03](https://blog.everbee.io/how-to-use-real-search-volume-data-to-pick-etsy-products)

eRank FAQ 現行文字亦說沒有普遍適用的最佳數據組合；低／中量長尾可能服務更明確的買家意圖。2020 作者個人例子提出月均 250 和 CTR 20%，但最後仍因成人尺寸而不選「for girls」。這恰好說明數據不能推翻適配，而非給本店沿用兩個門檻。[ER-D01](https://help.erank.com/faq/)、[ER-D03](https://help.erank.com/blog/what-if-my-keyword-has-no-etsy-searches/)

### 2. Marmalead engagement 定義不宜擴張

首頁和舊 Help Center 定義為預期 unique visits／views；2026 行銷文卻以 clicks、favorites、purchases 描述其 engagement 能力。這不足以把數值標成購買數、轉換率或確證購買意圖。保持實際欄名、來源版本及量測單位；未有定義就留待核。[MM-D01](https://marmalead.com/)、[MM-D02](https://intercom.help/marmalead/en/articles/2278968-keyword-comparison-tool-torial)、[MM-D04](https://blog.marmalead.com/best-etsy-keyword-tool/)

同一行銷文提出 95% 預測準確率及客戶成長倍數。它們是供應商自述，沒有在該文公布本次可審核的逐詞誤差、抽樣及因果識別；不能轉成 ±5%、每詞 95% 信心、或本店收益預測。其「不要混合多工具」可保留口徑一致原則，但不能据此禁止跨來源核查。[MM-D04](https://blog.marmalead.com/best-etsy-keyword-tool/)

### 3. 工具分數不等於產品相關度

EverBee Keyword Score 教學把它形容為 searchable／relevant，但公式僅搜尋量÷競爭 listing×1000，並說沒有通用 good score。公式不含產品材質、買家任務或內頁；高分仍須獨立 fit。eRank KD 的既有文字／方向疑義本次仍存在，維持 raw score，不反推、不與 EverBee 或 MarmaMeter 合分。[EB-D06](https://help.everbee.io/en/article/52-keyword-score)、[ER-D05](https://hc.erank.com/en/articles/11178612-understand-erank-metrics-in-5-minutes)

## 套用 MyGiftStyle：只示範判斷，不冒充已查需求

授權背景：US 買家；Christian printed vegan leather journal；200 lined pages；只可改名字。本節是依產品事實的分析，不是供應商對本店作出的建議，也不含新搜尋量。

- personalized Christian journal／Christian journal with name：產品與個人化方式直接相符，可優先研究；尚不能因自然語言合理就稱已驗證高需求。
- Christian prayer journal：可服務自由書寫祈禱，但必須先查結果和買家期待；標清 lined interior，不能承諾祈禱提示、導引題目或預印禱文。
- Bible study journal／devotional journal：先檢查是否主要期待有結構的 study／devotional 內容；不以多加一個否定句補救一個根本誤導的主要標籤。
- Bible verse journal：只在該 SKU 真的有相應經文設計時再研究；Christian 風格本身不等於印有 Bible verse。
- pastor gift／Christian gift：可作收禮任務候選，但要核當前搜尋結果是否能由此日記本合理滿足；廣泛送禮量不能當作此 SKU 的需求量。
- engraved leather journal／genuine leather journal／custom scripture journal：與 printed vegan leather、name-only 不符時拒絕；即使高量高分也不能用。
- 200 pages 保留這一已核事實，不自行加 A5、100 sheets、頁厚、燙金、壓印、雕刻、禮盒等未核規格。

US 是研究目標，不是所有工具數字的默認地理標籤。eRank 可選國家；本次 EverBee／Marmalead 文本未解明所有數據的 US 地理範圍。未知 scope 要留未知，不能借用美元售價或英文介面證明 US 搜尋量。

## 建議正式整合方式

1. 在既有逐詞 accept／reject／hold 記錄加一個很短的「適配＋意圖＋可用證據」理由，不另發明權重總分。
2. 將 Unknown／<20 的來源補入既有 qualifier 規則；清楚註明 2020 門檻說明的年代限制。
3. 新增三工具時間窗對照和 Marmalead 預測／評級界線；每個工具／tab 留獨立原值。
4. 把 Sep 2026 EverBee 多因素教學作為判斷佐證；不新增必買工具、查詢配額或帳戶連接。
5. 新增回歸測試：低量真 fit 不被自動淘汰；高量假材質必拒；Marmalead forecast 不作歷史 actual；Tag Analyzer 不自動變成引流報表。

## 已知未核

未做本店／竞品新查詢、未取得任何新量化需求結果；未看影音、圖片或登入 UI。沒找到可用來統一 EverBee／Marmalead <20／Unknown 的現行第一方定義。既有 EB-O01 取消頁沒有主動重開；搜尋偶然回傳其摘要，不列為本輪已讀或採用來源。

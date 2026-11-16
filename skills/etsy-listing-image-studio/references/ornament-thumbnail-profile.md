# Ornament 掛飾 thumbnail 配方

在 Studio 內處理 ornament／聖誕吊飾的 image plan、fidelity pilot、生成及 QA 時讀。這份 profile 不另設 renderer，也不授權研究、改稿、上載或影片。完整 Growth → APOD 流程才讀 [ornament workflow](../../etsy-ornament-apod-workflow/SKILL.md)；已在 image phase 不回到上游重跑。

沿用 [Studio intake](handoff-intake.md)、[reference-led method](reference-led-geometry.md) 及 [acceptance](thumbnail-acceptance.md)。預設仍是 ChatGPT web／in-app browser 的 whole-image 方法；同款原圖、actual artwork、original logo 分工清楚。原生 size、exact-file QA、retry counter、owner gates 不在本檔複製另一套。

## 掛飾 source lock

出圖前打開實際同款 mockup／原稿。記：

- SKU／variant／artwork revision；正面圖案、exact printed name／固定字句／字體位置；哪一項可變，哪一項固定。
- 外輪廓、透明或不透明區、top tab、hole、cord/ribbon、結繩與接觸方式；清楚分辨透明邊、陰影和真正材料邊界。
- 材質、印刷方式、可見表面、附帶物及未見的背面／厚度。Acrylic、MDF、ceramic、metal 等依 source，不能由 ornament 名稱推斷。
- 同款實體 W/H 若有則記來源；沒有時使用 source-view silhouette 一致性，不從 artwork canvas、圖片 bounding box、手掌或聖誕樹估尺寸。

掛飾不是 journal：不要套書封矩形比例、四角量測、書脊／內頁、頁數或 leather texture。非矩形 custom-cut ornament 的 print canvas W/H 也不等於外輪廓實體尺寸。正面可對齊可見的輪廓 landmarks、hole/tab、主要圖案和字區檢查；斜角只做 source-supported perspective／形狀判讀，不能假稱精確 physical measurement。關鍵輪廓被手遮住則該項 HOLD；不能調選邊界來湊比例。

記錄 geometry mode：非矩形掛飾用 `SOURCE_VIEW_REVIEW`，不冒稱 numeric physical-ratio PASS；未知實體尺寸與 measured-scale rows 保留 HOLD。真正有矩形正面及已核實體 W/H 的款式才使用適用的 rectangle-ratio 檢查。若當前 owner brief 明文要求 verified physical geometry，仍須滿足該 gate，不能用 source-view comparison 當豁免。

透明 acrylic 不能畫成玻璃、發光寶石、金屬箔、雕木、凸浮雕或有未證的彩色透光；stained-glass-style artwork 不代表真 stained glass。只有來源支持才展示背面、厚邊、sunlight transmission 或 double-sided printing。

## 一張一個買家問題

下表是可按 SKU 改寫的20-role規劃庫，不是每款必定20張、不代表預先批准 overlay。Full MyGiftStyle build 的20要求來自 Coach；narrow brief 用它的 N／active rows。優先沿用已批准同款 plan；不能借其他款姓名／信仰句／規格／時效。

|#|主要問題／功能|構圖方向與證據條件|
|01|完成品到底甚麼樣？|清楚完整 front／near-front hero，姓名及設計可見；AI mockup 不冒充實物照片，適用 real-photo gap 分開保留。|
|02|個人化放在哪？|姓名區細節；需要全件 inset 時與大圖分隔，不能用一條 cord 連兩個視圖。|
|03|固定文字寫甚麼？|來源中實際固定字句的可讀細節。無固定字句時另規劃一個有證據的問題，不硬造 faith message。|
|04|圖案是甚麼／有何意義？|同款原圖的主題細節，描述看得到的內容；不要重畫人物／符號或補神學／故事主張。|
|05|是甚麼材料？|可信正面材質表現＋已核材質文案；不靠藝術效果暗示另一種材質。|
|06|圖案如何附在產品？|已核 print/process；可用輕斜正面，未見背面不翻轉；不把 printed 稱 engraved。|
|07|輪廓有何特點？|整件外形及透明／留白區清楚，不裁掉 top tab/hole 或細小邊緣。|
|08|如何掛起？|孔與 cord/ribbon 的實際構造；不加磁石、扣環、支架或未核硬件。|
|09|收到幾件、包含甚麼？|實際單件＋附帶物；道具不假成 bundle／包裝／gift box。|
|10|用在自己家是甚麼感覺？|在適合位置懸掛／擺用的具體 action；生活場景不是尺寸量測。|
|11|適合送給誰？|與 approved buyer/giver/recipient 相符的示意送禮場景；不是客戶反應／見證。|
|12|另一個真實送禮關係？|選不同 buyer question 的關係和 action；只有換年齡／人物不算新用途。|
|13|具體場合怎樣使用？|例如已批准 host／family celebration 情境；道具標示不包含，不能憑空加售品。|
|14|原圖顏色與設計如何搭配？|清楚呈現固定色彩，在相容場景中保持印刷顏色；不是額外顏色選項。|
|15|怎樣下單？|Exact approved ordering steps＋產品；不造假 checkout UI／自動校對承諾。|
|16|輸入格式有何要注意？|同款真正的姓名／日期規則與 example；沒有 year field 不教人輸入年份。|
|17|甚麼可以改、甚麼固定？|明確分開 editable／fixed；禁止視覺上暗示未提供的字體／色／圖案選項。|
|18|製作與送達有甚麼分別？|只有可核 source 才寫 supplier average／shop processing／transit；沒有到貨證據不寫 guarantee。若 brief 要 delivery proof 而缺 source，保留 HOLD，不用一般日曆圖補數。|
|19|如何保養與收納？|同款 supplier care；未核不能畫成可水洗、防水、耐摔、永久不褪色。|
|20|最後一個重要購買疑問？|從真實 FAQ 選幾項可讀答案；有長限制時移回 description，改圖上 wording 先走原 copy 批准，不靜默刪字。|

不可用近似背景湊滿數量。若某角色的 source 缺失，標明依賴及 HOLD，保留其他獲授權 rows；改 role／copy／count 依既有 owner 範圍處理，不能把缺證據改稱已完成。

## 構圖與圖文

- Technical/name/text rows 優先清楚正面；supported gentle oblique、懸掛、hand-held 等按角色使用。Angle 多樣性不能犧牲 exact print 或發明背面。
- Printed text 和新增 overlay 分區。只渲染該 row 的 exact approved copy，不能把全 title/tag list 放上圖。Hero 的文字／logo依當前 brief及平台要求判斷。
- Dual-view：畫面必須讓人看清是同一件的 detail＋full view，不畫成兩件套裝；cord、手指、枝葉不能跨 inset 邊界接成不可能物體。
- Hands：分配每隻手屬於哪個人、拿 cord 還是接觸邊、受力和遮擋；不穿過材料、孔或印刷字，不靠遮住缺陷讓 QA 過關。
- 保持 original logo 的完整字形／比例；預留不壓產品與正文的品牌區。Approximate AI logo 不能當原裝。

## Logo-only 特定例外的處理

628811 曾有 owner 指定的 **logo-only 後製**，不是一般預設。新 brief 若同樣明確授權此方法，才可用指定原 PNG 作均勻縮放／alpha composite 到批准空白 ROI；輸出記 original logo hash、native before/after hash、ROI、scale 及 alpha 方法，驗證 ROI 外像素完全相同。這是 derived file，保留 native returned image。

ROI 不可碰產品／姓名／fixed text／overlay；不得以該例外修補 artwork、貼產品、換字、裁切、拉伸或 upscale。原背景無乾淨品牌區時，不能擴 ROI 擦走其他內容。沒有本輪適用授權就依 Studio 原規則 HOLD／請最少必要方法決定；不繼承舊產品的許可。

## Per-file QA 的掛飾加項

按既有 acceptance 對 exact final file 做全尺寸及150/300px檢查，分開記：

1. Silhouette、tab/hole、cord／ribbon 接點、透明邊與 source 一致，沒有厚度或材質幻想。
2. 同一 sample name、exact fixed words、人物／主題、花葉／星等圖案沒有漂移；每個小字、標點與重要 footer 仍可讀。
3. Angle／contact／hands 自然，inset 不相連；整件主視圖不意外截斷。
4. Overlay 只表達有 source 的事實及已批准選項，示意人物不是 customer proof。
5. Logo 是真實原 asset 的已驗方法；case-specific exception 與 technical finding 分開。
6. Role distinct、native dimensions、file hashes、attempt count 與 exact owner decision 都沿用同一 ledger。

一張成功不能預先通過全套。系統性產品漂移先停同類生成、診斷再在剩餘 retry budget 內改 supported input；改 filename、換 thread 或轉交 Skill 不重置重試。

輸出實際 numbered files、逐檔 QA／角色 map、contact sheet及必要ZIP。交回同一 workflow 的已授權 APOD 階段；不要在 Studio 自己新增上載權限或宣告 Etsy 已 ready。

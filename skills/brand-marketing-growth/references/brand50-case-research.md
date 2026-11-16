# 50家信仰與家人送禮品牌參考庫

版本 B50-2026-10-07.1。資料截至2026-10-07，各筆保留原觀察日期。本模組為分級案例庫，含原11品牌與GuidingCross共12家，另有38家；FARFETCH在此50家之外繼續保留。合計51個不同品牌參考，不能以13＋50相加。原有詳細案例與Etsy規則來源保持。

## 開始使用
先讀共同品牌轉用與工時限制，再查 `brand50-public-reference.json`。依case_id查品牌、依content_id查具體內容，最後開source_id的公開URL。品牌ID固定，comparison rank只代表本次代表商品相似度，不是商業成功排名。

50家分層：10家核心載體與信仰接近、22家其他信仰journal或角色／規格不同、13家家庭送禮或信仰品牌相鄰、5家商品接近但品類成交證據不足。FARFETCH與教師不計入50家。41家有可查商業資料不等於41家高利潤或純自然成長。

10家優先商品參照為TrendyGiftSpot、Naeliva、BlushandBo、WordsAndWaxCandleCo、CherishLaneGifts、BlissfulGiftCreation、glowheartgifts、HeartKraftedGifts、NirasCreative及dmireshop。其中數款只在標題／工具旗標見personalized，或工藝未核，須保留逐SKU限制。五家provisional為StacyStyleGifts、PetitsInstants、Calatina、DazzlingDrops、RealCuteGiftsCo，不能因相似分而自動升級。

## 查詢規則
1. 先指定買家任務，再查商品。分開實際付款者、文案的送禮者、收到空白本的人、寫字的人、日後讀回憶的人。商品稱from daughter只支持送禮角色，並非已驗證買家人口統計。
2. 商品相似分四軸：載體0–4、客製欄位0–2、代表商品信仰0–2、送禮任務0–2。評的是抽樣SKU與用途；不外推全品牌、不預測成交。
3. 商業資料獨立判讀：全店sales、單item評論、產品家族合併評論、品牌評論、自述收入、followers/views不得合併或相互換算。沒有單品銷量／利潤時維持unknown。
4. 身份取官網或Etsy外連優先。share buttons、預設Wix href、同名帳號、搜尋推薦caption不合資格。官方帳號已核也不等於內容已讀。
5. `read_level`決定能說甚麼。索引摘要只說摘要能證明的字句；metadata只支持標題、日期、指標；影片方法須讀逐字稿。字幕只有音樂不能補畫面。
6. 每筆留發布日期、觀察日期、閱讀日期；新讀舊快取不能改成新發布或即時價格。入口失敗不推定公司已結束。

## 新增產品與語意防錯
- MyGiftStyle：店頁About提mygiftstyle.com，但本輪HTTPS讀取TLS失敗，當前安全可用性未核。不能把該域名當已驗證轉換落點。72為本輪可見項目數，非完整盤點。廣泛30天退款說法與客製品頁退換條款有語意落差，先審核再作宣傳。母親款泛用文字提photo/date/message，但本輪只核15字姓名控制欄，先用已核範圍。
- Lissa Sue Designs：客製Letters to Daughter代表款由父母／祖父母書寫，孩子日後閱讀。官網footer social實際指Wix，正確帳號須採Etsy外連。`B50-LS-01`至`05`。
- Paper Sunday：姓名進入內頁經文，與本店姓名封面＋200間線頁不同。官網多卡片共用5622評價，不相加。`B50-PS-01`至`07`。
- MerryHeartCo：150間線頁；兩SKU姓名／背面經文選項與尺寸差異分開。`B50-QA-MER-01`核1874244267的9則item評論，非全店3761sales的替代量度。
- The Christian Art Company：Meadow為150間線頁、前面姓名／短句、背面經文與reference選項；journal頁輪播wall-art評論，journal需求待補。`cg-tc-product`。
- Personalization Mall：代表信仰journal顯示9評價含重複，不能當9個獨立買家。Personal Creations顯示19評價可能跨款，共用範圍未核。`cg-pm-product`、`cg-pc-review-check`。
- Duncan & Stone官方明確預印不客製；Dear Son由父母寫，Mom為母親回憶。Promptly選定Childhood沒有特定religious prompts，Christmas不能自動當Christian品牌。`ds:son`、`pj:faq`。
- dmireshop同頁custom engraving與custom-printed衝突保持未知。WoodPresentStudio入口價為paper-only不可與完整journal比較，未把精確完整款價納入排名。Naeliva母親款收禮／書寫者是媽媽，送禮方向不可倒轉。

## 可轉用的方法與證據深度
已讀口述教學可借：
- Daily Grace routine用真實使用次序展示產品。`CB-S038`，2022影片。
- James Method逐層解釋不同產品的任務。`CB-S172`，2024影片；不能將其guided系統套給空白間線本。
- Well-Watered Women用短FAQ回答能否單獨使用。`CB-S071`，2021影片。
- DaySpring示範如何開始手寫／標日期。`CB-S136`，2016歷史影片。
- Christian Art Gifts逐款講規格與收禮用途。`CB-S148`，2021；暢銷圖案只是該講者歷史自述。
- Elevated Faith開箱有實際產品細節但屬品牌寄贈。`CB-S103`，2023，不當純自發UGC。
Val Marie Paper只讀直播開頭約18,000字元，可借降低第一頁壓力；不稱整場看完。`CB-S090`。其2025接手前後身份與舊工時不能混用。

新增近類品牌的可用文字方法：Lissa Sue成人寫給未來孩子、Duncan & Stone分清不同親屬的書寫方向、PMall依信仰場合寫gift guide、TCAC逐欄解釋客製、Paper Sunday短反思接使用情境。這些是內容結構，沒有因果證據證明帶來多少訂單。

## 一次只選一個實驗
一個已售主力SKU、一個角色對、一個場合、一個變量、一個CTA、一個觀察窗。輸出每次包含：來源事實、分析假設、本店差異、原創hook、格式、產品真實限制、分鐘、可取得量度、資料不足／停止條件。

建議原創實驗：朋友信仰鼓勵或母女感謝二擇一，以真實姓名封面＋打開的200間線頁，示範一句成人自行寫的祝福。內容提出的問題只是使用示範，不是聲稱預印內頁。禁止複製藝術、文案、假UGC、假手工、未核捐款與屬靈結果承諾。

所有品牌與教練共用3–5小時／週，包括履約和客服。基準210分鐘：履約90、拍攝45、剪輯30、安排20、檢視25；3小時忙週減製作。只有本店已用IG且第一方資料支持時，才以IG為素材中心、FB重用、少量Pinterest衍生；否則先用目前有證據的主渠道。這是候選分配，不因參考庫而開新帳戶。Threads不加獨立產量，YouTube/TikTok先不增開。維持原90天零自行投放窗口，起訖未知不重設。

主要量度是可核商品點擊、有效詢問、同SKU店訪／訂單與工時；有能力才看貢獻毛利。Etsy conversion分母用visits，Social可能包括Offsite Ads，零主動投放不等於純自然。未取得post-level attribution就unknown。曝光不足不宣判利基失敗。

## 更新與品質閘門
此次137內容記錄包括36商品頁、部落格和社群；不能寫137社交貼文。390渠道審核列包含候選／空缺／受阻，並非390官方帳號；388不同品牌×平台cell。369來源記錄對應365不同URL。16個YouTube入口：6個可用口述逐字稿、1個部分逐字稿、2個音樂／無可用教學、7個metadata或描述級。

如使用者要求定期回看，可建議每月最多2品牌、各1商品與2內容，在原改善時間內替換，不另加工時；本參考庫沒有啟用排程或自動監控。先檢查身份與產品，再更新數字。所有新資料保留原ID；相同URL新快照新增觀察而不是抹去舊年份。獨立QA本輪覆核32比較品牌與owner baseline，修正買家角色、入口重複、Merry逐SKU範圍及來源日期；沒有宣稱50家皆由第二人重新查證。

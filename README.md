# ShineOn Design Skills

本倉庫收錄 **12 個 Skills**，支援 ShineOn／Etsy POD 的專案統籌、商業與設計判斷、研究、圖片製作、私人 APOD listing，以及模擬買家審視。各 Skill 連同現有 references、scripts、assets 等配套保存；不是完整 Etsy／POD 生態系統，也不包含產品圖稿、帳戶設定或發布授權。

## 12 個 Skills：用途與分工

| Skill | 主要用途與負責範圍 |
|---|---|
| [shineon-graphic-design-workflow](skills/shineon-graphic-design-workflow/SKILL.md) | **專案統籌入口**：確認產品、revision、授權範圍、階段、交接證據與下一步；協調跨產品資源。 |
| [etsy-coach-integrated](skills/etsy-coach-integrated/SKILL.md) | **商業與設計判斷**：買家／送禮定位、原創個人化概念、designer brief 與成品覆核、研究判斷、keyword 選擇及 listing 文案；亦涵蓋數位產品。 |
| [brand-marketing-growth](skills/brand-marketing-growth/SKILL.md) | **品牌與增長**：品牌故事、系列方向、bundle、內容營銷、自然增長，以及未選產品的新系列探索。 |
| [etsy-competitor-listing-optimization](skills/etsy-competitor-listing-optimization/SKILL.md) | **研究證據**：競品資格、店舖盤點、keyword 與 listing 事實核對，將可追溯證據交回 Coach 作建議。 |
| [etsy-keyword-pool-cleaning](skills/etsy-keyword-pool-cleaning/SKILL.md) | **Keyword 資料整理**：清理、去重、分類研究 CSV／試算表，保留原始資料、指標限定及來源。 |
| [etsy-listing-image-studio](skills/etsy-listing-image-studio/SKILL.md) | **圖片製作與視覺 QA**：同款、同 revision 縮圖／mockup，核對產品忠實度、可讀性及圖片品質。 |
| [etsy-pod-image-prompts](skills/etsy-pod-image-prompts/SKILL.md) | **圖片規劃**：用途、角色、分鏡及 prompts，支援 Studio；只要求 prompt 時保留該較窄範圍。 |
| [etsy-apod-product-workflow](skills/etsy-apod-product-workflow/SKILL.md) | **單款完整私人 APOD listing 協調**：串連來源、研究、圖片、文案與欄位，直到授權的私人保存及重開核對。 |
| [etsy-ornament-apod-workflow](skills/etsy-ornament-apod-workflow/SKILL.md) | **掛飾專用要求**：補充 ornament 來源、幾何、縮圖與流程要求，再接同一 APOD coordinator；單做縮圖可接 Studio。 |
| [etsy-mug-apod-workflow](skills/etsy-mug-apod-workflow/SKILL.md) | **杯款專用要求**：補充 mug variant、杯柄、印區與個人化證據，接同一 APOD coordinator 完成或續辦。 |
| [canva-personalizable-product-art](skills/canva-personalizable-product-art/SKILL.md) | **Canva 可編輯美術**：在 Canva 已屬授權範圍時處理圖層、文字、master 與匯出；不自動增加必經 Canva 步驟。 |
| [superpersona](skills/superpersona/SKILL.md) | **輔助 QA**：按需要以模擬買家／使用者觀點審視概念、送禮故事、個人化理解及使用流程；不代替真買家研究、技術 QA 或 owner 驗收。 |

## 如何配合

先讀適用的 [Project 規則](AGENTS.md) 與當次 owner 要求，再以 ShineOn 主流程確認範圍。每階段只有一個 artifact owner、一個 primary production Skill，沿用同一份 task record。

- **設計概念**：ShineOn 確認範圍 → Coach 處理故事、差異化及名字安排 → 按需要接圖片／Canva 製作。
- **品牌或研究**：Growth 處理品牌方向；研究 Skill 提供競品證據，Keyword Cleaning 整理資料；Coach 作產品／listing 建議。
- **完整私人 listing**：已選實體產品且要求完整流程時，由 APOD Skill 擔任該款唯一跨階段 coordinator；掛飾／杯款入口補充專用要求。ShineOn 接收狀態，不重複指揮工序。
- **買家角度審視**：按適用要求或實際需要加入 Superpersona，按風險選擇深度與次數，不預設每次執行完整評審。

單純解釋、概念、文案、prompt 或局部修改，不會自動擴大為完整 listing、20 張圖、影片或平台寫入。歷史案例的次數、方法例外及批准，不會自動沿用到新任務。

## 安裝方法

### 1. 取得套件

使用 GitHub 的 **Code → Download ZIP** 並解壓，或在已安裝 Git 的環境執行：

```sh
git clone https://github.com/trevor94899234-maker/shineon-design-skills.git
```

### 2. 確認目標與備份

確認目前 runtime 實際讀取的使用者 Skill 目錄。既有環境常用 `~/.codex/skills/`；Windows 常見位置為 `%USERPROFILE%\.codex\skills\`。若環境另有設定，以實際位置為準。

安裝前先備份會被更新的同名資料夾；保留本地修改及可還原副本。不要直接覆寫現有 WIP。

### 3. 複製完整 Skill 資料夾

將本倉庫 `skills/` 底下所選的各個資料夾，完整複製到目標 Skill 目錄。使用本專案全部分工時，可安裝這 12 個資料夾。

正確結構例如：

```text
<實際 Skill 目錄>/
  shineon-graphic-design-workflow/
    SKILL.md
    references/
  superpersona/
    SKILL.md
    references/
  etsy-competitor-listing-optimization/
    SKILL.md
    references/
    scripts/
    tests/
    assets/
    agents/
```

不要只複製 `SKILL.md`，也不要額外套一層 `skills/skills/`。保留各 Skill 實際附帶的 references、scripts、tests、assets 與 agents；並非每個 Skill 都有全部子目錄。**Superpersona 目前是 1 份 SKILL.md 加 9 份 references，沒有 scripts。**

### 4. 載入與核對

依目前 runtime 的正常重新載入方式，確認已安裝 Skill 名稱可被發現，且相對引用檔案存在。先以簡單、已授權的任務驗證所需入口。複製成功不等於平台連接成功、完整流程驗收或生產放行。

GitHub 上傳、Git clone 與本機安裝是不同步驟；遠端更新不會自動更新已安裝副本。更新時重新比對來源、備份本機版本，再複製已確認的變更。

## 依賴與限制

可只安裝所需 Skills，但跨 Skill 路由需要對應依賴。上述 12 個均已收錄；階段可能另用的 `connected-chrome-workflow`、`pod-university-playbook` 等 specialists **未包含在本套件**。引用它們不代表已安裝，缺少時應明示能力缺口。

各 script 的 Python／其他 runtime 與套件需求，以原 Skill 和 script 說明為準；複製 Skills 不會自動安裝執行環境、登入網站或連接服務。不要無差別執行所有 scripts。

## 證據與授權邊界

適用平台規則、當次 owner 指示及 Project 規則優先；Skill 能力描述不是操作授權。私人 APOD 保存、Etsy customer-field mapping、owner 接受及正式發布各自獨立。

本套件不授權 Send、Publish、Deploy、付款、Etsy push／sync、帳戶或安全設定變更。既有 logo、尺寸、嘗試上限、人手驗收、來源鎖定與完整 listing contract 仍按適用規則執行。

References 中的歷史案例、來源標籤或原專案路徑，不一定是本倉庫附帶檔案；案例日期不代表目前產品狀態。模擬觀點不是真實使用者證據，未知資料保留為 TBC。

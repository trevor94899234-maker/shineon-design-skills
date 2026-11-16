# ShineOn Design Skills

六個既有 Codex Skills 的有界更新套件；保留各 Skill 的現有 references、scripts、assets 與權限界線。這不是完整 Etsy／POD 生態系統，也不包含產品圖稿、原始聊天、帳戶設定或發布授權。

| Skill | 本次增量 |
|---|---|
| [shineon-graphic-design-workflow](skills/shineon-graphic-design-workflow/SKILL.md) | 核對交付者與接收者實際檔案；按需讀取有日期的交接、階段狀態及數位 preflight 案例 |
| [etsy-listing-image-studio](skills/etsy-listing-image-studio/SKILL.md) | 區分 prompt-only 與真正選區／遮罩操作；更正 QA 前先對齊交付檔，保留既有 logo、尺寸及 attempt gates |
| [etsy-coach-integrated](skills/etsy-coach-integrated/SKILL.md) | 按需使用參考圖→原創個人化概念／brief→designer 交付覆核方法 |
| [etsy-apod-product-workflow](skills/etsy-apod-product-workflow/SKILL.md) | 補 optional 空值、有限選項、複合署名及有界數位 preflight 的證據區分 |
| [etsy-pod-image-prompts](skills/etsy-pod-image-prompts/SKILL.md) | 在原創美術來源鎖定段落釐清適用 project／當次 owner 方法優先於歷史預設 |
| [canva-personalizable-product-art](skills/canva-personalizable-product-art/SKILL.md) | 同步方法優先次序；只有 Canva 階段在範圍內才套 Canva master／import／export 流程 |

## 安裝

1. 先備份目前使用者 Skill 目錄內會被更新的同名資料夾；保留本地修改及還原副本。
2. 將所需的 `skills/<skill-name>/` **完整資料夾**複製到目前使用者的 Codex Skill 目錄。一般位置是 `~/.codex/skills/`；Windows 通常是 `%USERPROFILE%\.codex\skills\`。若環境另有設定，以實際 Skill 目錄為準。
3. 確認目標為 `<skill-directory>/<skill-name>/SKILL.md`，並核對 references／scripts／assets 一併保留。依目前 runtime 的正常重新載入方式確認名稱可被發現；複製成功不代表已通過實際工作流程驗收。

可只安裝所需 Skills，但跨 Skill 路由要有對應依賴。依階段可能使用、而本倉庫**未收錄**的 specialists 包括 `brand-marketing-growth`、`superpersona`、`etsy-mug-apod-workflow`、`etsy-ornament-apod-workflow`、`connected-chrome-workflow` 及 `pod-university-playbook`。按名稱在當前環境確認，缺少時明示該能力缺口；不要把 sibling link 視為已安裝證據。各 script 的 runtime／套件需求以原 Skill 說明為準。

## 證據與範圍

新案例使用相對於原專案 root 的來源標籤，並非本倉庫附帶檔案或可點擊的 repo 路徑；案例保留實際事件日期，不代表目前商品狀態。既有來源檔及歷史紀錄保持原貌。

本次沒有改變每圖原裝 logo pixels gate、原有尺寸／嘗試上限、人手驗收、完整 listing contract 或私人 APOD 與 Etsy mapping／發布的分界。ShineOn 適用專案可使用 ChatGPT 網頁 art-only＋原生 APOD 文字；其他專案有效來源鎖定保留，不改成全域 web-only。

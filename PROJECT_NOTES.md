# 📒 PROJECT_NOTES.md  

## 🗂 專案名稱
**EastUSATours — POR v2 多語整合開發任務（MVP）**

---

## ✅ 專案目標
- Tour 模組（巴士 / 郵輪）  
- 多語內容（繁 → 簡自動轉換，英文獨立輸入）  
- 前後台語系切換、翻譯狀態 flag  
- 前台會員系統（登入 / 登出 / 訂單查詢）  
- 後台用 Django Admin（先）  
- API `/api/tours/` 提供前端 & 行銷串接  

---

## 📦 模組任務區

### 🚍 Tour 模組
- [x] `Tour` Model 建立，支援：
  - `tour_type` (Enum: bus_tour / cruise_tour)
  - JSONField 儲存多語內容 (`title`, `desc`, `faq`)
  - 翻譯狀態欄位 (`zh_Hant_translated`, `zh_Hans_synced`, `en_translated`)
- [x] Admin 後台：根據 `tour_type` 顯示不同欄位  
- [x] OpenCC 串接（繁簡自動轉換）

### 🌐 語言處理
- [x] `settings.py` 已整合多語系 (`zh-hant`, `zh-hans`, `en`)  
- [x] `locale/zh_Hant/LC_MESSAGES/django.po` 已初始化  
- [x] makemessages / compilemessages 驗證成功  
- [x] `LANGUAGE_COOKIE_NAME` & 切換功能完成  

### 🧾 Admin 管理
- [x] 語系欄位 Tab / Stack 切換  
- [x] 後台自動繁簡同步  
- [x] 根據 `tour_type` 顯示 Bus 或 Cruise 特定欄位  

### 🔗 API
- [x] `tours/serializers.py` → 多語 JSON 輸出  
- [x] `tours/views.py` → CRUD API + `?lang=` 支援  
- [x] `/api/tours/` & `/api/tours/<id>/` 已可正確輸出  

### 👤 會員系統 (accounts)
- [x] 登入 (`login.html`)  
- [x] 登出 (`logout.html`)  
- [x] Dashboard (`accounts/dashboard.html`)  
- [ ] 訂單列表 (TODO)  
- [ ] Voucher PDF (TODO)  
- [x] 已整合 **django-allauth**（取代舊 signup view）  

### 🏠 首頁 (templates/home.html)
- [x] 全域 `templates/base.html` 建立  
- [x] `home.html` 移到 `templates/` 根目錄  
- [x] `views.home` 提供：
  - 郵輪（cruise_tour） → 置頂  
  - 熱門行程（最新 6 筆）  
  - 美國巴士（bus_tour）  
  - 歐洲（預留）  
- [ ] 首頁搜尋功能（TODO）  

---

## 🛠 環境設定

### 🔹 本地
- `settings/local.py` → DEBUG=True, SQLite  
- 預設 `manage.py` / `wsgi.py` / `asgi.py` 使用 local  

### 🔹 Render Production
- `settings/production.py` → DEBUG=False, PostgreSQL via `dj_database_url`  
- `ALLOWED_HOSTS` & `CSRF_TRUSTED_ORIGINS` 設定完成  
- 需在 Render **環境變數** 設定：  


---

## 📅 進度紀錄

### 2025-09-09
- 完成 Tour model 與多語 JSON 架構  
- 設定 OpenCC 繁簡轉換  

### 2025-09-10
- 修正 Admin 表單，根據 tour_type 顯示欄位  
- API `/api/tours/` 可輸出多語 JSON  

### 2025-09-11
- 整合 allauth，移除舊 signup  
- 登入 / 登出 / Dashboard 初版完成  
- 首頁 `home.html` 改版 → 郵輪 & 搜索置頂  
- `local.py` / `production.py` 設定拆分完成  
- `manage.py` / `wsgi.py` / `asgi.py` → 預設 local  

---

## 📌 TODO
- [ ] 首頁搜尋功能  
- [ ] 訂單模組 (Order / Voucher PDF)  
- [ ] 前台會員 → 我的訂單 / 通知  
- [ ] 測試自動化 (pytest / Django TestCase)  
- [ ] Render 部署自動化（CI/CD）  
# 🗂 EastUSATours — POR v2 多語整合專案 & 系統資料

持續更新的專案筆記，用來追蹤架構、功能進度與每日紀錄。  
⚠️ 注意：不要手動刪舊紀錄，每天只需要 **追加** 新的更新。

---

## 📌 專案結構 (最新確認版)

eastusatours/ # 根目錄
├── accounts/ # 會員系統 App
│ ├── views.py # Dashboard, Profile, Orders
│ ├── urls.py # /accounts/login, logout, dashboard
│ └── templates/accounts/
│ ├── dashboard.html
│ ├── profile.html
│ └── orders.html
│
├── tours/ # Tours App (行程)
│ ├── views.py # Tour list / detail / 搜尋
│ ├── urls.py # /tours/, /tours/<id>/
│ └── templates/tours/
│ ├── tour_list.html
│ ├── tour_detail.html
│ └── search_results.html
│
├── eastusatours/ # 主專案設定
│ ├── init.py # 自動切換 settings（local / production）
│ ├── settings/
│ │ ├── base.py
│ │ ├── local.py
│ │ └── production.py
│ ├── urls.py # 全域路由 (首頁 / i18n / apps include)
│ ├── wsgi.py
│ └── asgi.py
│
├── templates/ # 全域共用 Templates
│ ├── base.html
│ ├── home.html # 首頁 (郵輪 + 搜索置頂)
│ ├── home_guest.html
│ ├── home_member.html
│ └── partials/
│ ├── navbar.html
│ └── footer.html
│
├── static/ # 靜態資源 (CSS / JS / Images)
│
├── locale/ # 多語翻譯
│ ├── zh_Hant/
│ ├── zh_Hans/
│ └── en/
│
├── scripts/ # 自動化腳本
│ └── update_notes.py # 快速追加更新紀錄
│
├── manage.py
└── requirements.txt
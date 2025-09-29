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

✅ 重整後建議結構 0924
eastusatours/
├── eastusatours/
│ ├── models.py # ✅ 所有資料結構都在這裡維護
│ ├── views.py # ✅ 首頁 Home
│ ├── urls.py
│ └── settings.py
│
├── tours/
│ ├── views.py # ✅ Tour 視圖 (bus tours)
│ ├── urls.py
│ └── templates/tours/
│
├── cruise/
│ ├── views.py # ✅ Cruise 視圖 (cruise tours)
│ ├── urls.py
│ └── templates/cruise/

📌 EastUSATours 專案進度報告

1. 專案架構

✅ 建好專案 eastusatours

✅ 建好 apps:

tours → 一般行程

cruise → 郵輪

accounts → 會員系統 (尚未完成串接)

🔜 建議新增 core → 放 Banner、FAQ、共用設定（明天可以處理）

2. Models（資料模型）

Tours

DepartureRegion ✅

DepartureCity ✅

Tour (尚未完整測試 admin)

Cruise

CruiseRegion ✅

CruisePort ✅

CruiseTour ✅（已修正關聯與欄位）

Core (未完成)

Banner ⏳

FAQ ⏳

狀態：
Tours 與 Cruise models 已成形，能支援搜尋與行程建立。Core 還需要一個乾淨的地方安置。

3. Admin（後台）

✅ Tours / Cruise 的 Admin 設定（list_display、filter、search 已完成基本設定）

🔜 Core admin 還沒建立

🔜 Tours Admin 匯入時遇到 ImportError，原因是 Tour model 還沒同步定義完整，需要再修一次。

4. Views & Templates

首頁

✅ 基本結構出來

⏳ Banner 尚未串資料

⏳ FAQ 尚未串資料

Tours

✅ tour list / detail / card template 已有

Cruise

✅ 搜尋框、搜尋列表 OK

✅ 已改用 Tour 作為主模型

Navbar

⏳ login/logout link 還沒修（accounts app 未接好）

5. 功能進度

✅ 行程搜尋（tours、cruise）

✅ 出發地區/城市 自動更新搜尋框

✅ 後台可新增 region/city/port，前台搜尋框自動更新

⏳ 登入/登出/註冊（accounts）

⏳ 首頁 Banner

⏳ FAQ

6. 明日任務建議

建立 core app → 搬 Banner 與 FAQ 過去

修正 tours/admin.py 裡 Tour 的 import 問題

串接 accounts（至少讓 login/logout 正常）

把首頁完整串起來（Banner、FAQ、熱門行程）
那你只要在 python manage.py shell 裡輸入這段：

from django.contrib.auth.models import User

u = User.objects.get(username="Nikki8858")
u.set_password("Nikki8858") # 把密碼設成跟帳號一樣
u.save()

接著可以檢查一下是否成功：

print(u.check_password("Nikki8858"))

如果回傳 True，就代表你的帳號密碼都設成功了 🎉
python manage.py reset_user Nikki8858

📂 EastUSATours 專案結構（整理版）
1️⃣ 主專案 (eastusatours/)

urls.py
👉 只負責「掛載各個 app」：

/ → core.urls (首頁、語言切換)

/tours/ → tours.urls

/cruise/ → cruise.urls

/admin/ → Django 後台

views.py（⚠️ 建議清空）
👉 原本有 home，但應該移到 core/views.py，主專案 views 保持乾淨。

2️⃣ Core App (core/)

views.py
👉 放首頁 & 語言切換：

home → 抓 Banner + FAQ + Tours + Cruise 顯示首頁

switch_language → 切換語言，寫入 session

urls.py
👉 路由設定：

/ → views.home

/switch-language/<lang_code>/ → views.switch_language

middleware.py
👉 處理國際化：

CustomLocaleMiddleware → 把 /tw/ → zh-hant、/cn/ → zh-cn

RedirectByBrowserLangMiddleware → 自動判斷瀏覽器語言 → 導向 /tw/、/cn/、/en/

models.py
👉 放 Banner、FAQ 模型

3️⃣ Tours App (tours/)

models.py → Tour 資料模型

views.py → Tour 列表 / 詳細頁

urls.py → /tours/... 路由

4️⃣ Cruise App (cruise/)

models.py → Cruise 資料模型

views.py → Cruise 列表 / 詳細頁

urls.py → /cruise/... 路由

5️⃣ Templates

base.html → 網站基底模板

navbar.html → 導航列（含 /tw/ /cn/ /en/ 語言切換）

home.html → 首頁內容，讀取 banners / tours / cruises / faq

🔑 最後效果

https://eastusatours.com/tw/ → 繁體

https://eastusatours.com/cn/ → 簡體

https://eastusatours.com/en/ → 英文

首頁、行程、郵輪都正常，後台 /admin/ 也正常

要不要我幫你做一份 「改版後檔案總覽」Markdown 文件（像 README 一樣），放在專案裡，讓你或其他人
# EastUSATours 專案架構說明

本文件釐清專案內各檔案的角色，避免混亂或誤修改。

---

## 1. 主專案 (eastusatours/)

- **urls.py**
  - 只負責掛載各 app
  - `/` → `core.urls`
  - `/tours/` → `tours.urls`
  - `/cruise/` → `cruise.urls`
  - `/admin/` → Django 後台

- **views.py**
  ⚠️ **保持空白**（不要再放 `home`）
  - 所有首頁邏輯請放到 `core/views.py`

---

## 2. Core App (core/)

- **views.py**
  - `home` → 首頁（讀取 `Banner`、`FAQ`、`Tours`、`Cruise`）
  - `switch_language` → 語言切換，更新 session

- **urls.py**
  - `/` → `views.home`
  - `/switch-language/<lang_code>/` → `views.switch_language`

- **middleware.py**
  - `CustomLocaleMiddleware`
    - `/tw/` → zh-hant
    - `/cn/` → zh-cn
    - `/en/` → en
  - `RedirectByBrowserLangMiddleware`
    - 沒有語言前綴時 → 根據瀏覽器語言自動導向 `/tw/`、`/cn/`、`/en/`
    - 會優先使用 session 中的 `preferred_lang`

- **models.py**
  - `Banner`
  - `FAQ`

---

## 3. Tours App (tours/)

- **models.py** → Tour 模型
- **views.py** → Tour 列表、詳細頁
- **urls.py** → `/tours/...`

---

## 4. Cruise App (cruise/)

- **models.py** → Cruise 模型
- **views.py** → Cruise 列表、詳細頁
- **urls.py** → `/cruise/...`

---

## 5. Templates

- **base.html**
  - 網站基底模板

- **navbar.html**
  - 導航列
  - 語言切換 → `/tw/`、`/cn/`、`/en/`

- **home.html**
  - 首頁內容
  - 顯示 `banners`、`tours`、`cruises`、`faqs`

---

## 6. 國際化設定 (i18n)

- URL 語言前綴：
  - `/tw/` → 繁體中文（實際讀取 zh_Hant 翻譯）
  - `/cn/` → 簡體中文（實際讀取 zh_CN 翻譯）
  - `/en/` → 英文

- 翻譯檔案位置：
📘 EastUSATours 專案開發筆記
1. Core App 建立與首頁整合

建立 core app 並加入 INSTALLED_APPS。

Models：

Banner (標題、圖片、連結、排序、是否啟用)。

FAQ (問題、答案、排序)。

Admin 註冊 Banner、FAQ。

core/views.py → 新增 home，整合 Banner + FAQ + Tours + Cruise。

home.html → 用迴圈顯示 banners 與 faqs。

✅ 狀態：後台可新增 Banner 與 FAQ，首頁自動更新。

2. Migration 與快取清理

migrations 過多 → 刪除所有舊 migrations，只留 __init__.py。

清理快取：

Linux/macOS:

find . -name "__pycache__" -type d -exec rm -rf {} +


Windows PowerShell:

Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force
Get-ChildItem -Recurse -Include *.pyc | Remove-Item -Force


⚠️ 避免多份 middleware.py → 只保留 core/middleware.py。

3. Middleware 國際化
問題

嘗試 "eastusatours.core.middleware.LocaleFromPathMiddleware" → 匯入失敗。

正確 import → "core.middleware.CustomLocaleMiddleware"。

Django 5 移除了 translation.LANGUAGE_SESSION_KEY → 改用 request.session.get("django_language")。

最終 core/middleware.py
from django.utils import translation

LANG_MAP = {"tw": "zh-hant", "cn": "zh-hans", "en": "en"}
REV_LANG_MAP = {v: k for k, v in LANG_MAP.items()}

class CustomLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        parts = request.path.strip("/").split("/")
        prefix = parts[0] if parts else None

        if prefix in LANG_MAP:
            lang_code = LANG_MAP[prefix]
            request.lang_prefix = prefix
            request.session["django_language"] = lang_code
        else:
            lang_code = request.session.get("django_language", "en")
            request.lang_prefix = REV_LANG_MAP.get(lang_code, "en")

        translation.activate(lang_code)
        request.LANGUAGE_CODE = lang_code

        response = self.get_response(request)
        translation.deactivate()
        return response

settings/base.py (MIDDLEWARE 區)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "core.middleware.CustomLocaleMiddleware",  # ✅ 在 CommonMiddleware 之前
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

4. URL 與 Views 對齊

錯誤：TypeError: home() got an unexpected keyword argument 'lang_code'
→ 因為 urls 有 <str:lang_code>/，view 沒接參數。

✅ 修正：home(request, lang_code=None)。

urls.py
from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core_views.home, name="home"),
    path("<str:lang_code>/", core_views.home, name="home_lang"),
    path("tours/", include(("tours.urls", "tours"), namespace="tours")),
    path("cruise/", include(("cruise.urls", "cruise"), namespace="cruise")),
]

views.py
from django.shortcuts import render

def home(request, lang_code=None):
    return render(request, "home.html")

5. 模板與 i18n

錯誤：Invalid block tag 'trans'
→ 缺少 {% load i18n %}。

✅ 修正：在模板最上方加：

{% load i18n %}

Navbar 語言切換範例
{% load i18n %}
<nav>
  <a href="/tw/" {% if request.lang_prefix == 'tw' %}class="active"{% endif %}>繁體</a>
  <a href="/cn/" {% if request.lang_prefix == 'cn' %}class="active"{% endif %}>简体</a>
  <a href="/en/" {% if request.lang_prefix == 'en' %}class="active"{% endif %}>English</a>
</nav>

6. 翻譯檔 (locale)

結構：

locale/tw/LC_MESSAGES/django.po
locale/cn/LC_MESSAGES/django.po
locale/en/LC_MESSAGES/django.po


指令：

django-admin makemessages -l zh_Hant
django-admin makemessages -l zh_Hans
django-admin makemessages -l en
django-admin compilemessages

7. 狀態 & 下一步
✅ 已完成

Core app 建立（Banner/FAQ + 首頁）

Migration/pycache 清理

Middleware 國際化（Django 5 兼容）

URL 與 Views 對齊

模板 i18n 修正

⚠️ 下一步

翻譯檔內容：補上實際翻譯文字，執行 compilemessages。

多 app 語言前綴：目前只有首頁 /tw/、/cn/、/en/；若 tours/cruise 也要加語言前綴，需改 urls。

快取清理：保留 PowerShell script，避免舊 .pyc 混亂。

專案文件化：本 NOTES.md 放在專案根目錄，供日後交接。

🔄 整合後的專案紀錄（新版 PROJECT_NOTES.md 建議稿）
🗂 專案名稱

EastUSATours — POR v2 多語整合開發任務（MVP）

✅ 已完成

Core App

新增 Banner / FAQ models

core/views.py → home 整合 Banner + FAQ + Tours + Cruise

core/middleware.py → CustomLocaleMiddleware（Django 5 兼容，用 django_language）

多語設定 (i18n)

語言前綴：/tw/（繁）、/cn/（簡）、/en/（英文）

翻譯檔：locale/zh_Hant/, locale/zh_Hans/, locale/en/

指令：makemessages / compilemessages 驗證成功

模板加上 {% load i18n %}

URL 與 Views

urls.py → path("", home) 與 path("<str:lang_code>/", home)

home(request, lang_code=None) 已修正

Models

Tours: DepartureRegion, DepartureCity, Tour

Cruise: CruiseRegion, CruisePort, CruiseTour

Core: Banner, FAQ

Tour 使用 JSONField 儲存多語內容（title, desc, faq）

Admin

Tours / Cruise Admin 設定完成（list_display, filter, search）

根據 tour_type 顯示不同欄位

OpenCC 繁簡自動轉換

會員系統 (accounts)

已導入 django-allauth

登入 / 登出 / 註冊 / Dashboard 基本頁

首頁 (home.html)

結構已建立（Banner + FAQ + Tours + Cruise）

Navbar / Footer partials

Hero Swiper 區塊（待補圖）

熱門目的地 demo icon

🚧 進行中 / 待完成

翻譯檔補齊 → 實際填入文字，執行 compilemessages。

語言前綴擴展 → Tours 與 Cruise app 也要支援 /tw/tours/、/cn/cruise/。

Navbar 語言切換 → 改為 <a href="/tw/">繁體</a> 類型，避免 form+csrf。

首頁 Hero → 加假圖 or 後台 Banner 管理。

搜尋功能

Tours: /tours/search/ → tours/search_results.html

Cruise: /cruise/search/ → cruise/search_results.html

Orders 模組（尚未建立）

訂單 model（含語言欄位）

PDF 匯出（WeasyPrint）

Email 通知

SEO

sitemap.xml

canonical / hreflang

快取清理 script（PowerShell & Linux 指令保留）

專案文件化 → 把這份 PROJECT_NOTES.md 固定放根目錄，每次開發日追加。

⏭️ 建議立即動作（修復首頁用）

python manage.py makemessages -l zh_Hant -l zh_Hans -l en
→ 補齊翻譯檔，然後 compilemessages。

修改 navbar.html → 使用 /tw/ /cn/ /en/ 超連結切換語言。

在 home.html → include partials/search_box_tabs.html，測試 Tabs 切換。

在 core/views.py 的 home 加上：

from tours.models import Tour
from cruise.models import CruiseTour

def home(request, lang_code=None):
    banners = Banner.objects.all()
    faqs = FAQ.objects.all()
    tours = Tour.objects.all()[:6]
    cruises = CruiseTour.objects.all()[:6]
    return render(request, "home.html", {
        "banners": banners,
        "faqs": faqs,
        "tours": tours,
        "cruises": cruises,
    })


→ 這樣首頁能顯示資料，不會空白。

📌 更新紀錄（建議寫入 NOTES.md）
# EastUSATours — 更新紀錄 (2025-09-27)

## 🌍 國際化 (i18n)
- 語言策略最終定案：使用 URL 前綴 `/tw/`, `/cn/`, `/en/`
- `settings/base.py` 已更新：
  - `LANGUAGES = [("tw", "繁體中文"), ("cn", "简体中文"), ("en", "English")]`
  - `LANGUAGE_CODE = "tw"`
  - `LOCALE_PATHS = [BASE_DIR / "locale"]`
- 刪除舊的 `zh_Hant`, `zh_Hans` locale 資料夾
- 新建 `locale/tw`, `locale/cn`, `locale/en`
  - 每個語言有乾淨的 `django.po`
  - `compilemessages` 成功，生成 `.mo`

## 🖼️ Templates
- 拆分結構：


templates/
├─ base.html
├─ home.html
└─ partials/
├─ navbar.html
├─ footer.html
├─ lang_switch.html
├─ search_box_tabs.html
├─ tours_search_box.html
└─ cruise_search_box.html

- `base.html`：框架 (含 `{% block content %}`, 引入 navbar/footer)
- `home.html`：首頁，include 搜尋器與熱門行程
- `navbar.html`：已完成語言切換（使用 `lang_switch.html`）
- `footer.html`：翻譯化（{% trans %}），不包含語言切換
- `search_box_tabs.html`：分為 Tours 與 Cruise，include 對應 search box

## 🗄️ Models
- Tours
- `Tour` (待改為多語模型)
- `DepartureRegion`, `DepartureCity`
- Cruise
- `Cruise` (待改為多語模型)
- `CruiseCompany`
- `DeparturePort`
- 後台動態內容（Tour/Cruise 的名稱、描述）將走 **多語欄位 / django-parler**

## 🔧 待辦
1. 改造 `Tour` 與 `Cruise` 模型 → 支援多語 (建議用 django-parler)
2. Admin 後台優化 → 多語 Tab 輸入
3. 完成 `home.html` 最終穩定版（已對齊 partials 與 i18n）
4. 建立前台動態內容頁 (list/detail) → 測試多語資料正確顯示


👉 你要不要我幫你 直接輸出一份完整的 PROJECT_NOTES.md 最新版（包含這些更新），讓你直接下載覆蓋？
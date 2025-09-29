第一部分：專案根目錄 (project root)
eastusatours-bup-09272025/
├── accounts/                 # 使用者帳號 / 認證模組
├── core/                     # 專案核心，常用 view, model（首頁可能在這裡）
├── cruise/                   # 郵輪模組
├── eastusatours/             # 專案主設定 (settings, urls, wsgi, asgi)
├── locale/                   # 語言翻譯檔 (tw, cn, en)
├── registration/             # 使用者註冊模組
├── scripts/                  # 自動化腳本 (可能做資料匯入、工具)
├── static/                   # 靜態檔案 (css, js, images)
├── statistics/               # 統計相關模組
├── templates/                # HTML 模板
├── tours/                    # 旅遊行程模組
├── manage.py                 # Django 入口
└── requirements.txt?         # (如果有) Python 套件需求

第二部分：eastusatours/ 主設定
eastusatours/
├── __init__.py                # 啟動設定，判斷 local / production
├── asgi.py                    # ASGI 入口
├── wsgi.py                    # WSGI 入口
├── urls.py                    # URL 路由總入口 (會引用 core, cruise, tours 等)
└── settings/                  # 設定檔目錄
    ├── __init__.py            # 選擇載入 local 或 production
    ├── base.py                # 共用設定 (INSTALLED_APPS, MIDDLEWARE, 語言, DB)
    ├── local.py               # 開發用，import base
    └── production.py          # 上線用，import base
    📌 引用關係：

manage.py 啟動 → eastusatours/settings/__init__.py → 載入 base + local/production。

urls.py → 指到各 app (core/urls.py, cruise/urls.py, tours/urls.py)。

語言設定 (LANGUAGES, LOCALE_PATHS) 在 base.py，會連到 locale/。

📂 accounts/ 結構
accounts/
├── __init__.py               # 標記為 Python 模組，通常沒內容
├── admin.py                  # 註冊 models 到 Django 後台 (會連到 models.py)
├── apps.py                   # 定義 AppConfig，會被 settings.INSTALLED_APPS 引用
├── forms.py (如果有)          # 使用者註冊 / 登入表單 (會被 views.py 用到)
├── migrations/               # 資料庫遷移檔，和 models.py 對應
│   ├── __init__.py
│   └── 0001_initial.py       # 初始 migration，建 user 資料表
├── models.py                 # 定義 User 擴充（Profile?），會連 MySQL
├── tests.py                  # 測試用，非必要
├── urls.py (如果有)           # 帳號相關路由，例如 /login /logout
└── views.py                  # 控制邏輯，可能處理登入 / 註冊 / 登出

🔗 引用關係

models.py → MySQL

定義使用者資料表（可能有 Profile、會員資訊）。

會自動對應到 migrations/，產生資料表。

admin.py

引用 models，把帳號資料放到 Django Admin 後台管理。

views.py

接收 urls.py 的請求（例如 /login/）。

可能會用到 forms.py 來驗證使用者輸入。

urls.py (如果有)

被 eastusatours/urls.py include，負責帳號模組的路由。

migrations/

Django 建表時產生的紀錄，一定要保留，因為這跟 MySQL 資料庫結構同步。

✅ 結論：accounts/ 這個 app 和 MySQL 後台資料 直接相關（會員系統）。
→ 必須保留 models.py, migrations/, admin.py
→ tests.py 可以不管，forms.py 要看有沒有實作。

📂 core/ 結構
core/
├── __init__.py               # 標記為 Python 模組
├── admin.py                  # 把 Core 裡的 models (FAQ, Banner) 註冊到後台
├── apps.py                   # 定義 CoreConfig，會被 INSTALLED_APPS 使用
├── context_processors.py     # 提供全域變數給 templates (例如 request.lang_prefix)
├── migrations/
│   ├── __init__.py
│   └── 0001_initial.py       # 建立 FAQ / Banner 資料表
├── models.py                 # 定義 FAQ, Banner (跟 MySQL 連動)
├── urls.py                   # 定義 core app 的 URL (首頁, FAQ 頁)
├── views.py                  # 控制邏輯，回傳首頁、FAQ
└── templates/
    └── core/
        ├── home.html         # 首頁 (會 include partials/search_box_tabs.html)
        ├── faq.html          # FAQ 頁
        └── partials/
            ├── navbar.html   # 導覽列 (base.html include)
            ├── footer.html   # 頁腳
            ├── lang_switch.html # 語言切換 (navbar include)
            └── search_box_tabs.html

🔗 引用關係

models.py (FAQ, Banner)

和 MySQL 直接綁定。

有對應 migrations/0001_initial.py。

在 admin.py 註冊 → 可以在後台管理 Banner / FAQ。

views.py

定義首頁 home(request, lang_code=None)。

FAQ 頁也可能從這裡出來。

會用到 core/templates/core/home.html。

urls.py

提供 / (首頁)、/faq/ 這些路徑。

被 eastusatours/urls.py include。

context_processors.py

提供 request.lang_prefix 給 templates 用。

在 settings/base.py → TEMPLATES → OPTIONS.context_processors 設定引用。

重要：語言切換靠它運作。

templates/core/

home.html → 首頁 UI，會 include partials/

partials/navbar.html → base.html 會 include

partials/footer.html → base.html 會 include

partials/lang_switch.html → navbar 會 include

partials/search_box_tabs.html → home.html 會 include

✅ 結論

跟 MySQL 有關：models.py, migrations/, admin.py（FAQ, Banner）。

前端 UI：templates/ 下的所有東西，只透過 views.py render。

語言系統：context_processors.py + lang_switch.html → 必須保留。

📂 cruise/ 結構
cruise/
├── __init__.py
├── admin.py                  # 註冊 Cruise models (公司、港口、行程) 到後台
├── apps.py                   # CruiseConfig，會被 INSTALLED_APPS 使用
├── migrations/
│   ├── __init__.py
│   └── 0001_initial.py       # 建立郵輪資料表
├── models.py                 # 定義郵輪公司、港口、郵輪行程
├── urls.py                   # /cruise/ 底下的路由 (list, detail)
├── views.py                  # 控制邏輯，渲染 list.html / detail.html
└── templates/
    └── cruise/
        ├── list.html         # 郵輪清單頁
        └── detail.html       # 郵輪詳情頁

🔗 引用關係

models.py

會有像：

class CruiseCompany(models.Model): ...
class CruisePort(models.Model): ...
class Cruise(models.Model): ...


直接連 MySQL，必須保留。

admin.py

註冊上述 models → 後台可以管理郵輪公司、出發港口、郵輪行程。

migrations/

和 models.py 對應，建表紀錄。

一定要保留，跟 MySQL 同步。

views.py

提供 /cruise/ 清單頁（list.html）、詳情頁（detail.html）。

會讀取 models.py 內容（例如 Cruise.objects.all()）。

urls.py

定義 /cruise/list/ /cruise/<id>/ 之類的路由。

被 eastusatours/urls.py include。

templates/cruise/

list.html → 郵輪清單頁

detail.html → 郵輪詳情頁

這些會被 views.py render。

✅ 結論

必須保留 (跟 MySQL 直連)

models.py, migrations/, admin.py

前端頁面

templates/cruise/

views.py（負責 render）

引用鏈

eastusatours/urls.py → cruise/urls.py → cruise/views.py → templates/cruise/*.html

📂 tours/ 結構
tours/
├── __init__.py
├── admin.py                  # 註冊 Tour models (地區、城市、行程) 到後台
├── apps.py                   # ToursConfig，會被 INSTALLED_APPS 使用
├── migrations/
│   ├── __init__.py
│   └── 0001_initial.py       # 建立 tour 資料表
├── models.py                 # 定義 Tour, DepartureRegion, DepartureCity 等
├── urls.py                   # /tours/ 底下的路由 (list, detail)
├── views.py                  # 控制邏輯，渲染 list.html / detail.html
└── templates/
    └── tours/
        ├── list.html         # 行程清單頁
        └── detail.html       # 行程詳情頁

🔗 引用關係

models.py

會有像：

class DepartureRegion(models.Model): ...
class DepartureCity(models.Model): ...
class Tour(models.Model): ...


這些直接對應 MySQL 資料表。

Tour 會有 FK 關聯到 DepartureCity。

admin.py

註冊上述 models → 後台可以新增/編輯行程。

migrations/

建表紀錄，必須保留，和 MySQL 同步。

views.py

提供 /tours/ 清單頁、詳情頁。

會查詢 Tour.objects.filter(...) → render 到模板。

urls.py

定義 /tours/list/ /tours/<id>/。

被 eastusatours/urls.py include。

templates/tours/

list.html → 行程清單頁

detail.html → 行程詳情頁

和 views.py 搭配顯示。

✅ 結論

必須保留 (跟 MySQL 綁定)

models.py, migrations/, admin.py

前端頁面

templates/tours/（清單 / 詳情）

引用鏈

eastusatours/urls.py → tours/urls.py → tours/views.py → templates/tours/*.html

📂 templates/ 結構
templates/
├── base.html                  # 全域基底模板，其他頁面都會 extend
└── partials/
    ├── navbar.html            # 導覽列，base.html include
    ├── footer.html            # 頁腳，base.html include
    ├── lang_switch.html       # 語言切換 (包含 /tw /cn /en)
    ├── tours_search_box.html  # 行程搜尋表單 (home.html include)
    └── cruise_search_box.html # 郵輪搜尋表單 (home.html include)

🔗 引用關係

base.html

所有頁面 extends "base.html"。

會 include partials/navbar.html & partials/footer.html。

partials/navbar.html

引用 partials/lang_switch.html。

連到 /tours/, /cruise/。

partials/footer.html

版權、公司資訊。

使用 {% trans %}，跟 locale/ 翻譯檔有關。

partials/lang_switch.html

用 request.lang_prefix 產生 /tw /cn /en 語言切換網址。

partials/tours_search_box.html

搜尋條件：出發城市、目的地、日期、促銷、關鍵字。

用在首頁 home.html。

partials/cruise_search_box.html

搜尋條件：公司、地區、港口、月份、中文導遊、特價。

用在首頁 home.html。

📂 locale/ 結構
locale/
├── tw/
│   └── LC_MESSAGES/
│       ├── django.po          # 繁體中文翻譯檔
│       └── django.mo          # 編譯後的翻譯檔
├── cn/
│   └── LC_MESSAGES/
│       ├── django.po          # 簡體中文翻譯檔
│       └── django.mo
└── en/
    └── LC_MESSAGES/
        ├── django.po          # 英文翻譯檔
        └── django.mo

🔗 引用關係

django.po

{% trans "文字" %} 的翻譯會存這裡。

修改後要跑：

django-admin makemessages -l tw -l cn -l en
django-admin compilemessages


編譯成 .mo 供 Django 使用。

settings/base.py

設定：

LOCALE_PATHS = [BASE_DIR / "locale"]
LANGUAGES = [
    ("tw", "Traditional Chinese"),
    ("cn", "Simplified Chinese"),
    ("en", "English"),
]


這會連動 locale/。

✅ 結論

templates/ → 前端骨架（base, partials, 搜尋框）。

locale/ → 語言翻譯檔，跟 .po/.mo + {% trans %} 連動。

這部分跟 MySQL 沒有直接關聯，但跟 i18n 多語系顯示 完全綁定。

📂 registration/ 結構
registration/
├── __init__.py
├── admin.py                  # 如果有自訂註冊模型，會放這裡
├── apps.py                   # RegistrationConfig
├── migrations/
│   ├── __init__.py
│   └── 0001_initial.py       # 若有自訂資料表
├── models.py                 # 註冊相關資料表 (如果有自訂)
├── urls.py                   # 註冊相關路由 (/signup/ /activate/)
├── views.py                  # 註冊流程控制
└── templates/
    └── registration/
        ├── login.html
        ├── signup.html
        ├── password_reset.html
        └── ...

🔗 引用關係

urls.py

被 eastusatours/urls.py include，提供 /accounts/login/、/accounts/signup/。

views.py

登入/註冊表單處理。

如果有用 Django 內建 auth，這裡會覆寫部分流程。

templates/registration/

Django 規定放在這個目錄下，登入註冊畫面會自動找這裡。

📌 跟 MySQL 的關聯：

如果只用 Django 內建 User → 這裡只是前端模板，不直接建表。

如果有自訂 models.py → 就會跟 DB 連動。

📂 statistics/ 結構
statistics/
├── __init__.py
├── admin.py                  # 後台數據管理
├── apps.py                   # StatisticsConfig
├── migrations/
│   ├── __init__.py
│   └── 0001_initial.py       # 統計資料表
├── models.py                 # 定義報表 / 日誌 / 統計數據
├── urls.py                   # /statistics/ 底下的路由
├── views.py                  # 提供報表 API 或頁面
└── templates/
    └── statistics/
        └── dashboard.html     # 可能的報表頁面

🔗 引用關係

models.py

可能會有像：

class PageVisit(models.Model): ...
class BookingReport(models.Model): ...


直接跟 MySQL 綁定。

views.py

提供數據給前端圖表。

或輸出成報表頁。

templates/statistics/

前端頁面 (dashboard, charts)。

📌 跟 MySQL 的關聯：

一定有資料表（統計數據）。

必須保留 models.py + migrations/ + admin.py。

✅ 結論

registration/ → 偏 UI/流程，除非有自訂 models，不然 MySQL 依賴不大。

statistics/ → 偏後台數據，MySQL 依賴很大（要留）。

📂 scripts/

這通常是放工具腳本（不直接跟網站功能連動）。

scripts/
├── __init__.py              # 標記為模組
├── cache_clear.py           # 清快取（可能清 Redis 或 Django cache）
├── import_tours.py          # 匯入 tours 資料（txt → MySQL）
├── import_cruise.py         # 匯入 cruise 資料
└── utils.py                 # 通用工具方法

🔗 引用關係

import_tours.py / import_cruise.py

會讀像你提供的 tours分類出發名字.txt / 郵輪出發名港口.txt。

然後寫進 MySQL (Tour, CruisePort 等 models)。

屬於「一次性工具」，正式網站不一定需要。

cache_clear.py

可能會在部署時用，清除舊快取。

📌 結論：

開發/部署用，不是網站主要功能。

可以保留，但不需要跟 i18n 或前端結合。

📂 static/

這是前端靜態資源。

static/
├── css/
│   └── style.css             # 全站樣式 (可能是 Tailwind build 出來的)
├── js/
│   └── main.js               # 全站 JavaScript
└── images/
    ├── logo.png
    ├── icon_cruise.png
    ├── icon_us.png
    ├── icon_canada.png
    ├── icon_europe.png
    ├── icon_asia.png
    ├── icon_custom.png
    ├── icon-email.png
    ├── icon-fb.png
    └── icon-whatsapp.png

🔗 引用關係

logo.png → navbar.html

icon_*.png → navbar 分類用圖示

icon-email.png, icon-fb.png, icon-whatsapp.png → footer 聯絡資訊

style.css, main.js → base.html 會 {% load static %} 引用

📌 結論：

全部都是前端用，跟 MySQL 無關。

必須保留，否則 UI 會壞掉。

✅ 這樣整個專案目錄 已經完全展開 了。
下一步就是你要的 第二階段：檢查 & 報告：

哪些檔案 必須保留（因為跟 MySQL / 後台連動）。

哪些檔案 是前端 UI（templates, static, locale）。

哪些檔案 可以算工具/非必要（scripts, tests.py）。

哪些可能是 多餘/要刪的（如果有舊版 home.html 或 duplicate partials）。

📑 EastUSATours 檔案檢查 & 後台資料庫連動報告
1️⃣ 必須保留（跟 MySQL/後台強烈綁定）

這些檔案定義了資料表結構、管理介面，刪掉會導致 DB/後台壞掉：

*/models.py → 定義資料表 (Tour, Cruise, FAQ, Banner, User, Statistics)

*/migrations/ → 建表紀錄，必須保留，否則 migrate 會錯誤

*/admin.py → 把 models 註冊到後台

eastusatours/settings/base.py → DB 設定、i18n 設定

eastusatours/settings/local.py / production.py → 啟動時載入不同 DB

eastusatours/urls.py → 總路由

accounts/ → 會員系統，登入註冊必須要有

core/models.py → Banner/FAQ 資料

tours/models.py → DepartureRegion, DepartureCity, Tour

cruise/models.py → CruiseCompany, CruisePort, Cruise

statistics/models.py → 報表 / 日誌

📌 結論：這些檔案是「後台 + MySQL 基石」，一定要留。

2️⃣ 前端 UI（顯示層，不直接跟 MySQL 互動）

這些檔案只負責顯示內容，刪掉不會壞資料庫，但網站會沒畫面：

templates/base.html

templates/partials/navbar.html

templates/partials/footer.html

templates/partials/lang_switch.html

templates/partials/tours_search_box.html

templates/partials/cruise_search_box.html

core/templates/core/home.html

core/templates/core/faq.html

tours/templates/tours/list.html / detail.html

cruise/templates/cruise/list.html / detail.html

statistics/templates/statistics/dashboard.html

static/css/style.css

static/js/main.js

static/images/*

📌 結論：純前端 UI，用 {% trans %} 時會依賴 locale。

3️⃣ 語言與翻譯（i18n 系統）

這些是 Django 語言切換的基礎，刪掉會失去多語系：

locale/tw/LC_MESSAGES/django.po / django.mo

locale/cn/LC_MESSAGES/django.po / django.mo

locale/en/LC_MESSAGES/django.po / django.mo

core/context_processors.py → 提供 request.lang_prefix 給 templates

middleware/LocaleFromPathMiddleware（應該在 settings 裡定義）

📌 結論：必須保留，否則 /tw /cn /en 語言網址會壞掉。

4️⃣ 工具/非必要檔案

這些檔案不是主流程，刪掉不會壞核心，但可能會失去輔助功能：

scripts/import_tours.py → 匯入 tours 資料（txt → MySQL）

scripts/import_cruise.py → 匯入 cruise 資料

scripts/cache_clear.py → 清快取工具

*/tests.py → 測試程式，不影響正式功能

📌 結論：可選保留。建議留著以防之後需要批次匯入。

✅ 總結

跟後台 + MySQL 綁定的核心檔案：models.py, migrations/, admin.py, settings/, urls.py

前端 UI：templates/, static/

語言系統：locale/, context_processors.py

非必要工具：scripts/, tests.py

🗂️ EastUSATours 首頁修復與專案整理計畫 — 執行檢查清單
1️⃣ 首頁 Routing 檢查

 /tw/, /cn/, /en/ → 要能正確 render home.html
→ 目前只支援 /zh-hant/, /zh-hans/, /en/，所以 /tw/、/cn/ 要 redirect。

 urls.py → views.py → templates/home.html 流程確認。

 修復首頁：確保不再使用 home_guest.html / home_member.html。

👉 下一步工作：
我建議直接改 urls.py 加上 /tw/ → /zh-hant/，/cn/ → /zh-hans/ 的 redirect。

2️⃣ Navbar / Footer / 語言切換

 partials/navbar.html 與 partials/footer.html 有正常 include。

 partials/lang_switch.html 按鈕能正確切換 /tw/, /cn/, /en/。

 確保語言切換連結與 urls.py 定義一致。

👉 下一步工作：
檢查 lang_switch.html 裡的連結，目前應該要改成 /tw/, /cn/, /en/，並且測試 redirect 是否正確。

3️⃣ Templates 整理

 home.html 要統一，避免跟 home.code.txt、core/home.html 打架。

 確認 partials 分工：

partials/search_box_tabs.html

partials/tours_search_box.html

partials/cruise_search_box.html

👉 下一步工作：
刪掉或註解掉舊的 core/home.html，讓唯一首頁就是 templates/home.html。

4️⃣ 資料庫串接 (MySQL)

 python manage.py makemigrations && migrate → 確保 Tours / Cruise / Accounts 建好。

 Admin 可管理 Tours, Cruise, FAQ, Banner。

 首頁搜尋 <select> 下拉選單要能正確讀取 DB（例如目的地、出發地）。

👉 下一步工作：
測試 admin/ → 新增一筆 Tour / Cruise，看首頁是否顯示。

5️⃣ Accounts (會員系統)

 Allauth 登入/註冊 → 確認 templates/account/。

 自訂會員專區 templates/accounts/（dashboard, profile, orders）。

 移除舊的 templates/auth/（避免混淆）。

👉 下一步工作：
先測試 /accounts/login/ /accounts/signup/ 是否能正確進入。

6️⃣ 部署準備

 本地測試 /tw/ /cn/ /en/ 首頁正常顯示。

 push GitHub。

 Render 部署（先 SQLite，再 MySQL）。

 測試雲端 /tw/ /cn/ /en/ 正常運作。

👉 下一步工作：
本地確認首頁 → push GitHub → 部署到 Render（用 SQLite 測）。

✅ 總結：目前要做的

修復 Routing

/tw/ → /zh-hant/

/cn/ → /zh-hans/

/en/ → /en/

確認首頁顯示

urls.py → views.py → home.html 串接正確

Navbar/Footer/語言切換 正常

清理 Templates

移除舊的 home_guest.html / home_member.html / core/home.html

🔍 確認點補充 1️⃣ Routing 修復 現況：Django 自帶的語言代碼是 zh-hant / zh-hans / en 需求：你要 /tw/、/cn/，所以要 redirect。 👉 做法： 在 urls.py 最上層加： from django.shortcuts import redirect urlpatterns = [ path("tw/", lambda request: redirect("/zh-hant/")), path("cn/", lambda request: redirect("/zh-hans/")), path("en/", lambda request: redirect("/en/")), ] 這樣 /tw/ /cn/ /en/ 都會正確轉向。 2️⃣ Navbar / Footer / 語言切換 確保 partials/lang_switch.html 按鈕用 /tw/ /cn/ /en/，而不是 /zh-hant/。 點擊後，實際會 redirect 到正確語系頁面。 👉 測試方式： 點一下 navbar 的語言按鈕，看 URL 有沒有變成 /tw/ 並成功進首頁。 3️⃣ Templates 整理 目前重複的有： home.html（主模板） core/home.html（舊版） home_guest.html、home_member.html（切割過） 👉 要留下的只有： ✅ templates/home.html 其它（core/home.html, home_guest.html, home_member.html）可以移除或註解掉，避免打架。 4️⃣ 資料庫串接 (MySQL) 測試指令： python manage.py makemigrations python manage.py migrate python manage.py createsuperuser 登入 /admin/ → 新增一筆 Tour、Cruise，回首頁看 <select> 有沒有更新。 5️⃣ Accounts 測試： /accounts/login/ → allauth login /accounts/signup/ → allauth signup /accounts/profile/ → 應該 redirect 到 dashboard（需要設定 LOGIN_REDIRECT_URL = "/accounts/dashboard/"）。 6️⃣ 部署準備 本地跑通 → push GitHub Render 部署時，建議先 SQLite（不用設定 MySQL） → 確保首頁能跑。 成功後再加 MySQL（Render Database 或外部連線）。 ✅ 總結： 你的整理完全正確 → 現在的優先就是 Routing + 首頁顯示，確認能跑，再處理 DB 與部署。 我們補充之後 開始
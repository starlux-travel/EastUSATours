EastUSATours — POR v2.1（MVP 多語 + 會員整合）

專案任務清單（含設定檔與 Git 管理）

最後更新：2025-09-13

✅ 目前狀態快照

Templates 統一放在 templates/

首頁 統一用 templates/home.html（已去除 guest/member 分頁）

會員系統：採用 django-allauth（登入/登出/註冊/重設密碼）

Settings 分流：eastusatours/settings/

**init**.py（依 DJANGO_ENV 讀取）

base.py（共用設定）

local.py（本機）

production.py（雲端）

多語：UI 用 {% trans %}（.po/.mo），商品內容之後用 JSON 欄位

Git：已初始化（需確保 Render 連的是最新 Git 分支）

Render：已連線，但上一次部署使用了舊快照 → 需重新部署最新 commit

🧱 專案結構（目錄樹）
eastusatours/ # 根目錄
├─ accounts/ # 會員 App（allauth 覆寫頁）
│ ├─ templates/accounts/
│ │ ├─ login.html
│ │ ├─ logout.html
│ │ ├─ password_reset.html
│ │ ├─ dashboard.html
│ │ └─ profile.html
│ ├─ urls.py
│ └─ views.py
├─ tours/ # 行程 App
│ ├─ templates/tours/
│ │ ├─ search_results.html
│ │ └─ tour_detail.html
│ ├─ urls.py
│ └─ views.py
├─ eastusatours/ # 主專案
│ ├─ settings/
│ │ ├─ **init**.py # 依 DJANGO_ENV 載入 local/production
│ │ ├─ base.py # 共用設定（apps、templates、i18n…）
│ │ ├─ local.py # 本機環境
│ │ └─ production.py # 雲端環境
│ ├─ urls.py
│ ├─ asgi.py
│ └─ wsgi.py
├─ templates/ # 全站共用
│ ├─ base.html
│ └─ home.html
├─ static/ # collectstatic 產出（雲端）
├─ locale/ # i18n 語系檔（zh_Hant / zh_Hans / en）
├─ requirements.txt
└─ manage.py

🧼 清理完成 / 待移除（避免衝突）

移除 templates/auth/（舊 Django auth 模板）

移除 templates/registration/（舊註冊/密碼頁）

不再使用 home_guest.html、home_member.html（首頁統一 home.html）

頁面中 請統一使用 allauth 路由名稱：

account_login / account_logout / account_signup / account_reset_password

🎨 首頁規劃（home.html）

目標：單一首頁就把價值放到最前面，減少跳轉。

建議區塊：

Hero：品牌標語 + CTA（登入 / 馬上找行程）

快速搜尋：關鍵字 + 類別切換（郵輪｜美東｜美西｜夏威夷）

主打卡片：分區塊載入（可走 API：/api/home_cards?category=cruise）

會員快速入口：登入/註冊，登入後顯示「前往會員中心」

範例（Jinja）：

{% extends "base.html" %}
{% load i18n %}
{% block content %}

<section class="hero">
  <h1>{% trans "歡迎來到 EastUSATours" %}</h1>
  {% if user.is_authenticated %}
    <a href="{% url 'dashboard' %}" class="btn">{% trans "會員中心" %}</a>
  {% else %}
    <a href="{% url 'account_login' %}" class="btn">{% trans "登入" %}</a>
    <a href="{% url 'account_signup' %}" class="btn btn-secondary">{% trans "註冊" %}</a>
  {% endif %}
</section>

<section class="cruise-tours">
  <h2>{% trans "精選郵輪" %}</h2>
  <a class="btn btn-outline-primary" href="{% url 'tour_list' %}?type=cruise">
    {% trans "查看郵輪行程" %}
  </a>
</section>

<section class="bus-tours">
  <h2>{% trans "巴士團" %}</h2>
  <a class="btn btn-outline-primary" href="{% url 'tour_list' %}?type=bus">
    {% trans "查看巴士行程" %}
  </a>
</section>

{% endblock %}

若頁面仍嘗試 render tours/home_guest.html，請把對應 views.home 改為 render(request, "home.html", context)。

👤 會員系統（django-allauth）

路由名稱（模板要用這些）：

account_login

account_logout

account_signup

account_reset_password

覆寫模板路徑： templates/accounts/…（你已放對）

會員中心：

/accounts/dashboard/ → dashboard.html

/accounts/profile/ → profile.html
（可在 accounts/urls.py 內定義自己的 view 名稱 dashboard / profile）

🌐 URL & 語系
短期（穩定優先）

直接用 /{lang}/… 前綴：/zh-hant/、/zh-hans/、/en/

中介層讀取 lang 設定 translation.activate(lang)，避免 i18n_patterns 造成跳轉混亂

簡易 middleware（擺在自家 middleware.py）

from django.utils import translation

SUPPORTED = {"zh-hant": "zh_Hant", "zh-hans": "zh_Hans", "en": "en"}

class LocaleFromPathMiddleware:
def **init**(self, get_response):
self.get_response = get_response
def **call**(self, request):
lang = request.path.strip("/").split("/", 1)[0].lower()
code = SUPPORTED.get(lang)
if code:
translation.activate(code)
request.LANGUAGE_CODE = code
return self.get_response(request)

settings/base.py 設：

MIDDLEWARE = [

# … 其他 …

"eastusatours.middleware.LocaleFromPathMiddleware", # 放在 Session/Locale 之前
]
LANGUAGES = [
("zh_Hant", "Traditional Chinese"),
("zh_Hans", "Simplified Chinese"),
("en", "English"),
]
LOCALE_PATHS = [BASE_DIR / "locale"]

🧩 Settings 分流（已完成）

eastusatours/settings/**init**.py

讀 DJANGO_ENV（預設 local）→ 匯入 .local 或 .production

base.py：共用 Apps、Templates、i18n、REST、allauth

local.py：Debug=True、SQLite、本機主機名

production.py：dj_database_url、ALLOWED_HOSTS、STATIC_ROOT、（可選）WhiteNoise

本機切換（PowerShell）

$env:DJANGO_ENV="local"
python manage.py runserver

雲端（Render）

DJANGO_ENV=production
SECRET_KEY=xxxx
ALLOWED_HOSTS=your-service.onrender.com,www.eastusastours.com
DATABASE_URL=postgres://...
PYTHON_VERSION=3.11.x # 依 requirements

🧪 開發用指令

# 建置 / 遷移

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 語系

django-admin makemessages -l zh_Hant -l zh_Hans -l en
django-admin compilemessages

# 本機啟動

python manage.py runserver

🔧 Git 與 Render 部署
Git 基本
git add -A
git commit -m "POR v2.1: unify home, allauth templates, settings split, i18n hooks"
git push origin main

Render（建議設定）

Environment: Python 3

Build Command:

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

Start Command（ASGI 建議）:

gunicorn eastusatours.asgi:application -k uvicorn.workers.UvicornWorker

環境變數（最低需求）:

DJANGO_ENV=production

SECRET_KEY=…

DATABASE_URL=…

ALLOWED_HOSTS=your-render-subdomain.onrender.com,www.eastusastours.com

若 Render 顯示舊畫面：請確定 已 push 最新 commit 並在 Render Redeploy（必要時 Clear build cache）。

📋 任務清單（POR v2.1）
A. 系統基礎建設（路由與語系）

固定 URL 前綴 /zh-hant/、/zh-hans/、/en/

自訂 LocaleFromPathMiddleware（上方程式）

建立/整理 .po/.mo（locale/）

get_lang_field() helper（之後 Tour JSON 欄位用）

B. 首頁與前台（single home）

移除 guest/member 分頁，統一 home.html

補上搜尋欄位 + 主要類別 CTA 區

API endpoint 草稿 /api/home_cards?category=...（可選）

C. 會員中心 /accounts/

導入 allauth，模板覆寫 templates/accounts/…

Dashboard / Profile 基本頁

Orders 頁（串真實資料）

Order.language（下單時保存語系）

D. 後台管理（Admin）

Tour 模型加多語 JSON 欄位（title/desc/faq）

Admin 表單：tab/折疊切語系

一鍵「繁 → 簡」按鈕（OpenCC/GPT）

E. 行程詳情頁

SEO 友善網址 /NY/east-usa/new-york-6787719/

短碼 /p/{CODE}/ → 301 到 canonical

選日 → /api/departure/{id}/pickups/

F. 通知 & PDF

信件樣板（繁／簡／英）

PDF（WeasyPrint）依 order.language 套版

G. SEO & Sitemap

canonical 與 hreflang

sitemap.xml（3 語）

fallback：缺語言 → 顯示繁中

🧭 Sprint 建議順序（下一輪）

語系中介層 / 固定 /zh-hant 等路由

首頁完成版（Hero + 搜尋 + 類別 CTA + 卡片）

Tour 模型多語 JSON + Admin 編輯 UI

詳情頁與 /p/ 短碼導向

Orders 模組（model、列表、PDF、通知信）

SEO（sitemap、canonical、hreflang）

🛠️ 常見錯誤排查

TemplateDoesNotExist: tours/home_guest.html
→ 某處仍 render 舊檔名。請把 views.home 改成：
return render(request, "home.html", context)

NoReverseMatch: account_login
→ 仍用到舊 Django auth 的名稱，請改用 allauth 名稱：
account_login / account_logout / account_signup / account_reset_password

Render 顯示舊版
→ 沒有 push 最新 commit 或 Render 連錯分支；在 Render 後台 Redeploy latest（必要時 Clear build cache）。
EastUSATours — POR v2.1（MVP 多語 + 會員整合）
📊 進度追蹤（POR v2.1）

Templates 統一（guest/member 移除 → home.html） — 完成：2025-09-13

accounts → django-allauth 導入（login/logout/signup/reset/dashboard/profile） — 完成：2025-09-13

Settings 分流（base/local/production） — 完成：2025-09-13

語系中介層（LocaleFromPathMiddleware / 固定 /zh-hant/ /zh-hans/ /en/ 路由）

首頁完成版（Hero、搜尋、主要類別 CTA、卡片 API）

Tour 模型多語 JSON 欄位 + Admin 編輯 UI

行程詳情頁（SEO 友善網址 + 短碼 /p/ 導向）

Orders 模組（model、列表、PDF、Email 通知）

SEO（sitemap、canonical、hreflang、fallback）

# EastUSATours — POR v2.1（MVP 多語 + 會員整合）

## 📊 進度追蹤（POR v2.1）

- [~] 會員系統（allauth：登入/註冊/登出/重設密碼/會員中心/dashboard/profile）  
  → 已導入 allauth，模板搬到 `templates/accounts/`，但 Dashboard/Profile 未完成、舊流程需清理
- [~] Templates 統一（guest/member → home.html）  
  → 已移除 guest/member 首頁，home.html 可用，但搜尋欄位、主打卡片未加
- [~] Settings 分流（base/local/production）  
  → 已分檔，可在本機使用，但 production 尚未完整測試
- [~] Git / Render 部署  
  → Git 初始化、Render 已連線，但目前仍是舊快照，需 redeploy 最新 commit
- [~] Tour 模型（多語欄位 + tour_type）  
  → 模型已加欄位，但 Admin JSON 編輯、多語顯示未完成

- [ ] 語系中介層（LocaleFromPathMiddleware / 固定 /zh-hant/ /zh-hans/ /en/ 路由）
- [ ] 首頁完成版（Hero、搜尋、主要類別 CTA、卡片 API）
- [ ] 行程詳情頁（SEO 友善網址 + 短碼 /p/ 導向）
- [ ] Orders 模組（model、列表、PDF、Email 通知）
- [ ] SEO（sitemap、canonical、hreflang、fallback）

---

EastUSATours — POR v2.1（MVP 多語 + 會員整合）

專案任務清單（含設定檔與 Git 管理）

最後更新：2025-09-13

✅ 目前狀態快照

Templates 統一放在 templates/

首頁 統一用 templates/home.html（已去除 guest/member 分頁）

會員系統：採用 django-allauth（登入/登出/註冊/重設密碼）

Settings 分流：eastusatours/settings/

**init**.py（依 DJANGO_ENV 讀取）

base.py（共用設定）

local.py（本機）

production.py（雲端）

多語：UI 用 {% trans %}（.po/.mo），商品內容之後用 JSON 欄位

Git：已初始化（需確保 Render 連的是最新 Git 分支）

Render：已連線，但上一次部署使用了舊快照 → 需重新部署最新 commit

🧱 專案結構（目錄樹）
eastusatours/ # 根目錄
├─ accounts/ # 會員 App（allauth 覆寫頁）
│ ├─ templates/accounts/
│ │ ├─ login.html
│ │ ├─ logout.html
│ │ ├─ password_reset.html
│ │ ├─ dashboard.html
│ │ └─ profile.html
│ ├─ urls.py
│ └─ views.py
├─ tours/ # 行程 App
│ ├─ templates/tours/
│ │ ├─ search_results.html
│ │ └─ tour_detail.html
│ ├─ urls.py
│ └─ views.py
├─ eastusatours/ # 主專案
│ ├─ settings/
│ │ ├─ **init**.py # 依 DJANGO_ENV 載入 local/production
│ │ ├─ base.py # 共用設定（apps、templates、i18n…）
│ │ ├─ local.py # 本機環境
│ │ └─ production.py # 雲端環境
│ ├─ urls.py
│ ├─ asgi.py
│ └─ wsgi.py
├─ templates/ # 全站共用
│ ├─ base.html
│ └─ home.html
├─ static/ # collectstatic 產出（雲端）
├─ locale/ # i18n 語系檔（zh_Hant / zh_Hans / en）
├─ requirements.txt
└─ manage.py

🧼 清理完成 / 待移除（避免衝突）

移除 templates/auth/（舊 Django auth 模板）

移除 templates/registration/（舊註冊/密碼頁）

不再使用 home_guest.html、home_member.html（首頁統一 home.html）

頁面中 請統一使用 allauth 路由名稱：

account_login / account_logout / account_signup / account_reset_password

🎨 首頁規劃（home.html）

...（以下內容保持不動）

## 2025-09-15 進度

- 首頁大搜尋器（Tab 分類展開式）上線
- tours（美國團）搜尋表單完成（城市/目的地/日期/促銷/關鍵字）
- cruise（郵輪）搜尋表單完成（公司/地區/港口/月/中文導遊/特價）
- 多語支援全部完成，templates 用 {% trans %}，資料動態帶對應語言
- views.py 查詢＋結果卡片頁 OK
  你理想的 Django 專案結構應該像這樣：
  eastusatours/ <-- Django Project
  │
  ├── eastusatours/ <-- 專案設定
  │ └── settings/ <-- settings/base.py, local.py, production.py
  │
  ├── tours/ <-- 美國團 app
  │ ├── models.py
  │ ├── views.py
  │ ├── urls.py
  │ └── templates/
  │ └── tours/ <-- tours/search_results.html ...
  │
  ├── cruise/ <-- 郵輪 app
  │ ├── models.py
  │ ├── views.py
  │ ├── urls.py
  │ └── templates/
  │ └── cruise/ <-- cruise/search_results.html ...
  │
  ├── templates/ <-- 共用模板
  │ ├── base.html
  │ ├── navbar.html
  │ ├── footer.html
  │ └── partials/
  │ ├── search_box_tabs.html
  │ ├── tours_search_box.html
  │ └── cruise_search_box.html
  │
  ├── static/ <-- 靜態資源
  │ └── ...
  │
  ├── manage.py
  │
  └── ...（其他 app/管理工具/requirements.txt）

✅ 這樣分的好處：

tours 跟 cruise 彼此獨立，完全不會互相污染

搜尋條件、樣板、後端查詢邏輯都可以微調

專案升級、分工都方便
你只要確保這幾點就好：

tours app 下有 templates/tours/search_results.html

這個是顯示「搜尋結果」的頁面，不用馬上貼 code，結構對了先過！

cruise app 下有 templates/cruise/search_results.html

郵輪的搜尋結果頁

共用的 partials

templates/partials/ 下有：

search_box_tabs.html（切換分類大搜尋器）

tours_search_box.html（美國團搜尋框）

cruise_search_box.html（郵輪搜尋框）

home.html 正確引入 partials

{% include "partials/search_box_tabs.html" %}

urls.py 結構有分

每個 app 都有自己的 urls.py，然後在主 eastusatours/urls.py 用 include() 對應 path。

🔔 你這樣已經「架構完全正確」！
⏩ 下一步

1. 開始寫搜尋前後端（不用再變動架構）

可以先集中寫 tours，完全穩後再複製一份邏輯到 cruise。

2. 檢查 models & 搜尋欄位設計

等你說「OK，進入前後端搜尋表單+查詢」就給你 sample！

💡 重點提醒

結構對了才不會一直重來

以後每個 app 各自維護、可拓展（要多語就是 template + context 增加 i18n）

大搜尋器 partials 想怎麼排版都可以，前台 UI 再慢慢調
一、專案結構確認（正確！）

你現在的專案結構完全正確，cruise 是獨立 App，tours 也是獨立 App，templates 分層沒問題：

eastusatours/
├── cruise/
│ ├── models.py # 郵輪
│ ├── views.py
│ ├── urls.py
│ └── templates/cruise/
│ ├── cruise_search.html
│ └── cruise_detail.html
├── tours/
│ ├── models.py # 美國團/巴士團
│ ├── views.py
│ ├── urls.py
│ └── templates/tours/
│ ├── search_results.html
│ └── tour_detail.html
├── templates/
│ ├── base.html
│ └── home.html

會員 allauth 覆寫都在 /accounts/

設定檔 /eastusatours/settings/

靜態 /static/

語系 /locale/

這樣完全 OK！可放心繼續！

📌 2025-09-16 ｜前台搜尋表單分類選單後台化 — 流程整理

為了讓 tours（美國團）、cruise（郵輪）搜尋器能夠靈活管理選項，不再依賴硬編碼 <option>，本日任務重點為：

🎯 目標

讓搜尋選單（出發城市、出發區域、港口…）完全由 Django Admin 後台控制，未來行程上架可自由新增或排序。

✅ 一、模型與後台 admin 設定

tours/models.py

class DepartureRegion(models.Model):
name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class DepartureCity(models.Model):
name = models.CharField(max_length=50)
region = models.ForeignKey(DepartureRegion, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

tours/admin.py

from .models import DepartureRegion, DepartureCity

admin.site.register(DepartureRegion)
admin.site.register(DepartureCity)

📌 若為郵輪，可建立 CruiseRegion / CruisePort 於 cruise/models.py。

✅ 二、views 裡加入 context，將分類資料傳入前台 template

# tours/views.py

from .models import DepartureCity

def home(request):
cities = DepartureCity.objects.select_related("region").all()
return render(request, "home.html", {"departure_cities": cities})

📍 若是 cruise 就在 cruise/views.py 使用同邏輯。

✅ 三、partials 搜尋框 template 改為動態載入

<!-- partials/tours_search_box.html -->
<select name="city">
  {% regroup departure_cities by region.name as city_groups %}
  {% for group in city_groups %}
    <optgroup label="{{ group.grouper }}">
      {% for city in group.list %}
        <option value="{{ city.name }}">{{ city.name }}</option>
      {% endfor %}
    </optgroup>
  {% endfor %}
</select>

✅ 可支援城市出發地分組顯示（西岸、東岸…）
✅ 資料來自後台管理，可隨時新增／排序

✅ 四、搜尋邏輯改寫以支援查詢

tours/views.py

def tours_search(request):
city = request.GET.get("city")
queryset = Tour.objects.all()
if city:
queryset = queryset.filter(city\_\_name=city)
return render(request, "tours/search_results.html", {"tours": queryset})

tours/models.py

class Tour(models.Model):
city = models.ForeignKey(DepartureCity, on_delete=models.SET_NULL, null=True)

📌 延伸計畫（未來選配）

支援 JSONField 多語選單名稱

後台可控排序欄位（例如加入 order = models.IntegerField(default=0)）

API endpoint：提供分類資料給前台 JS 使用（如 AJAX 搜尋）

cruise app 同步擴充（類似港口／地區結構）

🔑 以後 New Chat 要這樣說

只要你說這幾句，我就可以 100% 恢復接手：

我們在做 EastUSATours 的 POR v2.1，
搜尋表單的分類選單要改成後台控制，之前做到：

- models.py 裡有 DepartureCity / DepartureRegion
- 後台 admin 可以新增選單
- 搜尋表單要從資料庫撈
- partials 用的是 tours_search_box.html 和 cruise_search_box.html
- 請幫我繼續完成這個流程

🗓️ 2025-09-16 - 首頁 UI 分段實作流程說明（含 tabs 搜尋邏輯）
✅ 1. 首頁 Banner 與 Tabs 選單區（上方）
⛳ 對應 UI 區塊

頁首 tabs：「郵輪」、「美國旅遊」、「加拿大」、「亞洲」等

每一個 tab 下會有不同的搜尋條件表單（見下一步）

📁 前端結構

Partial 放在 templates/partials/navbar.html

搜尋框放在：

partials/cruise_search_box.html

partials/tours_search_box.html

✅ 小結：

每個 tab 切換 = 動態切換 partial 搜尋表單

使用 include + tabs JS 切換即可

✅ 2. 搜尋區塊（Tabs 對應搜尋表單）
⛳ 對應 UI 區塊

預設顯示的搜尋表單（例如亞洲旅遊 / 郵輪）

城市、出發日、關鍵字等欄位

⚙️ 對應後端

每個搜尋表單對應：

views.py > tours_search(request)

views.py > cruise_search(request)

都會渲染到 search_results.html

📁 對應 partials
templates/partials/
├── tours_search_box.html
├── cruise_search_box.html

✅ 3. 限時搶購、特價專區（首頁中段）
⛳ 對應 UI 區塊

搶購專區是即將出發的熱門行程（需從資料庫查出）

⚙️ 後端查詢邏輯

從 Tour 或 CruiseTour 查詢

有促銷標籤

排序依據：出發日 or order 欄位

📁 對應模板

放入 home.html 內，用 for tour in hot_tours 渲染

可呼叫 partials/tour_card.html

✅ 4. 人氣排行區塊
⛳ 對應 UI 區塊

右側顯示點閱高的行程清單

⚙️ 對應邏輯

Tour.objects.order_by('-views')[:5]

可另外設計一個 PopularTourManager 或 flag 欄位

✅ 5. Tabs 內的區塊（像「歐洲旅遊」、「美西經典」）
⚙️ 對應後台欄位

可對應到 TourCategory（旅遊主題分類）

後台分類後，首頁這裡只需 filter 指定類別

✅ 小結：整合後可支援功能
功能 狀態
tabs 切換搜尋框 ✅ 已可切換 partials
旅遊類型分開顯示（Cruise vs Tour） ✅ 分開 app / 搜尋處理
後台可控上下架排序分類 ✅ models 設計已支持
首頁動態渲染資料 ✅ 基本 loop / queryset 架構已可
📌 EastUSATours — POR v2.1 專案進度更新

🗓 更新日期：2025-09-19

✅ 已完成

Cruise 模組

models.py 已調整，city、cruise_ship 允許為可選（blank=True, null=True）。

已建立完整模型：Region / City / CruiseLine / CruiseShip / CruiseTour。

migrations 重新生成並套用。

fixture (cruise_sample.json) 成功匯入，資料庫已含有測試郵輪行程資料。

Accounts

整合 django-allauth，完成登入 / 註冊 / 登出 / 忘記密碼流程。

Templates

首頁模板已統一為 home.html，移除 guest/member 分流。

accounts 模板覆寫完成（login / logout / signup / reset / dashboard / profile）。

Settings

已分離 base.py / local.py / production.py，支援不同環境設定。

Git & Render

Git 初始化完成，Render 已連線，可隨時 redeploy 最新 commit。

🚧 進行中 / 待完成

Admin

Cruise 模組後台管理需優化 → list_display、search_fields、list_filter。

前台

首頁需補 Hero 區塊、搜尋欄位、CTA。

行程詳情頁（tour_detail.html）尚未串接資料。

多語系

.po/.mo 已可用，但 Tour / Cruise 資料的多語支援尚未完成。

Orders 模組

尚未建立（需包含 model、PDF 匯出、Email 通知）。

SEO

sitemap、canonical、hreflang 尚未完成。

🧭 下一步建議

完善 Cruise Admin → 讓管理更直覺。

擴充 fixture → 增加更多行程資料，用來測試搜尋與篩選功能。

補齊首頁 Hero + 搜尋功能。

建立 Orders 模組（含基本訂單流程 + PDF + Email）。

🔍 專案目前狀態（依你昨天、今天的紀錄 + 我讀過的 PROJECT_NOTES.md）

Cruise 模組

✅ models / fixture 已完成

🚧 admin 優化中

Accounts (allauth)

✅ 已整合，登入 / 註冊 / 登出流程正常

🚧 新 middleware AccountMiddleware 已加，但還沒驗證完整登入登出流程

Settings

✅ base / local / production 已分離

✅ INSTALLED_APPS 已補上 tours / cruise / accounts / allauth

✅ Middleware 有 LocaleMiddleware

🚧 需要清掉 i18n_patterns，只保留 gettext + .po/.mo 翻譯

Templates / 首頁

🚨 最大問題 → home.html 沒有正確渲染，語言 & 搜尋框都掛掉

原因：views.home 沒給 context，urls.py 引用錯誤

Tours 模組

🚧 /tours/ 沒有 root index → 404

✅ tour_list / tour_detail 存在

🚧 搜尋 view 還沒接上首頁

SEO / 多語

.po/.mo 已能運作

❌ URL 層級混亂 (i18n_patterns vs middleware)

✅ 要改成只走 middleware，保留 /tours/、/cruise/ 乾淨 URL

🚀 Git + Render 標準部署流程

1. 本機開發

修改程式碼（例如 settings、urls、views、templates）

測試：

python manage.py runserver

確認功能正常（這次重點是 /zh-tw/、/zh-cn/、/en/ 首頁顯示正確）

2. Git 提交

加入所有修改：

git add .

建立提交：

git commit -m "描述修改，例如：修正語言網址，首頁支援 /zh-tw/ /zh-cn/ /en/"

3. Push 到 GitHub

推送到主分支（假設是 main，你的專案若用 master 就改成 master）：

git push origin main

4. Render 自動部署

Render 會偵測到 GitHub 有新 commit，自動 build & deploy

如果有錯誤：

去 Render dashboard → Logs → 看 build log 與 runtime log

大多是 settings、requirements.txt、環境變數 問題

5. 緊急修正流程

發現 bug → 在本機修正 → 重新跑：

git add .
git commit -m "hotfix: 修正 xxx 問題"
git push origin main

Render 會重新部署最新版

# 📌 EastUSATours 專案 Roadmap

## 🎯 專案目標

建立一個支援中/簡/英三語的旅遊網站，提供行程（Tours）、郵輪（Cruise）、訂單（Orders）功能，並整合會員系統、SEO 與多語切換。

---

## ✅ 基礎版本（穩定基準）

### v0.2

- 首頁：`/zh-tw/` `/zh-cn/` `/en/`
- 語言網址固定，不會亂跳 `/zh-hant/`、`/zh-hans/`
- `.po/.mo` 翻譯運作正常
- `home.html` 保留現有設計（Hero、搜尋、區塊）
- Git + Render 自動部署流程測試完成

---

## 🚀 功能模組規劃

### v0.3 — Tours 模組

- Tours 列表 `/zh-tw/tours/`
- Tours 詳細 `/zh-tw/tours/<id>/`
- 支援中/簡/英欄位：`title`、`title_en`
- 後台 admin 優化（list_display、filter、search）

### v0.4 — Search 功能

- 首頁搜尋框可查 Tours / Cruise
- 結果頁顯示多語標題

### v0.5 — Accounts

- 登入 / 註冊 / 登出 / 忘記密碼
- Profile / Dashboard
- 驗證流程測試完成

### v0.6 — Cruise 模組

- Cruise 列表、詳細
- 船隊（CruiseLine）、郵輪（CruiseShip）資料
- Fixture 擴充（多艘船、多筆行程）

### v0.7 — Orders 模組

- 建立訂單 model
- 訂單確認信（Email）
- 訂單 PDF 匯出

### v0.8 — SEO

- sitemap.xml
- canonical tag
- hreflang 設定（/zh-tw/、/zh-cn/、/en/）

---

## 🔒 開發原則

1. **每完成一個功能 → Git commit → Push → Render 自動部署**
2. **每個版本打 Git Tag**
   ```bash
   git tag -a v0.3 -m "Tours 模組完成"
   git push origin v0.3
   不覆蓋現有功能，只在穩定基礎上擴充
   ```

每次部署後測試清單：

/zh-tw/ /zh-cn/ /en/ 首頁正常

Tours list/detail 正常

登入/登出正常

🗂️ Git Commit 規範（建議）

feat: → 新功能 (例：feat: 新增 Tours 詳細頁)

fix: → 修 bug (例：fix: 修正首頁語言切換)

refactor: → 重構，不影響功能 (例：refactor: 重構 admin 顯示)

docs: → 文件 (例：docs: 更新 PROJECT_PLAN.md)

hotfix: → 緊急修正 (例：hotfix: Render 部署錯誤)

⏳ 版本 Roadmap

v0.2 → 首頁 + 語言網址

v0.3 → Tours 模組

v0.4 → Search

v0.5 → Accounts

v0.6 → Cruise

v0.7 → Orders

v0.8 → SEO

---

📌 建議動作：

1. 把這份內容存成 `PROJECT_PLAN.md`
2. Commit 到 Git：
   ```bash
   git add PROJECT_PLAN.md
   git commit -m "docs: 新增專案 Roadmap 計劃"
   git push origin main
   ```

## ✅ 部署必測清單

| 功能區域    | 測試路徑                  | 預期結果                   |
| ----------- | ------------------------- | -------------------------- |
| 首頁 (繁體) | `/zh-tw/`                 | 顯示首頁，標題中文繁體     |
| 首頁 (簡體) | `/zh-cn/`                 | 顯示首頁，標題中文簡體     |
| 首頁 (英文) | `/en/`                    | 顯示首頁，標題英文         |
| Tours 列表  | `/zh-tw/tours/`           | 顯示旅遊行程列表           |
| Tours 詳細  | `/zh-tw/tours/<id>/`      | 顯示行程細節，標題翻譯正確 |
| Cruise 列表 | `/zh-tw/cruises/`         | 顯示郵輪行程               |
| 登入頁面    | `/accounts/login/`        | 顯示登入表單               |
| 註冊頁面    | `/accounts/signup/`       | 顯示註冊表單               |
| 登入流程    | `/accounts/login/` → 登入 | 成功跳轉 dashboard         |
| 登出流程    | `/accounts/logout/`       | 成功跳回首頁               |
| 語言切換    | `/zh-tw/` ↔ `/en/`        | URL 切換後翻譯正確         |
| 訂單測試    | 下單流程                  | 成功建立訂單 (v0.7 起)     |
| SEO         | `/sitemap.xml`            | 成功生成 sitemap (v0.8 起) |

---

📌 建議：

- 每次部署完成後，照表檢查一次（大約 2 分鐘）。
- 如果其中某一項壞掉，馬上回到上一個 Git tag，避免「壞一個拖垮全部」。  
  📓 2025-09-21 工作紀錄 — EastUSATours 專案
  🎯 今日目標

釐清 主專案 (eastusatours)、Tours app、Cruise app 三者的責任分工與資料來源。

🗂 分工結果

1. 主專案 (eastusatours/views.py)

職責：首頁 /（含 /zh-tw/、/zh-cn/、/en/）

用途：聚合來自各 app 的資料，提供首頁 context

banners → Banners app（未來可加）

featured_tours → Tours app

popular_tours → Tours app

featured_cruises → Cruise app（未來）

👉 首頁 home() 要放在這裡，不是 tours。

2. Tours app (tours/views.py)

職責：

Tours 列表 /tours/

Tours 搜尋 /tours/search/

Tours 詳細 /tours/<id>/

資料來源：tours/models.py

Tour

DepartureRegion

DepartureCity

👉 只負責「巴士團 / 行程」，不處理首頁。

3. Cruise app (cruise/views.py)

職責：

Cruise 列表 /cruise/

Cruise 搜尋 /cruise/search/

Cruise 詳細 /cruise/<id>/

資料來源：cruise/models.py

CruiseTour

CruiseLine

CruiseShip

CruiseRegion

CruisePort

👉 和 Tours 平行，互不干擾。

📊 分工表
層級 檔案 功能 資料來源
主專案 eastusatours/views.py 首頁 /（聚合多 app 資料） Tours / Cruise / Banners
Tours app tours/views.py Tours 列表 / 搜尋 / 詳細 tours/models.py
Cruise app cruise/views.py Cruise 列表 / 搜尋 / 詳細 cruise/models.py
✅ 今日成果

已釐清：

首頁 home() 必須放在 eastusatours/views.py

Tours/Cruise 各自獨立處理，資料不交叉

將來首頁 context 才能「聚合」來自 Tours + Cruise 的內容

後續：

移除 tours/views.py 裡多餘的 home()

調整 eastusatours/views.py → 用 Tour 當首頁資料來源

cruise/views.py 保持獨立，不再掛在主專案 home()

📓 2025-09-20 搜尋功能進度紀錄
🔍 Tours 搜尋 (tours/views.py)

已建立 tours_search(request)：

支援條件：

keyword → 用 title\_\_icontains

depart_date → 用 departure_date

city → 用 city\_\_icontains

region → 用 tour_type

搜尋結果會 render 到 tours/tour_list.html

傳入的 context 包含 search_mode, selected_city, selected_date, keyword, region

✅ 意義：已經有一個可用的 Tours 搜尋表單 + 結果頁。

🧩 首頁搜尋器（Tabs）

根據昨天的筆記：

home.html 會 include partials/search_box_tabs.html

Tabs 內再 include：

partials/tours_search_box.html

partials/cruise_search_box.html

搜尋條件 已經前後端對應：

Tours: 城市、目的地、日期、促銷、關鍵字

Cruise: 公司、地區、港口、月份、中文導遊、特價

✅ 意義：首頁大搜尋器已經有框架，partial 分工正確。

🗂️ Models 昨天的補強

Tours:

DepartureRegion

DepartureCity

Tour.city = ForeignKey(DepartureCity)

讓搜尋條件可以用後台 Admin 控制（不是硬編碼 option）

✅ 意義：搜尋選單 → 後台可控，不再寫死。

✅ 總結

昨天完成的重點：

Tours 搜尋 view (tours_search) 已可用。

首頁 Tabs 搜尋框 → partials 分好。

DepartureRegion/City → 已放入 models，可以後台控制搜尋選項。

👉 所以今天我們調整「首頁放哪裡」的時候，要注意：

不能刪掉 tours/views.py 的 tours_search（只刪掉多餘的 home()）。

## eastusatours/views.py 的 home() 只處理首頁 context，不要動搜尋邏輯。

# 🔑 Django SECRET_KEY 設定紀錄

## 1. 開發環境 (local.py)

- 開發用的 `SECRET_KEY` 可直接寫在 `settings/base.py`，方便測試。
- 目前專案開發用的 KEY（不建議放生產環境）：
  ```python
  SECRET_KEY = "django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxxx"
  ```

2. 生產環境 (production.py)

生產環境 不能硬編碼，必須從 環境變數讀取。

設定方式：

import os

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
if not SECRET_KEY:
raise ValueError("DJANGO_SECRET_KEY environment variable is not set!")

在伺服器 (Linux) 上設定環境變數：

export DJANGO_SECRET_KEY="隨機產生的一長串安全字串"

3. 如何產生新的 SECRET_KEY

使用 Django 提供的工具：

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

範例輸出：

k1f%4i0c*1s(6^b&+w)z#u7d93(ay&m*jhq@x1$e4n^tvlr

4. 注意事項

生產用的 KEY 不能公開在 GitHub。

每個環境（dev / staging / production）可以有不同的 KEY。

改了 KEY → 舊的加密 session / cookie 會失效（用戶需要重新登入）。

---

要不要我直接幫你寫一份完整的 `PROJECT_NOTES.md`（包含 SECRET_KEY、資料庫、static/media 設定紀錄），這樣整份專案文件就能一步到位？
📂 templates/partials/
檔案 用途 範例使用位置
navbar.html 頁首（導覽列，Logo、主選單、登入/註冊按鈕） 幾乎所有頁面都會 {% include "partials/navbar.html" %}
footer.html 頁腳（聯絡資訊、版權聲明、社群連結） 幾乎所有頁面都會 {% include "partials/footer.html" %}
hero.html Hero 區塊（首頁大圖/橫幅，通常是一張 Banner，含標題與 CTA 按鈕） 通常只在首頁 home.html 出現
popular_regions.html 熱門目的地區塊（例如「熱門地區：紐約、邁阿密、加勒比海」），可以是圖片格子或連結 可以放在首頁 Hero 下方，或搜尋前頁面
search_box_tabs.html 搜尋區塊（多 Tab 搜尋：航程 / 行程 / 機票…）

這樣就清楚了：

navbar → 每頁都用

footer → 每頁都用

hero → 大橫幅，通常首頁才有

search_box_tabs → 大型搜尋 UI

popular_regions → 熱門目的地區塊

👉 總結：

hero.html = 首頁大橫幅（Banner + 主標題）

popular_regions.html = 熱門地區卡片/連結

search_box_tabs.html = 大搜尋框（可能有多個 Tab）

📓 2025-09-22 工作紀錄 — EastUSATours 專案
✅ 今日完成

首頁模板結構

home.html → 已統一使用，不再有 guest/member。

templates/partials/ → 整理完成，功能對應：

navbar.html → 頁首，含「熱門目的地」展開選單（美國旅遊 / 加拿大旅遊 / 歐洲旅遊 / 郵輪假期）。

footer.html → 頁尾。

hero.html → 首頁橫幅 Banner（僅首頁出現）。

search_box_tabs.html → 大型搜尋 UI，內含 Tab 切換。

tours_search_box.html → 美國團搜尋表單。

cruise_search_box.html → 郵輪搜尋表單。

popular_regions.html → 熱門地區區塊（可放 Banner 下方，類似 KKday「熱門目的地」）。

Navbar 熱門目的地

修正：僅保留一排（像 KKday），展開時顯示對齊的子城市（支援小圖片 icon）。

已加上「郵輪假期」Tab，港口清單可從後台管理。

模型與後台

Tours → DepartureRegion / DepartureCity 已加入。

Cruise → CruiseRegion / CruisePort 已加入。

Admin 可直接新增/刪除，搜尋表單的 <select> 不再寫死。

Views 分工（釐清責任）

eastusatours/views.py → 負責首頁（聚合 Tours + Cruise）。

tours/views.py → 負責 /tours/ 搜尋 & 詳細頁。

cruise/views.py → 負責 /cruise/ 搜尋 & 詳細頁。

多語支援

LANGUAGES = [("zh_Hant", "繁體"), ("zh_Hans", "簡體"), ("en", "English")]

模板已統一使用 {% trans %}。

路由採 /zh-hant/、/zh-hans/、/en/ 前綴。

🚧 進行中 / 待完成

首頁 Hero + 熱門地區 → 要補上假資料圖片，避免空白。

Tours 搜尋結果頁（tours/search_results.html）需串接 tours_search view。

Cruise 搜尋結果頁（cruise/search_results.html）需串接 cruise_search view。

Navbar「熱門目的地」圖片資源缺少，暫用 demo。

Admin：Cruise 模組的 list_display / search_fields / filter 需優化。

⏩ 明日建議步驟

先跑 makemigrations → migrate → createsuperuser
確認 DepartureCity / DepartureRegion / CruisePort / CruiseRegion 都能在後台建立。

補齊首頁 Hero 假圖 → 不需要真的圖片，先用 Tailwind + placeholder 區塊。

接上搜尋表單：

/tours/search/ → render tours/search_results.html

/cruise/search/ → render cruise/search_results.html

測試 Navbar 展開：

熱門目的地 → 有子城市 & icon。

郵輪假期 → 有港口。
📌 專案目前狀況（依照你 Notes 的規劃）09.23.2025
1. 前端 (Templates / Partials)

✅ navbar.html → 已完成，含登入/註冊、語言、幣別切換

✅ footer.html → 已完成，社群 icon 都能正常顯示

✅ hero.html → 規劃中（首頁大圖 + slogan + CTA）

✅ search_box_tabs.html → Tabs 結構已完成

✅ cruise_search_box.html → 已有表單（還缺完整串接）

✅ us_search_box.html → 已有表單（還缺完整串接）

✅ tours_search_box.html → Canada / Europe / Asia 共用

2. 後端 (Views / Forms / Models)

Tour model ✅ 已有，支援 region (us/canada/europe/asia)

Cruise model ⚠️ 半完成，缺欄位（天數、港口、船公司）

Views:

/tours/search/ → 可用，但只做基本篩選

/us/search/ → 半完成，城市分類未串接

/cruise/search/ → 半完成，缺特有邏輯

Forms:

部分有寫，但還沒完全拆成 CruiseSearchForm / USTourSearchForm / GenericTourSearchForm

3. 靜態資源 (Static)

✅ static/css/style.css → 正常

✅ static/tailwind.css → 已整合

✅ static/images/ → 圖片整理完成，假 PNG 問題解決

⚠️ staticfiles/ → 已確認是 collectstatic 自動產生，建議不手動編輯

4. 部署 (Git + Render)

⚠️ 還沒開始

你之前 Notes 有寫「要用 Git 管理、再推到 Render」，但目前專案只在本機，還沒做：

git init → 建版本控制

git commit → 紀錄 milestone

render.yaml / requirements.txt → 部署設定

Render 平台建立 Web Service → 連 PostgreSQL

📌 下一步（照 Notes）

完成 H 區 + 搜尋區前端

Hero 區（大圖 + slogan + CTA 按鈕）

搜尋 Tabs → 五分類（Cruise / US / Canada / Europe / Asia）

後端串接

補齊 Cruise model 欄位 + CruiseSearchForm

補齊 USTourSearchForm（城市選單）

Tours 共用 Form → 確保 region 帶得進去

版本控制 + 部署

初始化 Git，先把目前進度全部 commit

建 Render 帳號，準備部署設定檔

推上去測試部署

📌 對話整理 → 主題化
主題 1：前端 UI

Navbar

Footer

Hero 區 (待完成)

Search Box Tabs (已完成結構，待串接後端)

熱門目的地區塊

主題 2：後端邏輯

Tours Model ✅

Cruise Model ⚠️ 待補（天數/港口/船公司）

Views:

tours_search → 基本完成

us_search → 半完成

cruise_search → 半完成

Forms: 分拆未完全

主題 3：靜態資源

Tailwind ✅

Style.css ✅

圖片 static/images ✅ （假 PNG 問題解決）

staticfiles ⚠️ → 只給 collectstatic 用

主題 4：部署

Git 還沒 init

Render 還沒配置

沒問題啦 😊 我一步一步教你，保證不會把檔案弄丟。
現在看到的 deleted / modified 紅字，只是 Git 在「記錄」裡以為被刪掉，但實際上檔案還在你電腦裡。
我們要做的是 把檔案狀態恢復正常 → 再推上去。

👩‍💻 你現在可以照著打：

（在專案根目錄，VSCode 的 terminal）

先把 Git 以為被刪掉的檔案「還原」：

git restore templates/


把所有變更（包含還原的檔案）重新加入 Git：

git add .


建立一次新的 commit（幫它寫個訊息）：

git commit -m "fix: restore templates and sync project files"


推上 GitHub：

git push origin master

🚨 小提醒

不要用 git rm，那個會真的刪檔。

如果 push 完，Render 部屬還是錯，我們再看 log，但這次至少「檔案不會消失」。
# tours/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# --- 首頁（直接把資料塞進模板，不用 API/序列化） ---
def site_home(request):
    # 這個結構就是給 templates/home.html 用的
    sections = [
        {
            "title": "美東精選",
            "cols": 3,
            "cards": [
                {
                    "title": "紐約經典一日遊",
                    "subtitle": "自由女神/華爾街/華盛頓廣場",
                    "price_label": "$199 起",
                    "tag": "熱銷",
                    "image_url": "/static/images/sample/nyc.jpg",
                    "link_url": "#",
                },
                {
                    "title": "尼加拉瀑布一日",
                    "subtitle": "瀑布遊船/夜景觀賞",
                    "price_label": "$249 起",
                    "tag": "",
                    "image_url": "/static/images/sample/niagara.jpg",
                    "link_url": "#",
                },
                {
                    "title": "波士頓文化一日",
                    "subtitle": "自由之路/昆西市場",
                    "price_label": "$179 起",
                    "tag": "特價",
                    "image_url": "/static/images/sample/boston.jpg",
                    "link_url": "#",
                },
            ],
        },
    ]
    return render(request, "home.html", {"sections": sections})

# --- 會員中心（保持你原本有的導覽） ---
@login_required
def member_dashboard(request):
    return render(request, "account/dashboard.html")

@login_required
def profile_view(request):
    return render(request, "account/profile.html")

@login_required
def orders_view(request):
    return render(request, "account/orders.html")

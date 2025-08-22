# cart/views.py
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .utils import get_product_model, price_of

SESSION_KEY = "cart_items"
Product = get_product_model()  # 由設定決定要用哪個模型

def overview(request: HttpRequest):
    ids = request.session.get(SESSION_KEY, [])
    items_qs = Product.objects.filter(id__in=ids)

    # 合計金額（數量=1；若有數量可再擴充）
    total_price: Decimal = sum((price_of(p) for p in items_qs), Decimal("0"))

    return render(request, "cart/overview.html", {
        "cart_items": items_qs,
        "cart_count": len(ids),
        "total_price": total_price,
    })

def add_to_cart(request, product_id: int):
    ids = request.session.get(SESSION_KEY, [])
    pid = int(product_id)
    if pid not in ids:
        # 確認商品存在
        get_object_or_404(Product, id=pid)
        ids.append(pid)
        request.session[SESSION_KEY] = ids
    return redirect("cart:overview")

def remove_from_cart(request, product_id: int):
    ids = request.session.get(SESSION_KEY, [])
    pid = int(product_id)
    if pid in ids:
        ids.remove(pid)
        request.session[SESSION_KEY] = ids
    return redirect("cart:overview")

def clear_cart(request):
    request.session[SESSION_KEY] = []
    return redirect("cart:overview")

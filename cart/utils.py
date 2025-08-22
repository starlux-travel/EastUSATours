# cart/utils.py
from django.apps import apps
from django.conf import settings
from decimal import Decimal
import re

def get_product_model():
    """
    依 settings.CART_PRODUCT_MODEL 取得模型類別。
    例如 "tours.SectionCard" -> tours.models.SectionCard
    """
    model_path = getattr(settings, "CART_PRODUCT_MODEL", "tours.SectionCard")
    app_label, model_name = model_path.split(".")
    return apps.get_model(app_label, model_name, require_ready=False)

def price_of(obj) -> Decimal:
    """
    嘗試從物件取價格：
    - 欄位：price / tour_price / price_amount / amount
    - 或從 price_label 解析數字（如 "$299 起" -> 299）
    取不到則回 0。
    """
    for attr in ("price", "tour_price", "price_amount", "amount"):
        if hasattr(obj, attr):
            try:
                return Decimal(str(getattr(obj, attr)))
            except Exception:
                pass
    if hasattr(obj, "price_label") and obj.price_label:
        s = str(obj.price_label).replace(",", "")
        m = re.search(r"(\d+(?:\.\d+)?)", s)
        if m:
            return Decimal(m.group(1))
    return Decimal("0")

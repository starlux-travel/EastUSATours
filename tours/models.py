from django.db import models
from django.contrib.sites.models import Site
from django.utils import timezone

class Channel(models.TextChoices):
    B2C = "b2c", "B2C（官網/消費者）"
    B2B = "b2b", "B2B（同業/代理）"
    MKT = "mkt", "行銷官網"
    APP = "app", "行動端/小程式"

class HomeConfig(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="home_configs")
    channel = models.CharField(max_length=8, choices=Channel.choices, default=Channel.B2C, db_index=True)

    # H 區（Hero）
    hero_title = models.CharField(max_length=200, blank=True, default="")
    hero_subtitle = models.CharField(max_length=300, blank=True, default="")
    hero_bg_image = models.URLField(blank=True, default="")
    show_breadcrumbs = models.BooleanField(default=True)

    # SEO
    seo_title = models.CharField(max_length=200, blank=True, default="")
    seo_description = models.CharField(max_length=300, blank=True, default="")
    seo_keywords = models.CharField(max_length=300, blank=True, default="")

    # 會員 Dashboard 小工具（登入後頁面可用）
    show_orders_widget = models.BooleanField(default=True)
    show_points_widget = models.BooleanField(default=True)
    show_profile_widget = models.BooleanField(default=True)
    show_coupons_widget = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = [("site", "channel")]
        ordering = ["site_id", "channel"]

    def __str__(self):
        return f"{self.site.domain} / {self.get_channel_display()}"

# ---- 首頁可配置區塊 ----

class SectionLayout(models.TextChoices):
    GRID = "grid", "格線"
    CAROUSEL = "carousel", "橫向滑動"
    LIST = "list", "清單"

class DividerStyle(models.TextChoices):
    NONE = "none", "無"
    LINE = "line", "水平線"
    SPACER = "spacer", "空白間距"

class Section(models.Model):
    home = models.ForeignKey(HomeConfig, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=120)                       # 區塊標題，如「精選行程」
    subtitle = models.CharField(max_length=200, blank=True, default="")
    slug = models.SlugField(max_length=60, blank=True, default="") # 可用來讓前端定位（ex: featured, cruise）
    layout = models.CharField(max_length=16, choices=SectionLayout.choices, default=SectionLayout.GRID)
    columns = models.PositiveIntegerField(default=3)               # 每列幾格（grid 用）
    show_divider = models.CharField(max_length=10, choices=DividerStyle.choices, default=DividerStyle.LINE)
    max_items = models.PositiveIntegerField(default=6)             # 顯示卡片上限（精選要多就調大）
    more_label = models.CharField(max_length=40, blank=True, default="") # 「更多」按鈕文字
    more_url = models.CharField(max_length=300, blank=True, default="")  # 「更多」連結
    order = models.PositiveIntegerField(default=0)                 # 區塊排序
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"[{self.home}] {self.title}"

class SectionCard(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="cards")
    # 通用卡片欄位（不鎖產品模型，之後要接 Tour ID 再擴充）
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=200, blank=True, default="")
    image_url = models.URLField(blank=True, default="")
    price_label = models.CharField(max_length=40, blank=True, default="")  # 如 "$299 起"
    tag = models.CharField(max_length=30, blank=True, default="")          # 如 "熱賣"、"早鳥"
    link_url = models.CharField(max_length=300)                             # 行程/專題/外部
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.section.title} / {self.title}"

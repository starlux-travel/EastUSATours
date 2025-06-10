from django.db import models
from django.utils.translation import gettext_lazy as _

class TourCategory(models.Model):
    # 多語言分類名稱
    name_en = models.CharField(max_length=100, verbose_name=_("英文分類名稱"))
    name_zh_tw = models.CharField(max_length=100, verbose_name=_("繁體分類名稱"))
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = _("行程分類")
        verbose_name_plural = _("行程分類（複數）")

    def __str__(self):
        # 這樣在 admin 顯示時會優先顯示繁體
        return self.name_zh_tw

class Tour(models.Model):
    category = models.ForeignKey(
        TourCategory, on_delete=models.CASCADE,
        related_name='tours', verbose_name=_("所屬分類")
    )
    # 多語言標題與說明
    title_en = models.CharField(max_length=200, verbose_name=_("英文標題"))
    desc_en = models.TextField(verbose_name=_("英文說明"), blank=True)
    title_zh_tw = models.CharField(max_length=200, verbose_name=_("繁體標題"))
    desc_zh_tw = models.TextField(verbose_name=_("繁體說明"), blank=True)

    duration_days = models.IntegerField(default=1, verbose_name=_("行程天數"))
    departure_city = models.CharField(max_length=100, verbose_name=_("出發城市"))
    departure_time = models.TimeField(verbose_name=_("出發時間"))
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("價格"))
    image = models.ImageField(upload_to='tours/', blank=True, null=True, verbose_name=_("主圖"))
    is_active = models.BooleanField(default=True, verbose_name=_("是否上架"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("行程")
        verbose_name_plural = _("行程列表")

    def __str__(self):
        return self.title_zh_tw

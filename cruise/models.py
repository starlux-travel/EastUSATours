from django.db import models
from django.utils import translation


class Region(models.Model):
    name_zh_hant = models.CharField(max_length=100, null=True, blank=True, verbose_name="地區名稱 (繁體)")
    name_zh_hans = models.CharField(max_length=100, null=True, blank=True, verbose_name="地区名称 (简体)")
    name_en = models.CharField(max_length=100, null=True, blank=True, verbose_name="Region Name (EN)")

    def __str__(self):
        return self.name_zh_hant or self.name_en or "Unnamed Region"


class CruisePort(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="ports", null=True, blank=True)
    name_zh_hant = models.CharField(max_length=100, null=True, blank=True, verbose_name="港口名稱 (繁體)")
    name_zh_hans = models.CharField(max_length=100, null=True, blank=True, verbose_name="港口名称 (简体)")
    name_en = models.CharField(max_length=100, null=True, blank=True, verbose_name="Port Name (EN)")

    def __str__(self):
        return self.name_zh_hant or self.name_en or "Unnamed Port"


class CruiseTour(models.Model):
    title_zh_hant = models.CharField(max_length=255, null=True, blank=True, verbose_name="標題 (繁體)")
    title_zh_hans = models.CharField(max_length=255, null=True, blank=True, verbose_name="标题 (简体)")
    title_en = models.CharField(max_length=255, null=True, blank=True, verbose_name="Title (EN)")

    description_zh_hant = models.TextField(null=True, blank=True, verbose_name="描述 (繁體)")
    description_zh_hans = models.TextField(null=True, blank=True, verbose_name="描述 (简体)")
    description_en = models.TextField(null=True, blank=True, verbose_name="Description (EN)")

    departure_region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="出發地區")
    departure_port = models.ForeignKey(CruisePort, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="出發港口")
    departure_date = models.DateField(null=True, blank=True, verbose_name="出發日期")

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="價格")
    is_active = models.BooleanField(default=True, verbose_name="是否啟用")

    def __str__(self):
        return self.title_zh_hant or self.title_en or "Unnamed Cruise Tour"

    # Helper: 根據語言自動顯示正確標題
    def get_title(self):
        lang = translation.get_language() or ""
        if lang.startswith("zh-hant"):
            return self.title_zh_hant or self.title_en
        elif lang.startswith("zh-hans"):
            return self.title_zh_hans or self.title_en
        return self.title_en or self.title_zh_hant or self.title_zh_hans

    # Helper: 根據語言自動顯示正確描述
    def get_description(self):
        lang = translation.get_language() or ""
        if lang.startswith("zh-hant"):
            return self.description_zh_hant or self.description_en
        elif lang.startswith("zh-hans"):
            return self.description_zh_hans or self.description_en
        return self.description_en or self.description_zh_hant or self.description_zh_hans

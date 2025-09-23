from django.db import models
from django.utils import translation


class DepartureRegion(models.Model):
    """巴士/團體旅遊的出發地區 (例：美東、美西、加拿大、歐洲、亞洲)"""
    name_zh_hant = models.CharField(max_length=100, null=True, blank=True, verbose_name="地區名稱 (繁體)")
    name_zh_hans = models.CharField(max_length=100, null=True, blank=True, verbose_name="地區名稱 (簡體)")
    name_en = models.CharField(max_length=100, null=True, blank=True, verbose_name="地區名稱 (英文)")

    def __str__(self):
        return self.name_zh_hant or self.name_en or "Unnamed Region"


class DepartureCity(models.Model):
    """具體出發城市 (例：紐約、波士頓、洛杉磯、拉斯維加斯)"""
    region = models.ForeignKey(DepartureRegion, on_delete=models.CASCADE, related_name="cities")
    name_zh_hant = models.CharField(max_length=100, null=True, blank=True, verbose_name="城市名稱 (繁體)")
    name_zh_hans = models.CharField(max_length=100, null=True, blank=True, verbose_name="城市名稱 (簡體)")
    name_en = models.CharField(max_length=100, null=True, blank=True, verbose_name="城市名稱 (英文)")

    def __str__(self):
        return self.name_zh_hant or self.name_en or "Unnamed City"


class Tour(models.Model):
    """旅遊產品 (巴士團、一日遊、多日團)"""
    title_zh_hant = models.CharField(max_length=200, null=True, blank=True, verbose_name="標題 (繁體)")
    title_zh_hans = models.CharField(max_length=200, null=True, blank=True, verbose_name="標題 (簡體)")
    title_en = models.CharField(max_length=200, null=True, blank=True, verbose_name="標題 (英文)")

    description_zh_hant = models.TextField(null=True, blank=True, verbose_name="描述 (繁體)")
    description_zh_hans = models.TextField(null=True, blank=True, verbose_name="描述 (簡體)")
    description_en = models.TextField(null=True, blank=True, verbose_name="描述 (英文)")

    departure_region = models.ForeignKey(DepartureRegion, on_delete=models.SET_NULL, null=True, blank=True)
    departure_city = models.ForeignKey(DepartureCity, on_delete=models.SET_NULL, null=True, blank=True)

    departure_date = models.DateField(null=True, blank=True, verbose_name="出發日期")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="是否啟用")

    def __str__(self):
        return self.get_title() or "Unnamed Tour"

    # === Helper: 語言自動切換 ===
    def get_title(self):
        lang = translation.get_language() or ""
        if lang.startswith("zh-hant"):
            return self.title_zh_hant or self.title_en
        elif lang.startswith("zh-hans"):
            return self.title_zh_hans or self.title_en
        return self.title_en or self.title_zh_hant or self.title_zh_hans

    def get_description(self):
        lang = translation.get_language() or ""
        if lang.startswith("zh-hant"):
            return self.description_zh_hant or self.description_en
        elif lang.startswith("zh-hans"):
            return self.description_zh_hans or self.description_en
        return self.description_en or self.description_zh_hant or self.description_zh_hans
    

class Banner(models.Model):
    title = models.CharField(max_length=200, verbose_name="標題")
    image = models.ImageField(upload_to="banners/", verbose_name="圖片")
    link = models.URLField(blank=True, null=True, verbose_name="連結")
    order = models.PositiveIntegerField(default=0, verbose_name="排序")
    is_active = models.BooleanField(default=True, verbose_name="是否啟用")

    class Meta:
        ordering = ["order"]
        verbose_name = "首頁 Banner"
        verbose_name_plural = "首頁 Banners"

    def __str__(self):
        return self.title


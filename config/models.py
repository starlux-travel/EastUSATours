from django.db import models

class SiteTheme(models.Model):
    site_name = models.CharField(max_length=100, default="EastUSA Tours")

    # Logo 圖片（淺底/深底）
    logo_light = models.ImageField(upload_to='logo/', help_text="適用於白色背景")
    logo_dark = models.ImageField(upload_to='logo/', help_text="適用於深色背景")

    # 色彩主題
    primary_color = models.CharField(max_length=7, default="#32C5D2")    # East Sky Blue
    secondary_color = models.CharField(max_length=7, default="#2B6A78")  # Deep Aqua Navy
    accent_color = models.CharField(max_length=7, default="#FEC271")     # Warm Gold
    background_color = models.CharField(max_length=7, default="#FFFFFF") # Liberty Cloud
    text_color = models.CharField(max_length=7, default="#333333")       # Modern Gray

    # 首頁主視覺圖片
    homepage_banner = models.ImageField(upload_to='banner/', null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name

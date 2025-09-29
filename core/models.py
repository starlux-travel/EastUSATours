from django.db import models


# 🔹 首頁 Banner（輪播圖）
class Banner(models.Model):
    title = models.CharField("標題", max_length=200)
    image = models.ImageField("圖片", upload_to="banners/")
    link = models.URLField("連結", blank=True, null=True)
    order = models.PositiveIntegerField("排序", default=0)
    is_active = models.BooleanField("是否啟用", default=True)

    class Meta:
        verbose_name = "首頁 Banner"
        verbose_name_plural = "首頁 Banner"
        ordering = ["order"]

    def __str__(self):
        return self.title


# 🔹 常見問題 (FAQ)
class FAQ(models.Model):
    question = models.CharField("問題", max_length=255)
    answer = models.TextField("答案")
    order = models.PositiveIntegerField("排序", default=0)

    class Meta:
        verbose_name = "常見問題"
        verbose_name_plural = "常見問題"
        ordering = ["order"]

    def __str__(self):
        return self.question
    
 



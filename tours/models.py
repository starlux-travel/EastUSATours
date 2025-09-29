from django.db import models


# 🔹 出發地區
class DepartureRegion(models.Model):
    name = models.CharField("出發地區", max_length=100)

    class Meta:
        verbose_name = "出發地區"
        verbose_name_plural = "出發地區"

    def __str__(self):
        return self.name


# 🔹 出發城市
class DepartureCity(models.Model):
    region = models.ForeignKey(
        DepartureRegion,
        on_delete=models.CASCADE,
        related_name="cities",
        verbose_name="所屬地區"
    )
    name = models.CharField("出發城市", max_length=100)

    class Meta:
        verbose_name = "出發城市"
        verbose_name_plural = "出發城市"

    def __str__(self):
        return f"{self.region.name} - {self.name}"


# 🔹 行程 (Tour)
class Tour(models.Model):
    title = models.CharField("行程標題", max_length=200, default="未命名行程")
    description = models.TextField("行程描述", blank=True, null=True)
    price = models.DecimalField("價格", max_digits=10, decimal_places=2, null=True, blank=True)
    departure_date = models.DateField("出發日期", null=True, blank=True)
    departure_city = models.ForeignKey(
        DepartureCity,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tours",
        verbose_name="出發城市"
    )
    views_count = models.PositiveIntegerField("瀏覽次數", default=0)

    class Meta:
        verbose_name = "行程"
        verbose_name_plural = "行程"

    def __str__(self):
        return self.title

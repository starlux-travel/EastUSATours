from django.db import models

class CruiseRegion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CruisePort(models.Model):
    region = models.ForeignKey(CruiseRegion, on_delete=models.CASCADE, related_name="ports")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.region.name})"


class CruiseTour(models.Model):
    region = models.ForeignKey(CruiseRegion, on_delete=models.CASCADE, related_name="cruises")
    departure_port = models.ForeignKey(
        CruisePort, on_delete=models.CASCADE, related_name="departures"
    )
    return_port = models.ForeignKey(
        CruisePort, on_delete=models.CASCADE, related_name="returns", blank=True, null=True
    )
    line = models.CharField(max_length=100, verbose_name="公司", blank=True, null=True)
    title = models.CharField(max_length=200)
    departure_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.line or 'No Line'})"

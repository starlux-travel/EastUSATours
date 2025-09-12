# tours/signals.py
"""
目前不使用任何 signals。
將來若要針對 Tour 模型加快取或同步邏輯，可以在這裡新增 receiver。
"""

from django.db.models.signals import post_save, post_delete  # noqa: F401
from django.dispatch import receiver  # noqa: F401

# 範例（之後需要再打開）
# from .models import Tour
# @receiver(post_save, sender=Tour)
# def tour_changed(sender, instance, **kwargs):
#     pass

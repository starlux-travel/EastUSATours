# tours/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import HomeConfig, Section, SectionCard

def _key(homecfg: HomeConfig):
    return f"home:{homecfg.site_id}:{homecfg.channel}"

def _invalidate(homecfg: HomeConfig):
    cache.delete(_key(homecfg))

@receiver(post_save, sender=HomeConfig)
@receiver(post_delete, sender=HomeConfig)
def home_changed(sender, instance, **kwargs):
    _invalidate(instance)

@receiver(post_save, sender=Section)
@receiver(post_delete, sender=Section)
def section_changed(sender, instance, **kwargs):
    _invalidate(instance.home)

@receiver(post_save, sender=SectionCard)
@receiver(post_delete, sender=SectionCard)
def card_changed(sender, instance, **kwargs):
    _invalidate(instance.section.home)

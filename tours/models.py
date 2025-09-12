from django.db import models
from django.utils import timezone

# ---- 現有其他模型（略） ----
# 若你已經有 HomeConfig / Section / SectionCard / TourCategory 等，保留即可

class TourType(models.TextChoices):
    BUS = "bus_tour", "巴士團"
    CRUISE = "cruise_tour", "郵輪團"
    

def _convert_hant_to_hans(text: str) -> str:
    """
    嘗試用 OpenCC 做繁→簡；若環境沒有 opencc 套件，使用簡易 fallback（不做破壞性轉換）。
    """
    if not text:
        return text
    try:
        # pip install opencc-python-reimplemented
        from opencc import OpenCC
        return OpenCC("t2s").convert(text)
    except Exception:
        # 安全 fallback：直接回傳原字串（等之後裝好 opencc 再轉）
        return text

class Tour(models.Model):
    # 基本
    tour_type = models.CharField(max_length=20, choices=TourType.choices, db_index=True)
    # 多語 JSON：各自包含 {"zh_Hant": "...", "zh_Hans": "...", "en": "..."}
    default=TourType.BUS,
    
    title = models.JSONField(default=dict, blank=True)
    desc = models.JSONField(default=dict, blank=True)
    faq = models.JSONField(default=dict, blank=True)

    # 同步旗標（語言流程控管）
    zh_Hant_translated = models.BooleanField(default=False, help_text="繁體已完成")
    zh_Hans_synced = models.BooleanField(default=True, help_text="簡體與繁體自動同步（未手改）")
    en_translated = models.BooleanField(default=False, help_text="英文已完成")

    # 巴士專用
    meeting_point = models.CharField(max_length=255, blank=True, default="")
    pickup_time = models.TimeField(blank=True, null=True)

    # 郵輪專用
    embark_port = models.CharField(max_length=255, blank=True, default="")
    sail_date = models.DateField(blank=True, null=True)
    cabin_type = models.CharField(max_length=100, blank=True, default="")

    # 其他可選
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cover_image = models.URLField(blank=True, default="")
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at", "-id"]

    def __str__(self):
        # 以繁體做為顯示名稱 fallback
        t = (self.title or {})
        return t.get("zh_Hant") or t.get("en") or f"Tour #{self.pk}"

    # ---- 語言同步（儲存前自動繁→簡）----
    def _autosync_lang_block(self, block: dict) -> dict:
        """
        block 結構如：{"zh_Hant": "...", "zh_Hans": "...", "en": "..."}
        若 zh_Hans_synced=True，則用 zh_Hant 自動轉 zh_Hans（保留 en）
        """
        block = block or {}
        hant = (block.get("zh_Hant") or "").strip()
        hans = (block.get("zh_Hans") or "").strip()
        en = (block.get("en") or "").strip()

        if self.zh_Hans_synced:
            # 以繁體為來源產生簡體
            hans = _convert_hant_to_hans(hant) if hant else hans

        return {"zh_Hant": hant, "zh_Hans": hans, "en": en}

    def _clear_fields_by_type(self):
        """避免存到不相干的欄位"""
        if self.tour_type == TourType.BUS:
            self.embark_port = ""
            self.sail_date = None
            self.cabin_type = ""
        elif self.tour_type == TourType.CRUISE:
            self.meeting_point = ""
            self.pickup_time = None

    def save(self, *args, **kwargs):
        # 語言同步
        self.title = self._autosync_lang_block(self.title)
        self.desc = self._autosync_lang_block(self.desc)
        self.faq = self._autosync_lang_block(self.faq)

        # 類型防呆
        self._clear_fields_by_type()
        super().save(*args, **kwargs)
